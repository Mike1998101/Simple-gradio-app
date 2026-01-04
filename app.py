import gradio as gr
import random
import os

# Function definitions
def greet(name):
    """Returns a greeting message."""
    return f"Hello {name}! 👋"

def check_weather(city):
    """Returns a random weather report for a selected city."""
    weather_options = ["☀️ Sunny", "🌧️ Rainy", "☁️ Cloudy", "❄️ Snowy"]
    return f"Weather in {city}: {random.choice(weather_options)}"

def calculator(num1, operation, num2):
    """Performs basic arithmetic operations."""
    if operation == "+":
        result = num1 + num2
        return f"{num1} + {num2} = {result}"
    elif operation == "-":
        result = num1 - num2
        return f"{num1} - {num2} = {result}"
    elif operation == "×":
        result = num1 * num2
        return f"{num1} × {num2} = {result}"
    elif operation == "÷":
        if num2 == 0:
            return "Error: Cannot divide by zero!"
        result = num1 / num2
        return f"{num1} ÷ {num2} = {result:.2f}"  # Format to 2 decimal places

# --- Build the Gradio Interface ---
with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("# 🚀 My Gradio Demo App")
    gr.Markdown("A simple interactive app with multiple features.")

    with gr.Tab("👋 Greeting"):
        gr.Markdown("### Get a friendly welcome")
        name_input = gr.Textbox(label="What is your name?", placeholder="Type your name here...")
        greet_button = gr.Button("Say Hello!")
        greet_output = gr.Textbox(label="Greeting", interactive=False)
        greet_button.click(fn=greet, inputs=name_input, outputs=greet_output)

    with gr.Tab("🌤️ Weather Check"):
        gr.Markdown("### Check the (random) weather anywhere")
        city_input = gr.Dropdown(
            choices=["New York", "London", "Tokyo", "Paris", "Sydney", "Mumbai"],
            label="Select a City",
            value="New York"
        )
        weather_button = gr.Button("Check Weather!")
        weather_output = gr.Textbox(label="Current Forecast", interactive=False)
        weather_button.click(fn=check_weather, inputs=city_input, outputs=weather_output)

    with gr.Tab("🧮 Calculator"):
        gr.Markdown("### Perform a quick calculation")
        with gr.Row():
            num1_input = gr.Number(label="First Number", value=10)
            operation_input = gr.Radio(["+", "-", "×", "÷"], label="Operation", value="+")
            num2_input = gr.Number(label="Second Number", value=5)
        calc_button = gr.Button("Calculate!")
        calc_output = gr.Textbox(label="Result", interactive=False)
        calc_button.click(fn=calculator, inputs=[num1_input, operation_input, num2_input], outputs=calc_output)

    with gr.Tab("ℹ️ About"):
        gr.Markdown("""
        ## About This App
        This is a demo app built with **Gradio** to showcase simple interactivity.

        **Features include:**
        1.  A personalized greeting.
        2.  A fun, randomized weather reporter.
        3.  A basic arithmetic calculator.

        **Deployment Info:**
        - This app is configured to run on cloud platforms like **Render**.
        - The `PORT` environment variable is read automatically for compatibility.
        """)

# --- Configuration for Render Deployment ---
# Get the PORT assigned by the Render environment; default to 7860 for local runs.
server_port = int(os.environ.get("PORT", 7860))
# Launch the app, making it accessible on the network.
demo.launch(server_name="0.0.0.0", server_port=server_port)
