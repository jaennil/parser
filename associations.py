""" module for getting associations for school categories """


import json
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import getlinks
import link2text


def init_headless_browser():
    """initialize invisible browser for parsing"""
    options = Options()
    options.headless = True
    browser = webdriver.Firefox(options=options)
    return browser


def main():
    """get all words and their amount from all school websites and save them to json file"""
    # TODO: remove brackets, punctuation marks, numbers, emoji, word.lower()
    browser = init_headless_browser()
    for category in categories:
        print(f"{category = }")
        for school_name in categories[category]["names"]:
            print(f"{school_name = }")
            links = getlinks.get_links(school_name, browser)
            print(f"{links[0] = }")
            text = link2text.get_page_text(links[0], browser)
            for word in text.split():
                word = word.lower()
                for word_dict in categories[category]["words"]:
                    if word in word_dict:
                        word_dict[word] += 1
                        break
                else:
                    categories[category]["words"].append({word: 1})
        categories[category]["words"].sort(
            key=lambda x: list(x.values())[0], reverse=True
        )

    browser.quit()
    with open("words.json", "w", encoding="utf-8") as file:
        json.dump(categories, file, ensure_ascii=False, indent=4)
    remove_common_words()
    with open("words_removed.json", "w", encoding="utf-8") as file:
        json.dump(categories, file, ensure_ascii=False, indent=4)

    print(f"{categories['art']['words'] = }")
    return categories


def remove_common_words():
    """remove word that exists in other categories"""
    for category in categories:
        other_categories = [c for c in categories if c != category]
        for word_dict in categories[category]["words"]:
            word = list(word_dict.keys())[0]
            for other_category in other_categories:
                for index, other_word_dict in enumerate(
                    categories[other_category]["words"]
                ):
                    if word in other_word_dict:
                        del categories[other_category]["words"][index]
                        break


def remove_common_words2():
    """remove word that exists in other categories2"""
    for category in categories:
        other_categories = [c for c in categories if c != category]
        for word_dict in categories[category]["words"]:
            word = list(word_dict.keys())[0]
            if word == list(categories[other_categories[0]]["words"].keys())[0]:
                ...
            if word == list(categories[other_categories[1]]["words"].keys())[0]:
                ...
            if word == list(categories[other_categories[0]]["words"].keys())[0] and word == list(categories[other_categories[1]]["words"].keys())[0]:
                ...


:


categories = {
    "music": {
        "names": [
            "Центральная музыкальная школа при Московской консерватории",
            "Московская средняя специальная музыкальная школа имени Гнесиных",
            "Детская музыкальная школа имени Прокофьева",
            "Детская музыкальная школа имени Одоевского",
            "Детская музыкальная школа имени Дунаевского",
            "Детская музыкальная школа имени Генделя",
            "Детская музыкальная школа имени Рихтера",
            "Музыкальная школа на базе международного образовательного комплекса Brookes Moscow",
        ],
        "words": [],
    },
    "art": {
        "names": [
            "Московская центральная художественная школа при Российской академии художеств(МЦХШ РАХ)",
            "Академия акварели и изящных искусств Сергея Андрияки",
            "Краснопресненская детская художественная школа",
            "Детская школа искусств «Старт»",
            "Тимирязевская детская художественная школа",
            "Детская художественная школаерова",
            "Детская художественная школа имени В.А.Ватагина",
            "Детская художественная школа им. М.А.Врубеля",
            "Детская художественная школа имени В.Ф.Стожарова",
            "Детская художественная школа им. И.Е.Репина",
        ],
        "words": [],
    },
    "phys-math": {
        "names": [
            "Лицей Вторая школа имени В. Ф. Овчинникова",
            "СУНЦ МГУ школа-интернат имени А.Н. Колмогорова",
            "Пятьдесят седьмая школа",
            "Школа № 2007 ФМШ",
            "Школа № 179",
            "Воробьевы горы",
            "Университетская гимназия (школа-интернат) МГУ имени М.В. Ломоносова",
            "Школа № 1535",
            "Бауманская инженерная школа № 1580",
            "Московская школа на Юго-Западе № 1543",
        ],
        "words": [],
    },
}


if __name__ == "__main__":
    main()
