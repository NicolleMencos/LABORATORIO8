import tkinter as tk
from tkinter import messagebox

# ----------- MODEL ----------- #
class Tarea:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre
        self.completada = False

    def __str__(self):
        return f"{self.id}. {self.nombre} {'✅' if self.completada else ''}"

class GestorTareas:
    def __init__(self):
        self.tareas = []
        self.contador_id = 1

    def agregar_tarea(self, nombre):
        self.tareas.append(Tarea(self.contador_id, nombre))
        self.contador_id += 1

    def eliminar_tarea(self, id):
        self.tareas = [t for t in self.tareas if t.id != id]

    def get_tareas(self):
        return self.tareas

# ----------- VIEW + CONTROLLER ----------- #
class AppTareas:
    def __init__(self, root):
        self.gestor = GestorTareas()

        root.title("Gestión de Tareas")
        root.geometry("400x300")

        # Campo de texto y botón para agregar
        self.entry = tk.Entry(root, width=25)
        self.entry.pack(pady=5)

        self.btn_agregar = tk.Button(root, text="Agregar", command=self.agregar_tarea)
        self.btn_agregar.pack(pady=5)

        # Lista de tareas
        self.lista = tk.Listbox(root, width=40, height=10)
        self.lista.pack(pady=5)

        # Botón eliminar
        self.btn_eliminar = tk.Button(root, text="Eliminar seleccionada", command=self.eliminar_tarea)
        self.btn_eliminar.pack(pady=5)

    def actualizar_lista(self):
        self.lista.delete(0, tk.END)
        for tarea in self.gestor.get_tareas():
            self.lista.insert(tk.END, str(tarea))

    def agregar_tarea(self):
        nombre = self.entry.get().strip()
        if nombre:
            self.gestor.agregar_tarea(nombre)
            self.entry.delete(0, tk.END)
            self.actualizar_lista()
        else:
            messagebox.showwarning("Atención", "La tarea no puede estar vacía.")

    def eliminar_tarea(self):
        seleccion = self.lista.curselection()
        if seleccion:
            index = seleccion[0]
            tarea = self.gestor.get_tareas()[index]
            self.gestor.eliminar_tarea(tarea.id)
            self.actualizar_lista()
        else:
            messagebox.showwarning("Atención", "Debes seleccionar una tarea para eliminar.")

# ----------- MAIN ----------- #
if __name__ == "__main__":
    root = tk.Tk()
    app = AppTareas(root)
    root.mainloop()
