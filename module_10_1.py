from time import sleep
import threading

def write_words(word_count, file_name):
    file_ = open(file_name, 'w', encoding='utf-8')
    for num in range(0, word_count):
        sleep(0.1)
        file_.write(f"Какое-то слово № {num + 1}\n")
    file_.close()
    print(f'Завершилась запись в файл {file_name}')

write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

tread1 = threading.Thread(target=write_words, args=(10, 'example5.txt'))
tread2 = threading.Thread(target=write_words, args=(30, 'example6.txt'))
tread3 = threading.Thread(target=write_words, args=(200, 'example7.txt'))
tread4 = threading.Thread(target=write_words, args=(100, 'example8.txt'))
tread1.start()
tread2.start()
tread3.start()
tread4.start()
