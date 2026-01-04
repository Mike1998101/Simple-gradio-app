import os
import gradio as gr
import random

# Set the GRADIO_SERVER_PORT to Render's PORT BEFORE any Gradio imports happen
# This is the most critical fix
if "PORT" in os.environ:
    os.environ["GRADIO_SERVER_PORT"] = os.environ["PORT"]

# Your existing functions
def greet(name):
    return f"Hello {name}! 👋"

def check_weather(city):
    weather_options = ["☀️ Sunny", "🌧️ Rainy", "☁️ Cloudy", "❄️ Snowy"]
    return f"Weather in {city}: {random.choice(weather_options)}"

def calculator(num1, operation, num2):
    if operation == "+":
        return f"{num1} + {num2} = {num1 + num2}"
    elif operation == "-":
        return f"{num1} - {num2} = {num1 - num2}"
    elif operation == "×":
        return f"{num1} × {num2} = {num1 * num2}"
    elif operation == "÷":
        if num2 == 0:
            return "Cannot divide by zero!"
        return f"{num1} ÷ {num2} = {num1 / num2}"

# Create the interface
with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("# 🚀 Simple Gradio Demo")
    
    with gr.Tab("Greeting"):
        gr.Markdown("## Say Hello")
        name_input = gr.Textbox(label="Your Name", placeholder="Enter your name here...")
        greet_output = gr.Textbox(label="Greeting")
        greet_button = gr.Button("Greet Me!")
    
    with gr.Tab("Weather"):
        gr.Markdown("## Check Weather")
        city_input = gr.Dropdown(["New York", "London", "Tokyo", "Paris", "Sydney"],
                                label="Select City")
        weather_button = gr.Button("Check Weather")
        weather_output = gr.Textbox(label="Weather Report")
    
    with gr.Tab("Calculator"):
        gr.Markdown("## Simple Calculator")
        with gr.Row():
            num1 = gr.Number(label="First Number", value=10)
            operation = gr.Radio(["+", "-", "×", "÷"], label="Operation")
            num2 = gr.Number(label="Second Number", value=5)
        calc_button = gr.Button("Calculate")
        calc_output = gr.Textbox(label="Result")
    
    with gr.Tab("About"):
        gr.Markdown("## About This Demo")
    
    # Connect functions
    greet_button.click(greet, inputs=name_input, outputs=greet_output)
    weather_button.click(check_weather, inputs=city_input, outputs=weather_output)
    calc_button.click(calculator, inputs=[num1, operation, num2], outputs=calc_output)

# Get port from environment - use 7860 as default for local testing
port = int(os.environ.get("PORT", 7860))
demo.launch(server_name="0.0.0.0", server_port=port)
