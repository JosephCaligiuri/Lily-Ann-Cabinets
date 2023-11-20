import openai

response = openai.File.create(
    file=open("tunning_data.jsonl", "rb"),
    purpose="fine-tune"
)

print(response)