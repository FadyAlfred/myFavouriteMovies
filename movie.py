import webbrowser

class Movie():
    def __init__(self,movie_title,poster_image,trailer_youtube,storyline):
        self.title   = movie_title #movie name
        self.poster_image_url  = poster_image #movie poster
        self.trailer_youtube_url = trailer_youtube #movie trailer
        self.storyline  = storyline #movie story

    def showTrailer(self): #this function display the movie trailer from the youtube url
        webbrowser.open(self.trailer)