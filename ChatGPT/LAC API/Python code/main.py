import openai

# Set up your OpenAI API credentials
openai.api_key = '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'



# Interact with the trained chatbot
def interact_with_chatbot(conversation):
    messages = [{'role': 'assistant', 'content': 'You are a helpful assistant that provides information about the company. You also work for this company and answer in character.'}]
    for message in conversation:
        messages.append({'role': message['role'], 'content': message['content']})
    
    response = openai.ChatCompletion.create(
        model="ft:gpt-3.5-turbo-0613:lac::7qr3DY9v",
        messages=messages,
        max_tokens=1000,
        n=1,
        temperature=0.7,
        stop=None,
    )

    return response.choices[0].message.content

# Interact with the trained model
conversation = [
    {'role': 'assistant', 'content': 'You are a helpful assistant that provides information about the company. You also work for this company and answer in character.'}
]

while True:
    user_input = input("User: ")
    if user_input.lower() == 'quit':
        break
    
    conversation.append({'role': 'user', 'content': user_input})
    response = interact_with_chatbot(conversation)
    conversation.append({'role': 'assistant', 'content': response})
    print("ChatBot:", response)