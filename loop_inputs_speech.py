import speech_recognition as sr
import subprocess


# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    subprocess.run(["clear"])
    #file =open('output1.txt','a+')
    print("-------------------------------------------------------------------------------------------------------------------")
    print("Speech to text convertion")
    print("-------------------------------------------------------------------------------------------------------------------")
    print("Please wait. Calibrating microphone...")
    # listen for 3 seconds and create the ambient noise energy level
    r.adjust_for_ambient_noise(source, duration=2)
    print("Say something!")
    audio = r.listen(source)

 # recognize speech using Sphinx

while(1):
    try:
        print("You said '" + r.recognize_google(audio) + "'")
        print("")
        print("Do you want to say something else: 1. Yes[y] " + " 2. No[N] ")
        choice = str(input())
        if(choice =='y'):
            with sr.Microphone() as source:

            #file =open('output1.txt','w')
            #print("-------------------------------------------------------------------------------------------------------------------")
            #print("Speech to text convertion")
            #print("-------------------------------------------------------------------------------------------------------------------")
            #print("Please wait. Calibrating microphone...")
           # listen for 3 seconds and create the ambient noise energy level
                r.adjust_for_ambient_noise(source, duration=2)
                print("Say something!")
                audio = r.listen(source)
                continue

        else:
            print("Exiting")
            exit()
    #    x=r.recognize_google(audio)
    #    file.write(x)
    except sr.UnknownValueError:
        print("Engine could not understand audio")
        print("")
        print("Do you want to say something else: 1. Yes[y] " + " 2. No[N] ")
        choice = str(input())
        if(choice =='y'):
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source, duration=2)
                print("Say something!")
                audio = r.listen(source)
                continue
        else:
            exit()

    except sr.RequestError as e:
        print("google speech engine error; {0}".format(e))
        print("Engine could not understand audio")
        print("")
        print("Do you want to say something else: 1. Yes[y] " + " 2. No[N] ")
        choice = str(input())
        if(choice =='y'):
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source, duration=2)
                print("Say something!")
                audio = r.listen(source)
                continue
        else:
            exit()
