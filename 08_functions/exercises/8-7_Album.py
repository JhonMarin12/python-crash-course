""" Write a function called make_album() that builds a dictionary describing a music album. The function should take in an artist name and an album title, and it should return a dictionary containing these two pieces of information. Use the function to make three dictionaries representing different albums. Print each return value to show that the dictionaries are storing the album information correctly.
Use None to add an optional parameter to make_album() that allows you to store the number of songs on an album. If the calling line includes a value for the number of songs, add that value to the album’s dictionary. Make at least one new function call that includes the number of songs on an album."""

def make_album(artist:str, title:str, release=0):
    """Show information about an almbun y dictionary format."""
    album = {'artist':artist, 'title':title}
    if release:
        album['release'] = release
    return album

# Examples
print(make_album('Three Days Grace', 'One-X'))
print(make_album('Bring Me The Horizon', 'Sempieternal'))
print(make_album('Twenty One Pilots', 'Clancy', 2024))
