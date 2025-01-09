import tkinter as tk
from tkinter import ttk, messagebox

class OrbitalApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Orbital - Ticket Management System")
        self.create_widgets()

    def create_widgets(self):
        # Create main frame
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Project type label and combobox
        ttk.Label(main_frame, text="Project Type:").grid(row=0, column=0, sticky=tk.W)
        self.project_type = ttk.Combobox(main_frame, values=["Type1", "Type2", "Type3"])
        self.project_type.grid(row=0, column=1, sticky=(tk.W, tk.E))

        # Ticket title label and entry
        ttk.Label(main_frame, text="Ticket Title:").grid(row=1, column=0, sticky=tk.W)
        self.ticket_title = ttk.Entry(main_frame)
        self.ticket_title.grid(row=1, column=1, sticky=(tk.W, tk.E))

        # Ticket description label and text
        ttk.Label(main_frame, text="Description:").grid(row=2, column=0, sticky=tk.W)
        self.ticket_description = tk.Text(main_frame, height=10, width=40)
        self.ticket_description.grid(row=2, column=1, sticky=(tk.W, tk.E))

        # Priority label and combobox
        ttk.Label(main_frame, text="Priority:").grid(row=3, column=0, sticky=tk.W)
        self.priority = ttk.Combobox(main_frame, values=["Low", "Medium", "High"])
        self.priority.grid(row=3, column=1, sticky=(tk.W, tk.E))

        # Status label and combobox
        ttk.Label(main_frame, text="Status:").grid(row=4, column=0, sticky=tk.W)
        self.status = ttk.Combobox(main_frame, values=["Open", "In Progress", "Closed"])
        self.status.grid(row=4, column=1, sticky=(tk.W, tk.E))

        # Buttons for creating and updating tickets
        self.create_button = ttk.Button(main_frame, text="Create Ticket", command=self.create_ticket)
        self.create_button.grid(row=5, column=0, sticky=tk.W)

        self.update_button = ttk.Button(main_frame, text="Update Ticket", command=self.update_ticket)
        self.update_button.grid(row=5, column=1, sticky=tk.E)

        # Ticket list
        self.ticket_list = ttk.Treeview(main_frame, columns=("Title", "Project Type", "Priority", "Status"), show="headings")
        self.ticket_list.heading("Title", text="Title")
        self.ticket_list.heading("Project Type", text="Project Type")
        self.ticket_list.heading("Priority", text="Priority")
        self.ticket_list.heading("Status", text="Status")
        self.ticket_list.grid(row=6, column=0, columnspan=2, sticky=(tk.W, tk.E))

        # Configure column weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)

    def create_ticket(self):
        title = self.ticket_title.get()
        project_type = self.project_type.get()
        description = self.ticket_description.get("1.0", tk.END).strip()
        priority = self.priority.get()
        status = self.status.get()

        if not title or not project_type or not description or not priority or not status:
            messagebox.showerror("Error", "All fields must be filled out")
            return

        self.ticket_list.insert("", "end", values=(title, project_type, priority, status))
        self.clear_fields()
        messagebox.showinfo("Success", "Ticket created successfully")

    def update_ticket(self):
        selected_item = self.ticket_list.selection()
        if not selected_item:
            messagebox.showerror("Error", "No ticket selected")
            return

        title = self.ticket_title.get()
        project_type = self.project_type.get()
        description = self.ticket_description.get("1.0", tk.END).strip()
        priority = self.priority.get()
        status = self.status.get()

        if not title or not project_type or not description or not priority or not status:
            messagebox.showerror("Error", "All fields must be filled out")
            return

        self.ticket_list.item(selected_item, values=(title, project_type, priority, status))
        self.clear_fields()
        messagebox.showinfo("Success", "Ticket updated successfully")

    def clear_fields(self):
        self.ticket_title.delete(0, tk.END)
        self.project_type.set("")
        self.ticket_description.delete("1.0", tk.END)
        self.priority.set("")
        self.status.set("")

if __name__ == "__main__":
    root = tk.Tk()
    app = OrbitalApp(root)
    root.mainloop()
