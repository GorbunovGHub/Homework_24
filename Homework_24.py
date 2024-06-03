file_name = 'byron.txt'
with open(file_name, mode='r', encoding='utf8') as file:
    file_name = file
    print(file_name.read())
print(file.closed) # - Оператор with автоматически закрывает файл.
