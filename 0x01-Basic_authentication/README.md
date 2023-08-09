Simple API
Simple HTTP API for playing with User model.

Files
models/
base.py: base of all models of the API - handle serialization to file
user.py: user model
api/v1
app.py: entry point of the API
views/index.py: basic endpoints of the API: /status and /stats
views/users.py: all users endpoints
Setup
$ pip3 install -r requirements.txt
Run
$ API_HOST=0.0.0.0 API_PORT=5000 python3 -m api.v1.app
Routes
GET /api/v1/status: returns the status of the API
GET /api/v1/stats: returns some stats of the API
GET /api/v1/users: returns the list of users
GET /api/v1/users/:id: returns an user based on the ID
DELETE /api/v1/users/:id: deletes an user based on the ID
POST /api/v1/users: creates a new user (JSON parameters: email, password, last_name (optional) and first_name (optional))
PUT /api/v1/users/:id: updates an user based on the ID (JSON parameters: last_name and first_name)

Basic authentication is a simple method used for authenticating users in web applications or APIs. It involves sending a username and password with each request to the server. However, it's important to note that Basic authentication is considered relatively insecure because the credentials are transmitted in an easily readable format, known as base64 encoding, which can be decoded by anyone with the right tools.
Here's how Basic authentication works:

Request: When a client (usually a web browser or a software application) wants to access a protected resource, it sends an HTTP request to the server.
Credentials: The client encodes the username and password into a single string using base64 encoding. This string is usually constructed in the format: "username:password".
Header: The encoded string is then included in the Authorization header of the HTTP request. The header looks like this:
Server Validation: The server receives the request and extracts the base64-encoded credentials from the Authorization header.
Decoding: The server decodes the base64-encoded credentials to retrieve the original username and password.
Authentication: The server then checks the validity of the username and password against its authentication system (such as a database of users).
Response: If the credentials are valid, the server grants access to the requested resource and returns the appropriate response. If the credentials are invalid, the server returns an error response (usually a 401 Unauthorized status code).
Here's an example of how Basic authentication might look in an HTTP request:
GET /secure/resource HTTP/1.1
Host: example.com
Authorization: Basic dXNlcm5hbWU6cGFzc3dvcmQ=
In this example, the base64-encoded credentials for the username "username" and password "password" are "dXNlcm5hbWU6cGFzc3dvcmQ=".
While Basic authentication is simple to implement, its security shortcomings make it unsuitable for protecting sensitive information. For more secure authentication, consider using protocols like OAuth or token-based authentication, which don't involve sending actual usernames and passwords with each request.