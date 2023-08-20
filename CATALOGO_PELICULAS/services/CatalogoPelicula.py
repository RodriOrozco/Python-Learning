import os
class CatalogoPeliculas:

    route_file = "movies.txt"
    @classmethod
    def add_movie(cls, movie):
        with open(cls.route_file, 'a', encoding='utf8') as file:
            file.write(f'{movie.name}\n')

    @classmethod
    def list_movies(cls):
        with open(cls.route_file, 'r', encoding='utf8') as file:
            print("Movie's List" .center(50, '-'))
            print(file.read())

    @classmethod
    def delet_list(cls):
        os.remove(cls.route_file)
        print(f'File deleted: {cls.route_file}')