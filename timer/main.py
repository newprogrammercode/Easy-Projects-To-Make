import time
from tkinter import *
import pygame 

pygame.init()
pygame.mixer.music.load("alarm.mp3")

def main():
    while True:
        s = input("Please enter the time(or \"exit\" if you want to leave): ")
        
        if s.strip().lower() == "exit":
            print("Bye")
            break
            
        try:
            s = int(s)
        except ValueError:
            print("Invalid input, please enter a number.")
            continue
            
        while s > 0:
            print(s)
            time.sleep(1)
            s -= 1

        root = Tk()
        root.title("Finished!")
        root.geometry("300x320")
        
        def stop():
            pygame.mixer.music.stop()
            root.destroy()
            
        root.protocol("WM_DELETE_WINDOW", stop)

        lab = Label(root, text="Time Finished.", font=("Arial", 20, "bold"))
        lab.pack(pady=20)

        but = Button(root, text="Finish", font=("Arial", 20, "bold"), command=stop)
        but.pack(pady=10)

        pygame.mixer.music.play(-1)
        root.mainloop()

if __name__ == "__main__":
    main()
