import tkinter as tk
import time

class Stopwatch:
    def __init__(self, master):
        self.master = master
        self.master.title("Cronômetro")
        
        # Variáveis de controle do tempo
        self.running = False
        self.start_time = None
        self.elapsed_time = 0
        
        # Rótulo para exibir o tempo
        self.time_label = tk.Label(master, text="00:00:00", font=("Arial", 24))
        self.time_label.grid(row=0, column=0, columnspan=3, pady=10)
        
        # Botões para controle do cronômetro
        self.start_button = tk.Button(master, text="Iniciar", command=self.start_stopwatch)
        self.start_button.grid(row=1, column=0, padx=5)
        
        self.stop_button = tk.Button(master, text="Parar", command=self.stop_stopwatch)
        self.stop_button.grid(row=1, column=1, padx=5)
        
        self.reset_button = tk.Button(master, text="Resetar", command=self.reset_stopwatch)
        self.reset_button.grid(row=1, column=2, padx=5)
        
        # Iniciar o loop principal para atualizar o tempo
        self.update_time()

    def update_time(self):
        if self.running:
            current_time = time.time()
            self.elapsed_time = current_time - self.start_time
        hours = int(self.elapsed_time // 3600)
        minutes = int((self.elapsed_time % 3600) // 60)
        seconds = int(self.elapsed_time % 60)
        time_str = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
        self.time_label.config(text=time_str)
        self.master.after(1000, self.update_time)

    def start_stopwatch(self):
        if not self.running:
            self.running = True
            self.start_time = time.time() - self.elapsed_time

    def stop_stopwatch(self):
        if self.running:
            self.running = False

    def reset_stopwatch(self):
        self.running = False
        self.start_time = None
        self.elapsed_time = 0
        self.time_label.config(text="00:00:00")

def main():
    root = tk.Tk()
    app = Stopwatch(root)
    root.mainloop()

if __name__ == "__main__":
    main()
