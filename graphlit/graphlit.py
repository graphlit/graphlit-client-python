import os
import jwt
import datetime
import httpx
import asyncio
import random
from graphlit_api.client import Client

class Graphlit:
    def __init__(self, organization_id=None, environment_id=None, jwt_secret=None, owner_id=None, api_uri=None):
        self.organization_id = organization_id if organization_id is not None else os.getenv("GRAPHLIT_ORGANIZATION_ID")
        self.environment_id = environment_id if environment_id is not None else os.getenv("GRAPHLIT_ENVIRONMENT_ID")
        self.owner_id = owner_id if owner_id is not None else os.getenv("GRAPHLIT_OWNER_ID")
        self.secret_key = jwt_secret if jwt_secret is not None else os.getenv("GRAPHLIT_JWT_SECRET")
        self.api_uri = api_uri if api_uri is not None else "https://data-scus.graphlit.io/api/v1/graphql/"
        
        self.token = self.generate_jwt()

        headers = {"Authorization": f"Bearer {self.token}"}
        
        self.client = Client(url=self.api_uri, headers=headers)
        self.client.http_client.timeout = httpx.Timeout(timeout=600.0)
        self.client.event_hooks = {'response': [self.exponential_backoff]}
        
        self.retry_state = {
            "attempts": 0,
            "max_attempts": 7,
            "base_delay": 1  # Base delay in seconds
        }

    def generate_jwt(self):
        expiration = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=1)
        
        payload = {
            "https://graphlit.io/jwt/claims": {
                "x-graphlit-organization-id": self.organization_id,
                "x-graphlit-environment-id": self.environment_id,
                "x-graphlit-role": "Owner",
            },
            "exp": expiration,
            "iss": "graphlit",
            "aud": "https://portal.graphlit.io",
        }

        if self.owner_id is not None:
            payload["https://graphlit.io/jwt/claims"]["x-graphlit-owner-id"] = self.owner_id
        
        return jwt.encode(payload, self.secret_key, algorithm="HS256")

    async def exponential_backoff(self, request: httpx.Request, response: httpx.Response):
        if response.status_code >= 500 and self.retry_state["attempts"] < self.retry_state["max_attempts"]:
            self.retry_state["attempts"] += 1
            
            delay = self.retry_state["base_delay"] * (2 ** (self.retry_state["attempts"] - 1))
            delay += random.uniform(0, self.retry_state["base_delay"])
            
            print(f'Graphlit API returned HTTP error {response.status_code}, retrying after {delay}.')

            await asyncio.sleep(delay)

            return await response.anext()
