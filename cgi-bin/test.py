#!/usr/bin/python3

print ("Content-type: text/html\n")
print (
    """<html>
    <head>
        <meta charset="UTF-8">
        <title>Тест по программированию</title>
        <link href="../styles.css" rel="stylesheet">
    </head>

    <body>
        <div class="container">
            <header class="test-header">
                <h1 class="test-name">Проверка знания языков программирования.</h1>
            </header> <hr>
            <div class="test">
                <form action="/cgi-bin/result.py" method="post">
                    <div class="question-block">
                        <header class="question">
                            <span>1.</span>
                            <span>2+2</span>
                        </header>
                        <div class="answers">
                            <p>
                            <label>
                                <input name="first" type="radio" value="right">
                                4
                            </label>
                            </p>  
                            <p>
                            <label>
                                <input name="first" type="radio" value="5">
                                5
                            </label>
                            </p>
                            <p>
                            <label>
                                <input name="first" type="radio" value="23">
                                23
                            </label>
                            </p>
                        </div>
                    </div>

                    <div class="question-block">
                        <header class="question">
                            <span>2.</span>
                            <span>3+3</span>
                        </header>
                        <div class="answers">
                            <p>
                            <label>
                                <input name="second" type="radio" value="right">
                                6
                            </label>
                            </p>  
                            <p>
                            <label>
                                <input name="second" type="radio" value="5">
                                3
                            </label>
                            </p>
                            <p>
                            <label>
                                <input name="second" type="radio" value="23">
                                11
                            </label>
                            </p>
                        </div>
                    </div>

                    <div class="question-block">
                        <header class="question">
                            <span>3.</span>
                            <span>4+4</span>
                        </header>
                        <div class="answers">
                            <p>
                            <label>
                                <input name="third" type="radio" value="right">
                                8
                            </label>
                            </p>  
                            <p>
                            <label>
                                <input name="third" type="radio" value="15">
                                15
                            </label>
                            </p>
                            <p>
                            <label>
                                <input name="third" type="radio" value="16">
                                16
                            </label>
                            </p>
                        </div>
                    </div>

                    <div class="btn-wrapper">
                        <label>
                            <input type="submit" value="Завершить" class="submit-btn">
                        </label>
                    </div>
                </form>
            </div>
        </div>
    </body>
</html> """)