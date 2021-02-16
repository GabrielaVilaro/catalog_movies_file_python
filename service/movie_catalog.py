import os


class MovieCatalog:
    path_file = '/home/gabriela/PycharmProjects/catalogoPeliculas/movies_list.txt'

    @staticmethod
    def add_movie(movie):
        global file
        try:
            # a =  append movie
            file = open(MovieCatalog.path_file, 'a')
            file.write(movie.__str__())
        except Exception as e:
            print('An exception occurred ', e)
        finally:
            file.close()

    @staticmethod
    def list_movies():
        global file
        try:
            # a =  append movie
            file = open(MovieCatalog.path_file, 'r')
            print(file.read())
        except Exception as e:
            print('An exception occurred ', e)
        finally:
            file.close()

    @staticmethod
    def delete_movie():
        try:
            os.remove(MovieCatalog.path_file)
            print('Archivo eliminado ', MovieCatalog.path_file)
        except Exception as e:
            print('An exception occurred ', e)
