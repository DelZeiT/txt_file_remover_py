# функция удаления слова из текста
def remove_word_from_text(text, word):
    lines = text.split()
    edited_lines = []    # список отфильтрованных слов
    for line in lines:
        words = line.split()
        for i in words:
            if i.lower() != word.lower():
                words_without_word = i
        edited_line = " ".join(words_without_word)
        edited_lines.append(edited_line)
    return "\n".join(edited_lines)


# главная функция
def main():
    input_file_name = "textWAR_I.txt"  # Путь к файлу

    # чтение содержимого файла
    try:
        with open(input_file_name, "r", encoding="utf-8") as file:
            content = file.read()

    except FileNotFoundError:
        print(f"Файл '{input_file_name}' не найден.")
        return

    # запрос слова, необходимого для удаления
    word_to_remove = input("Введите слово, которое нужно удалить из текста: ")

    edited_content = remove_word_from_text(content, word_to_remove)

    # запрос имени файла, в который нужно сохранить отредактированный текст
    output_file_name = input("Введите имя файла, куда сохранить отредактированный текст: ")

    # запись в файл
    with open(output_file_name, "w", encoding="utf-8") as file:
        file.write(edited_content)

    print(f"Отредактированный текст сохранен в файл '{output_file_name}'.")


if __name__ == "__main__":
    main()
