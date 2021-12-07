import sys
try:
    import pyttsx3
except ImportError:
    print('The pyttsx3 module needs to be installed to run this')
    print('program. On Windows, Open a Command Prompt or Powershell session and run:')
    print('\tpip install pyttsx3')
    print('On MacOS and Linux, open a Terminal and run:')
    print('\tpip3 install pyttsx3')
    sys.exit()

tts = pyttsx3.init()

print('''
Text to Speech Talker, from The Big Book of Small Python Projects\n
Text to Speech using the pyttsx3 module, which in turn uses\n
the NSSpeechSynthesizer (on MacOS), SAPI5 (on Windows), or\n
eSpeak (on Linux) speech engines.\n
''')

print('Enter the text to speak, or QUIT to quit.')
while True:
    text = input('> ')
    if text.upper() == 'QUIT':
        print('Thanks for playing!')
        sys.exit()

    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[7].id)
    tts.say(text)
    tts.runAndWait()