# /players
Return data for all players.

## Use cases
Player rankings page, to display a table with rows containing a player's first/last name, region, club and ranking score.

## URL parameters

### page
(optional) Which page to get.

### per_page
(optional) Number of records per page. Default value is 100.

### score_limit_2025
(optional) Minimum score for the player to be shown (default value = 0). Any player with a score lower than this parameter should not be included in the return data.

## Request body
N/A

## Example calls
- `https://riichi.ca/api/v1/players`
- `https://riichi.ca/api/v1/players?page=2&per_page=50`
- `https://riichi.ca/api/v1/players?page=3`
- `https://riichi.ca/api/v1/players?per_page=50&score_limit_2025=1000`

## Expected return data
HTTP 200

GET `https://riichi.ca/api/v1/players?page=2&per_page=100`
```json
{
	"metadata":
	{
		"score_limit_2025": 0,
		"page": 2,
		"per_page": 100,
		"page_count": 5,
		"total_count": 465,
		"links": [
			{"self": "/players?page=2&per_page=100"},
	        {"first": "/players?page=1&per_page=100"},
	        {"previous": "/players?page=1&per_page=100"},
	        {"next": "/players?page=3&per_page=100"},
	        {"last": "/players?page=5&per_page=100"}
		]
	},
	"records": [
		{
			"id": 101,
			"first_name": "Loïc",
			"last_name": "Roberge",
			"region": 1,
			"club": 1,
			"score_2025_cycle": 4937.11
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

`page` is a non-integer, or below 1
```json
{
	"message": "'page' parameter must be an integer greater than 0"
}
```

`per_page` is a non-integer, or below 1
```json
{
	"message": "'per_page' parameter must be an integer greater than 0"
}
```

`score_limit_2025` is not a number between 0 and 6000
```json
{
	"message": "'score_limit_2025' parameter must be a number between 0 and 6000"
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
Client tries to go to page X+1 or greater when there are only X pages
```json
{
	"message": "Page not found"
}
```

No player found with score greater than or equal to value of `score_limit_2025`
```json
{
	"message": "No player found with 2025 score greater than or equal to {score_limit_2025}"
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