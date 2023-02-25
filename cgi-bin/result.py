#!/usr/bin/python3

import cgi
import os
import http.cookies
import datetime

now = datetime.datetime.now().strftime('%Y-%m-%d__%H:%M:%S')

form = cgi.FieldStorage()
ans1 = form.getfirst("first")
ans2 = form.getfirst("second")
ans3 = form.getfirst("third")


right_counter = 0

if ans1 == 'right':
    right_counter += 1

if ans2 == 'right':
    right_counter += 1

if ans3 == 'right':
    right_counter += 1

cookie_value = ""
cookie = http.cookies.SimpleCookie(os.environ.get("HTTP_COOKIE"))
counter = cookie.get("COUNTER")
cur_date = cookie.get("CUR_DATE")


print("Set-cookie: COUNTER=" + str(right_counter) +";")
print("Set-cookie: CUR_DATE=" + str(now) + ";")
# print("Set-cookie: CUR_DATE=" + '"'+str(now) +'";')
print("Content-type: text/html\n")

print ("""
<!DOCTYPE html>
<html lang="ru">
    <head>
        <meta charset="UTF-8">
        <title>Тест по программированию</title>
        <link href="../styles.css" rel="stylesheet">
    </head>
    <body>
        <div class="container">

            <header class="test-header">
                <h1 class="test-name">Проверка знания языков программирования.</h1>
            </header>

            <section class="result">
                <div>
                    <div class="your-result">
                        <span>
                            Ваш результат: 
                        </span>
                        <span id="your-result">
""")
print(right_counter)
print ("""                 </span>
                        <span> 
                            из 3.
                        </span>
                    </div>
                    """)
print(now)
if not counter is None:
    print("""
                        <div class="your-result">
                            <span>
                                Ваш прошлый результат: 
                            </span>
                            <span id="your-result">
    """)
    print(counter.value)
    print(""" </span>

                        <span> 
                            из 3.
                        </span>
                    </div>
    """)
print(cur_date.value)
print("""
                </div>
            </section>
        </div>
    </body>
</html>
""")
