import speech_recognition as sr

# Create a recognizer instance
r = sr.Recognizer()

# Use the default microphone as the audio source
mic = sr.Microphone()

# Set the microphone input parameters
with mic as source:
    r.adjust_for_ambient_noise(source)
    print("Say something!")
    audio = r.listen(source)

# Convert speech to text
try:
    text = r.recognize_google(audio)
    print(f"You said: {text}")
except sr.UnknownValueError:
    print("Could not understand audio")
except sr.RequestError as e:
    print(f"Could not request results from Google Speech Recognition service; {e}")
