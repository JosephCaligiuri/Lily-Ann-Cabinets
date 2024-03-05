import os
import openai

openai.api_key = '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'


response = openai.FineTuningJob.create(training_file="file-duobKq0v2AlMW0s78lQkNSnl", model="gpt-3.5-turbo-0613")

#response = openai.FineTuningJob.list()
print(response)