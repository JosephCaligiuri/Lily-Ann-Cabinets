from flask import Flask, request, jsonify, render_template
import openai

app = Flask(__name__)

# Set up your OpenAI API credentials
openai.api_key = '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'

# Define your training data as input-output pairs
training_data = [

    {
        "input": "Thank you ->",
        "output": " No problem, thank you for buying from LilyAnn Cabinets"
    },
    
    # Add more training examples as needed
]

# Fine-tune the GPT model using your training data
def fine_tune_model(training_data):
    # Prepare the training examples in OpenAI Chat format
    examples = []
    for example in training_data:
        examples.append({'role': 'system', 'content': 'You are a helpful assistant that provides information About the company, Lily Ann Cabinets. you also work for this company and you answer in character'})
        examples.append({'role': 'user', 'content': example['input']})
        examples.append({'role': 'assistant', 'content': example['output']})

    # Fine-tune the GPT model with the training examples
    response = openai.ChatCompletion.create(
        model="ft:gpt-3.5-turbo-0613:lac::7qr3DY9v",
        messages=examples,
        max_tokens=500,
        n=1,
        temperature=1,
        stop=None,
        user="You are a helpful assistant that provides information About the company, Lily Ann Cabinets. you also work for this company and you answer in character."
    )

    return response

# Interact with the trained chatbot
def interact_with_chatbot(conversation):
    # Retrieve the last 4 messages from the conversation
    last_4_messages = conversation[-4:]

    # Prepare the messages for chatbot interaction
    messages = [{'role': 'system', 'content': 'You are a helpful assistant that provides information about the company, Lily Ann Cabinets. You also work for this company and answer in character.'}]
    messages.extend(last_4_messages)

    response = openai.ChatCompletion.create(
        model="ft:gpt-3.5-turbo-0613:lac::7qr3DY9v",
        messages=messages,
        max_tokens=150,
        n=1,
        temperature=1,
        stop=None,
    )

    return response.choices[0].message.content

# Store conversation history
conversation_history = []

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_input = data['user_input']

    # Add user input to conversation history
    conversation_history.append({'role': 'user', 'content': user_input})

    # Generate chatbot response
    response = interact_with_chatbot(conversation_history)

    # Add chatbot response to conversation history
    conversation_history.append({'role': 'assistant', 'content': response})

    return jsonify({'response': response})

if __name__ == '__main__':
    # Fine-tune the model
    fine_tune_model(training_data)
    app.run(host="0.0.0.0", port="8080", debug=True)
