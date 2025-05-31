import os
import jwt
import datetime
import httpx
from graphlit_api.client import Client

class Graphlit:
    def __init__(self, organization_id=None, environment_id=None, jwt_secret=None, owner_id=None, user_id=None, api_uri=None):
        self.organization_id = organization_id if organization_id is not None else os.getenv("GRAPHLIT_ORGANIZATION_ID")
        self.environment_id = environment_id if environment_id is not None else os.getenv("GRAPHLIT_ENVIRONMENT_ID")
        self.owner_id = owner_id if owner_id is not None else os.getenv("GRAPHLIT_OWNER_ID")
        self.user_id = user_id if user_id is not None else os.getenv("GRAPHLIT_USER_ID")
        self.secret_key = jwt_secret if jwt_secret is not None else os.getenv("GRAPHLIT_JWT_SECRET")
        self.api_uri = api_uri if api_uri is not None else "https://data-scus.graphlit.io/api/v1/graphql/"
        
        self.refresh_client()
        
    def refresh_client(self):
        self.client = None
        self._generate_token()
        
        headers = {"Authorization": f"Bearer {self.token}"}

        timeout = httpx.Timeout(connect=10.0, read=600.0, write=10.0, pool=60.0)
        
        self.client = Client(url=self.api_uri, headers=headers)
        self.client.http_client.timeout = timeout

    def _generate_token(self):
        expiration = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(days=1)
        
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
        
        if self.user_id is not None:
            payload["https://graphlit.io/jwt/claims"]["x-graphlit-user-id"] = self.user_id
        
        if self.secret_key is None:
            raise ValueError("JWT secret key is required. Please provide it via jwt_secret parameter or GRAPHLIT_JWT_SECRET environment variable.")
        
        self.token = jwt.encode(payload, self.secret_key, algorithm="HS256")
