from typing import List, Tuple
import json
from collections import Counter
from emoji import emoji_list  # Asegúrate de tener instalada la biblioteca emoji

def q2_memory(file_path: str) -> List[Tuple[str, int]]:
    """
    Encuentra los top 10 emojis más usados en un archivo de tweets, optimizado para el uso de memoria.
    
    Este método lee y procesa cada tweet de manera individual para minimizar el uso de memoria,
    contando la frecuencia de cada emoji encontrado y devolviendo los 10 emojis más frecuentes.
    
    Args:
        file_path (str): La ruta al archivo que contiene los tweets.
        
    Returns:
        List[Tuple[str, int]]: Una lista de tuplas que contiene los 10 emojis más usados y su respectivo conteo,
        ordenados de más a menos usado.
    """
    emoji_counter = Counter()
    
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            tweet_content = json.loads(line).get('content', '')
            
            # Se obtienen los emojis de la línea analizada y se actualiza el contador.
            tweet_emojis = [emoji['emoji'] for emoji in emoji_list(tweet_content)]
            emoji_counter.update(tweet_emojis)
    
    # Se devuelven los 10 emojis más presentes en todo el archivo.
    return emoji_counter.most_common(10)
