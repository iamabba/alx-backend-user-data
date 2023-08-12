Session authentication is a security mechanism used in web applications to ensure that users are who they claim to be before granting them access to certain resources or functionalities. It is a crucial component of web application security, as it helps prevent unauthorized access and protect sensitive data.

Here's how session authentication generally works:

User Login: When a user enters their credentials (such as username and password) on a web application, the server verifies the provided information. If the credentials are valid, the server creates a session for that user.

Session Creation: A session is a temporary storage container on the server that holds information about the user's identity and other relevant data. A unique session identifier (often stored in a cookie on the user's device) is generated and sent back to the user's browser. This identifier is used to associate subsequent requests from the same user with their specific session.

Session Management: During the user's interaction with the application, the session identifier is included in each request sent to the server. The server uses this identifier to look up the corresponding session data and verify the user's identity.

Authorization and Access Control: Once the user is authenticated through their session, the application can determine what resources or functionalities the user is allowed to access based on their user role and permissions. This helps ensure that users only have access to the parts of the application that they are authorized to use.

Session Expiry: Sessions usually have a limited duration to prevent attackers from hijacking a session and gaining prolonged access. The session duration can be set by the application and is commonly controlled by a combination of server-side settings and the expiration time set in the user's session cookie.

Logout: When a user logs out, their session data is typically invalidated on the server side, and the session identifier is marked as invalid. This prevents any further requests with that identifier from being considered valid.

It's important to note that while session authentication is a widely used approach, it's not without its security concerns. For instance:

Session Hijacking: Attackers might try to steal a user's session identifier to gain unauthorized access. This can be mitigated through techniques such as using secure cookies, implementing Transport Layer Security (TLS), and regularly rotating session identifiers.

Session Fixation: Attackers could potentially fix a session identifier to a known value, allowing them to predict and use the identifier to gain unauthorized access. Protecting against this requires generating a new session identifier upon login and properly managing the old session data.

Session Expiry: If session expiry times are set too long, attackers have more time to exploit stolen session identifiers. Conversely, if they are set too short, users might be frequently prompted to re-authenticate.

Cross-Site Scripting (XSS): Vulnerabilities like XSS can expose session identifiers to attackers, who can then use them to impersonate users.

# Simple API

Simple HTTP API for playing with `User` model.


## Files

### `models/`

- `base.py`: base of all models of the API - handle serialization to file
- `user.py`: user model

### `api/v1`

- `app.py`: entry point of the API
- `views/index.py`: basic endpoints of the API: `/status` and `/stats`
- `views/users.py`: all users endpoints


## Setup

```
$ pip3 install -r requirements.txt
```


## Run

```
$ API_HOST=0.0.0.0 API_PORT=5000 python3 -m api.v1.app
```


## Routes

- `GET /api/v1/status`: returns the status of the API
- `GET /api/v1/stats`: returns some stats of the API
- `GET /api/v1/users`: returns the list of users
- `GET /api/v1/users/:id`: returns an user based on the ID
- `DELETE /api/v1/users/:id`: deletes an user based on the ID
- `POST /api/v1/users`: creates a new user (JSON parameters: `email`, `password`, `last_name` (optional) and `first_name` (optional))
- `PUT /api/v1/users/:id`: updates an user based on the ID (JSON parameters: `last_name` and `first_name`)