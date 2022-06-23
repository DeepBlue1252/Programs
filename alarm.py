from tkinter import *
import datetime
import time
import winsound

current_alarms = []

def alarm(set_alarm_timer):
    current_time = datetime.datetime.now()
    now = current_time.strftime("%H:%M:%S")
    date = current_time.strftime("%m/%d/%Y")
    print("The Current Date is: ",date)
    while now != set_alarm_timer:
        time.sleep(1)
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M:%S")
        print(now)
        if now == set_alarm_timer:
            print("ALARM!")
            winsound.PlaySound("sound.wav", winsound.SND_ASYNC)


clock = Tk()
clock.title("Brian's Alarm Clock")
clock.geometry("400x200")




def main():
    main_window = Frame(width = 300, height = 200, bg = "DodgerBlue4")
    main_window.pack(side = RIGHT)

    side_window = Frame(width = 100, height = 200, bg = "SteelBlue")
    side_window.pack(side = LEFT)

    main_text = Label(main_window,text="Main",font=60).place(x=110)
    current_alarms_label = Label(side_window, text = "Alarms", font=60, bg= "SteelBlue", fg = "White").place(x="20",y=10)

    clock.mainloop()

main()