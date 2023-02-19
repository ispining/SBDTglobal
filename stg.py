import config
import customers
from config import sql, db, database, send, kmarkup, btn,  staff, stages, bot, lang, get_text, back
import texts

our = config.SBDT()
panel = customers.CustomerPanel()

def set_lang(chat_id, home_back_btn=True):
    k = kmarkup()
    msg = texts.set_lang
    k.row(btn("Русский", callback_data=f"set_lang||ru"))
    k.row(btn("English", callback_data=f"set_lang||en"))
    k.row(btn("עברית", callback_data=f"set_lang||he"))
    #k.row(btn("عرب", callback_data=f"set_lang||ar"))
    if home_back_btn:
        k.row(back(chat_id, "home"))
    send(chat_id, msg, reply_markup=k)

def start_message(chat_id):
    k = kmarkup()
    msg = get_text(chat_id, "start_message")
    k.row(btn(get_text(chat_id, "client_panel_btn"), callback_data=f"client_panel"))
    k.row(btn(get_text(chat_id, "student_panel_btn"), callback_data=f"student_panel"))
    k.row(btn(get_text(chat_id, "our_products_btn"), callback_data=f"our_products"),
          btn(get_text(chat_id, "i_need_specialist_btn"), callback_data=f"i_need_specialist"))
    k.row(btn(get_text(chat_id, "prog_lessons_btn"), callback_data=f"prog_lessons"))
    k.row(btn(get_text(chat_id, "contact_us_btn"), callback_data=f"contact_us"),
          btn(get_text(chat_id, "set_langs_btn"), callback_data=f"set_langs"))
    msg_photo = config.settings("main_photo")
    if msg_photo in [None, "None"]:
        send(chat_id, msg, reply_markup=k)
    else:
        bot.send_photo(chat_id=chat_id, photo=msg_photo, caption=msg, reply_markup=k)

def our_products_btn(chat_id):
    k = kmarkup()
    msg = get_text(chat_id, "our_products_msg")
    lng = lang(chat_id)

    for category in config.ProdCat().get():
        btn_name = category[lng + '_content'].split("||")[0]
        k.row(btn(btn_name, callback_data=f"select_prodcat||{str(category['cat_id'])}"))
    k.row(back(chat_id, "home"))
    send(chat_id, msg, reply_markup=k)

def client_panel(call):
    chat_id = call.message.chat.id
    if config.user_idToPhone(chat_id) in customers.client356AccessPoint:
        panel.Client356().panel(chat_id)
        try:
            bot.delete_message(chat_id, call.message.message_id)
        except:
            pass
    else:
        bot.answer_callback_query(call.id, get_text(chat_id, "not_allowed_to_CP_msg"), show_alert=True)

def my_customers(chat_id):
    if config.user_idToPhone(chat_id) in customers.client356AccessPoint:
        panel.Client356().customers(chat_id)
        stages(chat_id, "None")

def client356_search(chat_id, by=None):
    if by == None:
        panel.Client356().search(chat_id)

    else:
        panel.Client356().search_by(chat_id, by.lower())

def client356_add_one_by_one(chat_id):
    panel.Client356().new_client(chat_id)

def client356_add_users_from_csv(chat_id):
    panel.Client356().add_users_from_csv(chat_id)

def select_prodcat(chat_id, cat_id):
    k = kmarkup()
    lng = lang(chat_id)
    cat_name = config.ProdCat(cat_id=cat_id).get()[lng + '_content'].split("||")[0]
    msg = get_text(chat_id, "selected_prodcat_msg").format(**{
        "cat_name": cat_name
    })
    for product in config.Products(cat_id=cat_id).get():
        k.row(btn(product[lng + "_content"].split("||")[0], callback_data=f"select_product||{str(cat_id)}||{str(product['product_id'])}"))
    k.row(back(chat_id, "our_products"))
    send(chat_id, msg, reply_markup=k)

def select_product(chat_id, cat_id, product_id):
    product = config.Products(product_id=product_id).get()
    k = kmarkup()
    contentAndTitle = product[lang(chat_id)+"_content"]
    p_title = contentAndTitle.split("||")[0]
    p_content = contentAndTitle.split("||")[1]

    msg = f"<b>{p_title}</b>\n\n{p_content}"
    k.row(btn(get_text(chat_id, "take_it_btn"), callback_data=f"take_it||{cat_id}||{product_id}"))
    k.row(back(chat_id, f"select_prodcat||{cat_id}"))
    if product["photo_id"] in [None, "None"]:
        send(chat_id, msg, reply_markup=k)
    else:
        bot.send_photo(chat_id=chat_id, photo=product["photo_id"], caption=msg, reply_markup=k)

def take_it(call):
    chat_id = call.message.chat.id
    cds = call.data.split("||")

    k = kmarkup()
    k.row(btn("🔗️ Telegram", url="https://t.me/SBDT_admin"),
          btn("🔗️ WhatsApp", url="https://wa.me/972504834744"))
    k.row(btn("🔗️ Google", url="https://g.co/kgs/gLprpE"))

    k.row(back(chat_id, f"select_product||{cds[1]}||{cds[2]}"))
    send(chat_id, get_text(chat_id, f"take_it_msg"), reply_markup=k)

def i_need_specialist(chat_id):
    k = kmarkup()
    msg = get_text(chat_id, "i_need_specialist_msg")
    k.row(back(chat_id, "home"))
    send(chat_id, msg, reply_markup=k)
    stages(chat_id, "i_need_specialist_message")

def client_356_selected_user(chat_id, user_id):

    sql.execute(f"SELECT * FROM users WHERE user_id = '{str(user_id)}'")
    for user in sql.fetchall():
        k = kmarkup()
        msg = get_text(chat_id, f"client_356_selected_user_msg").format(**{
            "user_id": user[0],
            "first_name": user[1],
            "last_name": user[2],
            "tz": user[3],
            "birth_date": user[4],
            "known_from": user[5],
            "comment": user[6],
            "country": user[7],
            "city": user[8],
            "address": user[9],
            "phone": user[10]
        })

        # k.row(btn("✏️ " + get_text(chat_id, "first_name_btn"), callback_data=f"client356_user_edit||{str(user_id)}||first_name"))
        # k.row(btn("✏️ " + get_text(chat_id, "last_name_btn"), callback_data=f"client356_user_edit||{str(user_id)}||last_name"))
        # k.row(btn("✏️ " + get_text(chat_id, "country_btn"), callback_data=f"client356_user_edit||{str(user_id)}||country"))
        # k.row(btn("✏️ " + get_text(chat_id, "city_btn"), callback_data=f"client356_user_edit||{str(user_id)}||city"))
        # k.row(btn("✏️ " + get_text(chat_id, "address_btn"), callback_data=f"client356_user_edit||{str(user_id)}||address"))
        # k.row(btn("✏️ " + get_text(chat_id, "comment_btn"), callback_data=f"client356_user_edit||{str(user_id)}||comment"))
        # k.row(btn("✏️ " + get_text(chat_id, "known_from_btn"), callback_data=f"client356_user_edit||{str(user_id)}||known_from"))

        k.row(btn("remove_from_db_btn", callback_data=f"client356_remove_from_db||{str(user_id)}"))
        k.row(back(chat_id, "client356_search"))
        send(chat_id, msg, reply_markup=k)
        break

def contact_us(chat_id):
    k = kmarkup()
    k.row(btn("🔗️ Telegram", url="https://t.me/SBDT_admin"),
          btn("🔗️ WhatsApp", url="https://wa.me/972504834744"))
    k.row(btn("🔗️ Google", url="https://g.co/kgs/gLprpE"))

    k.row(back(chat_id, f"home"))
    send(chat_id, get_text(chat_id, f"contact_us_msg"), reply_markup=k)

def prog_lessons(chat_id):
     k = kmarkup()
     msg = get_text(chat_id, "prog_lessons_msg")
     k.row(btn("Python", callback_data=f"prog_python_lessons"))
     k.row(back(chat_id, "home"))
     send(chat_id, msg, reply_markup=k)

def prog_python_lessons(chat_id):
    k = kmarkup()
    msg = get_text(chat_id, "prog_python_lessons_msg")
    k.row(btn(get_text(chat_id, "take_it_btn"), callback_data=f"take_it_python_lessons"))
    k.row(back(chat_id, "prog_lessons"))
    send(chat_id, msg, reply_markup=k)

def take_it_python_lessons(chat_id):
    k = kmarkup()

    msg = get_text(chat_id, "take_it_msg")
    k.row(btn("🔗️ Telegram", url="https://t.me/SBDT_admin"),
          btn("🔗️ WhatsApp", url="https://wa.me/972504834744"))
    k.row(btn("🔗️ Google", url="https://g.co/kgs/gLprpE"))
    k.row(back(chat_id, "prog_python_lessons"))
    send(chat_id, msg, reply_markup=k)
