from lairway import *

@bot.message_handler(commands=['start','go','run','game'])
def StartCommand(message):
  IfInBox(Uid(message), message)
  Lairway(starter[0], message)

@bot.callback_query_handler(func=lambda call: True)
def самостоятельный(call):
  Lairway(call.data, call, new = 0)


#Команда lairway которая выводит основную информацию о движке
@bot.message_handler(commands=['lairway'])
def TextCommand(message):
  IfInBox(Uid(message), message)
  SM.New("LairWay",["en","ru"],["Welcome to the Lairway TB engine. \n Developers: catman (great and main), Ⰳⰰⱄⰰⱀⰱⰵⰽ ან ბრწყინვალე ഹസൻബെക് \nCommunication - LairWay Bot@gmail.com \n\n Lairway version - "+LairWayV+ "\n IV_"+ LairFaceV +" LWdb_"+LairBoxV+" EyeSys_"+LairEyeV+"\n\nThe number of users of this bot is "+str(len(Ids()))+"\nHave a nice game!","Вас приветствует ТБ-движек Lairway. \nРазработчики: catman(великий и главный), Ⰳⰰⱄⰰⱀⰱⰵⰽ ან ბრწყინვალე ഹസൻബെക് \nСвязь - LairWayBot@gmail.com \n\nВерсия Lairway - "+LairWayV+ "\nIV_"+ LairFaceV +" LWdb_"+LairBoxV+"   EyeSys_"+LairEyeV+"\n\nКоличество пользоватлей этого бота - "+str(len(Ids()))+"\nПриятной игры!"])
  Send(Uid(message),SM.Mess("LairWay",lang))


#Считывает файл сюжета игры
@bot.message_handler(commands=['Read','read'])
def ReadCommand(message):
  Send(Uid(message), "Фаил прочитан.")
  LairWayRead()

#Очищяет все неизменямые переменные
@bot.message_handler(commands=['ClearMe','reset',"Reset", 'Rebith', 'rebith'])
def CleanCommand(message):
  SM.New("reset", ["en", "ru"], ["Your achievements have been reset!", "Ваши достижения сброшены!"])
  if bye("id", Uid(message)):
    Send(Uid(message), SM.Mess("reset", lang))
  else: Send(Uid(message), "Error.")



@bot.message_handler(commands=['Size','size'])
def SizeCommand(message):
  SM.New("Size",["en","ru"],["In the game, in texts there are "+str(Size[0])+" symbols, in buttons there are "+str(Size[1])+" symbols, as well as additionally "+str(Size[2])+". SO total "+str(Size[0]+Size[1]+Size[2])+" characters.", "В игре в текстах " +str(Size[0])+" символов, в кнопках " +str(Size[1])+" символов, а так же дополнительно "+str(Size[2])+". ТЕ суммарно " +str(Size[0]+Size[1]+Size[2])+" символов."])
  if Size[0]==None:
    Size[0]=0
    for a in text:
      Size[0]+=len(text[a][0])
  if Size[1]==None:
    Size[1]=0
    for a in bttn:
      Size[1]+=len(bttn[a][0])
  if Size[2]==None:
    Size[2]=0
    for a in img:
      if len(img[a])>1:
        Size[2]+=len(img[a][1])
  Send(Uid(message), SM.Mess("Size",lang))
#Команды админов

SM.New("NoRole",["en","ru"],["You do not have sufficient rights to use this command!","У вас не хватает прав для использования этой команды!"])
SM.New("FE",["en","ru"],["You forgot to provide a file name, could not be found, or another error occurred.","Вы забыли указать название файла, фаил не найден или произошла другая ошибка."])
SM.New("FO",["en","ru"],['The file has been opened and read.','Фаил открыт и прочитан.'])
SM.New("tp",["en","ru"],["Write after /tp the number of the room where you need to teleport!","Напишите после /tp номер комнаты куда вам нужно телепортироваваться!"])
SM.New('save_error', ['en', 'ru'], ["GTSAVE is not possible. Perhaps you did not specify the GitHub token (GitHub) and the path to your repl (name) in the 'name/repl' format, or you did not create LW.db in GitHub", "GTSAVE невозможен. Возможно вы не указали токен GitHub (GitHub) и путь к вашему репл (name) в формате 'имя/репл', или же не создали LW.db в гитхабе"])
SM.New('save', ['en', 'ru'], ['SQL saved!', 'SQL сохранен!'])
SM.New("key_er",["en","ru"],['You did not specify the key or value of the variable, or forgot to specify it. (/key variable_name variable_change (remember that in the internal syntax there is "~" instead of " "))','Вы не указали ключ или значение переменной, или забыли указать их. (/key имя_переменной изменение_переменной (помните что во внутренем синтаксисе вместо " " идет "~"))'])
SM.New('bye', ["en", "ru"], ['The cleaning was completed successfully. You have cleared the Earth of these pathetic people, congratulations!',"Очистка произведена удачно. Вы очистили Землю от этих жалких людей, поздравляю!"])
SM.New('del_er1', ['en', 'ru'], ['Error. \nYou may have entered the nickname of a non-existent user or the name of a variable.','Error. \n Возможно вы ввели никнейм несущесвующего юзера или имя переменной.'])
SM.New('key', ['en', 'ru'], ['You have changed the value of a variable', 'Вы изменили значение переменной'])
SM.New('del_er2', ['en', 'ru'], ['Error. \nYou may have entered the nickname of a non-existent user.', 'Error. \n Возможно вы ввели никнейм несущесвующего юзера.'])




@bot.message_handler(commands=['bye', 'del', 'delete', 'clrsql',"clear"])
def DelCommand(message):
  if role(Uid(message),"lord"):
    dell=message.text.split()
    if len(dell)==1: 
      if not bye("all"):
        Send(Uid(message), "Error"); return
    elif dell[1]=="box": 
      if not bye("box"):
        Send(Uid(message), "Error") ; return  
    elif len(dell)==3:
      if not bye("user", dell[1],dell[2]):
        Send(Uid(message), SM.Mess('del_er1', lang)); return
    else: 
      if not bye("user", dell[1]):
        Send(Uid(message), SM.Mess('del_er2', lang)); return
    Send(Uid(message), SM.Mess("bye",lang))

  else:
   Send(Uid(message), SM.Mess("NoRole",lang))


@bot.message_handler(commands=['Say',"say"])
def SayCommand(message):
  if role(Uid(message),"lord"):
    say(message.text[4:])
  else:
    Send(Uid(message), SM.Mess("NoRole",lang))

@bot.message_handler(commands=['Inf',"inf"])
def InfCommand(message):
  uid=Uid(message)
  IfInBox(Uid(message), message)
  if role(Uid(message),"lord"): 
    infsay=message.text.split()
    if len(infsay)>1:
      if infsay[1]=="me": Send(Uid(message),Inf(Uid(message)))
      elif infsay[1] in ('players', 'big','+'):
        Send(uid,Inf("players",uid))
        
      else:  Send(Uid(message),Inf("@"+infsay[1]))
    else: 
      Send(Uid(message),Inf("all"))
  else:
    Send(Uid(message), SM.Mess("NoRole",lang))




@bot.message_handler(commands=['File','file'])
def LWreadCommand(message):
  if role(Uid(message),"lord"):
    try:
      bttn,text={},{}
      LWR(message.text[6:]+".lairway")
      Send(Uid(message), SM.Mess("FO",lang))
    except:
      Send(Uid(message), SM.Mess("FE",lang))
  else:
    Send(Uid(message), SM.Mess("NoRole",lang))

@bot.message_handler(commands=['save','Save',"GHS","gts","sql"])
def LWsaveCommand(message):
  if role(Uid(message),"h"):
    if GHS():
      Send(Uid(message), SM.Mess('save',lang))
    else: 
      Send(uid, SM.Mess("save_error",lang))
  else:
    Send(Uid(message), SM.Mess("NoRole",lang))

@bot.message_handler(commands=['tp',"Tp"])
def TpCommand(message):
  IfInBox(Uid(message), message)
  if role(Uid(message),"h") :
    try:
      gasanbek(starter[0], message, tp=message.text[4:])
    except:
      Send(Uid(message), SM.Mess(tp,lang))

  else:
    Send(Uid(message), SM.Mess("NoRole",lang))


@bot.message_handler(commands=['key','Key'],)
def perem(message):
  if role(Uid(message),"h"): 
    try:
      kct=message.text.split()[1:]
      if len(kct)==3:
        if role(Uid(message),"lord"):
          key(kct[1].replace("~"," "),kct[2].replace("~"," "), Who(kct[0]))
        else:
          Send(Uid(message),  SM.Mess("NoRole",lang))
          return
          
      else: key(kct[0].replace("~"," "),kct[1].replace("~"," "), Uid(message))
      Send(Uid(message), SM.Mess("key",lang))
    except Exception as e:
      print(e)
      Send(Uid(message),  SM.Mess("key_er",lang))
  else:
    Send(Uid(message), SM.Mess("NoRole",lang))

@bot.message_handler(commands=['send','Send'])
def LWtestCommand(message):
  if role(Uid(message),"lord"):
    try:
      name = message.text.split()[1]
      with open(name, "rb") as file: bot.send_document(Uid(message), file)
    except:
      Send(Uid(message), SM.Mess("FE",lang))
  else:
    Send(Uid(message), SM.Mess("NoRole",lang))

 #другом случае:
@bot.message_handler(commands=spl)
def Spell(message):
  uid = Uid(message)
  command=message.text.split()[0][1:]
  splway=spell[command]
  if len(splway)==1:
    Lairway(splway[0], message)
  elif len(splway)==2:
    if role(uid,splway[1]):
      Lairway(splway[0], message)
    else: 
      Send(uid, SM.Mess("NoRole",lang))
  elif len(splway)>2:
    if door(uid,splway[1],splway[2]):
      Lairway(splway[0], message)
    else:
      if len(splway) > 3:
          Send(Uid(message), RLW(splway[3], Uid(message)))
      else:
          Send(Uid(message), RLW(phrase[0], Uid(message)))
      
@bot.message_handler(content_types=['text'])
def TextCommand(message):
  Send(Uid(message), RLW(phrase[0], Uid(message)))


@bot.message_handler(content_types=['sticker'])
def stickCommand(message):
  Send(Uid(message), RLW(phrase[0], Uid(message)))
  
LWLS()
bot.polling(none_stop=True, timeout=123)