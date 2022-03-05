"""Exercise 23: Extract Class"""


class Actor:
    def __init__(self, first_name, last_name, birth_year, movies, email):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_year = birth_year
        self.movies = movies
        self.email = email

    def print_info(self):
        print(self.first_name, self.last_name)
        print('Movies Played: ', end='')
        for movie in self.movies:
            print(movie, end=', ')
        print()

    def send_hiring_email(self):
        print('email sent to: ', self.email)


first_names = ['elizabeth', 'Jim']
last_names = ['debicki', 'Carrey']
birth_year = [1990, 1962]
movies = [['Tenet', 'Vita & Virgina', 'Guardians of the Galexy', 'The Great Gatsby'],
          ['Ace Ventura', 'The Mask', 'Dubm and Dumber', 'The Truman Show', 'Yes Man']]
emails = ['deb@makeschool.com', 'jim@makeschool.com']

actors_list = []
for i, value in enumerate(emails):
    actors_list.append(
        Actor(first_names[i], last_names[i], birth_year[i], movies[i], value))

for actor in actors_list:
    if actor.birth_year > 1985:
        actor.print_info()
        actor.send_hiring_email()
