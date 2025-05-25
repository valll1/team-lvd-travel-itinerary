"""
This function sets up a basic Gradio interface to verify that environment components are properly set up.
It loads the environment variables, retrieves the Ticketmaster API key, and launches a basic Gradio UI
to verify Gradio installation and operation.
"""

import gradio as gr
import os
from dotenv import load_dotenv
import requests

def launch_environment_test():
    # Load environment variables
    load_dotenv()

    # Get API key from environment
    Ticketmaster_API_KEY = os.getenv('Ticketmaster_API_KEY')

    # Warn if the API key is missing
    if not Ticketmaster_API_KEY:
        print('Warning: Ticketmaster_API_KEY not found in environment variables.')
        print('Please create a .env file with your Ticketmaster API key')

    # Confirm environment setup
    print('Environment setup complete!')
    print(f'Ticketmaster_API_KEY available: {"Yes" if Ticketmaster_API_KEY else "No"}')

    # Create a simple Gradio interface
    with gr.Blocks(title='Environment Test') as demo:
        gr.Markdown('# Environment Test')
        gr.Markdown('If you can see this, Gradio is working correctly!')

        with gr.Row():
            input_text = gr.Textbox(label='Enter some text')
            output_text = gr.Textbox(label='Output')

        def echo(text):
            return f'You entered: {text}'

        # Button to trigger the echo function
        btn = gr.Button('Submit')
        btn.click(fn=echo, inputs=input_text, outputs=output_text)

        # Launch the interface
        demo.launch()

# Launch the Gradio app if the script is run directly
if __name__ == "__main__":
    launch_environment_test()