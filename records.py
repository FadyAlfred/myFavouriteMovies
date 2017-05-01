import movie
import fresh_tomatoes

theGodfather = movie.Movie("The GodFather",
                           "http://i2.wp.com/moeatthemovies.com/wp-content/uploads/2012/12/wpid-photo-jun-27-2012-931-pm.jpg",
                           "https://www.youtube.com/watch?v=sY1S34973zA&t=20s",
                           "The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.")
#first instance of movie class

theDarkKnight = movie.Movie("The Dark Knight",
                            "http://www.geeksofdoom.com/GoD/img/2008/news/2008-04-25-darkknight_lg.jpg",
                            "https://www.youtube.com/watch?v=EXeTwQWrcwY",
                            "When the menace known as the Joker wreaks havoc and chaos on the people of Gotham"
                            ", the caped crusader must come to terms with one of the greatest psychological tests of his ability to fight injustice.")
#second instance of movie class

insideOut = movie.Movie("Inside Out",
                           "http://fontmeme.com/images/inside-out-poster.jpg",
                           "https://www.youtube.com/watch?v=seMwpP0yeu4",
                           "After young Riley is uprooted from her Midwest life and moved to San Francisco, her emotions - Joy, Fear, Anger, Disgust and Sadness"
                           "- conflict on how best to navigate a new city, house, and school.")
#third instance of movie class

movies = [theGodfather,theDarkKnight,insideOut] #list of movies to pass to function open_moive+page

fresh_tomatoes.open_movies_page(movies) #this function in fresh tomatoes module open the html page with the records i added 