import pygame
import LCD1602
import time
import openai  # Import the OpenAI library
import speech_recognition as sr
from gtts import gTTS

# Set your OpenAI API key here
api_key = ""

openai.api_key = api_key

r = sr.Recognizer()

def recognize_speech():
    with sr.Microphone() as source:
        LCD1602.clear()
        LCD1602.write(0, 0, "Talk")
        print("Talk")
        audio_text = r.listen(source)
        print("Time over, thanks")

    try:
        text = r.recognize_google(audio_text)
        print("Recognized Text: " + text)
        return text
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))

    return ""

def generate_response(prompt):
    
    response = openai.Completion.create(
        engine="text-davinci-002",  
        prompt=prompt,
        max_tokens=400  
    )
    return response.choices[0].text.strip()

def text_to_speech(mytext, language='en'):
    myobj = gTTS(text=mytext, lang=language, slow=False)
    myobj.save("welcome.mp3")
    
    pygame.mixer.init()
    pygame.mixer.music.load("welcome.mp3")
    pygame.mixer.music.play()
    
    while pygame.mixer.music.get_busy():
        continue

def setup():
    LCD1602.init(0x27, 1)
    LCD1602.write(0, 0, "Ready")
    time.sleep(2)

def destroy():
    LCD1602.clear()

if __name__ == "__main__":
    try:
        setup()
        while True:
            recognized_text = recognize_speech()
            if recognized_text:
                LCD1602.clear()
                LCD1602.write(0, 0, recognized_text)
                
                response = generate_response(recognized_text)  # Generate a response based on recognized text
                LCD1602.clear()
                LCD1602.write(0, 0, response)
                
                text_to_speech(response)  # Convert the response to speech
    except KeyboardInterrupt:
        destroy()
