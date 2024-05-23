from LairWay.LWsql import *
from LairWay.LWbot import *
from LairWay.LWsm import *
import random


lang="en"

text = {}
bttn = {}
img = {}
maps={}
spell={}

def RLW(text,uid):
  text = text.replace("|", "\n")
  if text.startswith("@"):
    parts = text[1:].split("@")
    part = ""
    for k in parts:
      if k=="": continue
      elif k[0] == "!":
        part += str(Box(uid, k[1:]))
      elif k[0] == "$":
        part += str(Type(uid, k[1:]))
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
      elif k in ("S1","s1"): part+="~"
      elif k in ("S2","s2"):part+="|"
      elif k[0] in ("S3","s3"):part+="@"
      elif k[0]=="#":
        record=k[1:].split("//")
        for tname in Ids():
         if door(tname[0],record[0],record[1]):
           part+=str(Name(uid))+" "
      elif k[0]=="*":
        Fpart=k[1:].split("/*/")
        part+=str(globals()["F_"+Fpart[0]](uid,*tuple(Fpart[1:])))
      else:
        part += k
    text=part

  return text

def RoleCost(role: str) -> int:
  '''the function takes on a Required_Role and returns its value as an int. \n
  "lord"/"l" = 3 ; "herceg", "h" = 2 ; "wanderer", "w" = 1; other - 0\n'''
  if type(role)==int: return role
  elif role=="lord": return 3
  elif role in ("herceg","high","h"): return 2
  elif role in ("w","way","wanderer","low"):return 1
  else: return 0

def Required_Role(uid: int, rn: str) -> bool:
  '''The function checks the user's Required_Role relative to the required one and if his Required_Role is required or higher, then it returns True, otherwise False\n'''
  role=Role(uid)
  if RoleCost(role)>=RoleCost(rn): return True
  else: return False


def clear(uid:int, list: list=[]): 
  '''If the list is empty, then all normal variables are cleared, otherwise the variables in the list are cleared.'''
  if len(list) == 0:
    ClearNormal(uid)
  else:
    for a in list:
      ClearThis(uid,a)

key_commands = ("=", "+", "-", "d" , "*", "/", "\\", "^", "v")

def key(name: str, tokey: str, uid: int, IfType=False):
    '''Key changes the variable according to CCИП\n 
    name -) name of var in lairway. ('foo')\n
    tokey -) how  variable change requirement ('+5')'''
    if not IfType:IfInBox(name,uid)
    Who, sigh = 0, ""

    if tokey[0] in  ("!", "G", "M", "m"):
      if tokey[1] in key_commands:
        sigh = tokey[1]
        Who = tokey[2:]
      else:
        sigh = ''
        Who = tokey[1:]
      if tokey[0] == "!":
        Who = Box(uid, Who)
      else:
        Glist=[]
        for a in Boxs(Who):
          Glist.append(int(a[0]))
        if tokey[0] == "G": Who=sum(Glist)
        elif tokey[0] == "M":Who=max(Glist)
        elif tokey[0] == "m": Who=min(Glist)


    elif tokey[0] == "?":
      if tokey[1] in key_commands and tokey[1]!="-":
        RR = list(map(int, tokey[2:].split()))
        sigh = tokey[1]
      else:
        sigh = ''
        RR = list(map(int, tokey[1:].split()))
      R1, R2 = RR[0], RR[1]
      Who = random.randint(R1, R2)

    else:
      if tokey[0] in key_commands:
        sigh = tokey[0]
        Who = int(tokey[1:])
      else:
        sigh= ''
        Who = int(tokey)
    if IfType:
      if sigh in ("", "="): NewToType(uid, name, Who)
      elif sigh == "+": AddToType(uid, name, Who)
      elif sigh == "-": SubToType(uid, name, Who)
      elif sigh == "d": RSubToType(uid, name, Who)
      elif sigh == "*": MulToType(uid, name, Who)
      elif sigh == "/": DivToType(uid, name, Who)
      elif sigh == "\\": RDivToType(uid, name, Who)
      elif sigh == "%": ModToType(uid, name, Who)
      elif sigh == "|": RModToType(uid, name, Who)
    else:
      if sigh in ("", "="): NewBox(uid, name, Who)
      elif sigh == "+": AddBox(uid, name, Who)
      elif sigh == "-": SubBox(uid, name, Who)
      elif sigh == "d": RSubBox(uid, name, Who)
      elif sigh == "*": MulBox(uid, name, Who)
      elif sigh == "/": DivBox(uid, name, Who)
      elif sigh == "\\": RDivBox(uid, name, Who)
      elif sigh == "%": ModBox(uid, name, Who)
      elif sigh == "|": RModBox(uid, name, Who)
      elif sigh == "^": PowBox(uid, name, Who)
      elif sigh == "v": RPowBox(uid, name, Who)



def door(uid: int, name: str, key: str ="1")-> bool:
  '''Checks a variable conditionally according to СССП \n
  name -) name of var in lairway. ('foo')\n
  key -) condition (">5")'''
  IfInBox(name,uid)
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
      if Box(uid, name) >= int(bkey):Behind=True
      else:Behind=False

    elif key[1] == "<":
      bkey=Box(uid, key[2:])
      if Box(uid, name) <= int(bkey):Behind=True
      else:Behind=False

    elif key[0] == "%":
      bkey=Box(uid, key[2:])
      if Box(uid,name)%int(bkey)==0:Behind=True
      else:Behind=False

    elif key[0] == "|":
      bkey=Box(uid, key[2:])
      if int(bkey)%Box(uid,name)==0:Behind=True
      else:Behind=False
      
    else:
      bkey=Box(uid, key[1:])
      if Box(uid, name) == int(bkey):Behind=True
      else:Behind=False

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

    elif key[0] == "%":
      try:
        if Box(uid,name)%int(key[1:])==0:
          Behind=True
        else:
          Behind=False
      except:
        Behind = False

    elif key[0] == "|":
      try:
        if int(key[1:])%Box(uid,name)==0:
          Behind=True
        else:
          Behind=False
      except:
        Behind = False
        
    else:
      if Box(uid, name) == int(key):
        Behind=True
      else:
        Behind=False
  if rev:
    return not Behind
  else:
    return Behind

def fmap(uid: int, name: str="",mway: list = []) -> bool:
  '''This function is a complex condition. You can call either a map by *name* and then its complex condition will be checked, or you can enter your own in the form of a list in *mway*.'''
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
      if not Required_Role(uid, "lord"): maprole = False
    elif ExM in ("h","high","herceg"):
      if not Required_Role(uid, "h"): maprole = False
    elif ExM in ("w","low","wanderer"):
       if not Required_Role(uid, "w"): maprole = False
  return (cat and maprole)


def say(ad:str):
  '''writes a message to each Lairway user'''
  if ad=="":return
  for citizen in Ids():
    Send(citizen[0],ad.replace("|", "\n"))

def Player(id: int) -> str:
  '''return inf about user in lairway in format'''
  SM.New('inf', ['en', 'ru'], [Role(id)+" "+ Name(id)+" aka "+Rname(id)+" or agent "+str(id)+" : ",Role(id)+" "+ Name(id)+" он же "+Rname(id)+" или же агент "+str(id)+" : "])
  inf=SM.Mess("inf",lang)
  for bk in BoxAndKeys(id):
    inf +=str(bk[0])+" - "+str(bk[1])+" "
  inf += "\n\n"
  return inf


def Inf(id: str = "all", uid: int = None) -> str:
  '''Returns information in Lairway Inf format \n
  id = all -) inf about all lairway users
  id = big / players -) send users with specified uid inf about each lairway user, for each in its own message and then returns "Lairway BigInf"
  id = @... -) returns information about the user whose name is specified after @ (ex: "@my_telegram_nick") 
  id = ... -)  returns information about the user whose id is specified. (ex: "12345678") 
  ''' 
  try:
    messI = "LairWayINF:\n\n"
    if id == "all":
      idlist = Ids()
    elif id in ('players','big'):
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

def File(uid,typ,the_file,text=None):
  if typ=="img": return Foto(uid, the_file, text=text)
  elif typ=="doc": return Doc(uid,the_file, text=text)
  elif typ=="vid": return Vid(uid,the_file, text=text)
  elif typ=="aud": return Aud(uid,the_file, text=text)
  elif typ=="vc": return Vc(uid,the_file, text=text)
  elif typ=="stk": return Stk(uid,the_file)