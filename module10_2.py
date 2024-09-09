import threading
import time


class Knight(threading.Thread):
    total_enemies = 100  # Общее количество врагов
    enemies_left = total_enemies  # Оставшиеся враги

    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self.days = 0  # Количество дней сражений

    def run(self):
        print(f"{self.name}, на нас напали!")

        while Knight.enemies_left > 0:
            time.sleep(1)  # Задержка в 1 секунду (1 день сражений)
            self.days += 1

            # Уменьшаем количество оставшихся врагов на силу рыцаря
            Knight.enemies_left -= self.power

            # Не позволяем врагам стать отрицательными
            enemies_left_display = max(Knight.enemies_left, 0)

            print(f"{self.name}, сражается {self.days} день(дня)..., осталось {enemies_left_display} воинов.")

        print(f"{self.name} одержал победу спустя {self.days} дней(дня)!")


# Создание экземпляров класса Knight
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight('Sir Galahad', 20)

# Запуск потоков
first_knight.start()
second_knight.start()

# Ожидание завершения потоков
first_knight.join()
second_knight.join()

# Вывод, когда все битвы закончены
print("Все битвы закончились!")
