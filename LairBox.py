import sqlite3

LairBoxV="SQL-0.1"


conn = sqlite3.connect('LW.db', check_same_thread=False)
cur = conn.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS box (id, box, key, skey, mod )''')
cur.execute('''CREATE TABLE IF NOT EXISTS UsInf (id, name, rname, role, Blockid, fotoid )''')



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

def NewFotoId(uid) : cur.execute("UPDATE UsInf SET fotoid = '' WHERE id = ?", (uid, )); conn.commit()
def BlockId(uid): return cur.execute("SELECT Blockid FROM UsInf WHERE (id) = (?)",(uid, )).fetchall()[0][0]
def FotoId(uid): return cur.execute("SELECT fotoid FROM UsInf WHERE (id) = (?)",(uid, )).fetchall()[0][0]
def AddFotoId(uid): cur.execute("UPDATE UsInf SET fotoid = ? WHERE id = ?", 
                                (cur.execute("SELECT fotoid FROM UsInf WHERE (id) = (?)",(uid, )).fetchall()[0][0] + '@' + str(foto.id),uid,))
def BlockIdIs(fbi,uid): cur.execute("UPDATE UsInf SET Blockid = ? WHERE (id) = (?)",(fbi,uid,))


def Ids():return cur.execute("SELECT id FROM UsInf").fetchall()
def BoxAndKeys(uid): return cur.execute("SELECT box, key FROM box WHERE id = ?", (uid, )).fetchall()


def Save(uid): cur.execute("UPDATE box SET skey = key WHERE (mod,id) = ('',?)", (uid, ))
def Load(uid): cur.execute("UPDATE box SET key = skey WHERE (mod,id) = ('',?)", (uid, ))
  

def ClearNormal(uid): cur.execute("UPDATE box SET key = 0, skey = 0 WHERE (mod,id) = ('',?)",(uid, ))
def ClearThis(uid,this):
  cur.execute("UPDATE box SET key = 0, skey = 0 WHERE (mod,box,id) = ('',?, ?)",(this,uid,))
  cur.execute("UPDATE box SET key = 0 WHERE (mod,box, id) = ('@', ?,?)", (this,uid,))
def RoleClear(): cur.execute("UPDATE UsInf SET role = 'commoner' ")

def NewRole(role,name): cur.execute("UPDATE UsInf SET role = ? WHERE (name) = (?)",(role, name))
def Who(name): return cur.execute("SELECT id FROM UsInf WHERE (name) = (?)",(name,)).fetchall()[0][0]

def Box(uid,boxname): return cur.execute("SELECT key FROM box WHERE (id, box) = (?, ?)",(uid, boxname)).fetchall()[0][0]
def Name(uid): return cur.execute("SELECT name FROM UsInf WHERE (id) = (?)",(uid,)).fetchall()[0][0]
def Role(uid): return cur.execute("SELECT role FROM UsInf WHERE (id) = (?)",(uid,)).fetchall()[0][0]
def Rname(uid): return cur.execute("SELECT rname FROM UsInf WHERE (id) = (?)",(uid, )).fetchall()[0][0] 

def Boxs(box): cur.execute("SELECT key FROM box WHERE box = (?)",(box)).fetchall()
def NewBox(uid,box,key): cur.execute("UPDATE box SET key = ? WHERE (id,box) = (?,?)",(key,uid,box))
def AddBox(uid, box, key):  cur.execute("UPDATE box SET key = key+? WHERE (id,box) = (?,?)",(key,uid,box))
def SubBox(uid, box, key):  cur.execute("UPDATE box SET key = key-? WHERE (id,box) = (?,?)",(key,uid,box))

