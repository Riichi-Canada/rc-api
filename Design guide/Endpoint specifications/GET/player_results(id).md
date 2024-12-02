# /player_results/{player_id}
Return all event results for a given player.

## Use cases
Player page, to show the player's results.

## URL parameters
N/A

## Request body
N/A

### Example calls
`https://riichi.ca/api/v1/player_results/14`

## Expected response
HTTP 200

GET `https://riichi.ca/api/v1/player_results/14`
```json
{
  "records": [
    {
      "id": 32,
      "event_id": "2024-020002",
      "event_type": 2,
      "event_start_date": "2024-02-04",
      "event_end_date": "2024-05-20",
      "placement": 9,
      "number_of_players": 23,
      "2025_main_points": 636,
      "2025_tank_points": 69.58
    },
    {
      "id": 1500,
      "event_id": "2022-010002",
      "event_type": 1,
      "event_start_date": "2022-06-11",
      "event_end_date": "2022-06-12",
      "placement": 16,
      "number_of_players": 24,
      "2025_main_points": 347,
      "2025_tank_points": 0
    },
    ...
  ]
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