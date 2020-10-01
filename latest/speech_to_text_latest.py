import speech_recognition as sr

 # obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Please wait. Calibrating microphone...")
   # listen for 3 seconds and create the ambient noise energy level
    r.adjust_for_ambient_noise(source, duration=3)
    print("Say something!")
    audio = r.listen(source)

 # recognize speech using Sphinx
try:
    print("google speech engine thinks you said '" + r.recognize_google(audio) + "'")
except sr.UnknownValueError:
    print("google speech engine could not understand audio")
except sr.RequestError as e:
    print("google speech engine error; {0}".format(e))

