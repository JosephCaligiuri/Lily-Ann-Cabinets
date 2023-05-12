import openai
import datetime

openai.api_key = "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"

date = "2023-05-12"

def find_model_ids(date):
    # List all models
    models = openai.Model.list()

    # Collect all the model IDs that were fine-tuned on the specified date
    model_ids = []
    for model in models['data']:
        try:
            if model['model_type'] == 'text-davinci-002' and model['fine_tuned']['datetime'].startswith(date):
                model_ids.append(model['id'])
        except KeyError:
            pass  # ignore models that don't have 'model_type' key
    return model_ids

def generate_response(input_text, model_ids):
    for model_id in model_ids:
        prompt = (f"You are an AI Helper here to assist with questions"
                  f"\n\n"
                  f"Human: {input_text}\n"
                  f"AI:")
        completions = openai.Completion.create(
            engine=model_id,
            prompt=prompt,
            max_tokens=1000,
            stop = ["/n",],
            n=1,
            temperature=0.2,
        )
        message = completions.choices[0].text.strip()
        if message:
            return message  # return the first non-empty response
    return ""  # if all responses are empty, return an empty string
