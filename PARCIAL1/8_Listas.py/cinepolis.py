# movie_manager.py

def agregar_pelicula(peliculas, nombre):
    """Agrega una película a la lista."""
    peliculas.append(nombre)
    return f'Película "{nombre}" agregada con éxito.'

def remover_pelicula(peliculas, nombre):
    """Remueve una película de la lista si existe."""
    if nombre in peliculas:
        peliculas.remove(nombre)
        return f'Película "{nombre}" removida con éxito.'
    else:
        return f'Película "{nombre}" no encontrada.'

def consultar_peliculas(peliculas):
    """Devuelve una lista de todas las películas."""
    if peliculas:
        return "\n".join(peliculas)
    else:
        return "No hay películas en la lista."