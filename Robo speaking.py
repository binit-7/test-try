import platform
import subprocess
print("MADE BY BINIT !!")
print("ROBO SPEAKING..")
while True:
    def main():
        x=input("ENTER THE COMMAND YOU WANT ME TO SAY:")
        system=platform.system()
        try:
            if system=='Windows':
                command = ["powershell", "-Command", f'Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak("{x}")']
                subprocess.run(command)
        except FileNotFoundError:
            print("FILE IS NOT FOUND MAY BE THE COMMAND YOU TYPE IS WRONG !!")
    main()
    again=input("DO YOU WANT ME TO SAY AGAIN ? (Y/N)").lower()
    options=['y','n']
    if again not in options:
        print("INVALID OPTION!")
        break
    if again=='n':
        break
    print("THANK YOU !")
        