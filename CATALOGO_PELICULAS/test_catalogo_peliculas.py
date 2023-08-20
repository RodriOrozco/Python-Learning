from CATALOGO_PELICULAS.domain.Pelicula import Pelicula
from CATALOGO_PELICULAS.services.CatalogoPelicula import CatalogoPeliculas as cp

opcion = None

while opcion != 4:
    try:
        print('Options: ')
        print('1. Add new movie')
        print('2. Show list of movies')
        print("3. Delete movie's list")
        print('4. exit')
        opcion = int(input('Write your option (1-4): '))

        if opcion == 1:
            name_movie = input('Write the name of the movie: ')
            movie = Pelicula(name_movie)
            cp.add_movie(movie)
        if opcion == 2:
            cp.list_movies()
        if opcion == 3:
            cp.delet_list()

    except Exception as e:
        print(f'This exception occur: {e}, Tipo: {type(e)}')
        opcion = None