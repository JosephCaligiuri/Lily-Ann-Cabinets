import json
import openai

openai.api_key = "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"

training_data = [{
    "prompt": "I just to see if I can get an update. We had an order that we picked up last week and there were some decorative doors that were not, they didn't have in stock. And I just wanted to see if we had an update of when they thought those would be in stock ->",
    "completion": " Sure thing!, I just need your order number.\n"
},
{
    "prompt": "My order number is 523452 ->",
    "completion": " Perfect, give me a second to check the system.\n"
},
{
    "prompt": "Thank you ->",
    "completion": " No problem, thank you for buying from LilyAnn Cabinets"
}]

file_name = "training_data.jsonl"

upload_response = openai.File.create(
    file=open(file_name, "rb"),
    purpose='fine-tune'
)

file_id = upload_response.id

fine_tune_response = openai.FineTune.create(training_file=file_id, model="davinci")

print("Fine-tuned model ID:", fine_tune_response.model)

