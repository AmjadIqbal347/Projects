import webbrowser

#Generic Movie class
class Movie():
    #Constructor
    def __init__(self,movie_title,movie_storyline,movie_poster,movie_trailer):
        #Members of the movie class
        self.title=movie_title
        self.storyline=movie_storyline
        self.poster_image_url=movie_poster
        self.trailer_youtube_url=movie_trailer
    # Function to show trailer for the trailer_youtube_url
    def showtrailer(self):
        #Opens the trailer in the webbrowser
        webbrowser.open(self.trailer)
