#This is GUI for ChatGPT_Spotify_V1.0.py. This GUI allows you to input a song name and it's artist which is then fed into ChatGPT_Spotify_V1.4, which then contacts Chat GPT for sugestions which are then fed into spotify where a playlist with thoes songs is created.
#Created by: Disk5464
#Last Modified: 10/22/24
#Version 1.0: Inital Commit
#####################################################################
#Import the required libaries
import subprocess, os, sys
import tkinter as tk
from tkinter import ttk, scrolledtext

#####################################################################
#Get the current working directory, this will allow us to avoid hard coding paths.
script_directory = os.path.dirname(os.path.abspath(sys.argv[0])) 

#####################################################################
#Create the new GUI, give it a title, and an icon at the top
window = tk.Tk()
window.title("ChatGPT X Spotify Playlist Creator")
window.geometry('700x500')
window.minsize(200, 200)
window.maxsize(1000, 600)
window.iconbitmap(script_directory + "\hank.ico")

#Create the grid. https://www.pythontutorial.net/tkinter/tkinter-grid/
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)

#Add a header at the top center and add it to the window. Make it bold and stretch over two columns
greeting = ttk.Label(text="ChatGPT X Spotify Playlist Creator", font=("Helvetica", 12, "bold"), compound='left')
greeting.grid(column=0, row=0, columnspan=2, padx=5, pady=5)

#####################################################################
#Define the triggers for when different events happen. The first one is triggered when the button is pressed
def button_press(event):
    #Print out that the button has been pressed and define the file path.
    print("Button Pressed")
    file_path = f"{script_directory}\ChatGPT_Spotify_V1.0.py"

    #Create a new python subprocess with the script path, then send the standard output and standard errors to stdout & stderr. This is just the set up nothing is ran yet
    process = subprocess.Popen(["python", file_path, songEntry.get(), artistEntry.get()], stdout=subprocess.PIPE , stderr=subprocess.PIPE, text=True)

    #Run the process defined above (process.communicate) and save the output to the two variables. 
    stdout, stderr = process.communicate()

    #Wipe out any text in the variable that will display the output, then insert the data into it. The if statement inserts the errors instead of the data if there are errors
    output_text.delete(1.0, tk.END) 
    output_text.insert(tk.END, stdout)
    if stderr:
        output_text.insert(tk.END, "\nErrors:\n" + stderr)

#This is triggered when the user hit the esc key. It closes the window.
def close_window(event):
    window.destroy()

#####################################################################
#This section will fill out the first column. The first step is to create a dictionary with key value pairs. They key is the name of the variable and the value is what the lable with be shown.
left_label_texts = {
    "option1_Label":"Enter the name of the song", 
    "option2_Label":"Enter the name of the artist"
}

#For loop that loops through each dictornay value and creates label bassed of each
for i, (key, text) in enumerate(left_label_texts.items()):  #For each item in the dict reach each key/value
    label = ttk.Label(window, text=text)    #Create a new label with the info for the current object
    label.grid(row=i+1, column=0, sticky=tk.EW, padx=5, pady=5) #Put the label on a grid

#####################################################################
#This section is fills out the middle column. Create the textbox then place it on the grid
songEntry = tk.StringVar() #Set a variable that will contain the account the user wants to search for 
songEntryTextBox = ttk.Entry(window, textvariable=songEntry)
songEntryTextBox.grid(column=1, row=1, padx=5, sticky=tk.E)

artistEntry = tk.StringVar() #Set a variable that will contain the account the user wants to search for 
artistEntryTextBox = ttk.Entry(window, textvariable=artistEntry)
artistEntryTextBox.grid(column=1, row=2, padx=5, sticky=tk.E)

#####################################################################
#This section fills out the right column. Create the textbox then place it on the grid. 
button = ttk.Button(window, text="Click me to create the new playlist")    #Create a new button with the info for the current object
button.grid(column=0, row=3, columnspan=2, sticky=tk.EW, padx=5, pady=5) #Put the label on a grid
button.bind("<Button-1>", button_press)

#####################################################################
#Create the output window https://www.pythontutorial.net/tkinter/tkinter-scrolledtext/
output_text = scrolledtext.ScrolledText(window)
output_text.grid(column=0, row=4, columnspan=3, padx=5, pady=5, sticky="nsew")

#Set it so that the escape key closes the window. Then start a loop that pauses the shell until the menu is closed
window.bind('<Escape>', close_window)
window.mainloop()
