
#import libraries
import gradio as gr
from input_processor import process_dates

def gradio_interface(): # Defines the gradio_interface function

    ui = gr.Interface(
        fn=process_dates, #this is where the ollama response is going to go
        inputs=[
            gr.Textbox(lines=1, label='Enter your Destination City Here', placeholder = 'e.g Denver, New York'), # Where the user inputs their destination city
            gr.DateTime(label='Enter your start date Here'), # Where the user inputs their start date
            gr.DateTime(label='Enter your end date Here') # Where the user inputs their end date
        ],
        outputs=gr.Textbox(label='Travel Itinerary'),
        title='Travel Itinerary Generator', # Title of the UI
        description='Enter your desired city and trip dates to generate a custom travel plan!', # Description


    )
    return ui
