def count_words(text: str):
    words = []
    for word in text.split():
        word = word.lower()
        for word_dict in words:
            if word in word_dict:
                word_dict[word] += 1
                break
        else:
            words.append({word: 1})
    words.sort(
    key=lambda x: list(x.values())[0], reverse=True
    )
    return words

