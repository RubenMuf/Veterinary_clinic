def slug(word):
    word1 = ''
    for i in word.lower():
        if i == 'а':
            word1 += 'a'
        elif i == 'б':
            word1 += 'b'
        elif i == 'в':
            word1 += 'v'
        elif i == 'г':
            word1 += 'g'
        elif i == 'д':
            word1 += 'd'
        elif i == 'е':
            word1 += 'e'
        elif i == 'ё':
            word1 += 'e'
        elif i == 'ж':
            word1 += 'zch'
        elif i == 'з':
            word1 += 'z'
        elif i == 'и':
            word1 += 'i'
        elif i == 'й':
            word1 += 'i'
        elif i == 'к':
            word1 += 'k'
        elif i == 'л':
            word1 += 'l'
        elif i == 'м':
            word1 += 'm'
        elif i == 'н':
            word1 += 'n'
        elif i == 'о':
            word1 += 'o'
        elif i == 'п':
            word1 += 'p'
        elif i == 'р':
            word1 += 'r'
        elif i == 'с':
            word1 += 's'
        elif i == 'т':
            word1 += 't'
        elif i == 'у':
            word1 += 'u'
        elif i == 'ф':
            word1 += 'f'
        elif i == 'ч':
            word1 += 'ch'
        elif i == 'ш':
            word1 += 'sch'
        elif i == 'щ':
            word1 += 'sch'
        elif i == 'ъ':
            word1 += ''
        elif i == 'ы':
            word1 ='i'
        elif i == 'ь':
            word1 += "''"
        elif i == 'э':
            word1 += 'e'
        elif i == 'ю':
            word1 += 'q'
        elif i == 'я':
            word1 += 'ya'
    return word1