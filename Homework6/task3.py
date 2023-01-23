#Написать функцию, аргументы имена сотрудников, возвращает словарь, 
#ключи — первые буквы имён, значения — списки, содержащие имена, начинающиеся с соответствующей буквы.
#in
#"Иван", "Мария", "Петр", "Илья", "Марина", "Петр", "Алина", "Бибочка"

#out

#{'А': ['Алина'], 'Б': ['Бибочка'], 'И': ['Иван', 'Илья'], 'М': ['Марина', 'Мария'], 'П': ['Петр', 'Петр']}

def f(*names):
    res = {}
    for name in names:
        key = name[0]
        if key not in res:
            res[key] = []
        res[key].append(name)
    return res

print(f("Иван", "Мария", "Петр", "Илья"))