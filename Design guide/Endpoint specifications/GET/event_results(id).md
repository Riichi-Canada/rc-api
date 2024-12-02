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
	"message": "Unexpected URL parameter {parameter}"
}
```

Request body is not empty
```json
{
	"message": "Unexpected request body"
}
```

### 401 Unauthorized
Not using the basic "non-admin" API key
```json
{
	"message": "Unauthorized"
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
	"message": "Method is not allowed"
}
```

### 406 Not Acceptable
If the client can't accept JSON
```json
{
	"message": "Only 'application/json' content type is supported"
}
```

### 429 Too Many Requests
Gonna have to look into rate limiting...
```json
{
	"message": "Too many requests! Try again later."
}
```