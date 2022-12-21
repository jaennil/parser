""" module for getting associations for school categories """


from utils import categories
import init_browser
import json

import link2text
import query2links


def main():
    generate(init_browser.headless())


def generate(browser):
    """get all words and their amount from all school websites and save them to json file"""
    # TODO: remove brackets, punctuation marks, numbers, emoji, word.lower()
    for category in categories:
        print("working with category: " + category)
        print("------------------------")
        for school_name in categories[category]["names"]:
            print("working with school: " + school_name)
            school_links = query2links.get(school_name, browser, amount=2)
            print("school links: " + str(school_links))
            for link in school_links:
                text = link2text.get_page_text(link, browser)
                for word in text.split():
                    word = word.lower()
                    for word_dict in categories[category]["words"]:
                        if word in word_dict:
                            word_dict[word] += 1
                            break
                    else:
                        categories[category]["words"].append({word: 1})
        # sort words by amount
        categories[category]["words"].sort(
            key=lambda x: list(x.values())[0], reverse=True
        )
    # write to json
    with open("words.json", "w", encoding="utf-8") as file:
        json.dump(categories, file, ensure_ascii=False, indent=4)
    # remove words that exist in other categories
    remove_common_words()
    # write removed words to json
    with open("words_removed.json", "w", encoding="utf-8") as file:
        json.dump(categories, file, ensure_ascii=False, indent=4)
    print(f"{categories['art']['words'] = }")
    return categories


def remove_common_words():
    """remove word that exists in other categories2"""
    for category in categories:
        for index, word_dict in enumerate(categories[category]["words"]):
            word_deleted = False
            word = [key for key in word_dict][0]
            for other_category in categories:
                if other_category != category:
                    for other_index, other_word_dict in enumerate(categories[other_category]["words"]):
                        if word in other_word_dict:
                            del categories[other_category]["words"][other_index]
                            if not word_deleted: del categories[category]["words"][index]
                            word_deleted = True
                            break


if __name__ == "__main__":
    main()
