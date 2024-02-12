from lairway import *


@bot.message_handler(commands=['start','go','run','game'])
def StartCommand(message):
  IfInUsInf(Uid(message), message)
  Lairway(starter[0], message)


@bot.callback_query_handler(func=lambda call: True)
def самостоятельный(call):
  CallSave[Uid(call)]=call
  Lairway(CallBack(call), call, new = 0)


@bot.message_handler(commands=['lairway', 'LairWay','engine','about'])
def LairWayAbout_Command(message):
  IfInUsInf(Uid(message), message)
  Send(Uid(message),SM.MessArg("LairWay",lang,LairWayV,LairFaceV,LairBoxV,LairEyeV,str(len(Ids()))))


#Считывает файл сюжета игры
@bot.message_handler(commands=['Read','read'])
def Read_Command(message):
  Send(Uid(message), "Фаил прочитан.")
  LairWayRead()

#Очищяет все неизменямые переменные
@bot.message_handler(commands=['ClearMe','reset',"Reset", 'Rebith', 'rebith'])
def Clean_Command(message):
  if bye("id", Uid(message)):
    Send(Uid(message), SM.Mess("reset", lang))
  else: Send(Uid(message), "Error.")



@bot.message_handler(commands=['Size','size'])
def Size_Command(message):
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
  Send(Uid(message), SM.MessArg("Size",lang,str(Size[0]),str(Size[1]),str(Size[2]),str(Size[0]+Size[1]+Size[2])))
#Команды админов


@bot.message_handler(commands=['bye', 'del', 'delete', 'clrsql',"clear"])
def Del_Command(message):
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
def Say_Command(message):
  if role(Uid(message),"lord"):
    say(message.text[4:])
  else:
    Send(Uid(message), SM.Mess("NoRole",lang))

@bot.message_handler(commands=['Inf',"inf"])
def Inf_Command(message):
  uid=Uid(message)
  IfInUsInf(Uid(message), message)
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
def FileRead_Command(message):
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
def GitHubSave_Command(message):
  if role(Uid(message),"h"):
    if GHS():
      Send(Uid(message), SM.Mess('save',lang))
    else: 
      Send(Uid(message), SM.Mess("save_error",lang))
  else:
    Send(Uid(message), SM.Mess("NoRole",lang))

@bot.message_handler(commands=['tp',"Tp"])
def TP_Command(message):
  IfInUsInf(Uid(message), message)
  if role(Uid(message),"h") :
    try:
      gasanbek(starter[0], message, tp=message.text[4:])
    except:
      Send(Uid(message), SM.Mess("tp", lang))

  else:
    Send(Uid(message), SM.Mess("NoRole",lang))


@bot.message_handler(commands=['key','Key'],)
def Key_Command(message):
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
def Send_Command(message):
  if role(Uid(message),"lord"):
    try:
      name = message.text.split()[1]
      with open(name, "rb") as file: bot.send_document(Uid(message), file)
    except:
      Send(Uid(message), SM.Mess("FE",lang))
  else:
    Send(Uid(message), SM.Mess("NoRole",lang))

 #другом случае:




      
@bot.message_handler(content_types=['text'])
def Spell(message):
  uid = Uid(message)
  command=message.text.split()[0]
  if command in spell:
    splway=spell[command]
    if len(splway)==1:
      if splway[0][0]=="@": 
        try: Lairway(splway[0][1:],CallSave[uid], new=0)
        except:Send(uid,SM.Mess("SE", lang))
      else: Lairway(splway[0], message)
    elif len(splway)==2:
      if role(uid,splway[1]):
        if splway[0][0]=="@":
          try:Lairway(splway[0][1:],CallSave[uid], new=0)
          except:SM.Mess("SE", lang)
        else:Lairway(splway[0], message)
      else: 
        Send(uid, SM.Mess("NoRole",lang))
    elif len(splway)>2:
      if door(uid,splway[1],splway[2]):
        if splway[0][0]=="@": 
          try:Lairway(splway[0][1:],CallSave[uid], new=0)
          except:SM.Mess("SE", lang)
        else: Lairway(splway[0], message)
      else:
        if len(splway) > 3:
            Send(Uid(message), RLW(splway[3], Uid(message)))
        else:
            if phrase[0]!="": Send(Uid(message), RLW(phrase[0], Uid(message)))
  else:
    if phrase[0]!="":Send(uid, RLW(phrase[0], Uid(message)))


@bot.message_handler(content_types=['sticker'])
def Stick_Command(message):
  if phrase[0]!="":Send(Uid(message), RLW(phrase[0], Uid(message)))
  
LWLS()
bot.polling(none_stop=True, timeout=123)