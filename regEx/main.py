import re

txt = 'Мама', 'авТо', 'гриБ', 'Яблоко', 'яБлоко', 'ябЛоко', 'яблОко', 'яблоКо', 'яблокО','агент007', 'стриж', 'ГТО', 'Три богатыря'

for x in txt:
    c = re.findall(r"(^[а-я]*[А-Я][а-я]*)$", x)
    print(c)
