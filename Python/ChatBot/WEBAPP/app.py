from flask import Flask, request, jsonify, render_template
import openai
import os

app = Flask(__name__)

openai.api_key = "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" # Replace with your actual OpenAI API key

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
    prompt = (f"You work for Lily Ann Cabinets as a AI customer service representative"
              f"\n\n"
              f"Human: {input_text}\n"
              f"AI:")
    completions = openai.Completion.create(
        model="ft:gpt-3.5-turbo-0613:lac::7qr3DY9v", # Replace with the OpenAI API engine you want to use
        prompt=prompt,
        max_tokens=1000,
        stop = ["/n", "Human"],
        n=1,
        temperature=0.2,
    )
    message = completions.choices[0].text.strip()
    return message

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)
