# /clubs
Return data for all clubs.

## Use cases
Clubs page, to display info on all clubs.

## URL parameters
N/A

## Request body
N/A

## Example calls
`https://riichi.ca/api/v1/clubs`

## Expected return data
HTTP 200

GET `https://riichi.ca/api/v1/clubs`
```json
{
	"records": [
		{
			"id": 1,
			"club_name": "Club Riichi de Montréal",
			"club_short_name": "CRM"
		},
		{
			"id": 2,
			"club_name": "Toronto Riichi Club",
			"club_short_name": "TORI"
		},
		{
			"id": 3,
			"club_name": "University of British Columbia Mahjong Club",
			"club_short_name": "UBC Mahjong"
		},
		{
			"id": 4,
			"club_name": "Capital Riichi Club",
			"club_short_name": "CRC"
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