import os
import requests
import jwt
import datetime

class Graphlit:
    def __init__(self, environment_id=None, organization_id=None, secret_key=None):
        # Get environment variables or use default values
        self.issuer = os.getenv("ISSUER", "graphlit")
        self.audience = os.getenv("AUDIENCE", "https://portal.graphlit.io")
        self.role = os.getenv("ROLE", "Owner")

        # Get other environment variables or use parameters
        self.environment_id = environment_id if environment_id is not None else os.getenv("ENVIRONMENT_ID")
        self.organization_id = organization_id if organization_id is not None else os.getenv("ORGANIZATION_ID")
        self.secret_key = secret_key if secret_key is not None else os.getenv("SECRET_KEY")

        self.base_url = "https://data-scus.graphlit.io/api/v1" # Example base URL

        # Specify the expiration (one hour from now)
        expiration = datetime.datetime.utcnow() + datetime.timedelta(hours=1)

        # Define the payload
        payload = {
            "https://graphlit.io/jwt/claims": {
                "x-graphlit-environment-id": self.environment_id,
                "x-graphlit-organization-id": self.organization_id,
                "x-graphlit-role": self.role,
            },
            "exp": expiration,
            "iss": self.issuer,
            "aud": self.audience,
        }

        # Sign the JWT
        self.token = jwt.encode(payload, self.secret_key, algorithm="HS256")

    def request(self, query, variables={}):
        token = self.token
        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }
        payload = {
            "query": query,
            "variables": variables
        }
        response = requests.post(f"{self.base_url}/graphql", json=payload, headers=headers)
        return response.json()
