# Создайте функцию introspection_info(obj), которая принимает объект obj.
# 2. Используйте встроенные функции и методы интроспекции Python для получения информации о переданном объекте.
# 3. Верните словарь или строки с данными об объекте, включающий следующую информацию:
#   - Тип объекта.
#   - Атрибуты объекта.
#   - Методы объекта.
#   - Модуль, к которому объект принадлежит.
#   - Другие интересные свойства объекта, учитывая его тип (по желанию).
import inspect

def introspection_info(obj):
    return {"type":type(obj),"attributes":list(dir(obj)),
            "methods":list(method for method in dir(obj) if callable(getattr(obj, method))),"модуль": inspect.getmodule(obj)}



number_info = introspection_info(42)
print(number_info)

