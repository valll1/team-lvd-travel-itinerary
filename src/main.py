'''
This function connects the Ticketmaster API, Ollama AI, and a Gradio user interface to run the app with the proper environment setup.
'''

import os
from dotenv import load_dotenv
from test_setup import check_environment
from itinerary_generator import check_ollama_availability
from gradio_ui import gradio_interface

def main():
    # Check the environment setup
    check_environment()

    # Check if the Ollama AI server is running
    result = check_ollama_availability()
    print(result[1]["message"])

    # If Ollama is not available, exit the app
    if not result[0]:
        print('Ollama is not available. Please make sure the Ollama server exists.')
        return

    # Launch the Gradio app
    load_dotenv()  
    app = gradio_interface()
    app.launch()

# Ensures the app runs only when the script is executed directly
if __name__ == "__main__":
    main()