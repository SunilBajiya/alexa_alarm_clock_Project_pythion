# this is the user interactive interface 

import tkinter
from time import strftime

# creating the main application window
top = tkinter.Tk()
top.title("Live Clock")
top.resizable(0, 0)

# function to determine the time of day
def get_time_of_day(hour):
    if 5 <= hour < 12:
        return "Morning"
    elif 12 <= hour < 18:
        return "Afternoon"
    else:
        return "Evening"

# function to update the time display
def update_time():
    current_time = strftime("%H:%M:%S %p")
    
    hour = int(strftime("%H"))
    time_of_day = get_time_of_day(hour)
    
    # updating the text of the clockTime label with the current time and time of day
    clock_time.config(text=current_time + f"\nGood {time_of_day}!")
    
    # dynamically change the background color based on time of day
    color = (
        "lightblue"
        if time_of_day == "Morning"
        else "lightyellow" if time_of_day == "Afternoon" else "lightcoral"
    )
    top.config(background=color)
    
    # schedule the update_time function to be called again after 1000 milliseconds (1 second)
    clock_time.after(1000, update_time)

# create a label widget to display the time
clock_time = tkinter.Label(
    top,
    font=("courier new", 40),
    background="black",
    foreground="white"
)

# position the label widget in the center of the window
clock_time.pack(anchor="center")

# call the update_time function to start updating the time display
update_time()

# start the Tkinter main event loop
top.mainloop()
