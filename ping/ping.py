import tkinter as tk
from tkinter import messagebox, simpledialog
import ping3
import threading
import time
import os

FILE_NAME = "ips.txt"

class PingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Monitor de IPs")
        self.root.geometry("800x600")  # Tamaño más grande por defecto
        
        self.ip_list = self.load_ips()
        self.status_labels = {}
        
        self.frame = tk.Frame(root, bg="#f8fafc")
        self.frame.pack(pady=20)
        
        self.add_button = tk.Button(self.frame, text="Agregar IP", command=self.add_ip, bg="#1d4ed8", fg="white", font=("Arial", 12))
        self.add_button.pack(side=tk.LEFT, padx=10)
        
        self.del_button = tk.Button(self.frame, text="Eliminar IP", command=self.delete_ip, bg="#ef4444", fg="white", font=("Arial", 12))
        self.del_button.pack(side=tk.LEFT, padx=10)
        
        self.ip_frame = tk.Frame(root, bg="#f8fafc")
        self.ip_frame.pack(pady=20)
        
        self.refresh_ui()
        
        self.run_pinger()
        
        self.footer = tk.Label(root, text="AEWhite Devs © 2024", bg="#111827", fg="white", font=("Arial", 10))
        self.footer.pack(side=tk.BOTTOM, fill=tk.X)
    
    def load_ips(self):
        if not os.path.exists(FILE_NAME):
            return {}
        with open(FILE_NAME, "r") as f:
            lines = f.readlines()
        ips = {}
        for line in lines:
            ip, name = line.strip().split(',')
            ips[ip] = name
        return ips
    
    def save_ips(self):
        with open(FILE_NAME, "w") as f:
            for ip, name in self.ip_list.items():
                f.write(f"{ip},{name}\n")
    
    def add_ip(self):
        ip = simpledialog.askstring("Input", "Ingrese la dirección IP:")
        if not ip:
            return
        name = simpledialog.askstring("Input", "Ingrese el nombre para esta IP:")
        if not name:
            return
        self.ip_list[ip] = name
        self.save_ips()
        self.refresh_ui()
    
    def delete_ip(self):
        ip = simpledialog.askstring("Input", "Ingrese la dirección IP a eliminar:")
        if ip in self.ip_list:
            del self.ip_list[ip]
            self.save_ips()
            self.refresh_ui()
        else:
            messagebox.showerror("Error", "IP no encontrada")
    
    def refresh_ui(self):
        for widget in self.ip_frame.winfo_children():
            widget.destroy()
        
        for ip, name in self.ip_list.items():
            frame = tk.Frame(self.ip_frame, bg="#f8fafc", pady=5)
            frame.pack(fill=tk.X)
            
            label = tk.Label(frame, text=f"{name} ({ip})", bg="#f8fafc", font=("Arial", 12))
            label.pack(side=tk.LEFT, padx=10)
            
            status_label = tk.Label(frame, text="Verificando...", width=10, bg="#f8fafc", font=("Arial", 12))
            status_label.pack(side=tk.LEFT, padx=10)
            
            self.status_labels[ip] = status_label
    
    def run_pinger(self):
        def pinger():
            while True:
                for ip in self.ip_list:
                    response = ping3.ping(ip)
                    status_label = self.status_labels[ip]
                    if response:
                        status_label.config(text="En línea", bg="green")
                    else:
                        status_label.config(text="Fuera de línea", bg="red")
                time.sleep(3)
        
        thread = threading.Thread(target=pinger, daemon=True)
        thread.start()

if __name__ == "__main__":
    root = tk.Tk()
    app = PingApp(root)
    root.mainloop()
