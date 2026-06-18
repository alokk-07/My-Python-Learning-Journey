# Install an external module and use it to perform an oprtatio of your self 

# For example, you can use the pyttsx3 module to convert text to speech. You can install it using pip and then use it to say something.
#install pyttsx3 module using pip install pyttsx3
import pyttsx3
engine = pyttsx3.init()

engine.say("")
engine.runAndWait()