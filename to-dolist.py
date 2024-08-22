import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("400x400")

        # List to hold tasks as a tuple (task, variable, checkbox)
        self.tasks = []

        # Title Label
        self.title_label = tk.Label(root, text="My To-Do List", font=("Helvetica", 16))
        self.title_label.pack(pady=10)

        # Task Entry Widget
        self.task_entry = tk.Entry(root, width=35, font=("Helvetica", 14))
        self.task_entry.pack(pady=10)

        # Buttons Frame
        self.buttons_frame = tk.Frame(root)
        self.buttons_frame.pack(pady=10)

        # Add Task Button
        self.add_task_button = tk.Button(self.buttons_frame, text="Add Task", command=self.add_task)
        self.add_task_button.grid(row=0, column=0, padx=5)

        # Delete Task Button
        self.delete_task_button = tk.Button(self.buttons_frame, text="Delete Task", command=self.delete_task)
        self.delete_task_button.grid(row=0, column=1, padx=5)

        # Clear All Button
        self.clear_all_button = tk.Button(self.buttons_frame, text="Clear All", command=self.clear_all)
        self.clear_all_button.grid(row=0, column=2, padx=5)

        # Frame to hold the list of tasks
        self.tasks_frame = tk.Frame(root)
        self.tasks_frame.pack(pady=10)

    def add_task(self):
        task_text = self.task_entry.get()
        if task_text != "":
            var = tk.BooleanVar()
            cb = tk.Checkbutton(self.tasks_frame, text=task_text, variable=var,
                                onvalue=True, offvalue=False, font=("Helvetica", 12),
                                fg="blue", bg="lightyellow", activeforeground="green", activebackground="lightgrey")
            cb.pack(anchor='w')
            self.tasks.append((task_text, var, cb))
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")

    def delete_task(self):
        selected_tasks = [task for task in self.tasks if task[1].get()]
        if selected_tasks:
            for task in selected_tasks:
                task[2].destroy()  # Remove the Checkbutton widget
                self.tasks.remove(task)
        else:
            messagebox.showwarning("Warning", "You must select a task to delete.")

    def clear_all(self):
        for task in self.tasks:
            task[2].destroy()  # Remove all Checkbutton widgets
        self.tasks.clear()

# Main Program Execution
if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)  # Instantiate the TodoApp with root as an argument
    root.mainloop()