from flask import Flask, render_template, request
import google.generativeai as palm

# Configure the Google Generative AI API
palm.configure(api_key="AIzaSyCCT1K99BJ1JbLwhCE7qOcQ5KOZcPJ9ZZ4")

model = {"model": "models/chat-bison-001"}

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Get the user input from the form
        user_input = request.form.get("q")
        if user_input:
            # Append a predefined message to the user input
            user_input1 = f"""Generate a detailed business startup plan focusing on 
            {user_input}. Include key elements such as market analysis, target audience,
            revenue model, and scalability. Additionally, discuss potential risks and mitigation 
            strategies involved in launching this business.
            Maximum word output is only 200 words"""

            # Get the response from the chatbot
            response = palm.chat(**model, messages=user_input1)
            chatbot_response = response.last if response else "Sorry, there was an error processing your request."
            # Render the prob template with the chatbot response
            return render_template("prob.html", g=user_input, f=user_input1, r=chatbot_response)
    # Render the index template for GET requests
    return render_template("index.html")

@app.route("/main", methods=["GET"])
def main():
    return render_template("main.html", r=None)

if __name__ == "__main__":
    app.run(debug=True)
