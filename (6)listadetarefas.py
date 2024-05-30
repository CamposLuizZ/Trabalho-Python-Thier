import tkinter as tk

class ToDoListApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Lista de Tarefas")
        
        # Lista de tarefas
        self.tasks = []

        # Rótulo e entrada para adicionar tarefas
        self.task_label = tk.Label(master, text="Tarefa:")
        self.task_label.grid(row=0, column=0, sticky="W")
        self.task_entry = tk.Entry(master, width=30)
        self.task_entry.grid(row=0, column=1)
        
        # Botão para adicionar tarefas
        self.add_button = tk.Button(master, text="Adicionar Tarefa", command=self.add_task)
        self.add_button.grid(row=0, column=2)
        
        # Lista de tarefas
        self.tasks_listbox = tk.Listbox(master, width=50)
        self.tasks_listbox.grid(row=1, column=0, columnspan=3, padx=10, pady=10)
        
        # Botão para remover tarefas
        self.remove_button = tk.Button(master, text="Remover Tarefa", command=self.remove_task)
        self.remove_button.grid(row=2, column=0, columnspan=3, pady=5)
        
    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.update_tasks_listbox()
            self.task_entry.delete(0, tk.END)

    def remove_task(self):
        try:
            index = self.tasks_listbox.curselection()[0]
            del self.tasks[index]
            self.update_tasks_listbox()
        except IndexError:
            # Tratar caso nenhum item seja selecionado
            pass

    def update_tasks_listbox(self):
        self.tasks_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.tasks_listbox.insert(tk.END, task)

def main():
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
