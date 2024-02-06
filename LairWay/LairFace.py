import telebot
import os

token =  os.environ['token']
bot = telebot.TeleBot(token) 

LairFaceV="TG1"
biglim=4096
btlim=64

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
SM=Mess()

def Send(uid,str,kb=None): bot.send_message(uid, text=str, reply_markup=kb)
def Kill(cid,mid): bot.delete_message(cid,mid)
def Edit(cid,mid,text,kb=None):bot.edit_message_text(chat_id=cid, message_id=mid, text=text,reply_markup=kb)
def Foto(uid,l,text=None): return bot.send_photo(uid, l, caption=text )
def Doc(uid,l,text=None): return bot.send_document(uid, l, caption=text)

def Keyboard(width=2): return telebot.types.InlineKeyboardMarkup(row_width=width)
def NewBt(kb,text,way): kb.add(telebot.types.InlineKeyboardButton(text=text,callback_data=way))

def Uid(message): return message.from_user.id 
def Mtx(message): return message.text
def Mid(message): 
  try: return message.message.id
  except: return message.message_id
