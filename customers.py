from config import *

client356AccessPoint = ["972504834744", "972524494346"]

class CustomerPanel:
    class Client356:
        def panel(self, chat_id):
            k = kmarkup()
            msg = get_text(chat_id, "client356")
            k.row(btn(get_text(chat_id, "my_customers_btn"), callback_data=f"my_customers"))
            k.row(btn(get_text(chat_id, "whatsapp_ads_btn"), callback_data=f"whatsapp_ads"))
            k.row(btn(get_text(chat_id, "whatsapp_notifier_btn"), callback_data=f"whatsapp_notifier"))

            k.row(back(chat_id, f"home"))
            send(chat_id, msg, reply_markup=k)

        def customers(self, chat_id):
            k = kmarkup()
            msg = get_text(chat_id, "client356_customers_msg").format(**{
                "clients_num": str(clients_amount(chat_id))
            })
            k.row(btn(get_text(chat_id, "search_btn"), callback_data=f"client356_search"))
            k.row(btn(get_text(chat_id, "add_one_by_one_btn"), callback_data=f"client356_add_one_by_one"))
            k.row(btn(get_text(chat_id, "add_users_from_csv_btn"), callback_data=f"client356_add_users_from_csv"))
            k.row(back(chat_id, "client_panel"))
            send(chat_id, msg, reply_markup=k)

        def search(self, chat_id):
            k = kmarkup()
            msg = get_text(chat_id, "client356_search_msg").format(**{
                "clients_num": str(clients_amount(chat_id))
            })
            k.row(btn(get_text(chat_id, "find_by_user_id_btn"), callback_data=f"find_by||user_id"))
            k.row(btn(get_text(chat_id, "find_by_first_name_btn"), callback_data=f"find_by||first_name"))
            k.row(btn(get_text(chat_id, "find_by_last_name_btn"), callback_data=f"find_by||last_name"))
            k.row(btn(get_text(chat_id, "find_by_phone_btn"), callback_data=f"find_by||phone"))
            k.row(btn(get_text(chat_id, "find_by_country_btn"), callback_data=f"find_by||country"))
            k.row(back(chat_id, "my_customers"))
            send(chat_id, msg, reply_markup=k)

        def search_by(self, chat_id, by):
            k = kmarkup()
            msg = get_text(chat_id, f"search_by_msg").format(**{"by": by})
            k.row(back(chat_id, "client356_search"))
            send(chat_id, msg, reply_markup=k)
            stages(chat_id, f"search_by||{by}")

        def whatsapp_ads(self, chat_id):
            k = kmarkup()
            msg = get_text(chat_id, "whatsapp_ads_msg")
            k.row(btn(get_text(chat_id, "edit_content_btn"), callback_data=f"client356_edit_content"))
            k.row(btn(get_text(chat_id, "start_advertise_btn"), callback_data=f"client356_start_advert"))
            k.row(back(chat_id, "client_panel"))
            send(chat_id, msg, reply_markup=k)

        def edit_content(self, chat_id):
            k = kmarkup()
            msg = get_text(chat_id, "client356_edit_content_msg").format(**{"content": settings('content')})
            k.row(btn(get_text(chat_id, "edit_content_btn"), callback_data=f"client356_enter_new_content"))
            k.row(back(chat_id, "whatsapp_ads"))
            send(chat_id, msg, reply_markup=k)

        def enter_new_content(self, chat_id):
            k = kmarkup()
            msg = get_text(chat_id, "edit_content_msg")
            k.row(back(chat_id, "edit_content"))
            send(chat_id, msg, reply_markup=k)
            stages(chat_id, "client356_edit_content")


        def new_client(self, chat_id):
            k = kmarkup()
            msg = get_text(chat_id, "client356_new_client_msg")

            k.row(back(chat_id, "my_customers"))
            send(chat_id, msg, reply_markup=k)
            stages(chat_id, f"client356_new_client")

        def add_users_from_csv(self, chat_id):
            #savePhonesListFromFile("c22.csv", chat_id)
            k = kmarkup()
            """need to add statistics"""
            #msg = get_text(chat_id, "users_adding_done_msg")
            msg = get_text(chat_id, "users_adding_send_file_msg")
            k.row(back(chat_id, "my_customers"))
            send(chat_id, msg, reply_markup=k)
            stages(chat_id, "add_users_from_csv")






