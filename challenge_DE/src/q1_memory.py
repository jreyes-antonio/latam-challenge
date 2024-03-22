from typing import List, Tuple
from datetime import datetime
import json

def q1_memory(file_path: str) -> List[Tuple[datetime.date, str]]:
    """
    Optimizado para memoria. Procesa el archivo de tweets para encontrar las 10 fechas más comunes
    de publicación y el usuario que más publicó en cada una, sin mantener todos los datos en memoria.

    Args:
        file_path (str): Ruta al archivo con los tweets.

    Returns:
        List[Tuple[datetime.date, str]]: Las 10 fechas más comunes con el usuario más activo en cada una.
    """
    # Paso 1: Contar tweets por fecha
    date_counts = {}
    with open(file_path, 'r') as f:
        for line in f:
            date = datetime.strptime(json.loads(line)['date'].split('T')[0], "%Y-%m-%d").date()
            if date in date_counts:
                date_counts[date] += 1
            else:
                date_counts[date] = 1

    # Paso 2: Identificar las 10 fechas más comunes
    most_common_dates = sorted(date_counts, key=date_counts.get, reverse=True)[:10]

    # Paso 3: Para cada fecha, encontrar el usuario más activo
    results = []
    for date in most_common_dates:
        user_counts = {}
        with open(file_path, 'r') as f:
            for line in f:
                tweet = json.loads(line)
                tweet_date = datetime.strptime(tweet['date'].split('T')[0], "%Y-%m-%d").date()
                if tweet_date == date:
                    username = tweet['user']['username']
                    if username in user_counts:
                        user_counts[username] += 1
                    else:
                        user_counts[username] = 1
        most_common_user = max(user_counts, key=user_counts.get)
        results.append((date, most_common_user))

    return results

