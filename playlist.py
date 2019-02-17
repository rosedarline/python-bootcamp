playlist = {
    'title': 'YOLO',
    'author': 'Rose Adam',
    'songs': [
        {'title': 'Hello', 'artist': ['Adele'], 'duration': 4.56},
        {'title': 'When we were young', 'artist': ['Adele', 'Beyonce'], 'duration': 4.50},
        {'title': 'God is a woman', 'artist': ['Ariana Grande'], 'duration': 3.0}
    ] 
}

total_length = 0
for song in playlist['songs']:
    total_length += song['duration']
    total_length = round(total_length,2)
print(total_length)