# /events/{event_id}
Return data for a specific event.

## Use cases
Event page, to get an event's data.

## URL parameters
N/A

## Request body
N/A

## Example calls
`https://riichi.ca/api/v1/events/2024-010011`

## Expected return data
HTTP 200

GET `https://riichi.ca/api/v1/events/2024-010011`
```json
{
  "id": 51,
  "event_id": "2024-010011",
  "event_name": "Montréal Riichi Open 2024",
  "event_region": 1,
  "event_type": 1,
  "event_start_date": "2024-06-01",
  "event_end_date": "2024-06-02",
  "event_city": "Montréal",
  "event_country": "Canada",
  "number_of_players": 32,
  "is_online": false
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
    "message": "No event with id {id}"
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