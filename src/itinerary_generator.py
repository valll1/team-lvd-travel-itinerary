#import libraries
import requests
from datetime import datetime

def check_ollama_availability():
  '''
    This function checks if Ollama is available and running.
  '''
  try:
    response = requests.post(
        'http://localhost:11434/api/generate',
        json={
          "model": "mistral",
          "prompt": "Hello",
          "stream": False
        },
        timeout=5 # 5 second timeout
      )
    if response.status_code == 200:
      return True, {"status": "available", "message": "Ollama is running and responding correctly."}
    else:
      return False, {"status": "error", "message": f"Ollama returned status code: {response.status_code}"}
  except requests.exceptions.ConnectionError:
    return False, {"status": "connection_error", "message": "Ollama is not available."}
  except requests.exceptions.Timeout:
    return False, {"status": "timeout", "message": "Connection to Ollama timed out. The server might be overloaded."}
  except Exception as e:
    return False, {"status": "unknown_error", "message": f"An unexpected error occurred: {str(e)}"}




def generate_with_ollama(city, start_date, end_date, events):
  '''
    This function uses AI to generate a personalized travel itinerary based on the provided events and trip details.
  '''
  #check if Ollama is available
  if not check_ollama_availability():
    return 'Ollama is not available. Please check if it is running and try again later.'

  #calculate length of trip
  start_from_timestamp = datetime.fromtimestamp(start_date) # turn the unixtime stamp into a datetime
  end_from_timestamp = datetime.fromtimestamp(end_date)
  length = (end_from_timestamp - start_from_timestamp).days + 1 #plus 1 to include arrival and departure date

  prompt = f"""
    I am planning a {length} day trip to {city}.
    Please generate a organized and balanced personalized itinerary based on the following events:
    {events}.
    The itinerary should be realistic and include breaks between events.
    Please organize it in readable bullet points and seperate by each day.
  """

  #send to Ollama
  try:
    response = requests.post(
        'http://localhost:11434/api/generate',
        json={
          "model": "mistral",
          "prompt": prompt,
          "stream": False,
          "temperature": 0.7,
        }
      )
    if response.status_code == 200:
      result = response.json()
      return result.get('response','No response generated')
    else:
      return f'Error communicating with Ollama: {response.status_code}'
  except Exception as e:
    return f'Error communicating with Ollama: {str(e)}'
