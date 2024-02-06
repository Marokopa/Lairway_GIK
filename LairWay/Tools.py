from LairWay.LairEye import *
from LairWay.LairBox import *
from LairWay.LairFace import *
import random
lang="en"
SM.New('LW', ['en', 'ru'], ["Created using LairWay. Good game!\n","Создано при использововании LairWay. Удачной игры!\n "])
SM.New('RKE', ['en', 'ru'], ["ERROR 1R : Syntax error. Required @?key/?/needkey/?/text1/?/text2, where key is the name of the variable and needkey is the key of the desired value of the variable, text1 is the text if the condition is true, text2 is the text if the condition is true lie","ERROR: Ошибка синтаксиса. Требуеться @?key/?/needkey/?/text1/?/text2, где key - название переменной а needkey - ключ нужного значения переменной, text1 - текст если условине - истино, text2 - текст если условие - ложь"])
SM.New('RSE', ['en', 'ru'], ["ERROR 2R: Door syntax error inside '@?'","ERROR 2R: Ошибка синтаксиса door внутри '@?'"])
SM.New('P', ['en', 'ru'], ["Error 0: Some minor problem. I'll try again after some time.","Error 0: Какая-то небольшая проблема. Попробуйье еще раз через какое-то время."])



def RoleCost(role):
  if type(role)==int: return role
  elif role=="lord": return 3
  elif role in ("herceg","high","h"): return 2
  elif role in ("w","way","wanderer","low"):return 1
  else: return 0

def role(uid, rn):
  role=Role(uid)
  if RoleCost(role)>=RoleCost(rn): return True
  else: return False


def clear(uid, list=[]):
  if len(list) == 0:
    ClearNormal(uid)
  else:
    for a in list:
      ClearThis(uid,a)

def key(name, tokey, uid):
    IfTheBox(name,uid)
    if tokey[0] == "=": NewBox(uid,name,int(tokey[1:]))
    elif tokey[0] == "+": AddBox(uid, name,int(tokey[1:]))
    elif tokey[0] == "-": SubBox(uid,name,int(tokey[1:]))
    elif tokey[0] == "*":
      MulBox(uid, name,int(tokey[1:]))
    elif tokey[0] == "/": DivBox(uid,name,int(tokey[1:]))
    elif tokey[0] == "%": ModBox(uid,name,int(tokey[1:]))
    elif tokey[0] == "^": PowBox(uid,name,int(tokey[1:]))

    elif tokey[0] == "?":
      if tokey[1] in  ("+","*","/","%", '^'):
        RR = list(map(int, tokey[2:].split()))
        R1, R2 = RR[0], RR[1]
        if tokey[1]=="+":AddBox(uid,name, random.randint(R1, R2))
        elif tokey[1]=="*":MulBox(uid,name, random.randint(R1, R2))
        elif tokey[1]=="/":DivBox(uid,name, random.randint(R1, R2))
        elif tokey[1]=="%":ModBox(uid,name, random.randint(R1, R2))
        elif tokey[1]=="^":PowBox(uid,name, random.randint(R1, R2))
      else:
        RR = list(map(int, tokey[1:].split()))
        R1, R2 = RR[0], RR[1]
        NewBox(uid,name,random.randint(R1, R2))

    elif tokey[0] == "!" or tokey[0] == "G" or tokey[0] == "M" :
      if tokey[0] == "!": 
         Who=Box(uid, tokey[2:])
      if tokey[0] == "G" or tokey[0] == "M":
        Glist=[]
        for a in Boxs(tokey[2:]):
          Glist.append(int(a[0]))
        if tokey[0] == "G":
          Who=sum(Glist)
        if tokey[0] == "M":
          Who=max(Glist)
      if tokey[1] == "+":AddBox(uid,name,Who)
      elif tokey[1] == "-":SubBox(uid,name,Who)
      elif tokey[1] == "*":MulBox(uid,name,Who)
      elif tokey[1] == "/":DivBox(uid,name,Who)
      elif tokey[1] == "%":ModBox(uid,name,Who)
      elif tokey[1] == "^":PowBox(uid,name,Who)
      else: NewBox(uid,name,Who)
    else:
      NewBox(uid,name,int(tokey))


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
      bkey=Box(uid, key[2:])
      if Box(uid, name) >= int(bkey):
        Behind=True
      else:
        Behind=False

    elif key[1] == "<":
      bkey=Box(uid, key[2:])
      if Box(uid, name) <= int(bkey):
        Behind=True
      else:
        Behind=False
    else:
      bkey=Box(uid, key[1:])
      if Box(uid, name) <= int(bkey):
        Behind=True
      else:
        Behind=False

  else: 
    if key[0] == ">":
      if Box(uid, name) >= int(key[1:]):
        Behind=True
      else:
        Behind=False

    elif key[0] == "<":
      if Box(uid, name) <= int(key[1:]):
        Behind=True
      else:
        Behind=False
    else:
      if Box(uid, name) == int(key):
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
    if ExM == "s": Save(uid)
    if ExM == "l": Load(uid)
    elif ExM in ("lord"):
      if not role(uid, "lord"): maprole = False
    elif ExM in ("h","high","herceg"):
      if not role(uid, "h"): maprole = False
    elif ExM in ("w","low","wanderer"):
       if not role(uid, "w"): maprole = False
  return (cat and maprole)


def say(ad):
  if ad=="":return
  for citizen in Ids():
    bot.send_message(citizen[0],ad.replace("|", "\n"))

def Player(id):
  SM.New('inf', ['en', 'ru'], [Role(id)+" "+ Name(id)+" aka "+Rname(id)+" or agent "+str(id)+" :",Role(id)+" "+ Name(id)+" он же "+Rname(id)+" или же агент "+str(id)+" :"])
  inf=SM.Mess("inf",lang)
  for bk in BoxAndKeys(id):
    inf +=str(bk[0])+" - "+str(bk[1])+" "
  inf += "\n\n"
  return inf


def Inf(id="all", uid = None):
  try:
    messI = "LairWayINF:\n\n"
    if id == "all":
      idlist = Ids()
    elif id == 'players':
      idlist = Ids()
      for ide in idlist:
        Send(uid, Player(ide[0]))
      return  "Lairway BigInf"
    elif str(id)[0]=="@":
      idlist = [[ Who(str(id)[1:])]]

    else:
      idlist = [[id]]
    for ide in idlist:
      messI+=Player(ide[0])
    return messI
  except Exception as err:
    print(err)
    return "Error Lairway Inf"

