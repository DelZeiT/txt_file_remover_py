# функция удаления слова из текста
def remove_word_from_text(text, word):
    words = text.split()

    filtered_words = []    # список отфильтрованных слов
    for w in words:
        if w.lower() != word.lower():
            filtered_words.append(w)

    edited_text = " ".join(filtered_words)
    return edited_text


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
