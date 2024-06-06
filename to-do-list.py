# to do list in python
import json
import tkinter as tk
from tkinter import *
from tkinter import messagebox

# Function to add a new task
def add_task():
    task_description = task_entry.get()
    if task_description:
        listbox.insert(tk.END, task_description)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "You must enter a task.")

# Function to delete a selected task
def delete_task():
    try:
        selected_task_index = listbox.curselection()[0]
        listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "You must select a task to delete.")

# Function to mark a task as completed
def complete_task():
    try:
        selected_task_index = listbox.curselection()[0]
        task = listbox.get(selected_task_index)
        listbox.delete(selected_task_index)
        listbox.insert(tk.END, task + " (Completed)")
    except IndexError:
        messagebox.showwarning("Warning", "You must select a task to complete.")

# Function to save tasks to a file
def save_tasks():
    tasks = listbox.get(0, tk.END)
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)
    messagebox.showinfo("Info", "Tasks saved to tasks.json")

# Function to load tasks from a file
def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
            listbox.delete(0, tk.END)
            for task in tasks:
                listbox.insert(tk.END, task)
        messagebox.showinfo("Info", "Tasks loaded from tasks.json")
    except FileNotFoundError:
        messagebox.showwarning("Warning", "No saved tasks found.")

root=Tk()
root.title("To Do List")
root.geometry("400x590+500+100")
root.resizable(False,False)
task_list=[]

heading=Label(root,text="TO-DO-LIST",font="arial 20 bold",fg="White",bg="light green")
heading.place(x=130,y=20)

frame=Frame(root,width=400,height=50,bg="White")
frame.place(x=0,y=110)

task_entry = tk.Entry( frame,width=18,font="Areal 20",bd=0,bg="sky blue")
task_entry.place(x=10,y=7)
task_entry.focus()

button=Button(frame,text="ADD",font="Areal 20 bold",width=6,bg="orange",fg="grey",bd=0,cursor="hand2",command=add_task)
button.place(x=300,y=0)

frame1=Frame(root,bd=3,width=700,height=100,bg="yellow")
frame1.pack(pady=(165,0))

frame2=Frame(root,bd=3,width=700,height=60,bg="pink")
frame2.pack(pady=(8,0))

load_button=Button(frame2,text="LOAD",font="Areal 20 bold",width=5,bg="#c1f004",fg="#eb0b56",bd=0,cursor="hand2",command=load_tasks)
load_button.place(x=285,y=1)

complete_button=Button(frame2,text="COMPLETE",font="Areal 20 bold",width=9,bg="yellow",fg="violet",bd=0,cursor="hand2",command=complete_task)
complete_button.place(x=114,y=1)

save_button=Button(frame2,text="SAVE",font="Areal 20 bold",width=5,bg="brown",fg="aquamarine",bd=0,cursor="hand2",command=save_tasks)
save_button.place(x=10,y=1)

listbox=Listbox(frame1,font=("areal",12),width=40,height=15,bg="#32405b",fg="white",cursor="hand2",selectbackground="#5a95ff")
listbox.pack(side=LEFT,fill=BOTH,padx=2,pady=2)

scrollbar=Scrollbar(frame1, cursor="hand2" )
scrollbar.pack(side=RIGHT,fill=BOTH)
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

delete_button=Button(frame,text="DELETE",font="Areal 20 bold",width=8,bg="green",fg="blue",bd=0)
Button(root,delete_button,bd=0,command=delete_task).pack(side=BOTTOM,pady=5)

root.mainloop()