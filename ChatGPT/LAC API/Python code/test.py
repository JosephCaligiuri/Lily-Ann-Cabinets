import openai

openai.api_key = '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'

test = openai.Completion.create(
    model="davinci:ft-lac-2023-07-17-17-12-20",
    prompt="hello")

print(test)