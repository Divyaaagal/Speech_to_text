"""
Below is the code to check list of microphones available, You can uncomment the code and see the device id of the available devices
"""

# import speech_recognition as sr

# def list_available_microphones():
#     microphones = sr.Microphone.list_microphone_names()
#     return microphones

# if __name__ == "__main__":
#     microphones = list_available_microphones()

#     if not microphones:
#         print("No microphones found.")
#     else:
#         print("Available Microphones:")
#         for index, microphone_name in enumerate(microphones):
#             print(f"{index}: {microphone_name}")


import speech_recognition as sr
def hindi_speech_to_text():
    recognizer = sr.Recognizer()

    with sr.Microphone(device_index=2) as source:
        print("Say something in Hindi...")
        audio = recognizer.listen(source)

        try:
            # Recognize the speech using Google Web Speech API
            text = recognizer.recognize_google(audio, language="hi-IN")
            return text
        except sr.UnknownValueError:
            return "Hindi speech not understood"
        except sr.RequestError as e:
            return f"Could not request results from Google Web Speech API; {e}"

if __name__ == "__main__":
    result = hindi_speech_to_text()
    print("Hindi Speech to Text:")
    print(result)

