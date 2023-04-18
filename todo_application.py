import tkinter as tk  #importing it as a tk
from tkinter import ttk #importing the ttk module from tkinter lib
from tkinter import messagebox #importing the messagebox module from the lib
import sqlite3 as sql #importing the sqlite3 module as sql

#defining an epty list to store the taks later and next we are adding functions 
tasks = []

#defining the function to add tasks to the list: 
def add_task():

    task_string = task_field.get()
    if len(task_string) == 0:
        messagebox.showinfo('Error', 'Field is Empty.')
    else:
    task.append(task_string)
    the_cursor.execute('insert into task values (?)', (task_string,))
    list_update()
    task_field.delete(0, 'end')
                                                           # Explanation: 
                                                           # In the above snippet of code, we have defined a function as add_task. 
                                                           # We have used the get() method to retrieve the string from the entry field and stored it in the task_string variable. 
                                                           # We then check whether the string is empty. 
                                                           # If the length of the task_string variable is zero, a message box will be displayed showing the 'Field is Empty' message. 
                                                           # In case the string is not empty, we have used the append() method to add this string to the list we created earlier. 
                                                           # We have also used the execute() method to execute the SQL statement 'insert into tasks values (?)'
                                                           # and stored the value present in the task_string in the database. 
                                                           # We have then called the list_update() function to update the list and deleted the entry in the entry field with the help of the delete() method.

#Now List Updates
def list_update():
    clear_list()
    for task in tasks: 
        task_listbox.insert('end', task)

        #Delete option added
        def delete_task():
            try:
                the_value = task_listbox.get(task_liastbox.curselection())
                if the_value in tasks:
                    tasks.remove(the_value)
                    list_update()     #calling the function to update the list after the process
                    the_cursor.execute('delete from tasks where title = ?', (the_value,))
                except: 
messagebox.showinfo('Wopsie daisy', 'You need to select the trash before you throw it out, boo.')

       #Adding option to delete full list options
       def delete_all_tasks():
    message_box = messagebox.askyesno('You are sure you want to wipe ALL tasks, right?')               #Interaction 
if message_box == True:                                                                                #Scenario 
    while(len(tasks) != 0):                                                                            #Conditions 
        tasks.pop()
        the_cursor.execute('delete from tasks')                                                        #Trigger 
    list_update()

# I have an idea where I want to add a function or option to automatically delete the completed tasks for me or to dump them in a separate "garbage" list.
# If I don't completely forget, cause I will follow through with the code given in the post to get used to it.
# <3 for attention
# :3
# MEOW!
# ^^^^^^^ Literal To-Do item here!! xD


#Additional function to clear the list, which p much does the same as the above unless I'm derping
def clear_list():
    task_listbox.delete(0, 'end')

#Closing the app:
def close():
    print(tasks)
    guiWindow.destroy()

#Fetch data from your DB:
def retrieve_database():
    while(len(tasks) != 0):
        tasks.pop()
        for row in the_cursor.execute('select title from tasks'):
            tasks.append(row[0])

            #Main window for the application (Or 'DASHBOARD' ,I guess.)



#The below is an OBJECT from the Tk() -class- of the Tkinter library~ (this object looks like a piece of CSS, basically, but for GUI XD <- following that syntax ofc)

if __name__=="_main_":
    guiWindow = tk.Tk()
    guiWindow.title("To-Do List Manager Dashboard - JAVATPOINT")
    guiWindow.geometry("500x500+750+250")    #margins
    guiWindow.resizable(0, 0)                #UI feature 
    guiWindow.configure(bg = "#CBBFFF")      #cosmetics 

#Just to mark off the object

#Now adding the DB to the actual app:
the_connection = sql.connect('listOfTasks.db')

#adding OBJECT of cursor class~
the_cursor = the_connection.cursor()
the_cursor.execute('create table if not exists tasks (title text)')  #I hope this is some weird SQL syntax, cause it doesn't make much sense XD



# I.Widgets
# II.Interactions
# III.Events


#1 Frames

#a - defining frames using the tk.Frame() widget
header_frame = tk.Frame(guiWindow, bg = "#CBBFFF")      #cosmetics 
functions_frame = tk.Frame(guiWindow, bg = "#CBBFFF")   #-
listbox_frame = tk.Frame(guiWindow, bg = "#FF96CB")     #-

#b using the pack() method to place the frames in the application 
header_frame.pack(fill="both")                                                      #UI
functions_frame.pack(side = "left", expand = True, fill = "both")                   #-
listbox_frame.pack(side = "right", expand = True, fill = "both")                    #-


#2 Labels

#a defining a label using the ttk.Label() widget:
header_label = ttk.Label(
    header_frame,
    text = "Jerry's To-Do List",         #title
    font = ("Brush Script MT", "30"),    #font
    background = "#CBBFFF",              #cosmetics 
    foreground = "99e2ff"
)
#a.b using pack() method to insert the label into the app ?interface?<dontquotemeonthis idk
header_label.pack(padx= 20, pady = 20)    #margins

#b defining a label again using same widget - ttk.Label() widget
task_label = ttk.Label(
    functions_frame,
    text = "Enter the Task:",
    font = ("Comic Sans MS", "11, "bold"),
)