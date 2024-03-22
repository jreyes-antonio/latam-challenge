from typing import List, Tuple
import json
from emoji import emoji_list  # Asegúrate de tener instalada la biblioteca emoji
from collections import Counter

def q2_time(file_path: str) -> List[Tuple[str, int]]:
    """
    Encuentra los top 10 emojis más usados en un archivo de tweets, optimizado para tiempo,
    utilizando el método emoji_list para una identificación eficiente de emojis.
    
    Args:
        file_path (str): La ruta al archivo que contiene los tweets.
        
    Returns:
        List[Tuple[str, int]]: Una lista de tuplas que contiene los emojis y su respectivo conteo,
        ordenados de más a menos usado.
    """
    emojis = []
    
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            tweet = json.loads(line)
            content = tweet.get('content', '')  
            emojis.extend([emoji['emoji'] for emoji in emoji_list(content)])
    
    return Counter(emojis).most_common(10)

