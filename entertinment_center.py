import fresh_tomatoes
import media

MSD_The_Untold_story = media.Movie("MSD - THE UNTOLD STORY",
                                   "Biopic of cricketer MS.Dhoni",
                                   "https://en.wikipedia.org/wiki/M.S._Dhoni:_The_Untold_Story#/media/File:M.S._Dhoni_-_The_Untold_Story_poster.jpg",
                                   "https://www.youtube.com/watch?v=6L6XqWoS8tw")

Minions = media.Movie("Minions",
                     "animated movie where minions search for their boss",
                     "https://en.wikipedia.org/wiki/Minions_(film)#/media/File:Minions_poster.jpg",
                     "https://www.youtube.com/watch?v=eisKxhjBnZ0")

neerja = media.Movie("NEERJA",
                     "Biopic of cricketer NEERRJA BANOT",
                     "https://en.wikipedia.org/wiki/Neerja#/media/File:Neerja_Poster.jpg",
                     "https://www.youtube.com/watch?v=7779JrWy04g")

ZOOTOPIA = media.Movie("ZOOTOPIA",
                       "how a animal helps in saving HER CITY ",
                       "https://en.wikipedia.org/wiki/Zootopia#/media/File:Zootopia.jpg",
                       "https://www.youtube.com/watch?v=jWM0ct-OLsM")

BABY_DAY_OUT  = media.Movie("BABY'S DAY OUT",
                              "how a small baby travels alone in city and visit all the places in the book and mistakingly harasses his kidnappers alot",
                              "https://en.wikipedia.org/wiki/Baby%27s_Day_Out#/media/File:Babys_day_out_poster.jpg ",
                              "https://www.youtube.com/watch?v=pzow5wUp7hY ")

frozen = media.Movie("FROZEN",
                     "Story about the love of two sisters and how they care and love each other",
                     "https://en.wikipedia.org/wiki/Frozen_(2013_film)#/media/File:Frozen_(2013_film)_poster.jpg ",
                     "https://www.youtube.com/watch?v=FLzfXQSPBOg ")

movies = [MSD_The_Untold_story, Minions, neerja, ZOOTOPIA, BABY_DAY_OUT, frozen]
fresh_tomatoes.open_movies_page(movies)


