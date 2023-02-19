#!/venv/Scripts/python
import random

import config
import customers
import texts
from config import sql, db, database, send, kmarkup, btn,  staff, stages, bot, lang, get_text
import stg


@bot.message_handler(commands=["start"])
def start_command(message):
    chat_id = message.chat.id
    if message.chat.type == "private":
        if lang(chat_id) not in [None, "None"]:
            stg.start_message(chat_id)
        else:
            stg.set_lang(chat_id, home_back_btn=False)


@bot.message_handler(content_types=['document'])
def globalDocument(message):
    chat_id = message.chat.id
    if message.chat.type == "private":
        stage = stages(chat_id)
        cds = stage.split("||")
        if cds[0] == "add_users_from_csv":
            config.download_file(message)
            config.savePhonesListFromFile("c22.csv", chat_id)
            send(chat_id, get_text(chat_id, "all_users_from_file_saved_msg"))
            stg.client356_search(chat_id)
            stages(chat_id, "None")


@bot.message_handler(content_types=['text'])
def globalText(message):
    chat_id = message.chat.id
    if message.chat.type == "private":
        stage = stages(chat_id)
        cds = stage.split("||")

        if cds[0] == "client356_new_client":
            def the_action():
                phone = message.text.replace("+", "")
                normalized_phone = None
                try:
                    int(phone)
                    if phone[0:3] == "972":
                        normalized_phone = phone[3:]
                    elif phone[0:2] == "05":
                        normalized_phone = "972" + phone[2:]
                except ValueError:
                    pass
                if normalized_phone != None:
                    config.client_crm(normalized_phone, chat_id)
                    sql.execute(f"SELECT * FROM users WHERE phone = '{normalized_phone}'")
                    if sql.fetchone() is None:
                        sql.execute(f"""INSERT INTO users VALUES(
                                              '{str(random.randint(int("1" * 9), int("9" * 9)))}',
                                              '{str(None)}',
                                              '{str(None)}',
                                              '{str(None)}',
                                              '{str(None)}',
                                              '{str(None)}',
                                              '{str(None)}',
                                              '{str(None)}',
                                              '{str(None)}',
                                              '{str(None)}',
                                              '{str(normalized_phone)}'
                                              )""")
                        db.commit()
                        return True
                    else:
                        send(chat_id, get_text(chat_id, "new_client_exists_msg"), reply_markup=kmarkup().row(stg.back(chat_id, "my_customers")))
            if the_action():
                k = kmarkup()
                msg = get_text(chat_id, "new_client_added_msg")
                send(chat_id, msg, reply_markup=k)
                stages(chat_id, "None")

                customers.CustomerPanel().Client356().new_client(chat_id)
        elif cds[0] == "i_need_specialist_message":
            k = kmarkup()
            msg = get_text(chat_id, "how_to_contact_with_client_msg")
            k.row(stg.back(chat_id, "i_need_specialist"))
            send(chat_id, msg, reply_markup=k)
            stages(chat_id, f"""how_to_contact_with_client||{message.text.replace('"', "").replace("'", "")}""")
        elif cds[0] == "how_to_contact_with_client":
            client = message.chat
            content = cds[1]
            contact = message.text

            send(config.admin_group, f"""
<b>Новый контакт ожидает</b>
{str(client.id)}            

{str(content)}            
{str(contact)}            
#NewUser""", kmarkup().row(btn("Done", callback_data="is_done")))

            msg = get_text(chat_id, "we_will_contact_you_msg")
            send(chat_id, msg)

            stg.start_message(chat_id)
            stages(chat_id, "None")
        elif cds[0] == "search_by":
            by = cds[1]
            k = kmarkup()

            msg = get_text(chat_id, f"select_a_user_msg")

            sql.execute(f"SELECT * FROM users WHERE {by} = '{str(message.text)}'")
            for user_info in sql.fetchall():
                k.row(btn("+" + user_info[-1], callback_data=f"client_356_selected_user||{str(user_info[0])}"))
            k.row(stg.back(chat_id, f"find_by||{by}"))
            send(chat_id, msg, reply_markup=k)
            stages(chat_id, "None")
        elif cds[0] == "client356_edit_content":
            config.settings("content", message.text.replace('"', '').replace("'", ""))
            send(chat_id, get_text(chat_id, "content_edited_msg"))
            stages(chat_id, "None")
            customers.CustomerPanel().Client356().whatsapp_ads(chat_id)


@bot.message_handler(content_types=['photo'])
def globalText(message):
    chat_id = message.chat.id

    if message.chat.type == "private":
        print(message.photo[-1].file_id)





@bot.callback_query_handler(func=lambda m: True)
def global_calls(call):
    chat_id = call.message.chat.id

    def dm():
        try:
            bot.delete_message(chat_id, call.message.message_id)
        except:
            pass
    cd = call.data
    cds = cd.split("||")

    if call.message.chat.type == "private":

        if cds[0] == "set_lang":
            lang(chat_id, cd.split("||")[1])
            stg.start_message(chat_id)
            dm()
        elif cds[0] == "home":
            stg.start_message(chat_id)
            dm()
        elif cds[0] == "client_panel":
            #
            stg.client_panel(call)
        elif cds[0] == "my_customers":
            stg.my_customers(chat_id)
            dm()
        elif cds[0] == "set_langs":
            stg.set_lang(chat_id, home_back_btn=True)
            dm()
        elif cds[0] == "client356_search":
            stg.client356_search(chat_id)
            dm()
        elif cds[0] == "client356_add_one_by_one":
            stg.client356_add_one_by_one(chat_id)
            dm()
        elif cds[0] == "client356_add_users_from_csv":
            stg.client356_add_users_from_csv(chat_id)
            dm()
        elif cds[0] == "student_panel":
            #
            bot.answer_callback_query(call.id, get_text(chat_id, "not_allowed_to_SP_msg"), show_alert=True)
        elif cds[0] == "our_products":
            stg.our_products_btn(chat_id)
            dm()
        elif cds[0] == "select_prodcat":
            cat_id = cds[1]
            stg.select_prodcat(chat_id, cat_id)
            dm()
        elif cds[0] == "select_product":
            cat_id = cds[1]
            product_id = cds[2]
            stg.select_product(chat_id, cat_id, product_id)
            dm()
        elif cds[0] == "take_it":
            stg.take_it(call)
            dm()
        elif cds[0] == "i_need_specialist":
            stg.i_need_specialist(chat_id)
            dm()
        elif cds[0] == "find_by":
            stg.client356_search(chat_id, by=cds[1])
            dm()
        elif cds[0] == "client_356_selected_user":
            user_id = cds[1]
            stg.client_356_selected_user(chat_id, user_id)
            dm()
        elif cds[0] == "client356_remove_from_db":
            user_id = str(cds[1])

            sql.execute(f"SELECT * FROM users WHERE user_id = '{user_id}'")
            lst = sql.fetchall()
            for i in lst:
                sql.execute(f"DELETE FROM users WHERE user_id = '{user_id}'")
                db.commit()
                sql.execute(f"DELETE FROM clients_crm WHERE phone = '{i[-1]}'")
                db.commit()

            bot.answer_callback_query(call.id, get_text(chat_id, "user_removed_msg"), show_alert=True)

            stg.client356_search(chat_id)
            dm()
        elif cds[0] == "whatsapp_ads":
            if config.user_idToPhone(chat_id) in customers.client356AccessPoint:
                customers.CustomerPanel().Client356().whatsapp_ads(chat_id)
                dm()
        elif cds[0] == "client356_edit_content":
            if config.user_idToPhone(chat_id) in customers.client356AccessPoint:
                customers.CustomerPanel().Client356().edit_content(chat_id)
                dm()
        elif cds[0] == "client356_enter_new_content":
            if config.user_idToPhone(chat_id) in customers.client356AccessPoint:
                customers.CustomerPanel().Client356().enter_new_content(chat_id)
                dm()
        elif cds[0] == "client356_start_advert":
            if config.user_idToPhone(chat_id) in customers.client356AccessPoint:
                sql.execute(f"SELECT * FROM callbacks WHERE from_user = '{str(chat_id)}'")
                if sql.fetchone() is None:
                    sql.execute(f"INSERT INTO callbacks VALUES ('{str(chat_id)}', '0000', 'start_advert')")
                    db.commit()
                    bot.answer_callback_query(call.id, get_text(chat_id, "client356_start_advert_msg"), show_alert=True)
                else:
                    bot.answer_callback_query(call.id, get_text(chat_id, "only_one_action_can_be_used_msg"), show_alert=True)
        elif cds[0] == "contact_us":
            stg.contact_us(chat_id)
            dm()
        elif cds[0] == "prog_lessons":
            stg.prog_lessons(chat_id)
            dm()
        elif cds[0] == "prog_python_lessons":
            stg.prog_python_lessons(chat_id)
            dm()
        elif cds[0] == "take_it_python_lessons":
            stg.take_it_python_lessons(chat_id)
            dm()

    else:
        if cds[0] == "is_done":
            dm()
            send(chat_id, call.message.text + f"\n\n<b>~ Confirmed</b>")



while True:
    try:
        bot.polling()
    except Exception as ex:
        print(ex)

