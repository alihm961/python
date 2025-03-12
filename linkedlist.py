class SongNode:
    def __init__(self, name):
        self.name = name  #stores song name
        self.next = None  #pointer to the next
        
class Playlist:
    def __init__(self):
        self.head = None  #Start of the playlist
        
    def add_song(self, song_name):
        """Adds a song to the end of the playlist."""
        new_song = SongNode(song_name)
        if not self.head:
            self.head = new_song
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_song
        print(f"'{song_name}' added.")
        
    def remove_song(self, song_name):
        """removes a song from the playlist."""
        if not self.head:
            print("Playlist is empty!")
            return
        
        # If the first song is the one to remove
        if self.head.name == song_name:
            self.head = self.head.next
            print(f"'{song_name}' removed from playlist!")
            return
        
        current = self.head
        while current.next and current.next.name != song_name:
            current = current.next
            
        if current.next:
            current.next = current.next.next 
            print(f"'{song_name}' removed from the playlist!")
        else:
            print(f"'{song_name}' not found in the playlist!")
            
    def view_playlist(self):
            """Display all songs in the playlist."""
            if not self.head:
                print("Playlist is empty!")
                return
            
            print("Your Playlist:")
            current = self.head
            while current:
                print(f"- {current.name}")
                current = current.next
                
    def play_next(self):
        """skip to the next song and removes the current one."""   
        if not self.head:
            print("No songs left to play!")
            return
        
        print(f"Now playing: {self.head.name}")
        self.head = self.head.next  #move to the next song
        
playlist = Playlist()

while True:
    print("Music Playlist")
    print("1. Add Song")
    print("2. Remove Song")
    print("3. View Playlist")
    print("4. Play Next Song")
    print("5. Exit")
    
    choice = input("Choose an option: ")
    
    if choice == "1":
        song_name = input("Enter song name: ")
        playlist.add_song(song_name)
        
    elif choice == "2":
        song_name = input("Enter song name to remove: ")
        playlist.remove_song(song_name)
        
    elif choice == "3":
        playlist.view_playlist()
        
    elif choice == "4":
        playlist.play_next()
        
    elif choice == "5":
        print("Exiting Music Playlist. Have a great day!")
        break
    
    else:
        print("Invalid option, Please try again.")