book = open('numbers_book.txt', 'w', encoding='UTF-8')
numbers = ['Вера;55443;Врач', 'Антон;43256;Музыкант', 'Николай;85674;Экономист']
book.write('\n'.join(numbers))
book.close

# #Поиск по характеристики 
name = str(input('Введите имя: '))

for i in numbers:
    if name in i:
        print(i.replace(';',' '))
    else:
        print('Контакт не найден!')

#Добавляем в список значение
new_numbers = str(input('Введите новый контакт в формате Имя;Телефон;Профессия: '))
numbers.append(new_numbers)
book = open('numbers_book.txt', 'w', encoding='UTF-8')
book.write('\n'.join(numbers))
book.close

#Копирование данных из одного файла в другой
number_of_line = int(input('Введите номер строки: '))
if number_of_line > len(numbers):
    print ('Превышено максимальное число строк!')

new_numbers = [numbers[number_of_line - 1]]

book_copy = open('book_copy.txt', 'w', encoding='UTF-8')
book_copy.write('\n'.join(new_numbers))
book_copy.close


