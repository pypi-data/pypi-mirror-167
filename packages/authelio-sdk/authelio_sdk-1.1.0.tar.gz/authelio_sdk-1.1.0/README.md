# Authelio Python SDK

## Description

**Authelio Python SDK** allows an easy and fast integration with **AUTHELIO** - authentication and authorization API.

#### Remarks

[Biomapas](https://biomapas.com) aims to modernize life-science
industry by sharing its IT knowledge with other companies and
the community. This is an open source library intended to be used
by anyone. Improvements and pull requests are welcome.

#### Related technology

- Python 3

#### Assumptions

The project assumes the following:

- You have basic-good knowledge in python programming.

#### Install

The project is built and uploaded to PyPi. Install it by using pip.

```
pip install authelio_sdk
```

Or directly install it through source.

```
pip install .
```

## Usage & Examples

### SDK client

Create **Authelio SDK** client using the given **AUTHELIO PUBLIC API URL**, **API KEY**, and **API SECRET**:

```python
from authelio_sdk.client import Client
from authelio_sdk.config import Config

AUTHELIO_PUBLIC_API_URL = 'http://localhost'
AUTHELIO_API_KEY = 'DFCC345BE3C0DC42DF8A123F7579'
AUTHELIO_API_SECRET = '4AomCEeUG2j7epT87GahHfh2e8YnaDRthx5k0zfgnnY='

sdk_client = Client(
    api_key=AUTHELIO_API_KEY,
    api_secret=AUTHELIO_API_SECRET,
    config=Config(
        public_api_url=AUTHELIO_PUBLIC_API_URL
    )
)
```

### Hosted login page

To get hosted login page URL, use SDK client method - `user.login`.

**Request syntax:**

```python
response = sdk_client.user.login(
    redirect_uri='https://example.com',
    response_type='code'
)
```

**Parameters**

- **redirect_uri** (string) [OPTIONAL] - URI of the resource for which login page is required. 
If omitted default resource URI will be used.
- **response_type** (string) [OPTIONAL] - The response type. Must be either `code` or `token`. 
Indicates whether the client wants an authorization code for the user (authorization code grant flow), 
or directly issues tokens for the user (implicit flow). Default: `code`

**Returns**

Hosted login page URL.

Return Type: String

### Create a user

To create user, use SDK client method - `user.create`.

**Request syntax:**

```python
response = sdk_client.user.create(
    email='string',
    username='string',
    first_name='string',
    last_name='string',
    user_id='string',
    group_ids=['string', 'string', '...'],
    permissions=['string', 'string', '...']
)
```

**Parameters**

- **email** (string) [REQUIRED] - Email address of the user.
- **preferred_username** (string) [REQUIRED] - Preferred username of the user.
- **first_name** (string) [REQUIRED] - Given name of the user.
- **last_name** (string) [REQUIRED] - Family name of the user.
- **username** (string) [OPTIONAL] - Unique idnetifier of the user.
- **group_ids** (list) [OPTIONAL] - A list of group unique identifiers.
- **permissions** (list) [OPTIONAL] - A list of user permissions.

**Returns**

Return Type: User

**User Attributes**:

- **username** (string) - Unique identifier of newly created user.
- **preferred_username** (string) - Preferred username of newly created user.
- **email** (string) - Email address of newly created user.
- **first_name** (string) - Given name of newly created user.
- **last_name** (string) - Family name of newly created user.
- **tmp_password** (string) - Temporary password of newly created user.
- **group_ids** (list) - A list of unique identifiers of assigned permission groups.
- **permissions** (list) - A list of directly assigned user permissions.

### Get User

Retrieval of previously created user.

**Request syntax:**

```python
response = sdk_client.user.get(user_id='string')
```

**Parameters**

- **username** (string) [REQUE] - Unique idnetifier of the user.

**Returns**

Return Type: User

**User Attributes**:

- **username** (string) - Unique identifier of newly created user.
- **preferred_username** (string) - Preferred username of newly created user.
- **email** (string) - Email address of newly created user.
- **first_name** (string) - Given name of newly created user.
- **last_name** (string) - Family name of newly created user.
- **group_ids** (list) - A list of unique identifiers of assigned permission groups.
- **permissions** (list) - A list of directly assigned user permissions.
- **is_active** (bool) - Specifies whether the user is enabled.

Please check the documentation available here, which contains information on how to use the library, 
and a complete API reference guide.

#### Testing

The project has tests that can be run. Simply run:

```
pytest authelio_sdk_tests
```

#### Contribution

Found a bug? Want to add or suggest a new feature?<br>
Contributions of any kind are gladly welcome. You may contact us
directly, create a pull-request or an issue in github platform.
Lets modernize the world together.
