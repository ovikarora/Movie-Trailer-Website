import fresh_tomatoes
import media
""" Info about black panther"""
black_panther = media.Movie("Black Panther",
                            "A Story of a king",
                            "https://upload.wikimedia.org/wikipedia/en/"
                            "0/0c/Black_Panther_film_poster.jpg",
                            "https://www.youtube.com/watch?v=xjDjIWPwcPU",
                            "29 Jan 2018")
""" Info about Padmaavaat"""
padmaavat = media.Movie("Padmaavat",
                        "A Historical Story of king and queen from"
                        "rajesthan",
                        "https://upload.wikimedia.org/wikipedia/en/"
                        "thumb/7/73/Padmaavat_poster.jpg/220px-Padmaavat"
                        "_poster.jpg",
                        "https://www.youtube.com/watch?v=8YaF2m7hCx0",
                        "25 Jan 2018")
""" Info about 3 Idiots"""
idiots = media.Movie("3 Idiots",
                     "A story of 3 idots",
                     "https://upload.wikimedia.org/wikipedia/en/"
                     "thumb/d/df/3_idiots_poster.jpg/220px-3_idiots"
                     "_poster.jpg",
                     "https://www.youtube.com/watch?v=K0eDlFX9GMc",
                     "25 Dec 2009")
""" Info about Student of The Year"""
student_of_the_year = media.Movie("Student of The Year",
                                  "A college story of friends",
                                  "https://upload.wikimedia.org/wikipedia/en/"
                                  "thumb/0/00/Student_of_the_Year_Poster.jpg/"
                                  "220px-Student_of_the_Year_Poster.jpg",
                                  "https://www.youtube.com/watch?"
                                  "v=fivOhPjX9YM",
                                  "19 Oct 2012")
""" Info of Sonu Ke Titu Ki Sweety """
sonu_ke_titu_ki_sweety = media.Movie("Sonu Ke Titu Ki Sweety",
                                     "A Story of fight between bromance and "
                                     "romance",
                                     "https://upload.wikimedia.org/"
                                     "wikipedia/en/"
                                     "thumb/7/77/Sonu_Ke_Titu_Ki_Sweety_-_"
                                     "Movie_Poster.jpg/220px-"
                                     "Sonu_Ke_Titu_Ki_Sweety_-_"
                                     "Movie_Poster.jpg",
                                     "https://www.youtube.com/watch?"
                                     "v=M2q64UowX9g",
                                     "23 Feb 2018")
""" Info about Pyar Ka Punchnama 2"""
pyar_ka_punchnama_2 = media.Movie("Pyaar Ka Punchnama 2",
                                  "A story describing problems"
                                  "of relationship",
                                  "https://upload.wikimedia.org/wikipedia/en"
                                  "/thumb/0/06/Pyaar-Ka-Punch.jpg/"
                                  "220px-Pyaar-Ka-Punch.jpg",
                                  "https://www.youtube.com/watch?"
                                  "v=tC-HGUhxyyc",
                                  "16 Oct 2015")

movies = [black_panther, padmaavat, idiots, student_of_the_year,
          sonu_ke_titu_ki_sweety, pyar_ka_punchnama_2]
fresh_tomatoes.open_movies_page(movies)
