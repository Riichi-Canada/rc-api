# /events
Return data for all events.

## Use cases
Events page, to show a list of all events. We may or may not go with an EMA-like setup where you can only look at data for one year at a time.

## URL parameters

### page
(optional) Which page to get.

### per_page
(optional) Number of records per page. Default value is 100.

### event_region
(optional) Event region(s). Any records not matching the given region(s) should not be included in the response.

### event_type
(optional) Type of event. Any records not of this type should not be included in the response.

### from_date
(optional) Start date of lookup window. Any records with an **end date** earlier than this value should not be included in the response.

### until_date
(optional) End date of lookup window. Any records with an **end date** later than this value should not be included in the response.

### event_city
(optional) Event city. Any records not matching the given city should not be included in the response.

### event_country
(optional) Event city. Any records not matching the given country should not be included in the response.

### minimum_player_count
(optional) Minimum number of players. Any records with a player number lower than this value should not be included in the response.

### online
(optional) `true` or `false`. If true, response should contain online events only. If false, response should contain live events only. If unspecified, response should contain all events.

## Request body
N/A

### Example calls
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
			{"self": "/events?page=1&per_page=100"},
	        {"first": "/events?page=1&per_page=100"},
	        {"last": "/events?page=1&per_page=100"}
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

`event_region` is a non-integer, or below 1
```json
{
	"message": "'event_region' parameter must be an integer greater than 0"
}
```

`event_type` is a non-integer, or below 1
```json
{
	"message": "'event_type' parameter must be an integer greater than 0"
}
```

`from_date` is not a valid date, is before `2000-01-01`, or is in the future
```json
{
	"message": "'from_date' parameter must be a date between 2000-01-01 and today"
}
```

`until_date` is not a valid date, is before `2000-01-01`, or is in the future
```json
{
	"message": "'until_date' parameter must be a date between 2000-01-01 and today"
}
```

`minimum_player_count` is a non-integer, or is below 1
```json
{
	"message": "'minimum_player_count' parameter must be an integer greater than 0"
}
```

`online` is not either `true` or `false`
```json
{
	"message": "'online' parameter value must be either 'true' or 'false'"
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
	"message": "Page {page} not found"
}
```

No results for given parameters
```json
{
	"message": "No records matching given parameters",
	"parameters": {
		"event_region": [1, 2, 3],
		"from_date": "2020-01-01",
		"minimum_player_count": 100,
		"online": false
	}
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