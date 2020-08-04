from telegram.ext import Filters, MessageHandler, CommandHandler, Updater
import os



TOKEN=os.environ.get('BOT_TOKEN',None)

updater=Updater(TOKEN,use_context=True)

START_TEXT = """Hlw I am Forwarded Tag Remover just Forward me Anything"""

HELP_TEXT = """Just Forward Your Message Here and See the Magic 😂"""

def start_text(u,c):
	u.message.reply_text(START_TEXT)
	
def help_text(u,c):
	u.message.reply_text(HELP_TEXT)	
	
	
def frwrd_file(u,c):
	u.message.reply_document(u.message.document.file_id)
	

def frwrd_media(u,c):
	u.message.reply_video(u.message.video.file_id) 

def frwrd_photo(u,c):
	u.message.reply_photo(u.message.photo[-1].file_id) 

def frwrd_text(u,c):
	u.message.reply_text(u.message.text) 


def frwrd_sticker(u,c):
	u.message.reply_sticker(u.message.sticker.file_id) 


def frwrd_voice(u,c):
	u.message.reply_voice(u.message.voice.file_id) 
		
	
dp=updater.dispatcher

#Commands
dp.add_handler(CommandHandler('start',start_text))

#Commands
dp.add_handler(CommandHandler('help',help_text))


dp.add_handler(MessageHandler(Filters.document,frwrd_file))


dp.add_handler(MessageHandler(Filters.video,frwrd_media))

dp.add_handler(MessageHandler(Filters.photo,frwrd_photo))

dp.add_handler(MessageHandler(Filters.text,frwrd_text))

dp.add_handler(MessageHandler(Filters.sticker,frwrd_sticker))

dp.add_handler(MessageHandler(Filters.voice,frwrd_voice))


#Bot Updating + Starting
updater.start_polling()
updater.idle()

