# /events
Return data for all events.

## Use cases
Events page, to show a list of all events.

We may or may not go with an EMA-like setup where you can only look at data for one year at a time.

## URL parameters

### page
_(optional)_ Which page to get.

### per_page
_(optional)_ Number of records per page. Default value is 100.

### event_region
_(optional)_ Event region(s). Any records not matching the given region(s) should not be included in the response.

### event_type
_(optional)_ Type of event. Any records not of this type should not be included in the response.

### from_date
_(optional)_ Start date of lookup window. Any records with an **end date** earlier than this value should not be
included in the response.

### until_date
_(optional)_ End date of lookup window. Any records with an **end date** later than this value should not be included in
the response.

### event_city
_(optional)_ Event city. Any records not matching the given city should not be included in the response.

### event_country
_(optional)_ Event country. Any records not matching the given country should not be included in the response.

### minimum_player_count
_(optional)_ Minimum number of players. Any records with a player number lower than this value should not be included in
the response.

### online
_(optional)_
`true` or `false`. If true, response should contain online events only. If false, response should contain live events
only. If unspecified, response should contain all events.

## Request body
N/A

## Example calls
- `https://riichi.ca/api/v1/events`
- `https://riichi.ca/api/v1/events?page=2&per_page=50`
- `https://riichi.ca/api/v1/events?online=false`
- `https://riichi.ca/api/v1/events?event_region=1&minimum_player_count=32`
- `https://riichi.ca/api/v1/events?event_region=1,2,3&from_date=2018-01-01`
- `https://riichi.ca/api/v1/events?event_country=Canada&event_type=1`

## Expected response
HTTP 200

GET `https://riichi.ca/api/v1/events?page=2&per_page=50`
```json
{
  "metadata":
  {
    "page": 2,
    "per_page": 50,
    "page_count": 3,
    "total_count": 130,
    "links": [
      {"self": "/events?page=2&per_page=50"},
      {"first": "/events?page=1&per_page=50"},
      {"previous": "/events?page=1&per_page=50"},
      {"next": "/events?page=3&per_page=50"},
      {"last": "/events?page=3&per_page=50"}
    ]
  },
  "records": [
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
    },
    ...
  ]
}
```

---

HTTP 200

GET `https://riichi.ca/api/v1/events?from_date=2022-01-01&until_date=2024-12-31&event_type=1&event_region=1,2,3,4,5`
```json
{
  "metadata":
  {
    "event_region": [1, 2, 3, 4, 5],
    "event_type": 1,
    "from_date": "2022-01-01",
    "until_date": "2024-12-31",
    "page": 1,
    "per_page": 100,
    "page_count": 1,
    "total_count": 12,
    "links": [
      {"self": "/events?page=1&per_page=100&from_date=2022-01-01&until_date=2024-12-31&event_type=1&event_region=1,2,3,4,5"},
      {"first": "/events?page=1&per_page=100&from_date=2022-01-01&until_date=2024-12-31&event_type=1&event_region=1,2,3,4,5"},
      {"last": "/events?page=1&per_page=100&from_date=2022-01-01&until_date=2024-12-31&event_type=1&event_region=1,2,3,4,5"}
    ]
  },
  "records": [
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

`event_region` is a non-integer
```json
{
  "error": {
    "code": 400,
    "type": "Bad Request", 
    "message": "'event_region' parameter must be an integer"
  }
}
```

`event_type` is a non-integer
```json
{
  "error": {
    "code": 400,
    "type": "Bad Request", 
    "message": "'event_type' parameter must be an integer"
  }
}
```

`from_date` is not a valid date
```json
{
  "error": {
    "code": 400,
    "type": "Bad Request", 
    "message": "'from_date' parameter must be a date"
  }
}
```

`until_date` is not a valid date
```json
{
  "error": {
    "code": 400,
    "type": "Bad Request", 
    "message": "'until_date' parameter must be a date"
  }
}
```

`minimum_player_count` is a non-integer
```json
{
  "error": {
    "code": 400,
    "type": "Bad Request", 
    "message": "'minimum_player_count' parameter must be an integer"
  }
}
```

`online` is not a string
```json
{
  "error": {
    "code": 400,
    "type": "Bad Request", 
    "message": "'online' parameter must be a string"
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

No results for given parameters
```json
{
  "error": {
    "message": "No records matching given parameters",
    "parameters": {
      "event_region": [1, 2, 3],
      "from_date": "2020-01-01",
      "minimum_player_count": 100,
      "online": false
    }
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

`event_region` is below 1
```json
{
  "error": {
    "code": 422,
    "type": "Unprocessable Entity", 
    "message": "'event_region' parameter value must be greater than 0"
  }
}
```

`event_type` is below 1
```json
{
  "error": {
    "code": 422,
    "type": "Unprocessable Entity", 
    "message": "'event_type' parameter value must be greater than 0"
  }
}
```

`from_date` is before `2000-01-01`, or is in the future
```json
{
  "error": {
    "code": 422,
    "type": "Unprocessable Entity", 
    "message": "'from_date' parameter value must be between 2000-01-01 and today"
  }
}
```

`until_date` is before `2000-01-01`, or is in the future
```json
{
  "error": {
    "code": 422,
    "type": "Unprocessable Entity", 
    "message": "'until_date' parameter value must be between 2000-01-01 and today"
  }
}
```

`minimum_player_count` is below 1
```json
{
  "error": {
    "code": 422,
    "type": "Unprocessable Entity", 
    "message": "'minimum_player_count' parameter value must be greater than 0"
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