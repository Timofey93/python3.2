import json
from pprint import pprint
from collections import Counter


def get_news(file, encoding):
    with open(file, encoding=encoding) as f:
        news = json.load(f)

    return news


def get_country_news():
    country_info = {
        '1': ('newsfr.json', 'ISO-8859-5'),
        '2': ('newscy.json', 'koi8-r'),
        '3': ('newsafr.json', 'utf8'),
        '4': ('newsit.json', 'cp1251')
    }

    input_country = input("Выберите страну \n 1 - Франция, 2 - Кипр, 3 - Африка, 4 - Италия \n")

    file, encoding = country_info[input_country]

    country_values = get_news(file, encoding)

    get_words(country_values)


def get_words(country_values):

    all_words = list()
    all_words_dict = dict()

    for word in country_values['rss']['channel']['item']:
        if type(word['title']) == str:
            words = word['title'] + word['description']
            all_words += words.split()
        else:
            words = word['title']['__cdata'] + word['description']['__cdata']
            all_words += words.split()
    for w in all_words:
        if len(w.strip('<br>')) >= 7:
            if w not in all_words_dict:
                all_words_dict[w] = 0
            else:
                all_words_dict[w] += 1
    top10 = Counter(all_words_dict).most_common(10)
    pprint(top10)


get_country_news()
