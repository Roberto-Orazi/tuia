import tkinter as tk
from tkinter import ttk, messagebox
import requests

BASE_URL = 'http://127.0.0.1:8000'

class MovieApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Movie App")
        self.geometry("600x500")

        self.create_widgets()

    def create_widgets(self):
        self.filter_label = ttk.Label(self, text="Filter by:")
        self.filter_label.pack(pady=10)

        self.filter_option = ttk.Combobox(self, values=["Year", "cast", "Genre"])
        self.filter_option.pack(pady=10)
        self.filter_option.set("Year")

        self.filter_value = ttk.Entry(self)
        self.filter_value.pack(pady=10)

        self.filter_button = ttk.Button(self, text="Filter", command=self.filter_movies)
        self.filter_button.pack(pady=10)

        self.movies_listbox = tk.Listbox(self, width=80, height=15)
        self.movies_listbox.pack(pady=10)

        self.view_all_button = ttk.Button(self, text="View All Movies", command=self.view_all_movies)
        self.view_all_button.pack(pady=10)

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

if __name__ == "__main__":
    app = MovieApp()
    app.mainloop()
