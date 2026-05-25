from transformers import pipeline
import pyttsx3
import speech_recognition as sr

# Load Hugging Face GPT-2 (free AI model)
print("Loading AI model... (first run may take time)")
generator = pipeline("text-generation", model="gpt2")

# Setup text-to-speech
engine = pyttsx3.init()

# Setup speech recognizer
recognizer = sr.Recognizer()
mic = sr.Microphone()

def ai_agent(prompt):
    # Generate AI response
    result = generator(prompt, max_length=120, do_sample=True, temperature=0.7)[0]['generated_text']
    reply = result[len(prompt):].strip()

    # Speak reply
    engine.say(reply)
    engine.runAndWait()
    return reply

print("\n🎤 Voice Chatbot is ready! Say 'exit' or 'quit' to stop.\n")

while True:
    try:
        with mic as source:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(source)  # reduce background noise
            audio = recognizer.listen(source)

        user_input = recognizer.recognize_google(audio)
        print("You:", user_input)

        if user_input.lower() in ["exit", "quit", "bye"]:
            print("AI: Goodbye!")
            engine.say("Goodbye!")
            engine.runAndWait()
            break

        reply = ai_agent(user_input)
        print("AI:", reply)

    except sr.UnknownValueError:
        print("⚠️ Didn't catch that, please try again.")
    except Exception as e:
        print("Error:", e)
