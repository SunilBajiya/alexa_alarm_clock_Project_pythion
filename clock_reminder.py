# for the clock project what thik are need 
# first of the clock with the hours , minits and seconds .
# added the timer functionality here to remind

from tkinter import *
import datetime
import time
from threading import *
from pygame import mixer
 
 
 # create objects
root = Tk()
root.geometry("500x250")
 
 
 # def the threading concepts here for the clock timers executes
def Threading():
    t1 = Thread(target=alarm)
    t1.start()

# then here declared the clock section for the time
def alarm():
    # alarm set
 while True:  # that for the repetition
    set_alarm_time = f"{hour.get()}:{minute.get()}:{second.get()}"
    time.sleep(1)  # that is here time applied here for the particular times

    # get current time
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    print(current_time, set_alarm_time)

    if current_time == set_alarm_time:
        print("hello please Wake Up now! ")
        # play the sound continuously
        mixer.init()
        mixer.music.load("sound.mp3")  # load the sound here
        mixer.music.play()
        break
 
 
def stop_alarm():
     mixer.music.stop()
     
     
     
     
Label(root, text="Alarm Clock", font=("Helvetica 20 bold"), fg= "red").pack(pady=10)
Label(root, text="Set Time", font=("Helvetical 15 bold")).pack()


frame = Frame(root)
frame.pack()


hour = StringVar(root)
hours = (
    "00",
    "01",
    "02",
    "03",
    "04",
    "05",
    "06",
    "07",
    "08",
    "09",
    "10",
    "11",
    "12",
    "13",
    "14",
    "15",
    "16",
    "17",
    "18",
    "19",
    "20",
    "21",
    "22",
    "23",
    "24",
)
hour.set(hours[0])
    
hrs = OptionMenu(frame, hour, *hours)
hrs.pack(side=LEFT)

minute = StringVar(root)
minutes = (
     "00",
    "01",
    "02",
    "03",
    "04",
    "05",
    "06",
    "07",
    "08",
    "09",
    "10",
    "11",
    "12",
    "13",
    "14",
    "15",
    "16",
    "17",
    "18",
    "19",
    "20",
    "21",
    "22",
    "23",
    "24",
    "25",
    "26",
    "27",
    "28",
    "29",
    "30",
    "31",
    "32",
    "33",
    "34",
    "35",
    "36",
    "37",
    "38",
    "39",
    "40",
    "41",
    "42",
    "43",
    "44",
    "45",
    "46",
    "47",
    "48",
    "49",
    "50",
    "51",
    "52",
    "53",
    "54",
    "55",
    "56",
    "57",
    "58",
    "59",
    "60",
)
minute.set(minutes[0])

mins = OptionMenu(frame, minute, *minutes)
mins.pack(side=LEFT)

second = StringVar(root)
seconds = (
    "00",
    "01",
    "02",
    "03",
    "04",
    "05",
    "06",
    "07",
    "08",
    "09",
    "10",
    "11",
    "12",
    "13",
    "14",
    "15",
    "16",
    "17",
    "18",
    "19",
    "20",
    "21",
    "22",
    "23",
    "24",
    "25",
    "26",
    "27",
    "28",
    "29",
    "30",
    "31",
    "32",
    "33",
    "34",
    "35",
    "36",
    "37",
    "38",
    "39",
    "40",
    "41",
    "42",
    "43",
    "44",
    "45",
    "46",
    "47",
    "48",
    "49",
    "50",
    "51",
    "52",
    "53",
    "54",
    "55",
    "56",
    "57",
    "58",
    "59",
    "60",
)
second.set(seconds[0])


secs = OptionMenu(frame, second, *seconds)
secs = OptionMenu(frame, second, *seconds)
secs.pack(side=LEFT)

Button(root, text="Set Alarms", font=("Helvetica 15"), command=Threading).pack(pady=20)


Button = Button(root, text="Stop Alarm", bg="red", fg="white", command=stop_alarm).pack(pady=30)

root.mainloop()