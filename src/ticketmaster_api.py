'''
This function returns the top upcoming events in a city using the Ticketmaster API. The parameters that it uses includes city, Ticketmaster_API_KEY, start_date, and end_date. It will return a dictionary with city, events, or an error message.
'''

import requests
import os
import json
from dotenv import load_dotenv

def get_top_events(city, Ticketmaster_API_KEY, start_date=None, end_date=None):
    # Check for presence of the API key
    if not Ticketmaster_API_KEY:
        return {'error': "API key not found. Please provide your Ticketmaster key."}

    # Ticketmaster API endpoint and query parameters
    url = "https://app.ticketmaster.com/discovery/v2/events.json"
    params = {
        'apikey': Ticketmaster_API_KEY,
        'city': city,
        'sort': 'date,asc',
        'size': 5  # Limit results to 5 events
    }

    # Optionally add date range filters to the request
    if start_date:
        params['startDateTime'] = start_date
    if end_date:
        params['endDateTime'] = end_date

    try:
        # Send GET request to Ticketmaster API
        response = requests.get(url, params=params)
        data = response.json()

        # Debug output for testing
        print(response.url)           # Full request URL
        print(response.status_code)   # HTTP status code
        print(data)                   # Parsed JSON response

        # Check if events are present in the response
        if '_embedded' not in data or 'events' not in data['_embedded']:
            return {"error": "No events found or unexpected API response."}

        # Handle non-successful HTTP status codes
        if response.status_code != 200:
            return {'error': f'Ticketmaster API returned status: {response.status_code}'}

        # Extract and format event data
        events = []
        for event in data['_embedded']['events']:
            name = event.get("name")
            start = event.get("dates", {}).get("start", {}).get("localDate", "N/A")
            url = event.get("url")

            # Only include events that have both a name and a URL
            if name and url:
                events.append({
                    'name': name,
                    'start_time': start,
                    'url': url
                })

        return {'city': city, 'events': events}

    except Exception as e:
        # Return error information if the request or parsing fails
        return {'error': f'Exception occurred: {str(e)}'}