import pyttsx3

# 1. Initialize the text-to-speech engine
engine = pyttsx3.init()

# 2. Queue the text you want the engine to say
engine.say("hello Ayush my son ")

# 3. Process the queue and wait for the speech to finish
engine.runAndWait()