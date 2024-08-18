import tkinter as tk
from tkinter import ttk, messagebox
import requests
import json
from requests.auth import HTTPBasicAuth

BASE_URL = 'http://192.168.18.133:8000'

class MovieApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Movie Filter App")
        self.geometry("665x700")
        self.user_data = None  # Para almacenar los datos del usuario logueado

        self.show_login_screen()

    def show_login_screen(self):
        self.login_frame = ttk.Frame(self)
        self.login_frame.pack(pady=100)

        ttk.Label(self.login_frame, text="Username:").pack(pady=5)
        self.username_entry = ttk.Entry(self.login_frame)
        self.username_entry.pack(pady=5)

        ttk.Label(self.login_frame, text="Password:").pack(pady=5)
        self.password_entry = ttk.Entry(self.login_frame, show="*")
        self.password_entry.pack(pady=5)

        ttk.Button(self.login_frame, text="Login", command=self.authenticate_user).pack(pady=20)

    def authenticate_user(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        with open("users.json") as f:
            users = json.load(f)
            print("Loaded users:", users)  # Debug print

        for user in users["users"]:  # Acceder a la lista de usuarios dentro del JSON
            if user["username"] == username and user["password"] == password:
                self.user_data = user
                self.auth = HTTPBasicAuth(username, password)
                print("Authenticated user:", self.user_data)  # Debug print
                self.login_frame.destroy()
                self.create_widgets()
                return

        messagebox.showerror("Error", "Invalid username or password")
    def logout(self):
        # Limpiar la información del usuario y volver a la pantalla de login
        self.user_data = None  # Limpiar la información de usuario
        self.destroy()  # Cerrar la ventana principal
        self.__init__()  # Mostrar de nuevo la pantalla de login

    def create_widgets(self):
        self.canvas = tk.Canvas(self, borderwidth=0)
        self.frame = ttk.Frame(self.canvas)
        self.vsb = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.vsb.set)

        self.vsb.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)
        self.canvas.create_window((4, 4), window=self.frame, anchor="nw", tags="self.frame")

        self.frame.bind("<Configure>", self.on_frame_configure)

        self.filter_label = ttk.Label(self.frame, text="Filter by:")
        self.filter_label.pack(pady=10)

        self.filter_option = ttk.Combobox(self.frame, values=["Title", "Year", "Cast", "Genre"])
        self.filter_option.pack(pady=10)
        self.filter_option.set("Title")

        self.filter_value = ttk.Entry(self.frame)
        self.filter_value.pack(pady=10)

        self.filter_button = ttk.Button(self.frame, text="Filter", command=self.filter_movies)
        self.filter_button.pack(pady=10)

        self.movies_listbox = tk.Listbox(self.frame, width=80, height=15)
        self.movies_listbox.pack(pady=10)

        self.view_all_button = ttk.Button(self.frame, text="View All Movies", command=self.view_all_movies)
        self.view_all_button.pack(pady=10)

        self.create_title_entry = self.create_labeled_entry(self.frame, "Title:")
        self.create_year_entry = self.create_labeled_entry(self.frame, "Year:")
        self.create_cast_entry = self.create_labeled_entry(self.frame, "Cast (comma separated):")
        self.create_genres_entry = self.create_labeled_entry(self.frame, "Genres (comma separated):")

        self.create_button = ttk.Button(self.frame, text="Add Movie", command=self.create_movie)
        self.create_button.pack(pady=10)

        self.filter_label = ttk.Label(self.frame, text="Update movie")
        self.filter_label.pack(pady=10)

        self.edit_title_entry = self.create_labeled_entry(self.frame, "Title of the movie to edit:")
        self.fetch_button = ttk.Button(self.frame, text="Search Movie", command=self.fetch_movie)
        self.fetch_button.pack(pady=10)

        self.new_title_entry = self.create_labeled_entry(self.frame, "Title:")
        self.new_year_entry = self.create_labeled_entry(self.frame, "Year:")
        self.new_cast_entry = self.create_labeled_entry(self.frame, "Cast (comma separated):")
        self.new_genres_entry = self.create_labeled_entry(self.frame, "Genres (comma separated):")

        self.update_button = ttk.Button(self.frame, text="Update Movie", command=self.update_movie)
        self.update_button.pack(pady=10)

        self.delete_title_entry = self.create_labeled_entry(self.frame, "Title to Delete:")
        self.delete_button = ttk.Button(self.frame, text="Delete Movie", command=self.delete_movie)
        self.delete_button.pack(pady=10)

        # Mostrar el rol del usuario y el botón de logout
        self.user_info_label = ttk.Label(self, text=f"Logged in as: {self.user_data['role']}")
        self.user_info_label.pack(pady=10)
        self.logout_button = ttk.Button(self, text="Logout", command=self.logout)
        self.logout_button.pack(pady=10)

    def create_labeled_entry(self, parent, label_text):
        label = ttk.Label(parent, text=label_text)
        label.pack(pady=5)
        entry = ttk.Entry(parent)
        entry.pack(pady=5)
        return entry

    def filter_movies(self):
        filter_type = self.filter_option.get().lower()
        filter_value = self.filter_value.get()

        endpoint = f'{BASE_URL}/movies/by-{filter_type}?{filter_type}={filter_value}'

        response = requests.get(endpoint, auth=self.auth)
        if response.status_code == 200:
            movies = response.json()
            self.display_movies(movies)
        else:
            messagebox.showerror("Error", "No movies found for the given filter")

    def view_all_movies(self):
        response = requests.get(f'{BASE_URL}/movies', auth=self.auth)
        if response.status_code == 200:
            movies = response.json()
            self.display_movies(movies)
        else:
            messagebox.showerror("Error", "Could not fetch movies")

    def display_movies(self, movies):
        self.movies_listbox.delete(0, tk.END)
        for movie in movies:
            self.movies_listbox.insert(tk.END, f"{movie['title']} ({movie['year']}) - {movie['cast']} - {movie['genres']}")

    def create_movie(self):
        title = self.create_title_entry.get()
        year = self.create_year_entry.get()
        cast = self.create_cast_entry.get().split(',')
        genres = self.create_genres_entry.get().split(',')

        movie_data = {
            "title": title,
            "year": int(year),
            "cast": [actor.strip() for actor in cast],
            "genres": [genre.strip() for genre in genres]
        }

        response = requests.post(f'{BASE_URL}/movies', json=movie_data, auth=self.auth)
        if response.status_code == 200:
            messagebox.showinfo("Success", "Movie added successfully")
            self.view_all_movies()
        else:
            messagebox.showerror("Error", "Failed to add movie")

    def fetch_movie(self):
        title = self.edit_title_entry.get()
        response = requests.get(f'{BASE_URL}/movies/by-title?title={title}', auth=self.auth)
        if response.status_code == 200:
            movie = response.json()[0]  # Tomar la primera coincidencia
            self.new_title_entry.delete(0, tk.END)
            self.new_title_entry.insert(0, movie['title'])
            self.new_year_entry.delete(0, tk.END)
            self.new_year_entry.insert(0, movie['year'])
            self.new_cast_entry.delete(0, tk.END)
            self.new_cast_entry.insert(0, ', '.join(movie['cast']))
            self.new_genres_entry.delete(0, tk.END)
            self.new_genres_entry.insert(0, ', '.join(movie['genres']))
        else:
            messagebox.showerror("Error", "Movie not found")

    def update_movie(self):
        title = self.edit_title_entry.get()
        new_title = self.new_title_entry.get()
        year = self.new_year_entry.get()
        cast = self.new_cast_entry.get().split(',')
        genres = self.new_genres_entry.get().split(',')

        movie_data = {
            "title": new_title,
            "year": int(year),
            "cast": [actor.strip() for actor in cast],
            "genres": [genre.strip() for genre in genres]
        }

        response = requests.put(f'{BASE_URL}/movies/{title}', json=movie_data, auth=self.auth)
        if response.status_code == 200:
            messagebox.showinfo("Success", "Movie updated successfully")
            self.view_all_movies()
        else:
            messagebox.showerror("Error", "Failed to update movie")

    def delete_movie(self):
        title = self.delete_title_entry.get()

        response = requests.delete(f'{BASE_URL}/movies/{title}', auth=self.auth)
        if response.status_code == 200:
            messagebox.showinfo("Success", "Movie deleted successfully")
            self.view_all_movies()
        else:
            messagebox.showerror("Error", "Failed to delete movie")

    def on_frame_configure(self, event=None):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

if __name__ == "__main__":
    app = MovieApp()
    app.mainloop()