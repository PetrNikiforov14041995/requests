
import requests
from lib2to3.tests import data
#  документация https://yandex.ru/dev/translate/doc/dg/reference/translate-docpage/

API_KEY = 'trnsl.1.1.20190712T081241Z.0309348472c8719d.0efdbc7ba1c507292080e3fbffe4427f7ce9a9f0'
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'

# открываем и читаем файлы
file1 = open("DE.txt", "r")
read1 = str(file1.readlines())

file2 = open ("ES.txt", "r")
read2 = str(file2.readlines())

file3 = open("FR.txt", "r")
read3 = str(file3.readlines())

# функция перевода файла 
def translate_it(text, to_lang):
    """
    https://translate.yandex.net/api/v1.5/tr.json/translate ?
    key=<API-ключ>
     & text=<переводимый текст>
     & lang=<направление перевода>
     & [format=<формат текста>]
     & [options=<опции перевода>]
     & [callback=<имя callback-функции>]
    :param to_lang:
    :return:
    """

    params = {
        'key': API_KEY,
        'text': text,
        'lang': 'ru'.format(to_lang)
           
    }

    response = requests.get(URL, params=params)
    json_ = response.json()
    
    
    return ''.join(json_['text'])
# закрытие файлов
file1.close()
file2.close()
file3.close()

# что покажет в терминале после перевода
if __name__ == '__main__':
    print(translate_it(read1, 'ru'))
    print(translate_it(read2, 'ru'))
    print(translate_it(read3, 'ru'))

# запись в файл
f1 = open("write.txt", "w")
f1.write(translate_it(read1, 'ru'))
f1.write(translate_it(read2, 'ru'))    
f1.write(translate_it(read3, 'ru'))   