import media
import fresh_tomatoes

# declaring instances of type Movie
#instance 1
toy_story=media.Movie("Toy Story",
                      "The Story of boy and his toys when they come to life",
                      "toystory.jpg",
                      r"https://www.youtube.com/watch?v=KYz2wyBy3kc")
#instance 2
serendipity=media.Movie("Serendipity",
                        "Can once in a lifetime happen twice"
                        ,r"serendipity.jpg"
                        ,r"www.youtube.com/watch?v=CsjR5P3TuWY")
#instance 3
into_the_wild=media.Movie("Into the wild",
                          "After graduating from Emory University,top student and athlete Christopher McCandless abandons his possessions,\
                            gives his entire $24,000 savings account to charity and hitchhikes to Alaska to live in the wilderness.\
                            Along the way, Christopher encounters a series of characters that shape his life."
                          ,r"into_the_wild.jpg"
                          ,r"www.dailymotion.com/video/x6gbmm_into-the-wild-trailer_shortfilms")
#instance 4
rocky=media.Movie("Rocky"
                  ,"Rocky Balboa, a small-time boxer gets a supremely rare chance to fight the heavy-weight champion, Apollo Creed,\
                    in a bout in which he strives to go the distance for his self-respect."
                    ,r"http://upload.wikimedia.org/wikipedia/en/1/18/Rocky_poster.jpg"
                      ,r"www.youtube.com/watch?v=Wif1EzGQ9Fk")
#instance 5
about_time=media.Movie("About Time",
                       "At the age of 21, Tim discovers he can travel in time and change what happens and has happened in his own life.\
                        His decision to make his world a better place by getting a girlfriend turns out not to be as easy as you might think."
                       ,r"http://ia.media-imdb.com/images/M/MV5BMTA1ODUzMDA3NzFeQTJeQWpwZ15BbWU3MDgxMTYxNTk@._V1_SX214_AL_.jpg"
                       ,r"www.youtube.com/watch?v=7OIFdWk83no")
#instance 6
thank_u_for_smoking=media.Movie("Thank you for smoking",
                                "Satirical comedy follows the machinations of Big Tobacco's chief spokesman,\
                                Nick Naylor, who spins on behalf of cigarettes while trying to remain a role model for his twelve-year-old son."
                                ,r"http://ia.media-imdb.com/images/M/MV5BMTI2MDk5MjE4NV5BMl5BanBnXkFtZTYwMjkwNTU3._V1_SY317_CR1,0,214,317_AL_.jpg"
                                ,r"www.youtube.com/watch?v=iBELC_vxqhI")

# list which contains all the movie instances above
movies=[toy_story, serendipity, into_the_wild,rocky,about_time,thank_u_for_smoking]

#pass the list to function for creating web page
fresh_tomatoes.open_movies_page(movies)
