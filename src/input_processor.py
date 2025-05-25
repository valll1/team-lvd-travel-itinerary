''' The functions do the following things:

    process_dates: Recieves the city, start date, and end date from the users through gradio, formatting it for proper API calling. It returns the
    Ollama AI-Generated response back to the user.

    extract_event_names: Extracts the names of the top events provided by the API call and puts it into a list
'''

# import libraries
from datetime import datetime

def process_dates(city, start_date,
                  end_date=None):  # Function that takes the date from the datetime box and formats it for api
    todays_date = datetime.today()  # Stores today's date into a variable
    formatted_city = city.capitalize()  # Formats the city name
    # Converts the timestamp into a datetime object
    start_datetime_ob = datetime.fromtimestamp(start_date)
    end_datetime_ob = datetime.fromtimestamp(end_date)

    if (end_datetime_ob >= start_datetime_ob):  # Makes sure that the Start Date is before the end date

        if start_datetime_ob.date() >= todays_date:  # Makes sure that the event is either today or later
            start_datetime_iso = start_datetime_ob.isoformat() + 'Z'  # Converts the datetime object into ISO format – The format used by the ticketmaster event
            end_datetime_iso = end_datetime_ob.isoformat() + 'Z'

            stored_events = get_top_events(formatted_city, Ticketmaster_API_KEY, start_datetime_iso,
                                           end_datetime_iso)  # Runs the api and stores the return data into variable

            return generate_with_ollama(formatted_city, start_date, end_date,
                                        extract_event_names(stored_events))  # returns the ollama response

        else:
            return "Start date must be today or later."
    else:
        return (f'Trip end date must be after {start_datetime_ob.date()}!')

def extract_event_names(event_dict):
  events_list = [] # Empty list for events
  for x in events['events']:
    if x['name'] not in events_list:
      events_list.append(x['name']) # Appends the event name into events_list
    else:
      continue
  return events_list


