surnames = {'МИФТАХОВА', 'ПЛУЖНИК', 'ПЕТРУШИН', 'ЛАПШИН', 'ЗАХАРКИНА', 'ОВСЯННИКОВ', 'ЧЕРКАШИН', 'ТАРАСОВ', 'РОЖОК', 'КУЛАКОВ', 'ГЕВОРКЯН', 'КОПЦЕВ', 'МЕЛЬНИКОВА', 'РУСОВА', 'КАЛИНКИНА', 'ЛУБЕНЕЦ', 'БОНАРЦЕВ', 'БИТКОВ', 'БАРУЗДИНА', 'ЛАРИОНОВА', 'СУХИНИН', 'БАРАНОВА', 'РАГУШИН', 'КОВАЛЁВ', 'БЕЛОКОБЫЛЬСКИЙ', 'ГЕТМАН', 'КРАСНЕНКОВА', 'АЛЕКСАНДРОВ', 'КИТАЕВ', 'РОМАНОВ', 'ВАСИЛЬЕВА'}
names = {'ДИНАРА', 'ЛУКА', 'ИВАН', 'МАРИЯ', 'АНДРЕЙ', 'АРТЁМ', 'АЛЕКСЕЙ', 'ВЛАДИМИР', 'РУСЛАН', 'БАГРАТ', 'ПЁТР', 'ОЛЕСЯ', 'ДАРЬЯ', 'ПАВЕЛ', 'СЕРГЕЙ', 'СОФЬЯ', 'ВИКТОРИЯ', 'ЮРИЙ', 'СТЕПЛЕР', 'НИКОЛАЙ', 'НИКИТА', 'ПОЛИНА', 'ДЕНИС', 'ЕЛИЗАВЕТТА'}
print('Добро пожаловать в самую wierd and suspicios игру. Не могу обещать, что она вам понравится, могу пожелать только удачи и здоровья погибшим.')
print('Немного правил: вы можете вводить как одну букву, так и целое слово, но ОБЯЗАТЕЛЬНО ЗАГЛАВНЫМИ БУКВАМИ!! Задача отгадать имя или фамилию человека из 8"В"(на выбор).')
print('В игре также есть фунция "помощь", которую можно вызвать, введя команду #help во время ввода букв')
print('С каждой неправильно отгаданной буквой вы будете приближаться к четвертованию. Максимальное количество неправильных ответов: 5')
print("Let's get started!")
print()
alph = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
end = 0
while end != 1:
    clos = list()
    word = ''
    win = 0
    life = 5
    print('Что вы хотите сделать? Введите цифру.')
    print('1.Отгадать имя')
    print('2.Отгадать фаилию')
    answ = input()
    while answ != '1' and answ != '2':
        print('Пожалуйста, вносите ответы корректно')
        answ = input()
    if answ == '1':
        word = names.pop()
        for i in range(len(word)):
            clos.append('☐')
        print('☐' * len(word))
        check = 0
        while ''.join(clos) != word:
            print('Введите букву или слово целиком')
            ans = input()
            for u in range(len(word)):
                if word[u] not in alph:
                    check = 1
                    break
            while check != 1 and ans != '#help' and ans != word and ans not in alph:
                print('Пожалуйста, вносите ответы корректно')
                ans = input()
            if ans in word and ans != word and ans != '':
                print('Ура! Вы отдаляетесь от смерти!')
                clos[word.find(ans)] = ans
                print(''.join(clos))
                print()
            elif ans == word:
                print('ОГО!!!')
                print()
                break
            elif (ans not in word or ans == '') and ans != '#help' and ans != word:
                print('Вы на шаг ближе к смерти! Это неверный ответ')
                life -= 1
            elif ans == '#help':
                print('Подсказок я не даю, но могу помочь кое-чем другим. Введите цифру:')
                print('1.Как вводить ответы?')
                print('2.Сколько неправильных ответов до смерти?')
                print('3.В чём смысл существования?')
                print('4.Я хочу закончить игру')
                ans = input()
                while ans != '1' and ans != '2' and ans != '3' and ans != '4' and ans != '52' and ans != '28':
                    print('Пожалуйста, вносите ответы корректно')
                    ans = input()
                if ans == '1':
                    print('Ответы нужно вводить заглавными русскими буквами. Можно вводить как одну букву, так и слово целиком.')
                elif ans == '2':
                    if life != 0:
                        print('До четвертования осталось', life, 'неверных ответов')
                    else:
                        print('Ну теперь ошибок совершать точно нельзя, остался всего один неверный ответ...')
                elif ans == '3':
                    print('Чтобы узнать ответ на это вопрос ым стоит перейти по ссылке, приложеной ниже. НО советую сделать это после окончания игры, иначе она вылетит')
                    print('https://youtu.be/dQw4w9WgXcQ?si=df-9e4dLgNhPq_tw')
                elif ans == '4':
                    print('Хорошо, твоё желание будет услышано')
                    end = 1
                    win = 2
                    break
                elif ans == '52':
                    print('Да здравствует Санкт-Петербург, и этот город наш!')
                elif ans == '28':
                    print('ДВАДЦАТЬ ВОСЕМЬ УДАРОВ НОЖОМ! ТЫ ДЕЙСТВОВАЛ НАВЕРНЯКА. ДА? ЭТО БЫЛА НЕНАВИСТЬ? ГНЕВ? ОН БЫЛ В КРОВИ, УМОЛЯЛ О ПОЩАДЕ, НО ТЫ СНОВА И СНОВА НАНОСИЛ ЕМУ УДАРЫ! Я ЗНАЮ, ТЫ УБИЙЦА!')
            if life < 0:
                win = 1
                break
        if win == 1:
            print('Упс, четвертования не избежать. Прощайте')
            print('Кстати, верный ответ был "', word, '"')
            print('...')
            print('Хмм... вас же можно воскресить с помощью тёмной магии...')
        else:
            print('Вам удалось избежать смерти, поздравляю!!')
        print('Хотите продолжить играть? введите цифру:')
        print('1.Да!  2.Нет.')
        ans = input()
        while ans != '1' and ans != '2':
            print('Пожалуйста, вносите ответы корректно')
            ans = input()
        if ans == '1':
            print('Ура! Давайте продолжим')
        elif ans == '2':
            print('Принято. Увидимся в следующий раз, удачи вам <3')
            end = 1
    elif answ == '2':
        word = surnames.pop()
        for i in range(len(word)):
            clos.append('☐')
        print('☐' * len(word))
        check = 0
        while ''.join(clos) != word:
            print('Введите букву или слово целиком')
            ans = input()
            for u in range(len(word)):
                if word[u] not in alph:
                    check = 1
                    break
            while check != 0 and ans != '#help' and ans != word and ans not in alph:
                print('Пожалуйста, вносите ответы корректно')
                ans = input()
            if ans in word and ans != word and ans != '':
                print('Ура! Вы отдаляетесь от смерти!')
                clos[word.find(ans)] = ans
                print(''.join(clos))
                print()
            elif ans == word:
                print('ОГО!!!')
                print()
                break
            elif (ans not in word or ans == '') and ans != '#help' and ans != word:
                print('Вы на шаг ближе к смерти! Это неверный ответ')
                life -= 1
            elif ans == '#help':
                print('Подсказок я не даю, но могу помочь кое-чем другим. Введите цифру:')
                print('1.Как вводить ответы?')
                print('2.Сколько неправильных ответов до смерти?')
                print('3.В чём смысл существования?')
                print('4.Я хочу закончить игру')
                ans = input()
                while ans != '1' and ans != '2' and ans != '3' and ans != '4' and ans != '52' and ans != '28':
                    print('Пожалуйста, вносите ответы корректно')
                    ans = input()
                if ans == '1':
                    print('Ответы нужно вводить заглавными русскими буквами. Можно вводить как одну букву, так и слово целиком.')
                elif ans == '2':
                    if life != 0:
                        print('До четвертования осталось', life, 'неверных ответов')
                    else:
                        print('Ну теперь ошибок совершать точно нельзя, остался всего один неверный ответ...')
                elif ans == '3':
                    print('Чтобы узнать ответ на это вопрос ым стоит перейти по ссылке, приложеной ниже. НО советую сделать это после окончания игры, иначе она вылетит')
                    print('https://youtu.be/dQw4w9WgXcQ?si=df-9e4dLgNhPq_tw')
                elif ans == '4':
                    print('Хорошо, твоё желание будет услышано')
                    end = 1
                    win = 2
                    break
                elif ans == '52':
                    print('Да здравствует Санкт-Петербург, и этот город наш!')
                elif ans == '28':
                    print('ДВАДЦАТЬ ВОСЕМЬ УДАРОВ НОЖОМ! ТЫ ДЕЙСТВОВАЛ НАВЕРНЯКА. ДА? ЭТО БЫЛА НЕНАВИСТЬ? ГНЕВ? ОН БЫЛ В КРОВИ, УМОЛЯЛ О ПОЩАДЕ, НО ТЫ СНОВА И СНОВА НАНОСИЛ ЕМУ УДАРЫ! Я ЗНАЮ, ТЫ УБИЙЦА!')
            if life < 0:
                win = 1
                break
        if win == 1:
            print('Упс, четвертования не избежать. Прощайте')
            print('Кстати, верный ответ был "', word, '"')
            print('...')
            print('Хмм... вас же можно воскресить с помощью тёмной магии...')
        else:
            print('Вам удалось избежать смерти, поздравляю!!')
        print('Хотите продолжить играть? введите цифру:')
        print('1.Да!  2.Нет.')
        ans = input()
        while ans != '1' and ans != '2':
            print('Пожалуйста, вносите ответы корректно')
            ans = input()
        if ans == '1':
            print('Ура! Давайте продолжим')
        elif ans == '2':
            print('Принято. Увидимся в следующий раз, удачи вам <3')
            end = 1











            
        
            
                
                    
                
                




                
            
        
        
