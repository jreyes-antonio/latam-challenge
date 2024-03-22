from typing import List, Tuple
from datetime import datetime
import json
from collections import Counter

def q1_time(file_path: str) -> List[Tuple[datetime.date, str]]:
    """
    Optimizado para tiempo. Analiza un archivo de tweets para identificar las 10 fechas más comunes
    de publicación y el usuario que más publicó en cada una de estas fechas.

    Args:
        file_path (str): Ruta al archivo con los tweets.

    Returns:
        List[Tuple[datetime.date, str]]: Las 10 fechas más comunes con el usuario más activo en cada una.
    """
    date_user_counter = Counter()
    user_date_counter = Counter()
    
    with open(file_path, 'r') as f:
        for line in f:
            tweet = json.loads(line)
            date = datetime.strptime(tweet['date'].split('T')[0], "%Y-%m-%d").date()
            username = tweet['user']['username']
            date_user_key = (date, username)
            date_user_counter[date_user_key] += 1
            user_date_counter[date] += 1

    # Obtener las 10 fechas más comunes
    most_common_dates = [date for date, _ in user_date_counter.most_common(10)]

    # Encontrar el usuario más activo para cada fecha
    results = []
    for date in most_common_dates:
        most_common_user = max(
            [(user, count) for (d, user), count in date_user_counter.items() if d == date],
            key=lambda x: x[1]
        )[0]
        results.append((date, most_common_user))

    return results

