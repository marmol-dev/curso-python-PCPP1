import tkinter as tk
import random



#
# MODEL
#
class Movie:
    title: str
    year: int
    director: str

    def __init__(self, title, year, director):
        self.title = title
        self.year = year
        self.director = director

def search_movies(text: str) -> list: 
    directors = [
        "Steven Spielberg",
        "Christopher Nolan",
        "Martin Scorsese",
        "Quentin Tarantino",
        "Francis Ford Coppola",
        "Stanley Kubrick",
        "Alfred Hitchcock",
        "Pedro Almodóvar",
        "Guillermo del Toro",
        "Sofia Coppola"
    ]
    peliculas = [
        "El Padrino",
        "Pulp Fiction",
        "Interstellar",
        "El laberinto del fauno",
        "La lista de Schindler",
        "Psicosis",
        "Vértigo",
        "2001: Odisea del espacio",
        "Mujeres al borde de un ataque de nervios",
        "Lost in Translation"
    ]
    return [
        Movie(random.choice(peliculas), random.randint(1950, 2025), random.choice(directors))
        for i in range(random.randint(3, 6)) 
    ]

#
# UI
#
# Crear la ventana principal
root = tk.Tk()
root.title("Contenedor Footer en Tkinter")
root.geometry("400x300")

# HEADER
header_frame = tk.Frame(root, bg='green', borderwidth=2)
header_frame.pack(side=tk.TOP, fill=tk.X)

SHOW_CONFIG_TEXT = "▼ Mostrar configuración"
HIDE_CONFIG_TEXT = "▲ Ocultar configuración"

def toggle_config_frame():
    if config_frame.winfo_manager() == 'pack':
        config_frame.pack_forget()
        button_config.config(text=SHOW_CONFIG_TEXT)
    else:
        config_frame.pack(fill=tk.X)
        button_config.config(text=HIDE_CONFIG_TEXT)

button_config = tk.Button(header_frame, text=SHOW_CONFIG_TEXT, command=lambda: toggle_config_frame())
button_config.pack(fill=tk.X)

config_frame = tk.Frame(header_frame, bg='red', borderwidth=2)
#config_frame.pack(fill=tk.BOTH)

apikey_frame = tk.Frame(config_frame)
apikey_frame.pack(fill=tk.X)

label_apikey = tk.Label(apikey_frame, text="API key:")
label_apikey.pack(side=tk.LEFT)

entry_apikey = tk.Entry(apikey_frame, width=30, bg='white')
entry_apikey.pack(side=tk.RIGHT, fill=tk.X, expand=True, padx=10, pady=10)


# MAIN
main_frame = tk.Frame(root, bg='white', borderwidth=2)
main_frame.pack(fill=tk.BOTH)

def clear_movies():
    # Obtener todos los hijos del frame
    for widget in main_frame.winfo_children():
        widget.destroy()

def print_movies(movies: list):
    # clean main_frame
    clear_movies()
    for movie in movies:
        tk.Label(main_frame, text=movie.title).pack(padx=10, pady=10)
    

footer_frame = tk.Frame(root, bg='yellow', borderwidth=2)
footer_frame.pack(side=tk.BOTTOM, fill=tk.X)

entry = tk.Entry(footer_frame, width=30, bg='white')
entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=10, pady=10)


def on_button_click():
    text = entry.get()
    print(f"Texto ingresado: {text}")  # Mensaje de depuración
    results = search_movies(text)
    print_movies(results)


button = tk.Button(footer_frame, text="🔍 Buscar", command=on_button_click)
button.pack(side=tk.RIGHT, padx=10, pady=10)


root.mainloop()