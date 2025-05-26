# Project #3: Travel Itinerary Generator

This project involves implementing a Python program that generates a custom travel itinerary based on user input through a Gradio-built web application. Users are prompted to enter their destination city along with their trip's start and end dates and are returned with a travel itinerary generated using the Ollama language model. 

To run the program, run: python src/main.py

## Members: 
* Lydia Mei
* Valeria Ortega Preciado
* Dora Zhu 

## Allocation of tasks

Lydia Mei - Lydia implemented the function check_ollama_availability() to verify if the Ollama server is properly running and responding. The function tests the responsiveness while running the program and displays a message for the users if it fails after five seconds. Lydia also implemented the function generate_with_ollama, which receives four parameters to generate a personalized trip itinerary based on trip length, destination, and local events using AI. The function checks the availability of Ollama and sends a prompt using the data from the user inputs through the Gradio interface.


Valeria Ortega Preciado - Valeria implemented the gradio_interface function, which builds the user interface using Gradio. This interface allows users to input their destination city, trip start date, and trip end date – parameters that are used in the Ollama-generated response. Valeria also created the process_dates function to format these inputs for compatibility with API calls and the extract_event_names function to extract event names from the dictionary returned by get_top_events and return them as a list for use in the generate_with_ollama function. Lastly, Valeria implemented the .README file.

Dora Zhu - Dora implemented the test_setup.py to verify that the environment is working correctly. This includes checking the python version, the virtual environment, required packages needed to run the project (gradio, ollama), Ticketmaster_API_KEY in .env, and if Ollama will run and respond. Dora also implemented the event_analyzer.py to set up a basic Gradio interface that verifies environment components are properly set up. In addition, she implemented the ticketmaster_api.py, which returns the top upcoming events in a city using the Ticketmaster API by using several parameters. Lastly, she implemented the main.py, which connects all components of the project. It runs an environment check, verifies that the local Ollama server is up and responsive, and launches the Gradio user interface if all previous steps pass.

