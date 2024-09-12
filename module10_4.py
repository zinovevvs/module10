import threading
import random
import time
from queue import Queue


class Table:
    def __init__(self, number):
        self.number = number  # Номер стола
        self.guest = None  # Гость за столом (по умолчанию None)


class Guest(threading.Thread):
    def __init__(self, name):
        super().__init__()  # Инициализация класса Thread
        self.name = name  # Имя гостя

    def run(self):
        time.sleep(random.randint(3, 10))  # Ожидание случайное время


class Cafe:
    def __init__(self, *tables):
        self.queue = Queue()  # Очередь для гостей
        self.tables = tables  # Список столов

    def guest_arrival(self, *guests):
        for guest in guests:
            # Поиск свободного стола
            for table in self.tables:
                if table.guest is None:
                    table.guest = guest  # гость за столом
                    guest.start()  # запуск потока гостя
                    print(f"{guest.name} сел(-а) за стол номер {table.number}")
                    break
            else:
                self.queue.put(guest)  # Если стола нет, помещаю в очередь
                print(f"{guest.name} в очереди")

    def discuss_guests(self):
        while not self.queue.empty() or any(table.guest is not None for table in self.tables):
            for table in self.tables:
                if table.guest is not None and not table.guest.is_alive():
                    print(f"{table.guest.name} покушал(-а) и ушёл(ушла)")
                    print(f"Стол номер {table.number} свободен")
                    table.guest = None  # Освобождаю стол

                    if not self.queue.empty():  # Если очередь не пуста
                        next_guest = self.queue.get()  # Беру следующего из очереди
                        table.guest = next_guest
                        next_guest.start()
                        print(f"{next_guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}")


tables = [Table(number) for number in range(1, 6)]

guests_names = [
    'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
    'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]

guests = [Guest(name) for name in guests_names]

cafe = Cafe(*tables)

cafe.guest_arrival(*guests)

cafe.discuss_guests()

