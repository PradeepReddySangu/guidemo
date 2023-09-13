#importing all the modules 
from tkinter import *
from tkinter import font
from tkinter.filedialog import askopenfilename









window =  Tk()
#naming the window
window.title("Ltune")


#adjusting the window size
window.geometry("1000x600")




#defining the menu
# Define a function to be called when the "Open" menu item is clicked
def open_file():
    # Implement the open file functionality here
     pass
# Define a function to be called when the "Exit" menu item is clicked
def exit_app():
    window.quit()

#defien a functin to be called when the send menu item is called
def send_file():
     pass






# Create a menu bar
menubar = Menu(window, tearoff=0)
menu_font = ("Serif", 10)




# Create a "File" menu
file_menu = Menu(menubar, tearoff=0,font = menu_font)  # tearoff=0 removes the dashed line at the top of the menu
file_menu.add_command(label="open", command=open_file, )
file_menu.add_separator()
file_menu.add_command(label="send to", command= send_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_app)




# Add the "File" menu to the menu bar
menubar.add_cascade(label="File", menu=file_menu)


#creating device
device_menu = Menu(menubar, tearoff=0, font = menu_font)
device_menu.add_command(label="open",command=open_file)
device_menu.add_separator()
device_menu.add_command(label="Exit", command=exit_app)




#add the device menu to the menu bar
menubar.add_cascade(label = "Device", menu = device_menu )




#creating operation
operation_menu = Menu(menubar, tearoff=0, font = menu_font)
operation_menu.add_command(label="open",command=open_file)
operation_menu.add_separator()
operation_menu.add_command(label="Exit", command=exit_app)



#add the device menu to the menu bar
menubar.add_cascade(label = "Operation", menu = operation_menu)



#creating  help
help_menu = Menu(menubar, tearoff=0, font = menu_font)
help_menu.add_command(label="open",command=open_file)
help_menu.add_separator()
help_menu.add_command(label="Exit", command=exit_app)



#add the device menu to the menu bar
menubar.add_cascade(label = "Help", menu = help_menu )



# Configure the root window to use the menu bar
window.config(menu=menubar)





# Create a frame for the status bar
horizontal_box = Frame(window, relief=RAISED, borderwidth=5, bg="blue", height=100)
horizontal_box.pack(fill =X) # This makes the frame expand horizontally

# Define a custom font with a specific size
custom_font = font.Font(family="Serif", size=12, weight="bold") 

# Add the "Status" label inside the horizontal box
status_label = Label(horizontal_box, text="Status", fg="white", bg="blue", font = custom_font)
status_label.grid(row = 0 , column = 10)



#adding the middle frame

middle_frame = Frame(window, relief=RAISED, borderwidth=5, bg = "white",height=400)
middle_frame.pack(fill=X)



# Create a frame for the settings  bar
setting_bar = Frame(window, relief=RAISED, borderwidth=5, bg="blue", height=35)
setting_bar.pack(fill =X) # This makes the frame expand horizontally

# Define a custom font with a specific size
custom_font1 = font.Font(family="Serif", size=12, weight="bold") 

# Add the "Status" label inside the horizontal box
status_label1 = Label(setting_bar, text="Settings", fg="white", bg="blue", font = custom_font1)
status_label1.grid(row = 0 , column = 100)









window.mainloop()