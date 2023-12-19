import tkinter as tk
from tkinter import messagebox

class TodoListApp:
    def __init__(self, master):
        self.master = master
        self.master.title("To-Do List")

        self.tasks = []
        self.task_entry = tk.Entry(master, width=30)
        self.task_entry.pack(pady=10)

        add_button = tk.Button(master, text="Add Task", command=self.add_task)
        add_button.pack(pady=5)

        self.task_listbox = tk.Listbox(master, selectmode=tk.SINGLE, width=30)
        self.task_listbox.pack(pady=10)

        remove_button = tk.Button(master, text="Remove Task", command=self.remove_task)
        remove_button.pack(pady=5)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def remove_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            task = self.tasks.pop(selected_index[0])
            self.task_listbox.delete(selected_index)
            messagebox.showinfo("Task Removed", f"Task '{task}' removed.")
        else:
            messagebox.showwarning("Warning", "Please select a task to remove.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoListApp(root)
    root.mainloop()
