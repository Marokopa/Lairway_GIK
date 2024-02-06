import random
from LairWay.Tools import *
from MyLairWay import *


def Lairway(f,message, tp=0, new = 1):
  #gasanbek(f=f,message=message, tp=tp, new = new)
  try:
    gasanbek(f=f,message=message, tp=tp, new = new)
  except Exception as e:
    print(e)
    Send(message.from_user.id,SM.Mess("P",lang) )



LairWayV="0.16 (GodOfEyes II)"


text = {}
bttn = {}
img = {}
maps={}
spell={}
spl=[]


phrase = [
  "Welcome to the game made on the basis of the Lairway TB engine. To start, click on /start",
      "The LairWayDefence protection system against bugs and glitches has been activated"
]

starter = ["1",None]
Size=[None,None,None]


SM = Mess()


lang="en"


def gasanbek(f, message, tp=0, new = 1):
  uid = Uid(message)
  mid=Mid(message)

    

  SM.New('TxNE', ['en', 'ru'], ["Error:\nText "+str(f)+" does not exist.", "Error 1:\nТекста "+str(f)+" не существует."])
  SM.New('TxL', ['en', 'ru'], 
      ["Error 2:\nText "+str(f)+" Too big or small. Restriction - must be at least 1 character and no more than "+str(biglim), 
      "Error 2:\nТекст "+str(f)+" Cлишком большой или маленький. Ограничение - должен быть минимум 1 симврол и не больше чем "+str(biglim)])

  


  if not f in text:
    Send(uid,SM.Mess("TxNE",lang))
    return "No_TX"
  if not(len(text[f][0]) > 0 and len(text[f][0]) < biglim):
    Send(uid,SM.Mess("TxL",lang))
    return

  kb=Keyboard()
  
  if new==1:
    NewFotoId(uid)
    clear(uid)

  if tp!=0:  NewBt(kb,"tp",tp)

  if new != 1 and not (BlockId(uid) == mid):
    Edit(uid,mid,phrase[1])
    return

  if starter[1]=="player":
    print(Inf(uid))
  elif starter[1]=="way":
    print(text,bttn,img,maps,spell)
  elif starter[1]!=None:
    print(Inf(str(starter[1])))



  #Удаление изображений
  if len(str(FotoId(uid))) != 0:
    fotoid = FotoId(uid)[1:]
    icount = fotoid.split("@")
    for imgid in icount:
      Kill(uid, int(imgid))
    NewFotoId(uid)

  for i in range(1, len(text[f])):
    SM.New("Empty", ['en','ru'], ["Error 3:\nYou are trying to use an empty button/image after the text.","Error 3:\n Вы пытаетесь использовать пустую кнопку/картинку после текста."])
    SM.New("ImgE", ['en','ru'], ["Error 4:\nThe picture does not exist, but it is listed after the text.",
                                "Error 4:\nКартинки не существует, но она указана после текста."])
    SM.New("BtE", ['en','ru'], ["Error 5:\nThe button does not exist, but it is indicated after the text.",
                        "Error 5:\nКнопки не существует, но она указана после текста."])
    SM.New("BtL", ['en','ru'], 
           ["Error 6:\nThe button does not comply with the length rules, which state that it must be greater than 0 and less than characters.","Error 6:\nКнопка не соответствует правилам длины, которые гласят, что тот должен быть больше 0 и меньше символов."])
    SM.New("BtM", ['en','ru'], 
       ["Error 7:\n For the button not enough parameters were specified, the number, text, and text it leads to are required.","Error 7:\nДля кнопки указали недостаточно параментров, требуться номер, текст, текст в который она ведет."])
    SM.New("SE", ['en','ru'], 
       ["Error 8:\nThe button has incorrect syntax.", "Error 8:\nКнопка имеет не правильный синтаксис."])
    

    
  
    
    if text[f][i] == "":
      Send(uid,SM.Mess("Empty",lang) )
      continue
    if text[f][i] == "KillGame" and new==0:
      try:Kill(uid, mid)
      except:Edit(uid, mid,"):")
      return

    if text[f][i][0] == "@": 
      if text[f][i][1:] not in img:
        Send(uid,SM.Mess("ImgE",lang) )
        continue
      imgway = img[text[f][i][1:]]
      l = open(imgway[1], "rb")
      if len(imgway) == 2:
        file = File(uid, imgway[0] ,l)
      else:
        if not (len(imgway[2]) > 0 and len(imgway[2]) < biglim):
          Send(uid,SM.Mess("TxL",lang))
          return
        file = File(uid, imgway[0], l, text=RLW(imgway[2],uid))
      AddFotoId(uid,file)
      l.close()
    else:    

      if text[f][i] not in bttn:
        Send(uid,SM.Mess("BtE",lang) )
        continue
      way = bttn[text[f][i]]
      if not(len(way[0]) > 0 and len(way[0]) < btlim):
        Send(uid,SM.Mess("BtL",lang) )
        continue
      try:
        if len(way) == 2:
          NewBt(kb,way[0],way[1])
        elif len(way)<2:
          Send(uid,SM.Mess("BtM",lang) )
          continue



        #Тип кнопки k. Позволяет создавать переменные и давать им значения
        elif way[2] == "k":
          if len(way) == 4:
            key(way[3],"1",uid)
          else:
            for k in range(0,len(way[2:])-1,2):
              key(way[k+3],way[k+4],uid)
          if way[1]!="":
            NewBt(kb,way[0],way[1])

        #Тип кнопки c. Позволяет отчищать
        elif way[2] == "c":
          if len(way) == 3:
            clear(uid)
          else:
            clear(uid, list=way[3:])

          if way[1]!="":
            NewBt(kb,way[0],way[1])

        #Тип кнопки r. Позволяет придавать значениям переменных рандомное значение
        elif way[2] == "r":  
            if way[1]=="@":
              rz=random.randint(4, len(way)-1)
              if rz%2==0: rz-=1
              NewBt(kb,way[rz+1],way[rz])

            elif len(way[1])!=0 and way[1][0]=="D":
              rdoor=way[1][1:].split("//")
              if door(uid,rdoor[0],rdoor[1]):
                NewBt(kb,way[0],way[random.randint(3,len(way) - 1)])
              elif len(rdoor)>2:
                NewBt(kb,way[0], rdoor[random.randint(2,len(rdoor) - 1)])
    
            else:
              NewBt(kb,way[0], way[random.randint(3,len(way) - 1)])
          



        #Тип кнопки d. Позволяет отправять разные сообщения взависемости от значения переменной
        elif way[2] == "d":
          if len(way) == 5:
            if door(uid, way[3]):
              NewBt(kb,way[0],way[4])
            else:
              NewBt(kb,way[0],way[1])

          else:
            if door(uid, way[3], way[5]):
              if len(way) == 7:
                NewBt(kb,way[6],way[4])
              else:
                NewBt(kb,way[0],way[1])

            else:
              NewBt(kb,way[0],way[1])

        elif way[2] == "i":
          if len(way) == 4:
            if door(uid, way[3]):
              NewBt(kb,way[0],way[1])
          else:
            if door(uid, way[3], way[4]):
              NewBt(kb,way[0],way[1])

        elif way[2] == "m":
          if fmap(uid,mway=way[4:]):
            NewBt(kb,way[0],way[1])
          else:
            if way[3]!="":
              NewBt(kb,way[0],way[3])


        elif way[2]=="u":
          #bt~way~text[0]~wayto0/""[1]~u[2]~name1[3]~if1[4]~wayto1[4]
          wayto=way[1]
          for ult in range(len(way[3:])//3):
            if door(uid, way[3+ult*3], way[4+ult*3]):
              wayto=way[5+ult*3]
              break
          if wayto!="":
            NewBt(kb,way[0],wayto)


        elif way[2] == "w":
          #bt~1~text[0]~[1]~w[2]~max[3]~foo[4]~way(2)[5]~bar[6]~way(3)[7]../
          ways= []
          if way[1]=="@":
             for a in range((len(way[3:]) // 3)):
              IfTheBox(way[4 + a * 3],uid)
              ways.append([Box(uid, way[4 + a * 3])] + [way[5 + a * 3]] +[ way[6 + a * 3]])
          else:
            for a in range((len(way[3:]) // 2)):
              IfTheBox(way[4 + a * 2],uid)
              ways.append([Box(uid, way[4 + a * 3])] + [way[5 + a * 2]])
              
          ways.sort(key=lambda x: x[0])
          wayslen  ,waytext =len(ways)-1,way[0]
          if way[3] == "max":
            if way[1] == "@":
                waytext = ways[wayslen][2]
            NewBt(kb, waytext, ways[wayslen][1])
      
          if way[3] == "min":
              if way[1] == "@":
                  waytext = ways[0][2]
              NewBt(kb, waytext, ways[0][1])
          if way[3] == "med":
              if way[1] == "@":
                  waytext = ways[wayslen//2][2]
              NewBt(kb, waytext, ways[wayslen//2][1])
        elif way[2] == "s":
          Save(uid)
          conn.commit()
          if way[1]!="":
            NewBt(kb,way[0],way[1])

        elif way[2] == "l":
          Load(uid)
          if way[1]!="":
            NewBt(kb,way[0],way[1])

        elif way[2] == "v":
          if role(uid,way[3]):
            NewBt(kb,way[0],way[1])

        elif way[2] == "f":
          F=globals()["F_"+way[3]](uid,*tuple(way[4:]))
          if isinstance(F, str ):
            NewBt(kb,way[0],F)
          elif F!=False:
            NewBt(kb,way[0],way[1])
            
      except Exception as e:
        Send(uid,SM.Mess("SE",lang) )
        print(e)
        continue

  if new == 1:
    forblockid=mid+1
    if len(str(FotoId(uid))) != 0:
      forblockid-=len(FotoId(uid).split("@")) - 3
    BlockIdIs(forblockid,uid,)
    sphr=""
    if f==starter[0]: sphr= SM.Mess("LW",lang)
    Send(uid, sphr+RLW(text[f][0], uid), kb=kb)
  else:
    Edit(uid, mid, RLW(text[f][0],uid), kb)

SM.New('LW', ['en', 'ru'], ["Created using LairWay. Good game!\n","Создано при использововании LairWay. Удачной игры!\n "])
SM.New('RKE', ['en', 'ru'], ["ERROR 1R : Syntax error. Required @?key/?/needkey/?/text1/?/text2, where key is the name of the variable and needkey is the key of the desired value of the variable, text1 is the text if the condition is true, text2 is the text if the condition is true lie","ERROR: Ошибка синтаксиса. Требуеться @?key/?/needkey/?/text1/?/text2, где key - название переменной а needkey - ключ нужного значения переменной, text1 - текст если условине - истино, text2 - текст если условие - ложь"])
SM.New('RSE', ['en', 'ru'], ["ERROR 2R: Door syntax error inside '@?'","ERROR 2R: Ошибка синтаксиса door внутри '@?'"])
SM.New('P', ['en', 'ru'], ["Error 0: Some minor problem. I'll try again after some time.","Error 0: Какая-то небольшая проблема. Попробуйье еще раз через какое-то время."])

def File(uid,typ,the_file,text=None):
  if typ=="img": return Foto(uid, the_file, text=text)
  elif typ=="doc": return Doc(uid,the_file, text=text)

def RLW(text,uid):
  text = text.replace("|", "\n")
  if text.startswith("@"):
    parts = text[1:].split("@")
    part = ""
    for k in parts:
      if k=="": continue
      if k[0] == "!":
        part += str(Box(uid, k[1:]))
      elif k[0] == "?":
        cake=k[1:].split("/?/")
        if len(cake)!=4:
          return SM.Mess("RKE",lang)
        try: 
          if door(uid, cake[0],cake[1]):
            part+=cake[2]
          else:
            part+=cake[3]
        except: return SM.Mess("RSE",lang)
      elif k=="name":part+=Name(uid)
      elif k=="rname":part+=Rname(uid)
      elif k=="fname":part+=Rname(uid).split()[0]
      elif k=="sname":part+=Rname(uid).split()[1]
      elif k=="role":part+=Role(uid)

      elif k in ("S1","s1"): 
         part+="~"
      elif k in ("S2","s2"):
          part+="|"
      elif k[0] in ("S3","s3"):
        part+="@"
      elif k[0]=="#":
        record=k[1:].split("//")
        for tname in Ids():
         if door(tname[0],record[0],record[1]):
           part+=str(Name(uid))+" "
           
      elif k[0]=="*":
        Fpart=k[1:].split("/*/")
        part+=globals()["F_"+Fpart[0]](uid,*tuple(Fpart[1:]))
      else:
        part += k
    text=part

  return text



def LairWayRead():
  RoleClear()
  if os.path.exists("cat.lairway"):
    with open("cat.lairway", 'r', encoding='utf-8') as cnt:
      first=cnt.readlines()
      for f in first[0].strip().split():
        LWR(f+".lairway")
  else:
    LWR("Game.lairway")

def LWR(game):
  global lang
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
            img[gg[1]] = ["img"]
            for i in range(2, len(gg)):
              img[gg[1]].append(gg[i])
          elif gg[0] == "doc":
            img[gg[1]] = ["doc"]
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
              
          elif gg[0]=="mod":
            if len(gg)>1:  starter[0] = gg[1]
            if len(gg)>2: lang = gg[2]
            if len(gg)>3: starter[1] = gg[3]
            

          elif gg[0] == "ph":
            if len(gg)>1:phrase[0] = gg[1]
            if len(gg)>2:phrase[1] = gg[2]

          elif gg[0] == "role":
            for lord in gg[1:]:
              if lord[0]=="@":
                NewRole('lord',lord[1:])
              elif lord[0]=="#":
                NewRole('herceg',lord[1:])
              else:
                NewRole('wanderer',lord[1:])
  except Exception as err:
      print(f"ERROR!:\n.Reading file {game} - \nError {err}")




LairWayRead()



