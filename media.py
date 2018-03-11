import webbrowser

class Movie():

    """This function runs at the time of initalising of object"""
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube,releasedate):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.release_date=releasedate
        
    """"This function shows trailer of the link entered by the object"""
    def show_trailer():
        webbrowser.open(self.trailer_youtube_url)
