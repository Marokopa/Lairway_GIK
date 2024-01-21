import random
import telebot
from LairEye import LWLS, GHS
import os
import sqlite3


text = {}
bttn = {}
img = {}
maps={}
spell={}
spl=[]

phrase = [
    "Приветвуем вас в игре сделаной на основе ТБ-двжика Lairway. Что бы начать нажмите на /start",
    "Cистема защиты от багов и глюков LairWayDefence была активирована"
]

starter = ["1",None]
Size=[None,None,None]

token =  os.environ['token']
bot = telebot.TeleBot(token) 

conn = sqlite3.connect('LW.db', check_same_thread=False)
cur = conn.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS box (id, box, key, skey, mod )''')
cur.execute('''CREATE TABLE IF NOT EXISTS UsInf (id, name, rname, role, Blockid, fotoid )''')




def gasanbek(f, message, tp=0, new = 1):
  if not f in text:
    bot.send_message(message.from_user.id, "Error:\nТекста "+str(f)+" не существует.")
    return "No_TX"
  if not(len(text[f][0]) > 0 and len(text[f][0]) < 4096):
    bot.send_message(message.from_user.id, "Error:\nТекст не соответствует правилам длины, которые гласят, что тот должен быть больше 0 и меньше 4096 символов. ")
    return


  keyboard1 = telebot.types.InlineKeyboardMarkup(row_width=2)
  uid = message.from_user.id

  if new==1:

    cur.execute("UPDATE UsInf SET fotoid = '' WHERE id = ?", (uid, ))
    conn.commit()
    clear(uid)

  if tp!=0:  keyboard1.add(telebot.types.InlineKeyboardButton(text="tp",callback_data=tp))

  BlockId=cur.execute("SELECT Blockid FROM UsInf WHERE (id) = (?)",(uid, )).fetchall()[0][0]
  if new != 1 and not (BlockId == message.message.id):
    bot.edit_message_text(chat_id=message.from_user.id, message_id=message.message.message_id,text=phrase[1])
    return
    
  if starter[1]=="player":
    print(Inf(uid))
  elif starter[1]=="way":
    print(text,bttn,img,maps,spell)
  elif starter[1]!=None:
    print(Inf(str(starter[1])))



  #Удаление изображений
  if len(str(cur.execute("SELECT fotoid FROM UsInf WHERE (id) = (?)",(uid, )).fetchall()[0][0])) != 0:
    fotoid = cur.execute("SELECT fotoid FROM UsInf WHERE (id) = (?)",(uid, )).fetchall()[0][0][1:]
    icount = fotoid.split("@")
    for imgid in icount:
      bot.delete_message(message.message.chat.id, int(imgid))
    cur.execute("UPDATE UsInf SET fotoid = '' WHERE id = ?", (uid, ))

  for i in range(1, len(text[f])):
    """
      В последующих строках мы спрашиваем, что если какой то элемент начинается на @, то мы задаём переменную imgway, которая содержит данные о фотографии (от ее пути и до конца). Далее мы открываем картинку по пути который содержится в imgway[0] и следом отправляем ее.
      """
    #отправка фотографии
    if text[f][i] == "":
      bot.send_message(message.from_user.id, "Error:\nВы пытаетесь использовать пустую кнопку/картинку "+str(text[f][i][1:])+" после текста "+str(f)+".")
      continue
    if text[f][i] == "KillGame" and new==0:
      try:bot.delete_message(message.from_user.id, message.message.id)
      except:bot.edit_message_text(chat_id=message.from_user.id, message_id=message.message.message_id, text="):")
      return
      
    if text[f][i][0] == "@": 
      if text[f][i][1:] not in img:
        bot.send_message(message.from_user.id, "Error:\nКартинки "+str(text[f][i][1:])+" не существует, но она указана после текста "+str(f)+".")
        continue
      imgway = img[text[f][i][1:]]
      l = open(imgway[0], "rb")
      if len(imgway) ==1:
        foto = bot.send_photo(message.from_user.id, l )
      else:
        if not (len(imgway[1]) > 0 and len(imgway[1]) < 4096):
          bot.send_message(message.from_user.id, "Error:\nТекст не соответствует правилам длины, которые гласят, что тот должен быть больше 0 и меньше 4096 символов. ")
          return
        foto = bot.send_photo(message.message.chat.id, l,caption=RLW(imgway[1],uid))
      cur.execute("UPDATE UsInf SET fotoid = ? WHERE id = ?", (cur.execute("SELECT fotoid FROM UsInf WHERE (id) = (?)",(uid, )).fetchall()[0][0] + '@' + str(foto.id),uid,))

      l.close()
    else:    

      if text[f][i] not in bttn:
        bot.send_message(message.from_user.id, "Error:\nКнопки "+str(text[f][i])+" не существует, но она указана после текста "+str(f)+".")
        continue
      way = bttn[text[f][i]]
      if not(len(way[0]) > 0 and len(way[0]) < 64):
        bot.send_message(message.from_user.id, "Error:\nКнопка не соответствует правилам длины, которые гласят, что тот должен быть больше 0 и меньше 64 символов.")
        continue
      try:
        if len(way) == 2:
          start_button2 = telebot.types.InlineKeyboardButton(text=way[0],callback_data=way[1])
          keyboard1.add(start_button2)

        elif len(way)<2:
          bot.send_message(message.from_user.id, "Error:\nДля кнопки "+str(text[f][i])+" указали недостаточно параментров, требуться номер, текст, текст в который она ведет.")
          continue



        #Тип кнопки k. Позволяет создавать переменные и давать им значения
        elif way[2] == "k":
          if len(way) == 4:
            key(way[3],"1",uid)
          else:
            for k in range(0,len(way[2:])-1,2):
              key(way[k+3],way[k+4],uid)
          if way[1]!="":
            start_button2 = telebot.types.InlineKeyboardButton(text=way[0],callback_data=way[1])
            keyboard1.add(start_button2)
          
        #Тип кнопки c. Позволяет отчищать
        elif way[2] == "c":
          if len(way) == 3:
            clear(uid)
          else:
            clear(uid, list=way[3:])
            
          if way[1]!="":
            start_button2 = telebot.types.InlineKeyboardButton(text=way[0],callback_data=way[1])
            keyboard1.add(start_button2)
        
        #Тип кнопки r. Позволяет придавать значениям переменных рандомное значение
        elif way[2] == "r":  
            if way[1]=="@":
              rz=random.randint(4, len(way)-1)
              if rz%2==0: rz-=1
              start_button2 = telebot.types.InlineKeyboardButton(text=way[rz+1], callback_data=way[rz])
              keyboard1.add(start_button2)

            elif len(way[1])!=0 and way[1][0]=="D":
              rdoor=way[1][1:].split("//")
              if door(uid,rdoor[0],rdoor[1]):
                start_button2 = telebot.types.InlineKeyboardButton(text=way[0], callback_data=way[random.randint(3,len(way) - 1)])
              elif len(rdoor)>2:
                start_button2 = telebot.types.InlineKeyboardButton(text=way[0], callback_data=rdoor[random.randint(2,len(rdoor) - 1)])
              keyboard1.add(start_button2)
            else:
              start_button2 = telebot.types.InlineKeyboardButton(text=way[0], callback_data=way[random.randint(3,len(way) - 1)])
              keyboard1.add(start_button2)






        #Тип кнопки d. Позволяет отправять разные сообщения взависемости от значения переменной
        elif way[2] == "d":
          if len(way) == 5:
            if door(uid, way[3]):
              start_button2 = telebot.types.InlineKeyboardButton(text=way[0], callback_data=way[4])
              keyboard1.add(start_button2)
            else:
              start_button2 = telebot.types.InlineKeyboardButton(text=way[0], callback_data=way[1])
              keyboard1.add(start_button2)

          else:
            if door(uid, way[3], way[5]):

              if len(way) == 7:
                start_button2 = telebot.types.InlineKeyboardButton(
                  text=way[6], callback_data=way[4])
              else:
                start_button2 = telebot.types.InlineKeyboardButton(
                  text=way[0], callback_data=way[4])

              keyboard1.add(start_button2)
            else:
              start_button2 = telebot.types.InlineKeyboardButton(
                  text=way[0], callback_data=way[1])
              keyboard1.add(start_button2)

        elif way[2] == "i":
          if len(way) == 4:
            if door(uid, way[3]):
              start_button2 = telebot.types.InlineKeyboardButton(
                  text=way[0], callback_data=way[1])
              keyboard1.add(start_button2)
          else:
            if door(uid, way[3], way[4]):
              start_button2 = telebot.types.InlineKeyboardButton(
                  text=way[0], callback_data=way[1])
              keyboard1.add(start_button2)

        elif way[2] == "m":
          #t0~k[1]~m[2]~k[3]~4+
          if fmap(uid,mway=way[4:]):
            start_button2 = telebot.types.InlineKeyboardButton(
                  text=way[0], callback_data=way[1])
            keyboard1.add(start_button2)
          else:
            if way[3]!="":
              start_button2 = telebot.types.InlineKeyboardButton(
                  text=way[0], callback_data=way[3])
              keyboard1.add(start_button2)


        elif way[2]=="u":
          #bt~way~text[0]~wayto0/""[1]~u[2]~name1[3]~if1[4]~wayto1[4]
          wayto=way[1]
          for ult in range(len(way[3:])//3):
            if door(uid, way[3+ult*3], way[4+ult*3]):
              wayto=way[5+ult*3]
              break
          if wayto!="":
            start_button2 = telebot.types.InlineKeyboardButton(text=way[0], callback_data=wayto)
            keyboard1.add(start_button2)


        elif way[2] == "w":
          #bt~1~text[0]~[1]~w[2]~max[3]~foo[4]~way(2)[5]~bar[6]~way(3)[7]../
          ways= []
          
          if way[1]=="@":
             for a in range((len(way[3:]) // 3)):
              IfTheBox(way[4 + a * 3],uid)
              ways.append([cur.execute("SELECT key FROM box WHERE (id, box) = (?, ?)", (uid, way[4 + a * 3])).fetchall()[0][0]] + [way[5 + a * 3]] +[ way[6 + a * 3]])
          else:
            for a in range((len(way[3:]) // 2)):
              IfTheBox(way[4 + a * 2],uid)
              ways.append([cur.execute("SELECT key FROM box WHERE (id, box) = (?, ?)", (uid, way[4 + a * 2])).fetchall()[0][0]] + [way[5 + a * 2]])

          ways.sort(key=lambda x: x[0])

          wayslen  ,waytext =len(ways)-1,way[0]
          if way[3]=="max":
            if way[1]=="@": waytext=ways[wayslen][2]
            start_button2 = telebot.types.InlineKeyboardButton(text=waytext, callback_data=ways[wayslen][1])
            keyboard1.add(start_button2)
    
          if way[3]=="min":
           if way[1]=="@": waytext=ways[0][2]
           start_button2 = telebot.types.InlineKeyboardButton(text=waytext, callback_data=ways[0][1])
           keyboard1.add(start_button2)
          if way[3]=="med":
           if way[1]=="@": waytext=ways[wayslen//2][2]
           start_button2 = telebot.types.InlineKeyboardButton(text=waytext, callback_data=ways[wayslen//2][1])
           keyboard1.add(start_button2)

        elif way[2] == "s":
          cur.execute("UPDATE box SET skey = key WHERE (mod,id) = ('',?)", (uid, ))
          conn.commit()
          start_button2 = telebot.types.InlineKeyboardButton(text=way[0],
                                                             callback_data=way[1])
          keyboard1.add(start_button2)

        elif way[2] == "l":
          cur.execute("UPDATE box SET key = skey WHERE (mod,id) = ('',?)", (uid, ))
          start_button2 = telebot.types.InlineKeyboardButton(text=way[0],
                                                             callback_data=way[1])
          keyboard1.add(start_button2)

        elif way[2] == "v":
          if role(uid,way[3]):
            start_button2 = telebot.types.InlineKeyboardButton(text=way[0],callback_data=way[1])
            keyboard1.add(start_button2)


      except Exception as e:
        bot.send_message(message.from_user.id, "Error:\nКнопка "+str(text[f][i])+" имеет не правильный синтаксис.")
        print(e)
        continue



  if new == 1:
    forblockid=message.message_id+1
    if len(str(cur.execute("SELECT fotoid FROM UsInf WHERE (id) = (?)",(uid, )).fetchall()[0][0])) != 0:
      forblockid-=len(cur.execute("SELECT fotoid FROM UsInf WHERE (id) = (?)",(uid,)).fetchall()[0][0].split("@")) - 3
    cur.execute("UPDATE UsInf SET Blockid = ? WHERE (id) = (?)",(forblockid,uid,))
    conn.commit()
    sphr=""
    if f==starter[0]: sphr= "Создано при использововании LairWay. Удачной игры! \n\n"
    bot.send_message(message.from_user.id, sphr+RLW(text[f][0], uid), reply_markup=keyboard1)
  else:
      bot.edit_message_text(chat_id=message.from_user.id, message_id=message.message.message_id, text=RLW(text[f][0],uid), reply_markup=keyboard1)




def IfInBox(uid,message):
  if (uid,) in cur.execute("SELECT id FROM UsInf").fetchall(): return
  cur.execute("INSERT OR IGNORE INTO UsInf VALUES (?, ?, ?,  'commoner', 0,'')", (uid, message.from_user.username,str(message.chat.first_name) + " " + str(message.chat.last_name)))
  conn.commit()
#cur.execute('''CREATE TABLE IF NOT EXISTS box (id, box, key, skey, mod )''')

def IfTheBox(name, uid):
  if (uid, name) in cur.execute("SELECT id,box FROM box").fetchall(): return
  if name[0]=="@":
    cur.execute("INSERT OR IGNORE INTO box VALUES (?, ?, 0, 'NO','@')", (uid,name))
    conn.commit()
  else:
    cur.execute("INSERT OR IGNORE INTO box VALUES (?, ?, 0, 0,'')", (uid,name))
    conn.commit()



def RLW(text,uid):
  text = text.replace("|", "\n")
  if text.startswith("@"):
    parts = text[1:].split("@")
    part = ""
    for k in parts:
      if k=="": continue
      if k[0] == "!":
        part += str(cur.execute("SELECT key FROM box WHERE (id, box) = (?, ?)",(uid, k[1:])).fetchall()[0][0] )
      elif k[0] == "?":
        cake=k[1:].split("/?/")
        if len(cake)!=4:
          return "ERROR: Ошибка синтаксиса. Требуеться @?key/?/needkey/?/text1/?/text2, где key - название переменной а needkey - ключ нужного значения переменной, text1 - текст если условине - истино, text2 - текст если условие - ложь"
        try: 
          if door(uid, cake[0],cake[1]):
            part+=cake[2]
          else:
            part+=cake[3]
        except: return "ERROR: Ошибка синтаксиса door внутри '@?'"
      elif k=="name":
        part+=str(cur.execute("SELECT name FROM UsInf WHERE (id) = (?)",(uid,)).fetchall()[0][0])
      elif k=="rname":
        part+=str(cur.execute("SELECT rname FROM UsInf WHERE (id) = (?)",(uid,)).fetchall()[0][0])
      elif k=="fname":
        part+=str(cur.execute("SELECT rname FROM UsInf WHERE (id) = (?)",(uid,)).fetchall()[0][0]).split()[0]
      elif k=="sname":
        part+=str(cur.execute("SELECT rname FROM UsInf WHERE (id) = (?)",(uid,)).fetchall()[0][0]).split()[1]
      elif k=="role":
        part+=str(cur.execute("SELECT role FROM UsInf WHERE (id) = (?)",(uid,)).fetchall()[0][0])
      
      elif k in ("S1","s1"): 
         part+="~"
      elif k in ("S2","s2"):
          part+="|"
      elif k[0] in ("S3","s3"):
        part+="@"
      elif k[0]=="#":
        record=k[1:].split("//")
        for tname in cur.execute("SELECT id FROM UsInf").fetchall():
         if door(tname[0],record[0],record[1]):
           part+=str(cur.execute("SELECT name FROM UsInf WHERE (id) = (?)",(uid,)).fetchall()[0][0])+" "
      else:
        part += k
    text=part
  
  return text

def RoleCost(role):
  if type(role)==int: return role
  elif role=="lord": return 3
  elif role in ("herceg","high","h"): return 2
  elif role in ("w","way","wanderer","low"):return 1
  else: return 0

def role(uid, rn):
  ticket=False
  role=cur.execute("SELECT role FROM UsInf WHERE (id) = (?)",(uid,)).fetchall()[0][0]
  if RoleCost(role)>=RoleCost(rn): return True
  else: return False



def clear(uid, list=[], mody="n"):
  if mody == "n":
    if len(list) == 0:
      cur.execute("UPDATE box SET key = 0, skey = 0 WHERE (mod,id) = ('',?)",(uid, ))
    else:
      for a in list:
        cur.execute("UPDATE box SET key = 0, skey = 0 WHERE (mod,box,id) = ('',?, ?)",(a,uid,))
        cur.execute("UPDATE box SET key = 0 WHERE (mod,box, id) = ('@', ?,?)", (a,uid,))
  
  if mody == "@":
    cur.execute("UPDATE box SET key = 0 WHERE (mod,box,id) = ('@',?)",(auid,))


def key(name, tokey, uid):
   
    IfTheBox(name,uid)
    if tokey[0] == "+":
      cur.execute("UPDATE box SET key = key+? WHERE (id,box) = (?,?)",(int(tokey[1:]), uid, name))

    elif tokey[0] == "-":
      cur.execute("UPDATE box SET key = key-? WHERE (id,box) = (?,?)", (int(tokey[1:]), uid, name))

    elif tokey[0] == "=": 

      cur.execute("UPDATE box SET key = ? WHERE (id,box) = (?,?)", (int(tokey[1:]), uid, name))

    elif tokey[0] == "?":
      if tokey[1] == "+":
        RR = list(map(int, tokey[2:].split()))
        R1, R2 = RR[0], RR[1]
        cur.execute("UPDATE box SET key = key+? WHERE (id,box) = (?,?)",
                    (random.randint(R1, R2), uid, name))
      else:
        RR = list(map(int, tokey[1:].split()))
        R1, R2 = RR[0], RR[1]
        cur.execute("UPDATE box SET key = ? WHERE (id,box) = (?,?)",
                    (random.randint(R1, R2), uid, name))

    elif tokey[0] == "!" or tokey[0] == "G" or tokey[0] == "M" :

      if tokey[0] == "!": 
         Who=int(cur.execute("SELECT key FROM box WHERE (id, box) = (?, ?)",(uid, tokey[2:])).fetchall()[0][0])   
      if tokey[0] == "G" or tokey[0] == "M":
        Glist=[]
        for a in cur.execute("SELECT key FROM box WHERE box = (?)",( tokey[2:],)).fetchall():
          Glist.append(int(a[0]))
        if tokey[0] == "G":
          Who=sum(Glist)
        if tokey[0] == "M":
          Who=max(Glist)
      if tokey[1] == "+":
          cur.execute("UPDATE box SET key = key+? WHERE (id,box) = (?,?)",(Who, uid, name))

      elif tokey[1] == "-":
          cur.execute("UPDATE box SET key = key-? WHERE (id,box) = (?,?)", (Who, uid, name))

      else:
        cur.execute("UPDATE box SET key = ? WHERE (id,box) = (?,?)", (Who, uid, name))
    else:
      cur.execute("UPDATE box SET key = ? WHERE (id,box) = (?,?)",(int(tokey), uid,name))
    conn.commit()


def door(uid, name, key="1"):
  IfTheBox(name,uid)
  if key=="map":
    return fmap(uid,name)

  rev=False
  Behind="Значение открости двери"
  if key[0]=="R":
    rev=True
    key=key[1:]

  if key[0]=="!":
    if key[1] == ">":
      bkey=cur.execute("SELECT key FROM box WHERE (id, box) = (?, ?)",(uid, key[2:])).fetchall()[0][0]
      if cur.execute("SELECT key FROM box WHERE (id, box) = (?, ?)",(uid, name)).fetchall()[0][0] >= int(bkey):
        Behind=True
      else:
        Behind=False

    elif key[1] == "<":
      bkey=cur.execute("SELECT key FROM box WHERE (id, box) = (?, ?)",(uid, key[2:])).fetchall()[0][0]
      if cur.execute("SELECT key FROM box WHERE (id, box) = (?, ?)",(uid, name)).fetchall()[0][0] <= int(bkey):
        Behind=True
      else:
        Behind=False
    else:
      bkey=cur.execute("SELECT key FROM box WHERE (id, box) = (?, ?)",(uid, key[1:])).fetchall()[0][0]
      if cur.execute("SELECT key FROM box WHERE (id, box) = (?, ?)",(uid, name)).fetchall()[0][0] <= int(bkey):
        Behind=True
      else:
        Behind=False


  else: 
    if key[0] == ">":
      if cur.execute("SELECT key FROM box WHERE (id, box) = (?, ?)",(uid, name)).fetchall()[0][0] >= int(key[1:]):
        Behind=True
      else:
        Behind=False

    elif key[0] == "<":
      if cur.execute("SELECT key FROM box WHERE (id, box) = (?, ?)",(uid, name)).fetchall()[0][0] <= int(key[1:]):
        Behind=True
      else:
        Behind=False
    else:
      if cur.execute("SELECT key FROM box WHERE (id, box) = (?, ?)",(uid, name)).fetchall()[0][0] == int(key):
        Behind=True
      else:
        Behind=False
  if rev:
    return not Behind
  else:
    return Behind

def fmap(uid, name="",mway=[]):
  maprole=True
  if mway==[]:
    mway=maps[name]
  mmod=mway[0].split()
  if mmod[0] == "or":
    cat = True
    for mecho in range(len(mway[1:]) // 2):
      if mway[1+mecho*2][0]=="K":
        key(mway[1 + mecho * 2],mway[2 + mecho * 2][1:],uid)
        continue
      if door(uid, mway[1 + mecho * 2], mway[2 + mecho * 2]):
        break
    else:
      cat  = False
  if mmod[0] == "and":
    cat = False
    for mecho in range(len(mway[1:]) // 2):
      if mway[2+mecho*2][0]=="K":
        key(mway[1 + mecho * 2],mway[2 + mecho * 2][1:],uid)
        continue
      if not door(uid, mway[1 + mecho * 2], mway[2 + mecho * 2]):
        break
    else:
      cat = True
  for ExM in mmod[1:]:
    if ExM == "s":
      cur.execute("UPDATE box SET skey = key WHERE (mod,id) = ('',?)", (uid, ))
    elif ExM in ("l","lord"):
      if not role(uid, "lord"): maprole = False
    elif ExM in ("h","high","herceg"):
      if not role(uid, "h"): maprole = False
    elif ExM in ("w","low","wanderer"):
       if not role(uid, "w"): maprole = False
  return (cat and maprole)

def say(ad):
  if ad=="":return
  for citizen in cur.execute("SELECT DISTINCT id FROM UsInf").fetchall():
    bot.send_message(citizen[0],ad.replace("|", "\n"))

def Player(id):
  messI=""
  role = cur.execute("SELECT role FROM UsInf WHERE (id) = (?)",(id,)).fetchall()[0][0]
  messI+=str(role) + " "
  name = cur.execute("SELECT name FROM UsInf WHERE (id) = (?)",(id, )).fetchall()[0][0]
  messI+=str(name) + " Он же "
  rname = cur.execute("SELECT rname FROM UsInf WHERE (id) = (?)",(id, )).fetchall()[0][0]
  messI+=str(rname) + " Или же агент " + str(id) + " "
  rows = cur.execute("SELECT box, key FROM box WHERE id = ?", (id, ))
  for row in rows:
    messI += str(row[0]) + " - " + str(row[1]) + " "
  messI += "\n\n"
  return messI

def bye(rez, who='',box=""):
  try:
    if rez == "all":
      cur.execute("DELETE FROM box")
      conn.commit()
      cur.execute("DELETE FROM UsInf")
      conn.commit()
    elif rez == "box":
      cur.execute("DELETE FROM box")
      conn.commit()
    elif rez == 'user':
      id = cur.execute("SELECT id FROM UsInf WHERE (name) = (?)",(who, )).fetchall()[0][0]
      if box=="":
        cur.execute("DELETE FROM box WHERE id = ?", (id,))
      else:
        cur.execute("DELETE FROM box WHERE (id,box) = (?,?)", (id,box))
      conn.commit()
    elif rez == 'id':
      cur.execute("DELETE FROM box WHERE id = ?", (who,))
      conn.commit()
    return True
  except Exception as e:
    print(e)
    return False



def Inf(id="all"):
  try:
    messI = "LairWayINF:\n\n"
    if id == "all":
      idlist = cur.execute("SELECT DISTINCT id FROM UsInf").fetchall()
    elif str(id)[0]=="@":
      idlist = cur.execute("SELECT DISTINCT id FROM UsInf WHERE (name) = (?)",(id[1:],)).fetchall()
    else:
      idlist = [[id]]
    for ide in idlist: 
      messI+=Player(ide[0])
    return messI
  except:
    return "Error Lairway Inf"
#Функция LairwayRead, которая читает файл игры и делит ее сначало построчно а затем делит ее на элементы по этому символу ~. В последующих строках мы спрашиваем его, чем является первый элемент этой строки. Если это tx, то мы превращаем последующие элементы строки в список и добавляем в словарь text, где ключом является номер текста, а значением все последующие значения текста. Аналогично для "bt" и "img"
def LairWayRead():
  cur.execute("UPDATE UsInf SET role = 'commoner' ")
  if os.path.exists("cat.lairway"):
    with open("cat.lairway", 'r', encoding='utf-8') as cnt:
      first=cnt.readlines()
      for f in first[0].strip().split():
        LWR(f+".lairway")
  else:
    LWR("Game.lairway")

def LWR(game):
  Size=[None,None,None]
  try:
    gencount=0
    with open(game, 'r', encoding='utf-8') as f:
      a = f.readlines()
      for line in a:
          gg = line.strip().split("~")
          if gg[0] == "tx":
            text[gg[1]] = []
            for i in range(2, len(gg)):
              text[gg[1]].append(gg[i])
          elif gg[0] =="bt":
            bttn[gg[1]] = []
            for i in range(2, len(gg)):
              bttn[gg[1]].append(gg[i])
          elif gg[0] == "fbt":
            bttn[gg[1]] = [gg[2],gg[1]]
            for i in range(3, len(gg)):
              bttn[gg[1]].append(gg[i])
          elif gg[0] == "key":
            bttn[gg[1]] = ["None","","k"]
            for i in range(2, len(gg)):
              bttn[gg[1]].append(gg[i])
          elif gg[0]=="qk":
            text[gg[1]] = [gg[2]]
            for i in range(4, len(gg),2):
              gencount+=1
              genway="QuickBttn№"+str(gencount)
              text[gg[1]].append(genway)
              bttn[genway]=[gg[i],gg[i-1]]  
          elif gg[0] == "img":
            img[gg[1]] = []
            for i in range(2, len(gg)):
              img[gg[1]].append(gg[i])
          elif gg[0] == "map":
            maps[gg[1]] = []
            for i in range(2, len(gg)):
              maps[gg[1]].append(gg[i])
          elif gg[0] in ("spell","spl"):
            spell[gg[1]] = []
            spl.append(gg[1])
            for i in range(2, len(gg)):
              spell[gg[1]].append(gg[i])
              
          elif gg[0] == "ph":
            if len(gg)==2:starter[0] = gg[1]
            if len(gg)==3:phrase[0] = gg[2]
            if len(gg)==4:phrase[1] = gg[3]
            if len(gg)==5: starter[1]= gg[4]  
          elif gg[0] == "role":
            for lord in gg[1:]:
              if lord[0]=="@":
                cur.execute("UPDATE UsInf SET role = 'lord' WHERE (name) = (?)",(lord[1:],))
              elif lord[0]=="#":
                cur.execute("UPDATE UsInf SET role = 'herceg' WHERE (name) = (?)",(lord[1:],))
              else:
                cur.execute("UPDATE UsInf SET role = 'wanderer' WHERE (name) = (?)",(lord,))
  except Exception as err:
      print(f"ERROR!:\n.Чтение файла {game} - \n Ошибка {err}")




LairWayRead()




def Lairway(f,message, tp=0, new = 1):
  try:
    gasanbek(f=f,message=message, tp=tp, new = new)
  except Exception as e:
    print(e)
    bot.send_message(message.from_user.id,"Какая-то небольшая проблема")


@bot.message_handler(commands=['start','go','run','game'])
def StartCommand(message):
  IfInBox(message.from_user.id, message)
  Lairway(starter[0], message)

@bot.callback_query_handler(func=lambda call: True)
def самостоятельный(call):
  Lairway(call.data, call, new = 0)


#Команда lairway которая выводит основную информацию о движке
@bot.message_handler(commands=['lairway'])
def TextCommand(message):
  IfInBox(message.from_user.id, message)
  bot.send_message(message.from_user.id,"Вас приветсвует текстовый ТБ-движек LairWay. Версия Lairway - Pre-Release 1.0 Attempt 2 or 1.14.1.  Основные разработчики - catman(великий и главный), Ⰳⰰⱄⰰⱀⰱⰵⰽ ან ბრწყინვალე ഹസൻബെക്. Количество пользователей этого бота - " + str(len(cur.execute("SELECT DISTINCT id FROM UsInf").fetchall())) +". Cвязь с разработчиком движка - LairWayBot@gmail.com.")


#Считывает файл сюжета игры
@bot.message_handler(commands=['Read','read'])
def ReadCommand(message):
  bot.send_message(message.from_user.id, "Фаил прочитан.")
  LairWayRead()

#Очищяет все неизменямые переменные
@bot.message_handler(commands=['ClearMe','reset',"Reset", 'Rebith', 'rebith'])
def CleanCommand(message):
  if bye("id", message.from_user.id):
    bot.send_message(message.from_user.id, "Ваши достижения сброшены!")
  else: bot.send_message(message.from_user.id, "Error.")



@bot.message_handler(commands=['Size','size'])
def SizeCommand(message):
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
  bot.send_message(message.from_user.id, "В игре в текстах " +str(Size[0])+" символов, в кнопках " +str(Size[1])+" символов, а так же дополнительно "+str(Size[2])+". ТЕ суммарно " +str(Size[0]+Size[1]+Size[2])+" символов.")
#Команды админов

@bot.message_handler(commands=['bye', 'del', 'delete', 'clrsql',"clear"])
def DelCommand(message):
  if role(message.from_user.id,"lord"):
    dell=message.text.split()
    if len(dell)==1: 
      if not bye("all"):
        bot.send_message(message.from_user.id, "Error"); return
    elif dell[1]=="box": 
      if not bye("box"):
        bot.send_message(message.from_user.id, "Error") ; return  
    elif len(dell)==3:
      if not bye("user", dell[1],dell[2]):
         bot.send_message(message.from_user.id, "Error. \n Возможно вы ввели никнейм несущесвующего юзера или имя переменной."); return
    else: 
      if not bye("user", dell[1]):
         bot.send_message(message.from_user.id, "Error. \n Возможно вы ввели никнейм несущесвующего юзера."); return
    bot.send_message(message.from_user.id, "Очистка произведена удачно. Вы очистили Землю от этих жалких людей, поздравляю!")
  
  else:
    bot.send_message(message.from_user.id, "У вас не хватает прав для использования этой команды!")


@bot.message_handler(commands=['Say',"say"])
def SayCommand(message):
  if role(message.from_user.id,"lord"):
    say(message.text[4:])
  else:
    bot.send_message(message.from_user.id, "У вас не хватает прав для использования этой команды!")

@bot.message_handler(commands=['Inf',"inf"])
def InfCommand(message):
  IfInBox(message.from_user.id, message)
  if role(message.from_user.id,"lord"): 
    infsay=message.text.split()
    if len(infsay)>1:
      if infsay[1]=="me": bot.send_message(message.from_user.id,Inf(message.from_user.id))
      else:  bot.send_message(message.from_user.id,Inf("@"+infsay[1]))
    else: 
      bot.send_message(message.from_user.id,Inf("all"))
  else:
    bot.send_message(message.from_user.id, "У вас не хватает прав для использования этой команды!")

@bot.message_handler(commands=['File','file'])
def LWreadCommand(message):
  if role(message.from_user.id,"lord"):
    try:
      bttn,text={},{}
      LWR(message.text[6:]+".lairway")
      bot.send_message(message.from_user.id, 'Фаил открыт и прочитан.')
    except:
      bot.send_message(message.from_user.id, "Фаил не найден.")
  else:
     bot.send_message(message.from_user.id, "У вас не хватает прав для использования этой команды!")

@bot.message_handler(commands=['save','Save',"GHS","gts","sql"])
def LWsaveCommand(message):
  if role(message.from_user.id,"h"):
    if GHS():
      bot.send_message(message.from_user.id, "SQL сохранен!")
    else: 
      bot.send_message(uid, "GTSAVE невозможен. Возможно вы не указали токен GitHub (GitHub) и путь к вашему репл (name) в формате 'имя/репл', или же не создали LW.db в гитхабе")
  else:
    bot.send_message(message.from_user.id, "У вас не хватает прав для использования этой команды!")

@bot.message_handler(commands=['tp',"Tp"])
def TpCommand(message):
  IfInBox(message.from_user.id, message)
  if role(message.from_user.id,"h") :
    try:
      gasanbek(starter[0], message, tp=message.text[4:])
    except:
       bot.send_message(message.from_user.id, "Напишите после /tp номер комнаты куда вам нужно телепортироваваться!")

  else:
    bot.send_message(message.from_user.id, "У вас не хватает прав для использования этой команды!")


@bot.message_handler(commands=['key','Key'],)
def perem(message):
  if role(message.from_user.id,"lord"): 
    try:
      key(message.text.split()[1], message.text.split()[2].replace("~"," "), uid=message.from_user.id)
      bot.send_message(message.from_user.id, 'Вы изменили значение переменной')
    except:
      bot.send_message(message.from_user.id, 'Вы не указали ключ или значение переменной, или забыли указать их. (/key имя_переменной изменение_переменной (помните что во внутренем синтаксисе вместо " " идет "~"))')
  else:
     bot.send_message(message.from_user.id, "У вас не хватает прав для использования этой команды!")

@bot.message_handler(commands=['send','Send'])
def LWtestCommand(message):
  if role(message.from_user.id,"lord"):
    try:
      name=message.text.split()[1]
      with open(name,"rb") as file:
        bot.send_document(message.from_user.id,file,"name")
    except:
      bot.send_message(message.from_user.id, "Вы забыли указать название файла, фаил не найден или произошла другая ошибка.")
  else:
     bot.send_message(message.from_user.id, "У вас не хватает прав для использования этой команды!")

 #другом случае:
@bot.message_handler(commands=spl)
def Spell(message):
  uid = message.from_user.id
  command=message.text.split()[0][1:]
  splway=spell[command]
  if len(splway)==1:
    Lairway(splway[0], message)
  elif len(splway)==2:
    if role(uid,splway[1]):
      Lairway(splway[0], message)
    else: 
      bot.send_message(uid, "У вас не хватает прав для использования этой команды!")
  elif len(splway)>2:
    if door(uid,splway[1],splway[2]):
      Lairway(splway[0], message)
    else:
      if len(splway)>3:
        bot.send_message(uid, RLW(splway[3],uid))
      else:
        bot.send_message(uid, RLW(phrase[0],uid))
      

      
  
@bot.message_handler(content_types=['text'])
def TextCommand(message):
  bot.send_message(message.from_user.id, RLW(phrase[0],message.from_user.id))


@bot.message_handler(content_types=['sticker'])
def stickCommand(message):
  bot.send_message(message.from_user.id, RLW(phrase[0],message.from_user.id))


LWLS()
bot.polling(none_stop=True, timeout=123)