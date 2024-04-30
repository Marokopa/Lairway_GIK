import sqlite3



conn = sqlite3.connect('data/LW.db', check_same_thread=False)
cur = conn.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS box (id, box, key, skey, mod, type )''')
cur.execute('''CREATE TABLE IF NOT EXISTS UsInf (id, name, rname, role, Blockid, fotoid )''')


def CloseSql():
  conn.close()


def IfInUsInf(uid: int, message):
  if (uid,) in cur.execute("SELECT id FROM UsInf").fetchall(): return
  cur.execute("INSERT OR IGNORE INTO UsInf VALUES (?, ?, ?,  'commoner', 0,'')", (uid, message.from_user.username,str(message.chat.first_name) + " " + str(message.chat.last_name)));conn.commit()

def IfInBox(name, uid):
  if (uid, name) in cur.execute("SELECT id,box FROM box").fetchall(): return
  if name[0]=="@": cur.execute("INSERT OR IGNORE INTO box VALUES (?, ?, 0, 'NO','etr', '')", (uid,name));conn.commit()
  elif name[0]=="%": cur.execute("INSERT OR IGNORE INTO box VALUES (?, ?, 0, '0','fly', '')", (uid,name));conn.commit()
  else:cur.execute("INSERT OR IGNORE INTO box VALUES (?, ?, 0, 0,'nor','')", (uid,name));conn.commit()

def ClearSQL(mod, who='',box=""):
  '''
  MOD == all -> clear UsInf+BOX
  MOD == box -> clear BOX
  MOD == UsInf -> clear UsInf
  MOD == box -> clear all (box) in BOX
  MOD == user => clear who's (box) in BOX, if box==0 -> clear who's BOX
  MOD == uid => clear BOX by id
  '''
  try:
    if mod == "all":
      cur.execute("DELETE FROM box");conn.commit()
      cur.execute("DELETE FROM UsInf");conn.commit()
    elif mod == 'user':
      if box=="": cur.execute("DELETE FROM box WHERE id = ?", (Who(who),)); cur.execute("DELETE FROM UsInf WHERE id = ?", (Who(who),))
      else: cur.execute("DELETE FROM box WHERE (id,box) = (?,?)", (Who(who),box))
      conn.commit()
    elif mod == "box":
      cur.execute("DELETE FROM box WHERE box = ?", (box,)); conn.commit()
    elif mod == 'id':
      cur.execute("DELETE FROM box WHERE id = ?", (who,)); conn.commit()
    return True
  except Exception as e:
    print(e)
    return False

def NewFotoId(uid: int): cur.execute("UPDATE UsInf SET fotoid = '' WHERE id = ?", (uid, )); conn.commit()
def BlockId(uid: int): return cur.execute("SELECT Blockid FROM UsInf WHERE (id) = (?)",(uid, )).fetchall()[0][0]
def FotoId(uid: int): return cur.execute("SELECT fotoid FROM UsInf WHERE (id) = (?)",(uid, )).fetchall()[0][0]
def AddFotoId(uid: int ,foto): cur.execute("UPDATE UsInf SET fotoid = ? WHERE id = ?", (cur.execute("SELECT fotoid FROM UsInf WHERE (id) = (?)",(uid, )).fetchall()[0][0] + '@' + str(foto.id),uid,))
def BlockIdIs(fbi,uid: int): cur.execute("UPDATE UsInf SET Blockid = ? WHERE (id) = (?)",(fbi,uid,))


def WithRole(role: str) -> list[tuple[str]]: return cur.execute("SELECT name FROM UsInf WHERE role = ?", (role,)).fetchall()
def Ids() -> list[tuple[int]]:'''returns the ids of all Lauway users'''; return cur.execute("SELECT id FROM UsInf").fetchall()
def BoxAndKeys(uid: int) -> list[tuple[str,int]]: '''returns all variables of a given user and their values'''; return cur.execute("SELECT box, key FROM box WHERE id = ?", (uid, )).fetchall()

def Save(uid: int):'''Remembers all variables of a given user at a given time'''; cur.execute("UPDATE box SET skey = key WHERE (mod,id) IN (('nor',?), ('fly',?))", (uid, uid )); conn.commit()
def Load(uid: int):'''Loads the last filled value into variables'''; cur.execute("UPDATE box SET key = skey WHERE (mod,id) IN (('nor',?), ('fly',?))", (uid,uid )); conn.commit()
  


def ClearNormal(uid: int): '''Clears the value of all standard and fly variables''';cur.execute("UPDATE box SET key = 0, skey = 0 WHERE (mod,id) = ('nor', ?) OR (mod,id) = ('fly', ?)", (uid,uid))
def ClearThis(uid: int,this: str): 
  '''clears the given variable'''
  cur.execute("UPDATE box SET key = 0, skey = 0 WHERE (mod,box,id) = ('',?, ?)",(this,uid,))
  cur.execute("UPDATE box SET key = 0 WHERE (mod,box, id) = ('etr',?,?)", (this,uid,))
def RoleClear():'''Sets the roles of all users to commoner'''; cur.execute("UPDATE UsInf SET role = 'commoner' ")
def KillFlies(uid: int): '''Decreases the value of key by 1 if it is greater than 0'''; cur.execute("UPDATE box SET key = CASE WHEN key > 0 THEN key - 1 ELSE 0 END WHERE (mod,id) = ('fly', ?)", (uid,))



def NewRole(role: str, name: str): '''changes the user's role (by name)''';cur.execute("UPDATE UsInf SET role = ? WHERE (name) = (?)",(role, name))
def Who(name: str) -> int: '''takes the username as input and returns the user ID''';return cur.execute("SELECT id FROM UsInf WHERE (name) = (?)",(name,)).fetchall()[0][0]

def Name(uid: int) -> str: '''return name of user. ex: "nick_in_telegram"'''; return cur.execute("SELECT name FROM UsInf WHERE (id) = (?)",(uid,)).fetchall()[0][0]
def Role(uid: int) -> str: '''return role of user. ex: "lord"''';return cur.execute("SELECT role FROM UsInf WHERE (id) = (?)",(uid,)).fetchall()[0][0]
def Rname(uid: int) -> str: '''return Real_Name of user. ex: "Akakiy Akakivich"''';return cur.execute("SELECT rname FROM UsInf WHERE (id) = (?)",(uid, )).fetchall()[0][0] 


def Type(uid:int,boxname: str) -> str: '''Return the Type of box'''; return cur.execute("SELECT type FROM box WHERE (id, box) = (?, ?)",(uid, boxname)).fetchall()[0][0]
def Box(uid: int,boxname:str)-> int: '''Return value of box.'''; return cur.execute("SELECT key FROM box WHERE (id, box) = (?, ?)",(uid, boxname)).fetchall()[0][0]
def Boxs(box:str) -> list[tuple[int]]: return cur.execute("SELECT key FROM box WHERE box = (?)",(box,)).fetchall()
  
def NewBox(uid: int, box: str ,key: int ): '''box = key'''; cur.execute("UPDATE box SET key = ? WHERE (id,box) = (?,?)",(key,uid,box)); conn.commit()
def AddBox(uid: int, box: str ,key: int ): '''box = box+key''';  cur.execute("UPDATE box SET key = key+? WHERE (id,box) = (?,?)",(key,uid,box))
def SubBox(uid: int, box: str ,key: int ): '''box = box-key''';  cur.execute("UPDATE box SET key = key-? WHERE (id,box) = (?,?)",(key,uid,box))
def RSubBox(uid: int, box:str, key: int): '''box = key-box''';  cur.execute("UPDATE box SET key = ?-key WHERE (id,box) = (?,?)",(key,uid,box))
def MulBox(uid: int, box: str ,key: int ): '''box = box*key''';cur.execute("UPDATE box SET key = ?*key WHERE (id,box) = (?,?)",(key,uid,box))
def PowBox(uid: int, box: str ,key: int ): '''box = box**key''';cur.execute("UPDATE box SET key = ? WHERE (id,box) = (?,?)",(Box(uid,box)**key,uid,box))
def RPowBox(uid: int, box: str ,key: int ): '''box = key**box''';cur.execute("UPDATE box SET key = ? WHERE (id,box) = (?,?)",(key**Box(uid,box),uid,box))
def DivBox(uid: int, box: str ,key: int ):'''box = box//key'''; cur.execute("UPDATE box SET key = key/? WHERE (id,box) = (?,?)",(key,uid,box)); NulltoZero()
def RDivBox(uid: int, box: str ,key: int ):'''box = key//box'''; cur.execute("UPDATE box SET key = ?/key WHERE (id,box) = (?,?)",(key,uid,box),uid,box); NulltoZero()
def ModBox(uid: int, box: str ,key: int ): '''box = box%key'''; cur.execute("UPDATE box SET key = key%? WHERE (id,box) = (?,?)",(key,uid,box)); NulltoZero()
def RModBox(uid: int, box: str ,key: int ): '''box = key%box'''; cur.execute("UPDATE box SET key = ?%key WHERE (id,box) = (?,?)",(key,uid,box)); NulltoZero()


def AddType(uid: int,box:str, btype: "str"): cur.execute("UPDATE box SET type = ? WHERE (id, box) = (?, ?)", (btype, uid, box)); conn.commit()

def NewToType(uid: int, btype: str ,key: int ): '''for type: box = key'''; cur.execute("UPDATE type SET key = ? WHERE (id,box) = (?,type)",(key,uid, btype)); conn.commit()
def AddToType(uid: int, btype: str ,key: int ): '''for type:box = box+key''';  cur.execute("UPDATE box SET key = key+? WHERE (id,type) = (?,?)",(key,uid,btype)); conn.commit()
def SubToType(uid: int, btype: str ,key: int ): '''for type:box = box-key''';  cur.execute("UPDATE box SET key = key-? WHERE (id,type) = (?,?)",(key,uid,btype)); conn.commit()
def RSubToType(uid: int, btype: str ,key: int ): '''for type:box = key-box''';  cur.execute("UPDATE box SET key = ?-key WHERE (id,type) = (?,?)",(key,uid,btype)); conn.commit()
def MulToType(uid: int, btype: str ,key: int ): '''for type:box = box*key''';  cur.execute("UPDATE box SET key = key*? WHERE (id,type) = (?,?)",(key,uid,btype)); conn.commit()
def DivToType(uid: int, btype: str ,key: int ):'''for type:box = box//key''';cur.execute("UPDATE box SET key = key/? WHERE (id,type) = (?,?)",(key,uid,btype)); NulltoZero()
def RDivToType(uid: int, btype: str ,key: int ):'''for type:box = key//box'''; cur.execute("UPDATE box SET key = ?/key WHERE (id,type) = (?,?)",(key,uid,btype)); NulltoZero()
def ModToType(uid: int, btype: str ,key: int ): '''for type:box = box%key'''; cur.execute("UPDATE box SET key = key%? WHERE (id,type) = (?,?)",(key,uid,btype)); NulltoZero()
def RModToType(uid: int, btype: str ,key: int ): '''for type:box = key%box''' ;cur.execute("UPDATE box SET key = ?%key WHERE (id,type) = (?,?)",(key,uid,btype)); NulltoZero()

def NulltoZero():cur.execute("UPDATE box SET key = 0 WHERE key IS NULL");conn.commit()
