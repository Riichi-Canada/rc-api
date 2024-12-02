# /players/{player_id}
Return data for a specific player.

## Use cases
Player page, to get a player's data.

## URL parameters
N/A

## Request body
N/A

## Example calls
`https://riichi.ca/api/v1/players/1`

## Expected return data
HTTP 200

GET `https://riichi.ca/api/v1/players/1`
```json
{
  "id": 1,
  "first_name": "Loïc",
  "last_name": "Roberge",
  "region": 1,
  "club": 1,
  "score_2025_cycle": 4937.11
}
```

## Error codes to handle

### 400 Bad Request
Unexpected URL parameters
```json
{
  "error": {
    "code": 400,
    "type": "Bad Request",
    "message": "Unexpected URL parameter",
    "parameters": ["{param1}", "{param2}"]
  }
}
```

Request body is not empty
```json
{
  "error": {
    "code": 400,
    "type": "Bad Request",
    "message": "Unexpected request body (must be empty)"
  }
}
```

### 401 Unauthorized
Not using the basic "non-admin" API key
```json
{
  "error": {
    "code": 401,
    "type": "Unauthorized",
    "message": "An API key is required to access this endpoint"
  }
}
```

Provided API key is invalid
```json
{
  "error": {
    "code": 401,
    "type": "Unauthorized",
    "message": "Provided API key is invalid"
  }
}
```

### 404 Not Found
Self-explanatory

```json
{
  "error": {
    "code": 404,
    "type": "Not Found",
    "message": "No player with id {player_id}"
  }
}
```

### 405 Method Not Allowed
For anything that isn't GET
```json
{
  "error": {
    "code": 405,
    "type": "Method Not Allowed",
    "message": "Requested method {method} is not allowed for this endpoint.",
    "allowed_methods": [
      "GET"
    ]
  }
}
```

### 406 Not Acceptable
If the client can't accept JSON
```json
{
  "error": {
    "code": 406,
    "type": "Not Acceptable",
    "message": "Requested content type is not supported",
    "supported_types": [
      "application/json"
    ]
  }
}
```

### 429 Too Many Requests
If the documents don't yet specify how rate limiting will work for this API,
feel free to @ the author of these lines with your complaints.
```json
{
  "error": {
    "code": 429,
    "type": "Too Many Requests",
    "message": "You have exceeded the allowed number of requests. Please try again later.",
    "retry_after": 60,
    "limit": 100
  }
}
```