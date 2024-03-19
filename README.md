# graphlit-client-python

## Overview

The Graphlit Client for Python enables easy interaction with the Graphlit API, allowing developers to execute queries and mutations against the Graphlit service. This document outlines the setup process and provides a basic example of using the client.

## Prerequisites

Before you begin, ensure you have the following:

- Python 3.x installed on your system.
- An active account on [grahlit.com](https://grahlit.com) with access to the API settings dashboard.

## Installation

To install the Graphlit Client, use pip:

```bash
pip install graphlit-client
```

## Configuration

The Graphlit Client requires three environment variables to be set for authentication and configuration:

- `ENVIRONMENT_ID`: Your environment ID.
- `ORGANIZATION_ID`: Your organization ID.
- `SECRET_KEY`: Your secret key for API access.

You can find these values in the API settings dashboard on [grahlit.com](https://grahlit.com).

### Setting Environment Variables

To set these environment variables on your system, use the following commands, replacing `your_value` with the actual values from your account.

For Unix/Linux/macOS:

```bash
export ENVIRONMENT_ID=your_environment_id_value
export ORGANIZATION_ID=your_organization_id_value
export SECRET_KEY=your_secret_key_value
```

For Windows Command Prompt (CMD):

```cmd
set ENVIRONMENT_ID=your_environment_id_value
set ORGANIZATION_ID=your_organization_id_value
set SECRET_KEY=your_secret_key_value
```

For Windows PowerShell:

```powershell
$env:ENVIRONMENT_ID="your_environment_id_value"
$env:ORGANIZATION_ID="your_organization_id_value"
$env:SECRET_KEY="your_secret_key_value"
```

## Usage Example

Here's a simple example of how to use the Graphlit Client to create a Feed.

```python
from graphlit_client import Graphlit

# Initialize the client
client = Graphlit()

# Print the client token
print(client.token)

# Execute a query
response = client.request(query="""
mutation CreateFeed($feed: FeedInput!) {
  createFeed(feed: $feed) {
    id
    name
    state
    type
  }
}""", variables={
  "feed": {
    "type": "WEB",
    "web": {
      "uri": "https://openai.com/blog"
    },
    "name": "OpenAI Blog"
  }
})

# Print the response
print(response)
```

## Support

For issues and support with the Graphlit Client or API, please visit [Graphlit Support](https://graphlit.com/).
