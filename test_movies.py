from domain.movie import Movie
from service.movie_catalog import MovieCatalog

option = None

while option != '4':
    print('Opciones disponibles: ')
    print('1- Agregar Película')
    print('2- Listar Películas')
    print('3- Eliminar catálogo de películas')
    print('4- Salir del programa')
    option = input('Elige una opción entre el 1 y el 4: ')
    if option == '1':
        movie_name = input('Ingresa el nombre de la película: ')
        movie = Movie(movie_name)
        MovieCatalog.add_movie(movie)
    elif option == '2':
        MovieCatalog.list_movies()
    elif option == '3':
        MovieCatalog.delete_movie()
else:
    print('Has salido del programa.')
