from src.analyze_log import (
    most_ordered_food,
    never_ordered_food,
    day_never_visited,
    day_more_visited,
    day_less_visited,
)


class TrackOrders:
    # aqui deve expor a quantidade de estoque

    def __init__(self) -> None:
        self._data = []
        self._len = 0

    def __len__(self):
        return len(self._data)

    def add_new_order(self, customer, order, day):
        self._data.append([customer, order, day])
        self._len += 1

    def get_most_ordered_dish_per_customer(self, customer):
        return most_ordered_food(self._data, customer)

    def get_never_ordered_per_customer(self, customer):
        return never_ordered_food(self._data, customer)

    def get_days_never_visited_per_customer(self, customer):
        return day_never_visited(self._data, customer)

    def get_busiest_day(self):
        return day_more_visited(self._data)

    def get_least_busy_day(self):
        return day_less_visited(self._data)
