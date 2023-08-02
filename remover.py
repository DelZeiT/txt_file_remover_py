# функция удаления слова из текста
def remove_words_from_text(text, words_to_remove):
    lines = text.split("\n")
    edited_lines = []  # список отфильтрованных слов
    deleted_words = []  # список удаленных слов

    for line in lines:
        words = line.split()
        text_without_words = [w for w in words if w.lower() not in words_to_remove]
        deleted_words.extend([w for w in words if w.lower() in words_to_remove])
        edited_line = " ".join(text_without_words)
        edited_lines.append(edited_line)

    return "\n".join(edited_lines), deleted_words


# функция удаления слов с указанной буквой
def remove_words_with_letter(text, letter_to_remove):
    lines = text.split("\n")
    edited_lines = []
    deleted_words = []  # список удаленных слов

    for line in lines:
        words = line.split()
        words_without_letter = [w for w in words if letter_to_remove not in w.lower()]
        deleted_words.extend([w for w in words if letter_to_remove in w.lower()])
        edited_line = " ".join(words_without_letter)
        edited_lines.append(edited_line)

    return "\n".join(edited_lines), deleted_words


# главная функция
def main():
    input_file_name = input(
        "Введите полный путь или относительный путь к файлу с текстом для редактирования: ")  # Путь к файлу
    print()
    # чтение содержимого файла
    try:
        with open(input_file_name, "r", encoding="utf-8") as file:
            content = file.read()

    except FileNotFoundError:
        print(f"Файл '{input_file_name}' не найден.")
        return

    print('''Варианты опции:
    1 - удалить слово из текста
    2 - удалить слово с указанной буквой
    ''')
    # запрос опции, которые нужно выполнить
    option = input('Введите опцию, которую нужно выполнить: ')

    if option == "1":
        # запрос слов, необходимых для удаления
        words_to_remove = input("Введите слова, которые нужно удалить из текста: ")
        words_to_remove = [word.strip().lower() for word in words_to_remove.replace(",", " ").split()]
        edited_content, deleted_words = remove_words_from_text(content, words_to_remove)

    elif option == "2":
        # запрос буквы, слова с которой нужно удалить
        letter_to_remove = input("Введите букву, слова с которой нужно удалить: ")
        edited_content, deleted_words = remove_words_with_letter(content, letter_to_remove)

    # запрос имени файла, в который нужно сохранить отредактированный текст
    output_file_name = input(
        "Введите полный путь или относительный путь к файлу, куда сохранить отредактированный текст: ")

    # запись в файл
    with open(output_file_name, "w", encoding="utf-8") as file:
        file.write(edited_content)

    # запись в файл список удаленных слов
    with open("deleted_words.txt", "w", encoding="utf-8") as file:
        for word in deleted_words:
            file.write(word + "\n")

    print(f"Отредактированный текст сохранен в файл '{output_file_name}'.")
    print(f"Список удаленных слов сохранен в файл 'deleted_words.txt'.")


main()
