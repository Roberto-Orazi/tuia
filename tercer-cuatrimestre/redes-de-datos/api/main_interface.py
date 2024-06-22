import tkinter as tk
from tkinter import ttk, messagebox
import requests

BASE_URL = 'http://127.0.0.1:8000'

class MovieApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Movie Filter App")
        self.geometry("665x700")

        self.create_widgets()

    def create_widgets(self):
        self.canvas = tk.Canvas(self, borderwidth=0)
        self.frame = ttk.Frame(self.canvas)
        self.vsb = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.vsb.set)

        self.vsb.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)
        self.canvas.create_window((4,4), window=self.frame, anchor="nw", tags="self.frame")

        self.frame.bind("<Configure>", self.on_frame_configure)

        self.filter_label = ttk.Label(self.frame, text="Filter by:")
        self.filter_label.pack(pady=10)

        self.filter_option = ttk.Combobox(self.frame, values=["Title", "Year", "cast", "Genre"])
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

        self.title_entry = self.create_labeled_entry(self.frame, "Title:")
        self.year_entry = self.create_labeled_entry(self.frame, "Year:")
        self.cast_entry = self.create_labeled_entry(self.frame, "Cast (comma separated):")
        self.genres_entry = self.create_labeled_entry(self.frame, "Genres (comma separated):")

        self.create_button = ttk.Button(self.frame, text="Add Movie", command=self.create_movie)
        self.create_button.pack(pady=10)

        self.update_button = ttk.Button(self.frame, text="Update Movie", command=self.update_movie)
        self.update_button.pack(pady=10)

        self.delete_title_entry = self.create_labeled_entry(self.frame, "Title to Delete:")
        self.delete_button = ttk.Button(self.frame, text="Delete Movie", command=self.delete_movie)
        self.delete_button.pack(pady=10)

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

        response = requests.get(endpoint)
        if response.status_code == 200:
            movies = response.json()
            self.display_movies(movies)
        else:
            messagebox.showerror("Error", "No movies found for the given filter")

    def view_all_movies(self):
        response = requests.get(f'{BASE_URL}/movies')
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
        title = self.title_entry.get()
        year = self.year_entry.get()
        cast = self.cast_entry.get().split(',')
        genres = self.genres_entry.get().split(',')

        movie_data = {
            "title": title,
            "year": int(year),
            "cast": [actor.strip() for actor in cast],
            "genres": [genre.strip() for genre in genres]
        }

        response = requests.post(f'{BASE_URL}/movies', json=movie_data)
        if response.status_code == 200:
            messagebox.showinfo("Success", "Movie added successfully")
            self.view_all_movies()
        else:
            messagebox.showerror("Error", "Failed to add movie")

    def update_movie(self):
        title = self.title_entry.get()
        year = self.year_entry.get()
        cast = self.cast_entry.get().split(',')
        genres = self.genres_entry.get().split(',')

        movie_data = {
            "title": title,
            "year": int(year),
            "cast": [actor.strip() for actor in cast],
            "genres": [genre.strip() for genre in genres]
        }

        response = requests.put(f'{BASE_URL}/movies/{title}', json=movie_data)
        if response.status_code == 200:
            messagebox.showinfo("Success", "Movie updated successfully")
            self.view_all_movies()
        else:
            messagebox.showerror("Error", "Failed to update movie")

    def delete_movie(self):
        title = self.delete_title_entry.get()

        response = requests.delete(f'{BASE_URL}/movies/{title}')
        if response.status_code == 200:
            messagebox.showinfo("Success", "Movie deleted successfully")
            self.view_all_movies()
        else:
            messagebox.showerror("Error", "Failed to delete movie")

    def on_frame_configure(self):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

if __name__ == "__main__":
    app = MovieApp()
    app.mainloop()
