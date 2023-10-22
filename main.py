import os

current_path = os.getcwd()

while True:
    code = input("""Выберите команду:
    pwd - просмотр теĸущей папĸи;\n
    cd - переход в другую папĸу\n 
    touch - создание пустого файла\n
    cat - вывод содержимого файла\n 
    ls - вывод списĸа файлов в папĸе\n 
    rm - удаление файла\n
    """)

    args = code.split()
    code = args[0]

    path = '' if len(args) < 2 else args[1]

    if code == "pwd":
        print("Текущая папка: ", current_path)

    elif code == "cd":
        new_path = os.path.join(current_path, path)
        if os.path.exists(new_path):
            os.chdir(new_path)
            current_path = new_path

    elif code == "touch":
        file_path = os.path.join(current_path, path)
        open(file_path, 'a')

    elif code == "cat":
        file_path = os.path.join(current_path, path)
        if os.path.isfile(file_path):
            with open(file_path, "r") as file:
                for line in file:
                    print(line.strip())

    elif code == "ls":
        print("Все файлы, находящиеся в папке: ", os.listdir(current_path))

    elif code == "rm":
        files_dir = os.path.join(current_path, path)
        os.remove(files_dir)

    else:
        print("Такой команды не существует!")