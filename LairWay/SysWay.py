class Mess:
  def __init__(self):
    self.ll = {}

  def New(self, mess_name, langs, mess):
    self.ll[mess_name] = {}
    for a in range(len(langs)):
      self.ll[mess_name][langs[a]] = mess[a]

  def Mess(self, mess_name, lang):
    try: return self.ll[mess_name][lang]
    except: return self.ll[mess_name]["en"]
      
  def MessArg(self, error_name, lang, *args):
    try:
      message = self.ll[error_name][lang]
      for i in range(len(args)):
          message = message.replace("/SEA/", args[i],1)
      return message
    except:
      if lang!="eng": return self.MessArg(error_name,"eng",*args)
      else: return("Error -1. Mess-Error")
      


SM=Mess()

SM.New("LairWay",["en","ru"],["Welcome to the Lairway TB engine. \n Developers: catman (great and main), Ⰳⰰⱄⰰⱀⰱⰵⰽ ან ბრწყინვალე ഹസൻബെക് \nCommunication - LairWay Bot@gmail.com \n\n Lairway version - /SEA/\n LairWaySysV_/SEA/_/SEA/_/SEA/\n\nThe number of users of this bot is /SEA/\nHave a nice game!","Вас приветствует ТБ-движек Lairway. \nРазработчики: catman(великий и главный), Ⰳⰰⱄⰰⱀⰱⰵⰽ ან ბრწყინვალე ഹസൻബെക് \nСвязь - LairWayBot@gmail.com \n\nВерсия Lairway - /SEA/\n LairWaySysV_/SEA/_/SEA/_/SEA/\n\nКоличество пользоватлей этого бота - /SEA/\nПриятной игры!"])


SM.New('LW', ['en', 'ru'], ["Created using LairWay. Good game!\n","Создано при использововании LairWay. Удачной игры!\n "])
SM.New('RKE', ['en', 'ru'], ["ERROR 1R : Syntax error. Required @?key/?/needkey/?/text1/?/text2, where key is the name of the variable and needkey is the key of the desired value of the variable, text1 is the text if the condition is true, text2 is the text if the condition is true lie","ERROR: Ошибка синтаксиса. Требуеться @?key/?/needkey/?/text1/?/text2, где key - название переменной а needkey - ключ нужного значения переменной, text1 - текст если условине - истино, text2 - текст если условие - ложь"])
SM.New('RSE', ['en', 'ru'], ["ERROR 2R: Door syntax error inside '@?'","ERROR 2R: Ошибка синтаксиса door внутри '@?'"])
SM.New('P', ['en', 'ru'], ["Error 0: Some minor problem. I'll try again after some time.","Error 0: Какая-то небольшая проблема. Попробуйье еще раз через какое-то время."])
SM.New('LW', ['en', 'ru'], ["Created using LairWay. Good game!\n","Создано при использововании LairWay. Удачной игры!\n "])
SM.New('RKE', ['en', 'ru'], ["ERROR 1R : Syntax error. Required @?key/?/needkey/?/text1/?/text2, where key is the name of the variable and needkey is the key of the desired value of the variable, text1 is the text if the condition is true, text2 is the text if the condition is true lie","ERROR: Ошибка синтаксиса. Требуеться @?key/?/needkey/?/text1/?/text2, где key - название переменной а needkey - ключ нужного значения переменной, text1 - текст если условине - истино, text2 - текст если условие - ложь"])
SM.New('RSE', ['en', 'ru'], ["ERROR 2R: Door syntax error inside '@?'","ERROR 2R: Ошибка синтаксиса door внутри '@?'"])
SM.New('P', ['en', 'ru'], ["Error 0: Some minor problem. I'll try again after some time.","Error 0: Какая-то небольшая проблема. Попробуйье еще раз через какое-то время."])
SM.New('TxNE', ['en', 'ru'], ["Error:\nText /SEA/ does not exist.", "Error 1:\nТекста /SEA/ не существует."])
SM.New('TxL', ['en', 'ru'], ["Error 2:\nText /SEA/ Too big or small. Restriction - must be at least 1 character and no more than /SEA/.", "Error 2:\nТекст /SEA/ Cлишком большой или маленький. Ограничение - должен быть минимум 1 символ и не больше чем /SEA/"])
SM.New("Empty", ['en','ru'], ["Error 3:\nYou are trying to use an empty button/image after the text.","Error 3:\n Вы пытаетесь использовать пустую кнопку/картинку после текста."])
SM.New("ImgE", ['en','ru'], ["Error 4:\nThe picture /SEA/ does not exist, but it is listed after the text.","Error 4:\nКартинки /SEA/ не существует, но она указана после текста."])
SM.New("BtE", ['en','ru'], ["Error 5:\nThe button /SEA/ does not exist, but it is indicated after the text.","Error 5:\nКнопки /SEA/ не существует, но она указана после текста."])
SM.New("BtL", ['en','ru'], ["Error 6:\nThe button /SEA/ does not comply with the length rules, which state that it must be greater than 0 and less than /SEA/ characters.","Error 6:\nКнопка /SEA/ не соответствует правилам длины, которые гласят, что тот должен быть больше 0 и меньше /SEA/ символов."])
SM.New("BtM", ['en','ru'], ["Error 7:\n For the button /SEA/ not enough parameters were specified, the number, text, and text it leads to are required.","Error 7:\nДля кнопки /SEA/ указали недостаточно параментров, требуться номер, текст, текст в который она ведет."])
SM.New("SE", ['en','ru'], ["Error 8:\nThe button has incorrect syntax.", "Error 8:\nКнопка имеет не правильный синтаксис."])
SM.New("reset", ["en", "ru"], ["Your achievements have been reset!", "Ваши достижения сброшены!"])
SM.New("SE",["en","ru"],["Error Spell. Casting a spell without a previous message or for starter.","Error Spell. Применение заклинанения без предыдущего сообщения или для стартового сообщения."])
SM.New("NoRole",["en","ru"],["You do not have sufficient rights to use this command!","У вас не хватает прав для использования этой команды!"])
SM.New("FE",["en","ru"],["You forgot to provide a file name, could not be found, or another error occurred.","Вы забыли указать название файла, фаил не найден или произошла другая ошибка."])
SM.New("FO",["en","ru"],['The file has been opened and read.','Фаил открыт и прочитан.'])
SM.New("tp",["en","ru"],["Write after /tp the number of the room where you need to teleport!","Напишите после /tp номер комнаты куда вам нужно телепортироваваться!"])
SM.New("NoElType", ['en','ru'], ["There is no element of type /SEA/.","Не существует элемента типа /SEA/."])
SM.New("ShowError", ['en','ru'], ["An error has occurred. Check that you have specified the two required arguments (the element type and its name), as well as whether this element exists. We also remind you that in the name of an element, instead of a space, we use “~”.","Произошла ошибка. Проверьте точно вы указали два нужных аргумента (тип элемента и его имя), а так же существет ли этот элемент. Так же напоминаем что в названии элемента мвесто пробелом мы испольуем ''~''."])
SM.New('save_error', ['en', 'ru'], ["GTSAVE is not possible. Perhaps you did not define the GitHub token (GitHub) and the path to your repl (name) in the 'name/repl' format, or you did not create LW.db in Github, or you forgot to specify the file that you want to save.", "GTSAVE невозможен. Возможно вы не указали токен GitHub (GitHub) и путь к вашему репл (name) в формате 'имя/репл', или же не создали LW.db в гитхабе, или забыли указать фаил который нужно сохранить."])
SM.New('save', ['en', 'ru'], ['The save was successful', 'Сохранение произошло успешно'])
SM.New('Create', ['en', 'ru'], ['The creation of VexMole.lairway was successful. ;)', 'Создание VexMole.lairway произошло успешно. ;)'])
SM.New('CreateError', ['en', 'ru'], ['An error occurred during creation. This is very bad.', 'При создании произошла ошибка. Это очень плохо.'])
SM.New('Add+', ['en', 'ru'], ['The adding process was successful.', 'Процес добовления произошел успешно.'])
SM.New('AddError', ['en', 'ru'], ['An error occurred while adding the element. Check your syntax for errors.', 'При добовлении элемента произошла ошибка. Проверте синтаксис на ошибки.'])
SM.New("key_er",["en","ru"],['You did not specify the key or value of the variable, or forgot to specify it. (/key variable_name variable_change (remember that in the internal syntax there is "~" instead of " "))','Вы не указали ключ или значение переменной, или забыли указать их. (/key имя_переменной изменение_переменной (помните что во внутренем синтаксисе вместо " " идет "~"))'])
SM.New('bye', ["en", "ru"], ["The cleanup was successful! Congratulations!","Очистка произошла успешна! Подравления!"])
SM.New('del_er1', ['en', 'ru'], ['Error. \nYou may have entered the nickname of a non-existent user or the name of a variable.','Error. \n Возможно вы ввели никнейм несущесвующего юзера или имя переменной.'])
SM.New('key', ['en', 'ru'], ['You have changed the value of a variable', 'Вы изменили значение переменной'])
SM.New('del_er2', ['en', 'ru'], ['Error. \nYou may have entered the nickname of a non-existent user.', 'Error. \n Возможно вы ввели никнейм несущесвующего юзера.'])
SM.New('Remove', ['en', 'ru'], ["The element was deleted successfully", "Удаление элемента прошло успешно"])
SM.New('RemoveError', ['en', 'ru'], ["There was some problem deleting the item.", "При удалении элемента произошла какая-то проблема."])
SM.New("Size",["en","ru"],["In the game, in texts there are /SEA/ symbols, in buttons there are /SEA/ symbols, as well as additionally /SEA/. SO total /SEA/ characters.", "В игре в текстах /SEA/ символов, в кнопках /SEA/ символов, а так же дополнительно /SEA/. ТЕ суммарно /SEA/ символов."])