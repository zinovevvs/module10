import threading
from time import sleep, time


def write_words(word_count, file_name):
    with open(file_name, 'w') as f:
        for i in range(1, word_count + 1):
            f.write(f"Какое-то слово № {i}\n")
            sleep(0.1)
    print(f"Завершилась запись в файл {file_name}")


# Измеряю время выполнения функции
start_time = time()

# Последовательно вызываю write_words
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

end_time = time()
print(f"Работа функций: {end_time - start_time:.6f} секунд")

# Создаю потоки для параллельного вызова функции
threads = []


def thread_function(word_count, file_name):
    write_words(word_count, file_name)


# Измеряю время выполнения потоков
start_time_threads = time()

thread1 = threading.Thread(target=thread_function, args=(10, 'example5.txt'))
thread2 = threading.Thread(target=thread_function, args=(30, 'example6.txt'))
thread3 = threading.Thread(target=thread_function, args=(200, 'example7.txt'))
thread4 = threading.Thread(target=thread_function, args=(100, 'example8.txt'))

# Добавляю потоки в список и запуск
threads.append(thread1)
threads.append(thread2)
threads.append(thread3)
threads.append(thread4)

for thread in threads:
    thread.start()

# Ожидаю завершения всех потоков
for thread in threads:
    thread.join()

end_time_threads = time()
print(f"Работа потоков: {end_time_threads - start_time_threads:.6f} секунд")
