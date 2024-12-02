# /event_types
Return all possible event types and their corresponding number.

## Use cases
????

## URL parameters
N/A

## Request body
N/A

## Example calls
`https://riichi.ca/api/v1/event_types`

## Expected return data
HTTP 200

GET `https://riichi.ca/api/v1/event_types`
```json
{
	"records": [
		{
			"id": 1,
			"event_type": "Tournament"
		},
		{
			"id": 2,
			"event_type": "League"
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
