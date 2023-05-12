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
    prompt = (f"You are an AI Helper here to assist with questions"
              f"\n\n"
              f"Human: {input_text}\n"
              f"AI:")
    completions = openai.Completion.create(
        engine="ft-WiOMRtc2jyZ2Xe0qiY3fYj92", # Replace with the OpenAI API engine you want to use
        prompt=prompt,
        max_tokens=1000,
        stop = ["/n",],
        n=1,
        temperature=0.2,
    )
    message = completions.choices[0].text.strip()
    return message

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)
