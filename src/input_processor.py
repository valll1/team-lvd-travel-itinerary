''' The functions do the following things:

    process_dates: Recieves the city, start date, and end date from the users through gradio, formatting it for proper API calling. It returns the
    Ollama AI-Generated response back to the user.

    extract_event_names: Extracts the names of the top events provided by the API call and puts it into a list
'''

# import libraries
import os
from datetime import datetime
from ticketmaster_api import get_top_events
from itinerary_generator import generate_with_ollama


def process_dates(city, start_date, end_date):  # Function that takes the date from the datetime box and formats it for api
    if not city and start_date and end_date:
        return "Please provide a city, a start date and an end date!"

    try:
        Ticketmaster_API_KEY = os.getenv("Ticketmaster_API_KEY")
        if not Ticketmaster_API_KEY:
            raise ValueError("Ticketmaster_API_KEY not found in environment variables.")
        
        todays_date = datetime.today().date()  # Stores today's date into a variable
        formatted_city = city.title().strip()  # Formats the city name

        # Converts the timestamp into a datetime object
        start_datetime_ob = datetime.fromtimestamp(start_date)
        end_datetime_ob = datetime.fromtimestamp(end_date)

        # Makes sure that the Start Date is before the end date
        if start_datetime_ob > end_datetime_ob:
            return f"Trip end date must be after {start_datetime_ob.date()}!"

        if start_datetime_ob.date() < todays_date:
            return "Start date must be today or later."

        # Converts the datetime object into ISO format – The format used by the ticketmaster event
        start_datetime_iso = start_datetime_ob.isoformat() + 'Z'
        end_datetime_iso = end_datetime_ob.isoformat() + 'Z'

        stored_events = get_top_events(formatted_city, Ticketmaster_API_KEY, start_datetime_iso, end_datetime_iso)  # Runs the api and stores the return data into variable
        event_names = extract_event_names(stored_events)
        generated_itinerary = generate_with_ollama(formatted_city, start_date, end_date,event_names)

        return generated_itinerary # Returns the ollama generated response

    except Exception as e:
        return f"An error occurred: {str(e)}"


def extract_event_names(event_dict):
    events_list = [] # Where the even names will be stored
    for x in event_dict['events']:
        # Appends the event name if it's not in the list
        if x['name'] not in events_list:
            events_list.append(x['name'])

    return events_list # Returns the event_list


