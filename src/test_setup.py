'''
This function checks if the Python environment is properly set up. 
It verifies the python version, virtual environment, Gradio and Ollama installations, .env file, and locl Ollama server availability.
'''

import sys
import os
import requests
from dotenv import load_dotenv

def check_environment():

  # Check Python version
  print(f'Python version: {sys.version}')

  # Check virtual environment
  if hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix):
    print("Virtual environment is active")
  else:
    print("Virtual environment is NOT active")

  # Check required packages
  try:
    import gradio
    print(f"Gradio installed (version {gradio.__version__})")
  except ImportError:
      print("Gradio not installed")
  try:
    import ollama
    print(f"Ollama client installed")
  except ImportError:
    print("Ollama client not installed")

  # Check .env file
  # Load environment variables
  load_dotenv()

  # Get API key from environment
  Ticketmaster_API_KEY = os.getenv('Ticketmaster_API_KEY')

  if Ticketmaster_API_KEY:
    print("Ticketmaster_API_KEY found in .env file")
  else:
    print("Ticketmaster_API_KEY not found in .env file")

  # Check Ollama availability
  try:
    response = requests.post(
        'http://localhost:11434/api/generate',
        json={
          "model": "mistral",
          "prompt": "Hello",
          "stream": False
        }
      )
    if response.status_code == 200:
        print(f'Ollama is running and responding')
    else:
        print(f'Ollama returned status code: {response.status_code}')
  except Exception as e:
    print(f'Ollama not available: {str(e)}')
    print('Make sure Ollama is installed and running.')

# Run the environment check if this script is executed directly.
if __name__ == "__main__":
  check_environment()