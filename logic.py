import keyboard

class Timer_Typer:
    def __init__(self):
        pass
    def event_loop(self):
        while True:
            if keyboard.read_key() == "enter":
                print('Pressed Enter')
                break
            if keyboard.read_key() == "tab":
                print('Pressed Tab')
                break

def main():
    t = Timer_Typer()
    t.event_loop()

if __name__ == '__main__':
    main()