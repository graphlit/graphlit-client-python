import os
import jwt
import datetime
import httpx
from graphlit_api.client import Client

class Graphlit:
    def __init__(self, organization_id=None, environment_id=None, jwt_secret=None, owner_id=None, api_uri=None):
        self.organization_id = organization_id if organization_id is not None else os.getenv("GRAPHLIT_ORGANIZATION_ID")
        self.environment_id = environment_id if environment_id is not None else os.getenv("GRAPHLIT_ENVIRONMENT_ID")
        self.owner_id = owner_id if owner_id is not None else os.getenv("GRAPHLIT_OWNER_ID")
        self.secret_key = jwt_secret if jwt_secret is not None else os.getenv("GRAPHLIT_JWT_SECRET")

        self.api_uri = api_uri if api_uri is not None else "https://data-scus.graphlit.io/api/v1/graphql/"

        # Specify the expiration (one hour from now in UTC)
        expiration = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=1)

        # Define the payload
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

        # Sign the JWT
        self.token = jwt.encode(payload, self.secret_key, algorithm="HS256")

        headers = {"Authorization": f"Bearer {self.token}"}

        self.client = Client(url=self.api_uri, headers=headers)
        self.client.http_client.timeout = httpx.Timeout(timeout=600.0)