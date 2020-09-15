import io
import aiml
import os

kernel = aiml.Kernel()
#kernel.bootstrap(brainFile = "bot_brain.brn")
#kernel.bootstrap(learnFiles = "startup.xml", commands = "LOAD AIML B")

if os.path.isfile("bot_brain.brn"):
    kernel.bootstrap(brainFile = "bot_brain.brn")
#else:
    #kernel.bootstrap(learnFiles = "startup.xml", commands = "load aiml b")
    #kernel.saveBrain("bot_brain.brn")

# kernel now ready for use
while True:
    print (kernel.respond(input("Enter your message >> ")))
