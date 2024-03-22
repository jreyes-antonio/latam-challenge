from typing import List, Tuple
from collections import Counter
import json

def q3_memory(file_path: str) -> List[Tuple[str, int]]:
    """
    Encuentra los 10 usuarios más mencionados en un conjunto de datos de tweets,
    optimizado para el uso eficiente de la memoria.
    
    Args:
        file_path (str): La ruta al archivo JSON que contiene los tweets.
        
    Returns:
        List[Tuple[str, int]]: Una lista de tuplas que contiene los nombres de usuario
        más mencionados y el número de veces que cada uno fue mencionado,
        ordenados de mayor a menor.
    """
    emoji_counter = Counter()
    
    # Procesar el archivo línea por línea para minimizar el uso de memoria.
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            # Cargar y procesar cada línea (tweet) individualmente.
            tweet = json.loads(line)
            mentionedUsers = tweet.get('mentionedUsers')
            if mentionedUsers:
                # Extraer y contar los usernames de los usuarios mencionados.
                for user in mentionedUsers:
                    if 'username' in user:
                        emoji_counter[user['username']] += 1

    # Devolver los 10 usernames más comunes.
    return emoji_counter.most_common(10)
