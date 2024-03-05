class Song:

    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self,name,artist,genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        self.add_song_to_count()
        self.add_to_genres(genre)
        self.add_to_artists(artist)
        self.add_to_genre_count(genre)
        self.add_to_artist_count(artist)

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    @classmethod
    def add_to_genres(cls,genre):
        cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls,artist):
        cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls,genre):
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    @classmethod
    def add_to_artist_count(cls,artist):
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1

# ninety_nine_problems = Song("99 Problems", "Jay-Z", "Rap")
ninety_nine_problems = Song.add_to_genres( "Rap")
ninety_nine = Song.add_to_artists('Kanye West')
ninety_nine = Song.add_to_genre_count('Rap')


print(Song.add_to_genre_count)   
