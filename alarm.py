from tkinter import *
import datetime
import time
import winsound
import customtkinter

#appearance/colors
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("dark-blue")

Clock = customtkinter.CTk()


class Clock(customtkinter.CTk):
    active = True
    WIDTH = 1000
    HEIGHT = 620
    hour = ""
    min = ""
    sec = ""

    alarms = []


    def __init__(self):
        super().__init__()

        self.title("Brian's Alarm Clock")
        self.geometry(f"{Clock.WIDTH}x{Clock.HEIGHT}")
        self.protocol("WM_DELETE_WINDOW", self.on_closing)  # call .on_closing() when app gets closed

        

        # ======= Create two frames ================
        # ============ 1st Frame ===================
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=3)
        self.grid_rowconfigure(0, weight=1)

        self.frame_left = customtkinter.CTkFrame(master=self,
                                                 width=500,
                                                 corner_radius=0)
        self.frame_left.grid(row=0, column=0, sticky="nswe")

        self.frame_right = customtkinter.CTkFrame(master=self)
        self.frame_right.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

        # ============ frame_left ============

        # configure grid layout (1x11)
        self.frame_left.grid_rowconfigure(0, minsize=10)   # empty row with minsize as spacing



        self.label_1 = customtkinter.CTkLabel(master=self.frame_left,
                                              text="Alarms",
                                              text_font=("Roboto Medium", 16))  # font name and size in px
        self.label_1.grid(row=1, column=0, pady=10, padx=50, sticky = "nwe")


         # ============ frame_right ============
        #self.frame_right.grid_columnconfigure(4, weight=2)

        # configure grid layout (3x7)
        self.frame_right.rowconfigure((0, 1, 2, 3), weight=1)
        self.frame_right.rowconfigure(7, weight=10)
        self.frame_right.columnconfigure((0, 1, 2, 3, 4), weight=1)
        self.frame_right.columnconfigure(2, weight=1)

        #self.frame_info = customtkinter.CTkFrame(master=self.frame_right)
        #self.frame_info.grid(row=0, column=0, columnspan=2, rowspan=4, pady=20, padx=20, sticky="nsew")

        self.soundFile = customtkinter.CTk

        self.entryHR = customtkinter.CTkEntry(master=self.frame_right,
                                            textvariable=Clock.hour,
                                            width=10,
                                            placeholder_text="Hour")
        self.entryHR.grid(row=7, column=0, columnspan=1, pady=20, padx=10, sticky="we")
        self.entryMN = customtkinter.CTkEntry(master=self.frame_right,
                                            textvariable=Clock.min,
                                            width=10,
                                            placeholder_text="Minute")
        self.entryMN.grid(row=7, column=1, columnspan=1, pady=20, padx=10, sticky="we")
        self.entryS = customtkinter.CTkEntry(master=self.frame_right,
                                            textvariable=Clock.sec,
                                            width=10,
                                            placeholder_text="Second")
        self.entryS.grid(row=7, column=2, columnspan=1, pady=20, padx=10, sticky="we")

        self.button = customtkinter.CTkButton(master=self.frame_right,
                                                text="Create Alarm",
                                                border_width=2,  # <- custom border_width
                                                fg_color=None,  # <- no fg_color
                                                command=self.actual_time)
        self.button.grid(row=8, column=2, columnspan=1, pady=20, padx=20, sticky="we")

        self.label_info_1 = customtkinter.CTkLabel(master=self.frame_right,
                                                   text="*Enter alarm time in military*\n" +
                                                        "*Do not leave any entries empty*\n" +
                                                        "*All entries must be 2 digits*" ,
                                                   height=70,
                                                   fg_color=("white", "gray38"))
        self.label_info_1.grid(column=0, row=8, sticky="sw", padx=15, pady=15)

        self.update()


    def update(self):
        if not(self.active):
            time.sleep(0.5)
            self.active = True
        self.current_date_display = customtkinter.CTkLabel(master = self.frame_right, 
                                                    text=time.strftime("%m/%d/%Y"), 
                                                    fg="white", bg="DodgerBlue4", 
                                                    text_font=("Arial",30,"bold"))
        self.current_date_display.grid(row=2, column=0, columnspan=3, pady=10, padx=20, sticky="we")
        self.current_time_display = customtkinter.CTkLabel(master = self.frame_right, 
                                    text=time.strftime("%I:%M:%S"), 
                                    fg="white", 
                                    bg="DodgerBlue4", 
                                    text_font=("Arial",100,"bold"))
        self.current_time_display.grid(row=4, column=0, columnspan=3, pady=10, padx=20, sticky="we")
        
        self.sort_alarms()
        self.display_alarms()
        
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M:%S")
        if len(self.alarms)>0:

            print(len(self.alarms) , " " , self.alarms[0])
            if now in self.alarms:
                #self.alarm_displays[0].destroy()
                #self.alarm_displays.pop(0)
                #self.alarms.remove(now)
                print("ALARM!")
                winsound.PlaySound("sound.wav", winsound.SND_ASYNC)
        
        for alarm in self.alarms:
            print(alarm)

        self.after(1000,self.update)
    

    def on_closing(self, event=0):
        self.destroy()
    
    def actual_time(self):
        if(self.active):
            self.active = False
            print("Actual_time has run")
            print(self.entryHR.get() , " + ", Clock.hour)
            set_alarm_timer = f"{self.entryHR.get()}:{self.entryMN.get()}:{self.entryS.get()}"
            print(set_alarm_timer)
            self.alarms.append(set_alarm_timer)



        
    
    def display_alarms(self):
        alarm_displays = []
        if(len(alarm_displays)<len(self.alarms)):
            for i in range(len(self.alarms)):
                alarm_displays.append(customtkinter.CTkLabel(master=self.frame_left, text=self.alarms[i], text_font=("Arial",30,"bold"), fg="white", bg="SteelBlue"))
                alarm_displays[i].grid(row=i+2, column=0, pady=10, padx=5)

        for alarm in alarm_displays:
            print(alarm.text)

        print(f"Displayed: {len(alarm_displays)} ___ Actual {len(self.alarms)}")

        

        

    def alarm_to_int(self, alarm_given):
        #print(type(alarm_given[0:2]))

        hr = int(alarm_given[0:2])
        mn = int(alarm_given[3:5])
        sc = int(alarm_given[6:])
        score = (hr*60*60)+(mn*60)+(sc)
        #print(score)
        return score

    def sort_alarms(self):
        alarm_sec = []
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M:%S")
        now_sec = self.alarm_to_int(now)
        for alarm in self.alarms:
            alarm_sec.append(self.alarm_to_int(alarm))
        if len(self.alarms) > 1:
            for i in range(len(alarm_sec)):
                alarm_sec[i] = now_sec - alarm_sec[i]
                if alarm_sec[i] < 0:
                    alarm_sec[i]+=(24*60*60)
            for i in range(len(alarm_sec)-1):
                if alarm_sec[i]<alarm_sec[i+1]:
                    hold = alarm_sec[i]
                    hold_alarm = self.alarms[i]
                    alarm_sec[i] = alarm_sec[i+1]
                    self.alarms[i] = self.alarms[i+1]
                    alarm_sec[i+1] = hold
                    self.alarms[i+1] = hold_alarm 



if __name__ == "__main__":
    clock = Clock()
    clock.mainloop()
