import speech_recognition as sr
import pyttsx3

# Initialize the recognizer
r = sr.Recognizer()

def recordText():
    #loop in case of errors
    while(1):
        try:
            #use the mic as source for input
            with sr.Microphone() as source2:
                #prepare recognizer to receive input
                r.adjust_for_ambient_noise(source2, duration=0.2)

                #listen for the user's input
                audio2 = r.listen(source2)

                # Using google to recognize audio
                MyText = r.recognize_google(audio2)

                return MyText

        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
                  
        except sr.UnknownValueError:
            print("unknown error occurred")
              
    return

def outputText(text):
    f = open("output.txt", "a")
    f.write(text)
    f.write("\n")
    f.close()
    return

while(1):
    text = recordText()
    outputText(text)

    print("Wrote text")
