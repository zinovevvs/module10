import threading
import random
import time


class Bank:
    def __init__(self):
        self.balance = 0  # Начальный баланс
        self.lock = threading.Lock()  # Замок для управления доступом

    def deposit(self):
        for _ in range(100):
            amount = random.randint(50, 500)  # Случайное значение для пополнения

        if self.balance >= 500 and self.lock.locked():
            self.lock.release()
        with self.lock:
            self.balance += amount
            print(f"Пополнение: {amount}. Баланс: {self.balance}")
            time.sleep(0.001)

    def take(self):
        for _ in range(100):
            amount = random.randint(50, 500)  # Случайное значение для снятия
            print(f"Запрос на {amount}")

            # Проверка наличия достаточных средств
            if amount <= self.balance:
                with self.lock:  # Блокировка при изменении баланса
                    self.balance -= amount
                    print(f"Снятие: {amount}. Баланс: {self.balance}")
            else:
                print("Запрос отклонён, недостаточно средств")
                self.lock.acquire()  # Блокируем поток при недостаточном балансе

            time.sleep(0.001)  # Имитация времени выполнения операции


# Создание объекта банка
bk = Bank()

# Создание потоков для методов deposit и take
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

# Запуск потоков
th1.start()
th2.start()

# Ожидание завершения потоков
th1.join()
th2.join()

# Вывод итогового баланса
print(f'Итоговый баланс: {bk.balance}')
