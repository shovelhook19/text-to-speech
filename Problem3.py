import pyjokes
import pyttsx3
engine = pyttsx3.init()


print("Printing joke....")
# this print a random joke
joke = pyjokes.get_joke()
print(joke)

# RATE
rate = engine.getProperty('rate')   # getting details of current speaking rate
print (rate)                        # printing current voice rate
engine.setProperty('rate', 125)     # setting up new voice rate
print("voice rate =",rate)
# VOICE
voices = engine.getProperty('voices')       # getting details of current voice
#engine.setProperty('voice', voices[0].id)  # changing index, changes voices. o for male
engine.setProperty('voice', voices[1].id)   # changing index, changes voices. 1 for female

engine.say(joke)
engine.runAndWait()

# # Making a loop 
# while 1>0:
#     hii= input("Enter your text =>")
#     engine.say(hii)
#     engine.runAndWait()








engine.stop()
# For Mac, If you face error related to "pyobjc" when running the `init()` method :
# Install 9.0.1 version of pyobjc : "pip install pyobjc>=9.0.1"

