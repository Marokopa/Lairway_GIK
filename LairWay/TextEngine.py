import random
from LairWay.LWTools import *
from Mod.MyLairWay import *


def Lairway(f,message, tp=0, new = 1):
  #gasanbek(f=f,message=message, tp=tp, new = new); return
  try:
    gasanbek(f=f,message=message, tp=tp, new = new)
  except Exception as e:
    print(e)
    Send(message.from_user.id,SM.Mess("P",lang) )



phrase = [
  "Welcome to the game made on the basis of the Lairway TB engine. To start, click on /start",
      "The LairWayDefence protection system against bugs and glitches has been activated"
]

starter = ["1",None]
Size=[None,None,None]
CallSave={}
gencount=[0]



def gasanbek(f: str,message: telebot.types.Message, tp: int=0, new: int = 1):
  uid = Uid(message)
  mid=Mid(message)
  if not f in text:
    Send(uid,SM.MessArg("TxNE",lang,str(f)))
    return "No_TX"
  if not(len(text[f][0]) > 0 and len(text[f][0]) < biglim):
    Send(uid,SM.MessArg("TxL",lang,str(f),str(biglim)))
    return

  kb=Keyboard()
  KillFlies(uid)

  if new==1:
    NewFotoId(uid)
    clear(uid)

  if tp!=0:  NewBt(kb,"tp",tp)
  if new != 1 and not (BlockId(uid) == mid):
    Edit(uid,mid,phrase[1])
    return

  if starter[1]=="player": print(Inf(uid))
  elif starter[1]=="way": print(text,bttn,img,maps,spell)
  elif starter[1]=="step": print("_step_")

  #Удаление изображений
    
  if len(str(FotoId(uid))) != 0:
    fotoid = FotoId(uid)[1:]
    icount = fotoid.split("@")
    for imgid in icount:
      Kill(uid, int(imgid))
    NewFotoId(uid)

    #обработка кнопок

  for i in range(1, len(text[f])):
    if text[f][i] == "":
      Send(uid,SM.Mess("Empty",lang) )
      continue
    if text[f][i] == "KillGame" and new==0:
      try:Kill(uid, mid)
      except:Edit(uid, mid,"):")
      return
    #LWIS2+
    if text[f][i][0] == "@": 
      if text[f][i][1:] not in img:
        Send(uid,SM.MessArg("ImgE",lang,text[f][i][1:]) )
        continue
      imgway = img[text[f][i][1:]]
      if not imgway[0] in ("stk"): l = open("GameFiles/"+imgway[1], "rb")
      else: l=imgway[1]
      if len(imgway) == 2:
        file = File(uid, imgway[0] ,l)
      #кнопки
      else:
        if not (len(imgway[2]) > 0 and len(imgway[2]) < biglim):
          Send(uid,SM.MessArg("TxL",lang,f,biglim))
          return
        file = File(uid, imgway[0], l, text=RLW(imgway[2],uid))
      AddFotoId(uid,file)
      if not imgway[0] in ("stk"): l.close()
    else:    

      if text[f][i] not in bttn:
        Send(uid,SM.MessArg("BtE",lang,text[f][i]) )
        continue
      way = bttn[text[f][i]]
      if not(len(way[0]) > 0 and len(way[0]) < btlim):
        Send(uid,SM.MessArg("BtL",lang,text[f][i],btlim) )
        continue
      try:
        if len(way) == 2:
          NewBt(kb,way[0],way[1])
        elif len(way)<2:
          Send(uid,SM.MessArg("BtM",lang,text[f][i]) )
          continue

        #Тип кнопки k. Позволяет создавать переменные и давать им значения
        elif way[2] in ("k", "key"):
          if len(way) == 4:
            key(way[3],"1",uid)
          else:
            for k in range(0,len(way[2:])-1,2):
              key(way[k+3],way[k+4],uid)
          if way[1]!="":
            NewBt(kb,way[0],way[1])
          
        #применяет что-то к классам
        elif way[2] in ("a", "apply"):
            for k in range(0,len(way[2:])-1,2):
              key(way[k+3],way[k+4],uid, IfType=True)
            if way[1]!="":NewBt(kb,way[0],way[1])

        #задает тип
        elif way[2] in ("t", "type"):
            for some_box in way[3:]:
              AddType(uid,some_box,way[3])
            if way[1]!="":NewBt(kb,way[0],way[1])

        #Тип кнопки c. Позволяет отчищать
        elif way[2] in ("c", "clear"):
          if len(way) == 3:
            clear(uid)
          else:
            clear(uid, list=way[3:])

          if way[1]!="":NewBt(kb,way[0],way[1])

        #Тип кнопки r. Позволяет придавать значениям переменных рандомное значение
        elif way[2] in ("r", "random"):  
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
        elif way[2] in ("d", "door"):
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

     

        elif way[2] in ("i", "idoor", "invisible"):
          if len(way) == 4:
            if door(uid, way[3]):
              NewBt(kb,way[0],way[1])
          else:
            if door(uid, way[3], way[4]):
              NewBt(kb,way[0],way[1])

        elif way[2] in ("m", "mapdoor"):
          if fmap(uid,mway=way[4:]):
            NewBt(kb,way[0],way[1])
          else:
            if way[3]!="":
              NewBt(kb,way[0],way[3])


        elif way[2] in ("u", "udoor"):
          #bt~way~text[0]~wayto0/""[1]~u[2]~name1[3]~if1[4]~wayto1[4]
          wayto=way[1]
          for ult in range(len(way[3:])//3):
            if door(uid, way[3+ult*3], way[4+ult*3]):
              wayto=way[5+ult*3]
              break
          if wayto!="":
            NewBt(kb,way[0],wayto)


        elif way[2] in ("w", "ways"):
          #bt~1~text[0]~[1]~w[2]~max[3]~foo[4]~way(2)[5]~bar[6]~way(3)[7]../
          ways= []
          if way[1]=="@":
             for a in range((len(way[3:]) // 3)):
              IfInBox(way[4 + a * 3],uid)
              ways.append([Box(uid, way[4 + a * 3])] + [way[5 + a * 3]] +[ way[6 + a * 3]])
          else:
            for a in range((len(way[3:]) // 2)):
              IfInBox(way[4 + a * 2],uid)
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

        elif way[2] in ("s", "safe"):
          Save(uid)
          if way[1]!="":
            NewBt(kb,way[0],way[1])
        elif way[2] in ("l", "load"):
          Load(uid)
          if way[1]!="":
            NewBt(kb,way[0],way[1])

        elif way[2] in ("v", "view", "viewing"):
          if Required_Role(uid,way[3]):
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
      forblockid+=len(FotoId(uid).split("@"))-1
    BlockIdIs(forblockid,uid,)
    sphr=""
    if f==starter[0]: sphr= SM.Mess("LW",lang)
    Send(uid, sphr+RLW(text[f][0], uid), kb=kb)
  else:
    Edit(uid, mid, RLW(text[f][0],uid), kb)


def WriteLWL(element_type,name=None):
  Vex=SM.MessArg("NoElType", lang , element_type)
  if element_type in ("button","bttn","bt","b","fbt"):
    Vex="bt~"+name
    for part in bttn[name]: Vex+="~"+part
  elif element_type in ("text","tx","qw","t"):
    Vex="tx~"+name
    for part in text[name]: Vex+="~"+part
  elif element_type in ("+","img","vc","vid","aud","stk"):
    Vex=img[name][0]+"~"+name
    for part in img[name][1:]: Vex+="~"+part
  elif element_type in ("spell","spl","sp","s"):
    Vex="spell~"+name
    for part in spell[name]: Vex+="~"+part
  elif element_type in ("mod","m"):
    try: Vex="mod~"+starter[0]+"~"+lang+"~"+starter[1]
    except: Vex="mod~"+starter[0]+"~"+lang
  elif element_type in ("ph","p","phrase"):
    Vex="phrase~"+phrase[0]+"~"+phrase[1]
  return Vex+"\n"

def Remove(element_type, name):
    if element_type in ("text","tx","qw","t"):
        del text[name]
    elif element_type in ("button","bttn","bt","b","fbt"):
        del bttn[name]
    elif element_type in ("+","img","vc","vid","aud","stk"):
        del img[name]
    if element_type in ("spell","spl","sp","s"):
        del spell[name]
      
def VexMole():
  with open("GameFiles/VexMole.lairway","w", encoding='utf-8') as vm:
    vm.write(WriteLWL("mod"))
    vm.write(WriteLWL("ph"))
    for worm in text: vm.write(WriteLWL("tx",worm)) 
    for worm in bttn: vm.write(WriteLWL("bt",worm)) 
    for worm in img: vm.write(WriteLWL("+", worm)) 
      
  



def ReadData():
  bttn, text, img, spell = {},{},{}, {}
  RoleClear()
  global core
  core = JSONread()
  list(map(GiveRole, ["lord", "herceg", "wanderer"]))
  for Game in core["games"]:
    ReadGame("GameFiles/"+Game+".lairway")

def GiveRole(role):
  for citizen in core[role]:
    NewRole(role, citizen)

def ReadGame(game):
  gencount=[0]
  Size=[None,None,None]
  try:
    with open(game, 'r', encoding='utf-8') as LWRST:
      for line in LWRST.readlines(): ReadLWL(line)
  except Exception as err:
      print(f"ERROR!:\n.Reading file {game} - \nError {err}")

def ReadLWL(line):
  global lang
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
  elif gg[0] == "scr":
    bttn[gg[1]] = ["None",""]
    for i in range(2, len(gg)):
      bttn[gg[1]].append(gg[i])
  elif gg[0]=="qk":
    text[gg[1]] = [gg[2]]
    for i in range(4, len(gg),2):
      gencount[0]+=1
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
  elif gg[0] == "vid":
    img[gg[1]] = ["vid"]
    for i in range(2, len(gg)):
      img[gg[1]].append(gg[i])
  elif gg[0] == "aud":
    img[gg[1]] = ["aud"]
    for i in range(2, len(gg)):
      img[gg[1]].append(gg[i])
  elif gg[0] == "vc":
    img[gg[1]] = ["vc"]
    for i in range(2, len(gg)):
      img[gg[1]].append(gg[i])
  elif gg[0] == "stk":
    img[gg[1]] = ["stk"]
    for i in range(2, len(gg)):
      img[gg[1]].append(gg[i])
  elif gg[0] == "map":
    maps[gg[1]] = []
    for i in range(2, len(gg)):
      maps[gg[1]].append(gg[i])
  elif gg[0] in ("spell","spl"):
    spell[gg[1]] = []
    for i in range(2, len(gg)):
      spell[gg[1]].append(gg[i])
  
  elif gg[0]=="mod":
    if len(gg)>1:  starter[0] = gg[1]
    if len(gg)>2: lang = gg[2]
    if len(gg)>3: starter[1] = gg[3]
  elif gg[0] == "ph":
    if len(gg)>1:phrase[0] = gg[1]
    if len(gg)>2:phrase[1] = gg[2]
  
ReadData()

