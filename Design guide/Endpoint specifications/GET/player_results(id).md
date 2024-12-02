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