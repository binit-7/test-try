import datetime
import time
import pygame
def set_alarm(alarm_time):
    print(f"Alarm time is {alarm_time} ")
sound_file="sound.mp3"
alarm_time=input("Enter the time you want to set alarm (HH:MM:SS) :")
set_alarm(alarm_time)
while True:
    curr_time=datetime.datetime.now().strftime("%H:%M:%S")
    print(f"Current time:{curr_time}")
    time.sleep(1)
    if curr_time==alarm_time:
        print("WAKE UP !!")
        pygame.mixer.init()
        pygame.mixer.music.load(sound_file)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            time.sleep(1)
        break
    