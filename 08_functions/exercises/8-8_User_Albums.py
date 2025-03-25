"""Start with your program from Exercise 8-7. Write a while loop that allows users to enter an album’s artist and title. Once you have that information, call make_album() with the user’s input and print the dictionary that’s created. Be sure to include a quit value in the while loop."""

def make_album(artist:str, title:str, release=0):
    """Show information about an almbun y dictionary format."""
    album_info = {'artist':artist, 'title':title}
    if release:
        album_info['release'] = release
    return album_info

while True:
    print("\nPlease, give the next info")
    print("Press q at any time to quit")
    artist_name = input("Artist's name: ")
    if artist_name == 'q':
        break
    album_name = input("Album's name: ")
    if album_name == 'q':
        break
    album = make_album(artist_name, album_name)
    print(album)

