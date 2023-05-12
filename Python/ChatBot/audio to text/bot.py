# Note: you need to be using OpenAI Python v0.27.0 for the code below to work
import openai

openai.api_key = "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"


prompt = input("Enter Input: ")

response = openai.Completion.create(
    engine="davinci",
    prompt=prompt,
    max_tokens=1000,
    n=1,
    stop=None,
    temperature=0.7,
)

print(response.choices[0].text)