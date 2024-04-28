import pyttsx3

def text_to_speech(text):
    # Initialize the text-to-speech engine
    engine = pyttsx3.init()

    # Set properties before adding things to say
    engine.setProperty('rate', 150)  # Speed percent (can go over 100)
    engine.setProperty('volume', 0.9)  # Volume 0-1

    # Convert text to speech
    engine.say(text)

    # Wait for speech to finish
    engine.runAndWait()

if __name__ == "__main__":
    # Ask user for input string
    input_string = input("Enter the text you want to convert to audio: ")

    # Convert input string to audio
    text_to_speech(input_string)

