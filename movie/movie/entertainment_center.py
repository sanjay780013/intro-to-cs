import media
import fresh_tomatoes

nepal = media.Movie
toy_story = media.Movie("Toy Story",
                        "Story of Boy",
                        "https://en.wikipedia.org/wiki/Toy_Story#/media/File:Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=qoqG7Px6cOQ")
#print(toy_story.storyline)

avatar = media.Movie("Avatar", "babbal movie","Image","trailer")

#print(avatar.storyline)
#toy_story.show_trailer()
movies = [toy_story, avatar]
#fresh_tomatoes.open_movies_page(movies)
#print(media.Movie.VALID_RATINGS)
print(media.Movie.__doc__)
