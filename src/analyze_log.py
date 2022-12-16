import csv
from collections import Counter


def get_csv(path_to_file):
    if not path_to_file.endswith('.csv'):
        raise FileNotFoundError(f'Extensão inválida: "{path_to_file}"')
    try:
        with open(path_to_file) as f:
            reader = csv.reader(f)
            file_reader = [row for row in reader]
            return file_reader
    except (FileNotFoundError):
        raise FileNotFoundError(f'Arquivo inexistente: "{path_to_file}"')


def most_ordered_food(data, name):
    foods_most_ordered = []

    for order in data:
        if order[0] == name:
            foods_most_ordered.append(order[1])
    # https://pythontic.com/containers/counter/most_common
    foods = Counter(foods_most_ordered)
    return foods.most_common(1)[0][0]


def count_ordered_food(data, name, food):
    count = 0
    for order in data:
        if order[0] == name and order[1] == food:
            count += 1
    return count


def food_data(data):
    foods_not_ordered = []
    for order in data:
        foods_not_ordered.append(order[1])
    return list(dict.fromkeys(foods_not_ordered))


def never_ordered_food(data, name):
    foods_not_ordered = set()

    data_foods = food_data(data)

    for order in data:
        if order[0] == name:
            for food in data_foods:
                if order[1] != food:
                    foods_not_ordered.add(food)

    return foods_not_ordered


def day_data(data):
    days_not_visited = []
    for order in data:
        days_not_visited.append(order[2])
    return list(dict.fromkeys(days_not_visited))


def day_never_visited(data, name):
    days_not_visited = set()

    data_days = day_data(data)

    for order in data:
        if order[0] == name:
            for day in data_days:
                if order[2] != day:
                    days_not_visited.add(day)

    return days_not_visited


def day_more_visited(data):
    days = dict()

    for order in data:
        if order[2] not in days:
            days[order[2]] = 1
        else:
            days[order[2]] += 1

    return max(days, key=days.get)


def day_less_visited(data):
    days = dict()

    for order in data:
        if order[2] not in days:
            days[order[2]] = 1
        else:
            days[order[2]] += 1

    return min(days, key=days.get)


def analyze_log(path_to_file):
    data_file = get_csv(path_to_file)
    new_data = [
        most_ordered_food(data_file, "maria"),
        count_ordered_food(data_file, "arnaldo", "hamburguer"),
        never_ordered_food(data_file, "joao"),
        day_never_visited(data_file, "joao"),
    ]
    with open('data/mkt_campaign.txt', 'w') as f:
        for line in new_data:
            f.write(f'{line}\n')
