import openai

openai.api_key = "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"

file = open("mp3\prompt1.mp3", "rb")
transcript = openai.Audio.transcribe("whisper-1", file)

print(transcript)