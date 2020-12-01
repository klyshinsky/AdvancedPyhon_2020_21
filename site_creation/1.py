#!/usr/bin/python3

# Библиотека для получения параметров из URL и отправка вывода клиенту с сервера в качестве отклика.
import cgi

# Библиотека для отладки - выводит диагностическое сообщение в виде html на клиента.
# !!! Следует отключать в рабочей версии!!!
import cgitb
cgitb.enable()

# Отклик сервера состоит из заголовка, который говорит что содержится в ответе 
# (и много чего еще, версию браузера, например), пустой строки и собственно нагрузки.
# Заголовок - говорит, что сейчас пойдет html в кодировке utf-8
#print("Content-Type: text/html;charset=utf-8")
#print("")
# Полезная нагрузка - простой html файл, который генерирует данный скрипт.
#print("<html><body><i>Hello!</i></body></html>")

# FieldStorage необходим чтобы получать из него параметры REST-запроса.
form = cgi.FieldStorage()

# Проверяем есть ли необходимые параметры в запросе.
# Если нет, отправляем код ошибки в виде json.
if "prefix" not in form or "page" not in form:
   print('Content-Type: application/json;charset=utf-8\n\n{"error":"prefix not found"}')
   exit()
  
# Получаем значения параметров.
prefix = form.getfirst("prefix")
page = form.getfirst("page")

# Генерируем отклик с учетом пришедших параметров.
print("Content-Type: application/json;charset=utf-8")
print("")
print('[{"asdf":"'+prefix+str(page)+'qwerty","zxc":"'+prefix+" "+str(page)+'fgfhj"},{"asdf":"qwerty2","zxc":"fgfh2j"},{"asdf":"qwerty3","zxc":"fgfhj4"}]')
