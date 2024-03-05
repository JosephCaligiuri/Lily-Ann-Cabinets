import openai

# Set up your OpenAI API credentials
openai.api_key = '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'

with open('tunning_data_prepared.jsonl', 'r', encoding='utf8') as f:
    training_data = f.readlines()

messages = []
for line in training_data:
    message = {
        'role': 'system',
        'content': line.strip()
    }
    messages.append(message)

response = openai.Completion.create(
    model="davinci:ft-lac-2023-07-17-17-12-20",
    messages=messages,
    max_tokens=500,
    n=1,
    temperature=0.7,
    stop=None,
    user="You are a helpful assistant that provides information about the company, Lily Ann Cabinets. You also work for this company and you answer in character."
)

print(response)  # Print the response to inspect its structure

checkpoint_id = response['id']

# Save the fine-tuned checkpoint ID
with open('checkpoint_id.txt', 'w') as f:
    f.write(checkpoint_id)
