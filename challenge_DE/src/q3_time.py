from typing import List, Tuple
from collections import Counter
import json

def q3_time(file_path: str) -> List[Tuple[str, int]]:
    """
    Encuentra los 10 usuarios más mencionados en un conjunto de datos de tweets.

    Args:
        file_path (str): La ruta al archivo JSON que contiene los tweets.

    Returns:
        List[Tuple[str, int]]: Una lista de tuplas que contiene los nombres de usuario más mencionados
        y el número de veces que cada uno fue mencionado, ordenados de mayor a menor.
    """
    # Se inicializa una lista vacía para almacenar los nombres de usuario mencionados.
    usernames = []
    
    # Se abre el archivo y se lee línea por línea.
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            tweet = json.loads(line)
            # Se comprueba si 'mentionedUsers' está presente y no es None.
            if tweet.get('mentionedUsers') is not None:
                # Por cada usuario mencionado en el tweet, se extrae su nombre de usuario.
                for user in tweet['mentionedUsers']:
                    usernames.append(user['username'])

    # Se utiliza Counter para contar las ocurrencias de cada nombre de usuario y obtener los 10 más comunes.
    top_usernames = Counter(usernames).most_common(10)
    
    return top_usernames
