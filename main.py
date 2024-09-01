import telebot
from telebot import types
import time


bot = telebot.TeleBot("7326773284:AAEUcGxC1lR4HnGQc8HNyeFdKgqhyaK-eqw")
ADMIN_ID = '6400925437'
target_user_id = None
kanal="@Samarqand_Kattaqorgon_tuman_IM"

@bot.message_handler(commands=['start'])
def start(message):
    bun = types.InlineKeyboardMarkup(row_width=1)
    bun.add(
        types.InlineKeyboardButton(text="1-kanalga obuna bo'ling", url="https://t.me/Samarqand_Kattaqorgon_tuman_IM"),
        types.InlineKeyboardButton(text="✅Tekshirish", callback_data="|checksub")
    )
    ulanganmi = bot.get_chat_member(kanal, message.from_user.id).status
    print(ulanganmi)
    if message.chat.id == int(ADMIN_ID):
        bot.send_chat_action(ADMIN_ID, 'typing')
        time.sleep(2)
        bot.send_message(ADMIN_ID, "👋")
        bot.send_message(ADMIN_ID, "Assalomu Alaykum Admin hizmatga tayyorman.")
    elif ulanganmi == "member" or ulanganmi == "creator" or ulanganmi == "admin" or ulanganmi == "administrator":


            bot.send_chat_action(message.from_user.id, 'typing')
            time.sleep(2)
            bot.send_message(message.from_user.id, f"Assalomu Alaykum hurmatli {message.from_user.first_name} {message.from_user.last_name}.")
            bot.send_message(message.from_user.id, "Habar yuborishingiz mumkin! \n Javobini shu botdan olasiz.")
    else:
        bot.send_chat_action(message.from_user.id, 'typing')
        time.sleep(2)
        bot.send_message(message.from_user.id, "Assalomu alykum habar yuborish uchun kanalga qo'shiling.", reply_markup=bun)
@bot.callback_query_handler(func=lambda call: call.data.startswith("ID_send_"))
def handle_id_send(call):
    global target_user_id
    target_user_id = int(call.data.split("_")[2])
    bot.send_chat_action(ADMIN_ID, 'typing')
    time.sleep(2)
    bot.send_message(ADMIN_ID,
                     f"Foydalanuvchi ID <code>{target_user_id}</code> saqlandi. Endi barcha xabarlar shu ID ga yuboriladi.",
                     parse_mode="html")
@bot.callback_query_handler(func=lambda call: call.data.startswith("name_"))
def handle_name(call):
    user_id = int(call.data.split("_")[1])
    user = bot.get_chat(user_id)
    first_name = user.first_name
    last_name = user.last_name if user.last_name else "familiya yo'q"
    bot.send_chat_action(ADMIN_ID, 'typing')
    time.sleep(2)
    bot.send_message(ADMIN_ID, f"Foydalanuvchi: {first_name} {last_name}")
@bot.callback_query_handler(func=lambda x:x.data)
def tek(msg:types.Message):
    match msg.data:
        case "|checksub":
                bot.delete_message(msg.message.chat.id, msg.message.id)

                bun=types.InlineKeyboardMarkup(row_width=1)
                bun.add(
                    types.InlineKeyboardButton(text="1-kanalga obuna bo'ling",url="https://t.me/Samarqand_Kattaqorgon_tuman_IM"),
                    types.InlineKeyboardButton(text="✅Tekshirish",callback_data="|checksub")
                )
                ulanganmi=bot.get_chat_member(kanal,msg.from_user.id).status

                if ulanganmi == "member" or ulanganmi=="creator" or ulanganmi=="admin":
                    bot.send_chat_action(msg.from_user.id, 'typing')
                    time.sleep(2)
                    bot.send_message(msg.from_user.id,f"Assalomu alaykum hurmatli {msg.from_user.username}. Siz habaringizni yuborishingiz mumkin.")
                else:
                            bun=types.InlineKeyboardMarkup(row_width=1)
                            bun.add(
                                        types.InlineKeyboardButton(text="1-kanalga obuna bo'ling",url="https://t.me/Samarqand_Kattaqorgon_tuman_IM"),
                                        types.InlineKeyboardButton(text="✅Tekshirish",callback_data="|checksub")
                            )
                            bot.send_chat_action(msg.from_user.id, 'typing')
                            time.sleep(2)
                            bot.send_message(msg.from_user.id,"Kanalga qo'shiling",reply_markup=bun)
        case "y":
            bot.send_chat_action(msg.from_user.id, 'typing')
            time.sleep(2)
            bot.send_message(msg.from_user.id,"Marxamat savolingizni yozing...")
@bot.message_handler(func=lambda message: message.from_user.id != int(ADMIN_ID))
def forward_to_admin(message):
    user_message = message.text
    user_id = message.chat.id
    bot.send_chat_action(ADMIN_ID, 'typing')
    time.sleep(2)

    id_button=types.InlineKeyboardMarkup(row_width=1)
    id_button.add(
        types.InlineKeyboardButton(text="Habar jo'natish💬",callback_data=f"ID_send_{user_id}"),
        types.InlineKeyboardButton(text="F.I.Sh👮",callback_data=f"name_{user_id}"),
    )
    bot.send_message(ADMIN_ID, f"Foydalanuvchidan xabar:\n\n{user_message}\n\n ID: <code>{user_id}</code>",
                     parse_mode="html",reply_markup=id_button)
@bot.message_handler(func=lambda message: message.from_user.id == int(ADMIN_ID) and target_user_id is not None)
def send_message_to_saved_id(message):
    bot.send_chat_action(target_user_id, 'typing')
    time.sleep(1)
    y=bot.send_message(target_user_id, f"{message.text}")
    bot.reply_to(y,"Bu habarni sizga  Samarqand viloyati Kattaqo'rg'on tumani Ixtisoslashtirilgan maktab agenligi tomonidan yuborildi.")
@bot.message_handler(func=lambda message: message.from_user.id == int(ADMIN_ID) and target_user_id is None)
def None_id(message):
    bot.send_chat_action(ADMIN_ID, 'typing')
    time.sleep(2)
    bot.send_message(ADMIN_ID, "Siz habar yuborish uchun ID kiritmadingiz.")











#rasm pasmlar

#admin
@bot.message_handler(content_types=['photo'],func=lambda message: message.from_user.id == int(ADMIN_ID) and target_user_id is not None)
def admin_send_photo(message):
    bot.send_chat_action(target_user_id, 'upload_photo')
    time.sleep(2)
    y=bot.send_photo(target_user_id, message.photo[-1].file_id,caption=message.caption)
    bot.reply_to(y, f"Bu rasm Samarqand viloyati Kattaqo'rg'on tumani Ixtisoslashtirilgan maktab agenligi tomonidan yuborildi.")
@bot.message_handler(content_types=['photo'],func=lambda message: message.from_user.id == int(ADMIN_ID) and target_user_id is None)
def admin_send_photo(message):
    bot.send_chat_action(ADMIN_ID, 'typing')
    bot.reply_to(message, f"Siz bu rasmni yuborish uchun ID kiritmadingiz")

@bot.message_handler(content_types=['video'],func=lambda message: message.from_user.id == int(ADMIN_ID) and target_user_id is not None)
def admin_send_video(message):
    bot.send_chat_action(target_user_id, 'upload_video')
    time.sleep(2)
    y=bot.send_video(target_user_id,message.video.file_id,caption=message.caption)
    bot.reply_to(y,f"Bu videoni Samarqand viloyati Kattaqo'rg'on tumani Ixtisoslashtirilgan maktab agenligi tomonidan yuborildi.")
@bot.message_handler(content_types=['video'],func=lambda message: message.from_user.id == int(ADMIN_ID) and target_user_id is None)
def admin_send_photo(message):
    bot.send_chat_action(ADMIN_ID, 'typing')
    bot.reply_to(message, f"Siz bu videoni yuborish uchun ID kiritmadingiz")
@bot.message_handler(content_types=['document'],func=lambda message: message.from_user.id == int(ADMIN_ID) and target_user_id is not None)
def admin_send_document(message):
    bot.send_chat_action(target_user_id, 'upload_document')
    time.sleep(2)
    y=bot.send_document(target_user_id,message.document.file_id,caption=message.caption)
    bot.reply_to(y,f"Bu hujjatni Samarqand viloyati Kattaqo'rg'on tumani Ixtisoslashtirilgan maktab agenligi tomonidan yuborildi.")
@bot.message_handler(content_types=['document'],func=lambda message: message.from_user.id == int(ADMIN_ID) and target_user_id is None)
def admin_send_photo(message):
    bot.send_chat_action(ADMIN_ID, 'typing')
    bot.reply_to(message, f"Siz bu hujjatni yuborish uchun ID kiritmadingiz")
#user
@bot.message_handler(content_types=['photo'],func=lambda message: message.from_user.id != int(ADMIN_ID))
def user_send_photo(message):
    bot.send_chat_action(ADMIN_ID, 'upload_photo')
    time.sleep(2)
    bot.send_photo(ADMIN_ID, message.photo[-1].file_id,caption=message.caption)

    user_message = message.text
    user_id = message.chat.id
    bot.send_chat_action(ADMIN_ID, 'typing')
    time.sleep(2)

    id_button = types.InlineKeyboardMarkup(row_width=1)
    id_button.add(
        types.InlineKeyboardButton(text="Habar jo'natish💬", callback_data=f"ID_send_{user_id}"),
        types.InlineKeyboardButton(text="F.I.Sh👮", callback_data=f"name_{user_id}"),
    )
    bot.send_message(ADMIN_ID, f"Foydalanuvchidan rasm", reply_markup=id_button)
@bot.message_handler(content_types=['video'],func=lambda message: message.from_user.id != int(ADMIN_ID))
def user_send_video(message):
    user_message = message.text
    user_id = message.chat.id
    bot.send_chat_action(ADMIN_ID, 'upload_video')
    time.sleep(2)
    bot.send_video(ADMIN_ID,message.video.file_id,caption=message.caption)
    id_button = types.InlineKeyboardMarkup(row_width=1)
    id_button.add(
        types.InlineKeyboardButton(text="Habar jo'natish💬", callback_data=f"ID_send_{user_id}"),
        types.InlineKeyboardButton(text="F.I.Sh👮", callback_data=f"name_{user_id}"),
    )
    bot.send_message(ADMIN_ID, f"Foydalanuvchidan video", reply_markup=id_button)
@bot.message_handler(content_types=['document'],func=lambda message: message.from_user.id != int(ADMIN_ID))
def user_send_document(message):
    user_message = message.text
    user_id = message.chat.id
    bot.send_chat_action(ADMIN_ID, 'upload_document')
    time.sleep(2)
    bot.send_document(ADMIN_ID,message.document.file_id,caption=message.caption)
    id_button = types.InlineKeyboardMarkup(row_width=1)
    id_button.add(
        types.InlineKeyboardButton(text="Habar jo'natish💬", callback_data=f"ID_send_{user_id}"),
        types.InlineKeyboardButton(text="F.I.Sh👮", callback_data=f"name_{user_id}"),
    )
    bot.send_message(ADMIN_ID, f"Foydalanuvchidan document", reply_markup=id_button)
bot.polling()