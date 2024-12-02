# /clubs/{club_id}
Return data for the specified club.

## Use cases
Club page, to show data for a specific club.

## URL parameters
N/A

## Request body
N/A

## Example calls
`https://riichi.ca/api/v1/clubs/1`

## Expected return data
HTTP 200

GET `https://riichi.ca/api/v1/clubs/1`
```json
{
	"id": 1,
	"club_name": "Club Riichi de Montréal",
	"club_short_name": "CRM"
},
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
	"message": "No data found at id {club_id}"
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