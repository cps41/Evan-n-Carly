import keyboard
from datetime import datetime

class Timer_Typer:
    def __init__(self):
        pass
    def event_loop(self):
        while True:
            if keyboard.read_key() == "enter":
                time = datetime.datetime.now()
                print(f'Pressed Enter at {time}')
                break
            if keyboard.read_key() == "tab":
                time = datetime.datetime.now()
                print(f'Pressed Tab at {time}')
                break

def main():
    t = Timer_Typer()
    t.event_loop()

if __name__ == '__main__':
    main()