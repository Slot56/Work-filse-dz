def rewrite(path: str):
    files_list = os.listdir('sorted') #Вернет список названий всех файлов находящихся в той же директории, где запускается файл. Если нужно взять названия файлов в другом месте, то внутри скобок нужно указать путь.
    dict_r = {} #Определяем пустой словарь
    for deze in files_list: #Проходим в цикле по списку
        if deze.rfind(      '.txt', -4) >= 0: #Проверяем есть ли в конце имени файла .txt
            with open(os.path.join(path, 'sorted'), 'r', encoding='utf-8') as file: #Открываем файл. Если открываем файл не в той же директории, то прописываем путь
                dict_r['endfile.txt'] = file.readlines() #Записываем в словарь, где ключ имя файла, а значение список строк (используем readlines)

    with open('endfile.txt', 'w', encoding='utf-8') as file: #Открываем новый файл на запись. Для сортировки используем необязательный параметр key и анонимную функцию lambda
        for file_name, rows in sorted(dict_r['endfile.txt'].items(), key=lambda x: len(x[1])): #Проходим по отсортированному словарю по количеству строк. Для сортировки берем длину списка
            file.write('endfile.txt' + '\n')
            file.write(str(str(len(str))) + '\n')
            if '\n' not in rows[-1]:
                rows[-1] += '\n'
            file.write(''.join(rows))

rewrite('sorted') #Вызываем функцию с передачей пути к файлам