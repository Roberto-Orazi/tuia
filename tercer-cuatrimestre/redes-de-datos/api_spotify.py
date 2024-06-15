import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Configura tus credenciales
client_id = 'TU_CLIENT_ID'
client_secret = 'TU_CLIENT_SECRET'
redirect_uri = 'TU_REDIRECT_URI'
# Inicia la autenticación de Spotify con Facebook
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, scope='user-library-read user-read-playback-state user-modify-playback-state'))

# Obtén la información del usuario
user_info = sp.me()
print(f'Bienvenido, {user_info["display_name"]}!')

# Obtiene los dispositivos activos
devices = sp.devices()['devices']

# Imprime los dispositivos disponibles
print("Dispositivos activos:")
for i, device in enumerate(devices, start=1):
    print(f"{i}. {device['name']} ({device['type']})")

# Solicita al usuario que seleccione un dispositivo
selected_device_index = int(input("Ingrese el número del dispositivo en el que desea reproducir la canción: "))

# Verifica si el índice seleccionado es válido
if 1 <= selected_device_index <= len(devices):
    selected_device_id = devices[selected_device_index - 1]['id']

    # Obtén las canciones de una playlist específica
    playlist_id = 'TU_PLAYLIST_ID'

    # Inicializa el contador de canciones
    contador_canciones = 0

    # Parámetros para la paginación
    limit = 100
    offset = 0

    print(f'Canciones en la playlist:')
    while True:
        playlist_tracks = sp.playlist_tracks(playlist_id, limit=limit, offset=offset)

        for track in playlist_tracks['items']:
            # Incrementa el contador de canciones
            contador_canciones += 1

            # Imprime información de la canción
            print(f'{contador_canciones}. {track["track"]["name"]} - {track["track"]["artists"][0]["name"]}')

        # Actualiza el offset para la próxima página
        offset += limit

        # Verifica si hay más páginas
        if not playlist_tracks['next']:
            break

    # Solicita al usuario que ingrese el nombre de la canción
    nombre_cancion_buscada = input("Ingrese el nombre de la canción que desea reproducir (sin distinguir mayúsculas o minúsculas): ")

    # Busca la canción en la lista de reproducción
    cancion_encontrada = None
    for track in playlist_tracks['items']:
        if nombre_cancion_buscada.lower() == track['track']['name'].lower():
            cancion_encontrada = track['track']['uri']
            break

    # Reproduce la canción encontrada en el dispositivo seleccionado
    if cancion_encontrada:
        print(f"Reproduciendo canción seleccionada en el dispositivo ...")
        sp.start_playback(uris=[cancion_encontrada], device_id=selected_device_id)
    else:
        print("La canción no se encontró en la playlist.")
else:
    print("Número de dispositivo no válido.")