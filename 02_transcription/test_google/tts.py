import io
import os
import speech_recognition as sr 

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "Masterarbeit-3f2d3dbaa1e3.json"

r = sr.Recognizer()

audio_file = sr.AudioFile("C:\Users\veren\OneDrive\DSIA\Masterarbeit\STT_Interviews\Interviews\Interview_1.mp3")

with audio_file as source:
    r.adjust_for_ambient_noise(source)
    audio = r.record(source)
result = r.recognize_google(audio)

with open("interview.txt",mode ="w") as file:
    file.write("Recognized text:")
    file.write("\n")
    file.write(result)
    print("Hurray! conversion is complete")