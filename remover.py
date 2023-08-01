# функция удаления слова из текста
def remove_words_from_text(text, words_to_remove):
    lines = text.split("\n")
    edited_lines = []    # список отфильтрованных слов
    for line in lines:
        words = line.split()
        words_without_word = [i for i in words if i.lower() not in words_to_remove]
        edited_line = " ".join(words_without_word)
        edited_lines.append(edited_line)
    return "\n".join(edited_lines)


# главная функция
def main():
    input_file_name = input("Введите полный путь или относительный путь к файлу с текстом для редактирования: ")  # Путь к файлу

    # чтение содержимого файла
    try:
        with open(input_file_name, "r", encoding="utf-8") as file:
            content = file.read()

    except FileNotFoundError:
        print(f"Файл '{input_file_name}' не найден.")
        return

    # запрос слов, необходимых для удаления
    words_to_remove = input("Введите слова, которые нужно удалить из текста: ")
    words_to_remove = [word.strip().lower() for word in words_to_remove.replace(",", " ").split()]

    edited_content = remove_words_from_text(content, words_to_remove)

    # запрос имени файла, в который нужно сохранить отредактированный текст
    output_file_name = input("Введите полный путь или относительный путь к файлу, куда сохранить отредактированный текст: ")

    # запись в файл
    with open(output_file_name, "w", encoding="utf-8") as file:
        file.write(edited_content)

    print(f"Отредактированный текст сохранен в файл '{output_file_name}'.")


if __name__ == "__main__":
    main()
