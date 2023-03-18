from telegram.ext import *
from io import BytesIO
import cv2
import numpy as np
import tensorflow as tf

TOKEN = '6214291680:AAFku6T9b4wOZ_uOsxA-N9RgrqSPGpMbqZI'

Model_Path = 'HindiModel1.h5'
model = tf.keras.models.load_model(Model_Path, custom_objects={'tf': tf})

def start(update, context):
    update.message.reply_text("Welcome!")

def help(update,context):
    update.message.reply_text('''
    /start - Start Conversation
    /help - Shows this message
    /send - Send photos
    ''')

def handle_message(update,context):
    update.message.reply_text("Send a Picture of a character! ")

def handle_message(update,context):
    update.message.reply_text("You can now send a photo! ")

def solve(prediction):
    output = np.argmax(prediction, axis=1)
    if output == 0:
        print("character is ञ")
    elif output == 1:
        print("character is ट")
    elif output == 2:
        print("character is ठ")
    elif output == 3:
        print("character is ड")
    elif output == 4:
        print("character is ढ")
    elif output == 5:
        print("character is ण")
    elif output == 6:
        print("character is त")
    elif output == 7:
        print("character is थ")
    elif output == 8:
        print("character is द")
    elif output == 9:
        print("character is ध")
    elif output == 10:
        print("character is क")
    elif output == 11:
        print("character is न")
    elif output == 12:
        print("character is प")
    elif output == 13:
        print("character is फ")
    elif output == 14:
        print("character is ब")
    elif output == 15:
        print("character is भ")
    elif output == 16:
        print("character is म")
    elif output == 17:
        print("character is य")
    elif output == 18:
        print("character is र")
    elif output == 19:
        print("character is ल")
    elif output == 20:
        print("character is व")
    elif output == 21:
        print("character is ख")
    elif output == 22:
        print("character is श")
    elif output == 23:
        print("character is ष")
    elif output == 24:
        print("character is स")
    elif output == 25:
        print("character is ह")
    elif output == 26:
        print("character is क्ष")
    elif output == 27:
        print("character is त्र")
    elif output == 28:
        print("character is ज्ञ")
    elif output == 29:
        print("character is ग")
    elif output == 30:
        print("character is घ")
    elif output == 31:
        print("character is ङ")
    elif output == 32:
        print("character is च")
    elif output == 33:
        print("character is छ")
    elif output == 34:
        print("character is ज")
    elif output == 35:
        print("character is झ")
    elif output == 36:
        print("character is ०")
    elif output == 37:
        print("character is १")
    elif output == 38:
        print("character is २")
    elif output == 39:
        print("character is ३")
    elif output == 40:
        print("character is ४")
    elif output == 41:
        print("character is ५")
    elif output == 42:
        print("character is ६")
    elif output == 43:
        print("character is ७")
    elif output == 44:
        print("character is ८")
    elif output == 45:
        print("character is ९")
    return output

def handle_photo(update,context):
    file = context.bot.get_file(update.message.photo[-1].file_id)
    f=BytesIO(file.download_as_bytearray())
    file_bytes =  np.asarray(bytearray(f.read()), dtype=np.uint8)

    img = cv2.imdecode(file_bytes,cv2.IMREAD_COLOR)
    img = cv2.cvtColor(img,cv2.COLOR_RGB2BGR)
    img = cv2.resize(img,(32,32), interpolation = cv2.INTER_AREA)

    prediction = model.predict(np.array([img/255]))
    update.message.reply_text(f"In this image {solve(prediction)}")


updater = Updater(TOKEN, update_queue=None)
dp=Updater.dispatcher

dp.add_handler(CommandHandler("start",start))
dp.add_handler(CommandHandler("help",help))
dp.add_handler(MessageHandler(Filters.text,handle_message))
dp.add_handler(MessageHandler(Filters.photo,handle_photo))

updater.start_polling()
updater.idle()

