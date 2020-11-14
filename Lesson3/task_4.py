"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
Можете условжнить задачу, реализовав ее через ООП
"""



import hashlib
from uuid import uuid4


class CacheClass:
    def __init__(self):
        self.cache = {}
        self.salt = uuid4().hex

    def cache_display(self):
        print(self.cache)

    def push_in(self, URL):
        if self.cache.get(URL):
            return f'{URL} уже записан в КЭШ'

        else:
            res = hashlib.sha256(self.salt.encode() + URL.encode()).hexdigest()
            self.cache[URL] = res
            return f'{URL} записан в КЭШ'

    def pop_out(self, URL):
        print(f'{URL} удален из КЭШа ')
        return self.cache.pop(URL)


cc = CacheClass()

print(cc.push_in('https://github.com/'))
print(cc.push_in('https://github.com/'))

cc.cache_display()

print(cc.push_in('https://www.google.com/'))
cc.pop_out('https://github.com/')
print(cc.push_in('https://www.youtube.com/'))
cc.cache_display()