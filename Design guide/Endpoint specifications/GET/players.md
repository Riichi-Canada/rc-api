# /players
Return data for all players.

## Use cases
Player rankings page, to display a table with rows containing a player's first/last name, region, club and ranking score.

## URL parameters

### page
_(optional)_ Which page to get.

### per_page
_(optional)_ Number of records per page. Default value is 100.

### score_limit_2025
_(optional)_ Minimum score for the player to be shown (default value = 0). Any player with a score lower than this parameter should not be included in the return data.

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
  "metadata": {
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

`page` is a non-integer
```json
{
  "error": {
    "code": 400,
    "type": "Bad Request", 
    "message": "'page' parameter must be an integer"
  }
}
```

`per_page` is a non-integer
```json
{
  "error": {
    "code": 400,
    "type": "Bad Request", 
    "message": "'per_page' parameter must be an integer"
  }
}
```

`score_limit_2025` is not a number
```json
{
  "error": {
    "code": 400,
    "type": "Bad Request", 
    "message": "'score_limit_2025' parameter must be a number"
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
Client tries to go to page X+1 or greater when there are only X pages
```json
{
  "error": {
    "code": 404,
    "type": "Not Found",
    "message": "Page {page} not found"
  }
}
```

No player found with score greater than or equal to value of `score_limit_2025`
```json
{
  "error": {
    "code": 404,
    "type": "Not Found",
    "message": "No player found with 2025 score greater than or equal to {score_limit_2025}"
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

### 422 Unprocessable Entity
`page` is below 1
```json
{
  "error": {
    "code": 422,
    "type": "Unprocessable Entity", 
    "message": "'page' parameter value must be greater than 0"
  }
}
```

`per_page` is below 1
```json
{
  "error": {
    "code": 422,
    "type": "Unprocessable Entity", 
    "message": "'per_page' parameter value must be greater than 0"
  }
}
```

`score_limit_2025` is not between 0 and 6000
```json
{
  "error": {
    "code": 422,
    "type": "Unprocessable Entity", 
    "message": "'score_limit_2025' parameter value must be between 0 and 6000"
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