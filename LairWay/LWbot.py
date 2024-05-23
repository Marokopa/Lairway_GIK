from LairWay.LWjson import *
import telebot


bot = telebot.TeleBot(FindBotToken())

biglim=4096
btlim=64



def Send(uid:str,text:str,kb: telebot.types.ReplyKeyboardMarkup =None) -> telebot.types.Message: return bot.send_message(uid, text=text, reply_markup=kb)
def Kill(cid: int,mid: int): bot.delete_message(cid,mid)
def Edit(cid: int,mid: int,text: str,kb=None):bot.edit_message_text(chat_id=cid, message_id=mid, text=text,reply_markup=kb)
  
def Foto(uid: int,File,text: str = None): return bot.send_photo(uid, File, caption=text )
def Doc(uid: int,File,text: str = None): return bot.send_document(uid, File, caption=text)
def Aud(uid: int,File,text: str = None): return bot.send_audio(uid, File, caption=text)
def Vid(uid: int,File,text: str = None): return bot.send_video(uid, File, caption=text)
def Vc(uid: int,File,text: str = None): return bot.send_voice(uid, File, caption=text)
def Stk(uid: int, stiker_id: str): return bot.send_sticker(uid, stiker_id)


def Keyboard(width=2) -> telebot.types.InlineKeyboardMarkup: return telebot.types.InlineKeyboardMarkup(row_width=width)
def NewBt(kb: telebot.types.InlineKeyboardMarkup, text: str, way: str): kb.add(telebot.types.InlineKeyboardButton(text=text,callback_data=way))

def Uid(message: telebot.types.Message) -> int: return message.from_user.id 
def CUid(call: telebot.types.CallbackQuery) -> int: return call.from_user.id
def CallBack(call: telebot.types.CallbackQuery) -> str: return call.data
def StkIdBack(message: telebot.types.Message) -> str: return message.sticker.file_id
def Mtx(message: telebot.types.Message) -> str: '''return message text'''; return message.text
def Mid(message: telebot.types.Message) -> int: 
  '''return message id.'''
  try: return message.message.id
  except: return message.message_id

def StopLairWay():
   print("LWbot stop.")
   bot.stop_bot()

def StartLairWay(): 
   print("LWbot start.")
   bot.polling()
   

