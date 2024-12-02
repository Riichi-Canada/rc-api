# /event_results/{event_id}
Return results for a given event.

## Use cases
Event page, to show the event's results.

## URL parameters
N/A

## Request body
N/A

### Example calls
`https://riichi.ca/api/v1/event_results/2024-010011`

## Expected response
2025 scores should only appear if the result points to a registered player (`player_id` is defined).

If `placement` is negative (ex. `–2`), it indicates the player did not finish the tournament (disqualified or other).

HTTP 200

GET `https://riichi.ca/api/v1/event_results/2024-010011`
```json
{
	"records": [
        {
			"id": 1549,
			"player_first_name": "Jason",
			"player_last_name": "Qin",
			"placement": 1,
			"score": 51700,
		},
		{
			"id": 1550,
			"player_id": 4,
			"player_first_name": "Michael",
			"player_last_name": "McLeod",
			"placement": 2,
			"score": 33400,
			"2025_main_score": 967,
			"2025_tank_score": 200
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

### 404 Not Found
Self-explanatory
```json
{
	"message": "No data found at id {event_id}"
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