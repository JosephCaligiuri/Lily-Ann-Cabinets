from flask import Flask, request, jsonify, render_template
import openai
import os

app = Flask(__name__)

openai.api_key = "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"  # Replace with your actual OpenAI API key

short_term_memory = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_input = request.form['user_input']
        response = generate_response(user_input)
        return render_template('index.html', response=response)
    return render_template('index.html')

@app.route("/chat")
def chat():
    return render_template("index.html")

@app.route("/get_response", methods=["POST"])
def get_response():
    prompt = request.form["prompt"]
    response = generate_response(prompt)
    return jsonify({"response": response})

def generate_response(input_text):
    global short_term_memory  # Add global keyword to access the shared memory

    prompt = (f"You are an AI Helper here to assist with questions"
              f"\n\n"
              f"Human: {input_text}\n"
              f"AI:")
    
    # Append input_text to the short-term memory
    short_term_memory.append(input_text)
    
    completions = openai.Completion.create(
        engine="davinci",  # Replace with the OpenAI API engine you want to use
        prompt=prompt,
        max_tokens=1000,
        stop=["/n", "Human"],
        n=1,
        temperature=0.2,
    )
    message = completions.choices[0].text.strip()
    return message

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)
