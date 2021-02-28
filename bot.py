from telegram.ext import Updater,CallbackContext,CommandHandler
from telegram import Update
from time import time


TOKEN = ""
CHANNEL = 
ALLOWED = []

def kanger(update:Update, context: CallbackContext):
    begin = time()
    message = update.message
    bot = context.bot
    send_content = ""
    is_photo,is_video,is_gif = False, False, False
    if message.from_user.id not in ALLOWED:
        message.reply_text("sorry bro you're not allowed..")
        return
    if not message.reply_to_message:
        message.reply_text("bruh, reply to something you want me to kang.")
        return
    rep_msg = message.reply_to_message
    if rep_msg.photo:
        send_content = rep_msg.photo[-1].file_id
        is_photo = True
    elif rep_msg.video:
        send_content = rep_msg.video.file_id
        is_video = True
    elif rep_msg.animation:
        send_content = rep_msg.animation.file_id
        is_gif = True
    else:
        message.reply_text("no media provided in the message...")
        return
    caption = update.message.text.replace("/kang","")
    text = message.reply_text("downloading your media...")
    if is_gif:
        bot.send_animation(chat_id=CHANNEL,animation=send_content,caption=caption)
    elif is_video:
        bot.send_video(chat_id=CHANNEL,video=send_content,caption=caption)
    elif is_photo:
        bot.send_photo(chat_id=CHANNEL,photo=send_content,caption=caption)
    text.edit_text(f"process finished in {round(time() - begin,2)}s")

if __name__ == "__main__":
    update = Updater(TOKEN,use_context=True)
    dp = update.dispatcher
    dp.add_handler(CommandHandler("kang",kanger))
    print(f"{update.bot.name} has started!")
    update.start_polling()
    update.idle()
