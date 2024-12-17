import tkinter as tk
from tkinter import messagebox
def pool(chlorine, v, chlorine_type):
    if chlorine_type == 1:
        pool_chlorine = (v * chlorine) / (1000000 * 0.10)
        result = f"La Cantidad de cloro requerida en su piscina es de {pool_chlorine} Litros"
    elif chlorine_type == 2:
        pool_chlorine = (v * chlorine) / (1000000 * 0.65) 
        pool_chlorine_g = pool_chlorine * 0.001
        result = f"La cantidad de cloro requerida en su piscina es de {pool_chlorine_g} gramos"
    else: 
        result = "El tipo de cloro no es válido"
    messagebox.showinfo("Resultado", result)

def calculate_pool_chlorine():
    estado = estado_var.get()
    chlorine_type = int(chlorine_type_var.get())
    chlorine = float(chlorine_var.get())
    
    if estado.lower() == "no":
        large = float(large_var.get())
        ancho = float(ancho_var.get())
        profundidad_media = float(profundidad_media_var.get())
        v = large * ancho * profundidad_media * 1000
    else:
        v = float(volumen_var.get())
    
    pool(chlorine, v, chlorine_type)

# Crear la ventana principal
root = tk.Tk()
root.title("Calculadora de Cloro para Piscinas")
root.geometry("1000x400")

# Crear un frame para la parte izquierda (informativa)
left_frame = tk.Frame(root, bg="#007FFF", width=400, height=400)
left_frame.pack(side="left", fill="y")

# Añadir texto al frame izquierdo
left_label = tk.Label(left_frame, text="Bienvenido a la Calculadora de Cloro", bg="#007FFF", fg="white", font=("Helvetica", 16, "bold"))
left_label.place(x=20, y=50)

left_text = tk.Label(left_frame, text="Utilice esta herramienta para calcular la cantidad\n"
                                      "de cloro necesaria para su piscina.\n"
                                      "Complete los detalles a la derecha para comenzar.",
                     bg="#007FFF", fg="white", font=("Helvetica", 12))
left_text.place(x=20, y=100)

# Crear un frame para la parte derecha (formulario)
right_frame = tk.Frame(root, width=400, height=400)
right_frame.pack(side="right", fill="y", padx=20, pady=20)

# Variables de tkinter
estado_var = tk.StringVar(value="Si")
chlorine_type_var = tk.StringVar(value="1")
chlorine_var = tk.StringVar()
large_var = tk.StringVar()
ancho_var = tk.StringVar()
profundidad_media_var = tk.StringVar()
volumen_var = tk.StringVar()

# Estilo de las entradas y etiquetas
label_style = {"font": ("Helvetica", 12), "bg": "white"}
entry_style = {"font": ("Helvetica", 12), "bg": "#F0F0F0", "width": 30, "borderwidth": 0, "highlightthickness": 0}

# Crear y colocar los widgets en el frame derecho
tk.Label(right_frame, text="Tiene el valor del volumen de su piscina (Si/No):", **label_style).grid(row=0, column=0, sticky="w", pady=5)
tk.Entry(right_frame, textvariable=estado_var, **entry_style).grid(row=0, column=1, pady=5)

tk.Label(right_frame, text="Escriba 1 para Cloro Líquido y 2 para Granulado:", **label_style).grid(row=1, column=0, sticky="w", pady=5)
tk.Entry(right_frame, textvariable=chlorine_type_var, **entry_style).grid(row=1, column=1, pady=5)

tk.Label(right_frame, text="Escriba la concentración Deseada de Cloro para su Piscina:", **label_style).grid(row=2, column=0, sticky="w", pady=5)
tk.Entry(right_frame, textvariable=chlorine_var, **entry_style).grid(row=2, column=1, pady=5)

tk.Label(right_frame, text="Escriba el Largo de su Piscina (si no tiene volumen):", **label_style).grid(row=3, column=0, sticky="w", pady=5)
tk.Entry(right_frame, textvariable=large_var, **entry_style).grid(row=3, column=1, pady=5)

tk.Label(right_frame, text="Escriba el Ancho de su Piscina (si no tiene volumen):", **label_style).grid(row=4, column=0, sticky="w", pady=5)
tk.Entry(right_frame, textvariable=ancho_var, **entry_style).grid(row=4, column=1, pady=5)

tk.Label(right_frame, text="Escriba la Profundidad Media de su Piscina (si no tiene volumen):", **label_style).grid(row=5, column=0, sticky="w", pady=5)
tk.Entry(right_frame, textvariable=profundidad_media_var, **entry_style).grid(row=5, column=1, pady=5)

tk.Label(right_frame, text="Introduzca el Volumen de su Piscina (si lo tiene):", **label_style).grid(row=6, column=0, sticky="w", pady=5)
tk.Entry(right_frame, textvariable=volumen_var, **entry_style).grid(row=6, column=1, pady=5)

tk.Button(right_frame, text="Calcular", command=calculate_pool_chlorine, bg="#007FFF", fg="white", font=("Helvetica", 12)).grid(row=7, column=0, columnspan=2, pady=20)

# Fondo blanco para el frame derecho
right_frame.config(bg="white")

# Iniciar el bucle de eventos
root.mainloop()