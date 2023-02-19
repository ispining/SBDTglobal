import random

import psycopg2

from db_connector import *
import texts

admin_group = -1001419432437

class SBDT:

    class CRM:

        def __init__(self, user_id=None, phone=None):
            self.user_id = user_id
            self.first_name = None
            self.last_name = None
            self.phone = phone
            self.country = None
            self.city = None
            self.address = None
            self.comment = None
            self.facebook = None
            self.instagram = None
            self.linkedin = None
            self.companies_id = None

        def add(self) -> str:
            """
            Add new user to main SBDT crm.
            Phone number needed

            :return: new user_id
            """

            if self.user_id == None:
                self.user_id = random.randint(int("1"*9), int("9"*9))
            if self.phone != None:
                sql.execute(f"""INSERT INTO sbdt_crm VALUES (
                '{str(self.user_id)}',
                '{str(self.first_name)}',
                '{str(self.last_name)}',
                '{str(self.phone)}',
                '{str(self.country)}',
                '{str(self.city)}',
                '{str(self.address)}',
                '{str(self.comment)}',
                '{str(self.facebook)}',
                '{str(self.instagram)}',
                '{str(self.linkedin)}',
                '{str(self.companies_id)}'
                )""")
                db.commit()

            return str(self.user_id)

        def set(self, column, value):
            if self.phone != None:
                sql.execute(f"UPDATE sbdt_crm SET {column} = {value} WHERE user_id = '{str(self.user_id)}'")
            elif self.user_id != None:
                sql.execute(f"UPDATE sbdt_crm SET {column} = {value} WHERE phone = '{str(self.phone)}'")
            db.commit()

        def get(self) -> dict:
            if self.user_id != None:
                sql.execute(f"SELECT * FROM sbdt_crm WHERE user_id = '{self.user_id}'")
            elif self.phone != None:
                sql.execute(f"SELECT * FROM sbdt_crm WHERE phone = '{self.phone}'")
            for i in sql.fetchall():
                return {
                    "user_id": i[0],
                    "first_name": i[1],
                    "last_name": i[2],
                    "phone": i[3],
                    "country": i[4],
                    "city": i[5],
                    "address": i[6],
                    "comment": i[7],
                    "facebook": i[8],
                    "instagram": i[9],
                    "linkedin": i[10],
                    "companies_id": i[11]
                }

class ProdCat:
    def __init__(self, cat_id=None):
        self.cat_id = cat_id

    def get(self):
        """
        if cat_id is None, return {cat_id, ru_content, en_content, he_content, ar_content, photo_id, eval_func}.

        Else return dicts list
        """
        if self.cat_id == None:
            result = []
            sql.execute(f"SELECT * FROM product_cats")
            for row in sql.fetchall():
                result.append({
                    "cat_id": row[0],
                    "ru_content": row[1],
                    "en_content": row[2],
                    "he_content": row[3],
                    "ar_content": row[4],
                    "photo_id": row[5],
                    "eval_func": row[6],
                })
            return result

        elif self.cat_id != None:
            sql.execute(f"SELECT * FROM product_cats WHERE cat_id = '{str(self.cat_id)}'")
            for row in sql.fetchall():
                return {
                    "cat_id": row[0],
                    "ru_content": row[1],
                    "en_content": row[2],
                    "he_content": row[3],
                    "ar_content": row[4],
                    "photo_id": row[5],
                    "eval_func": row[6],
                }

class Products:
    def __init__(self, product_id=None, cat_id=None):
        self.product_id = product_id
        self.cat_id = cat_id

    def exists(self):
        if self.product_id != None:
            sql.execute(f"SELECT *  FROM products WHERE product_id = '{str(self.product_id)}'")
            if sql.fetchone() is None:
                return False
            else:
                return True

        elif self.cat_id != None:
            sql.execute(f"SELECT *  FROM products")
            for product_info in sql.fetchall():
                print(product_info)
                cat_ids = product_info[1].split("||")
                print(cat_ids)
                if self.cat_id in cat_ids:
                    return True
                else:
                    return False

    def get(self):
            if self.product_id != None:
                sql.execute(f"SELECT *  FROM products WHERE product_id = '{str(self.product_id)}'")
                for product_info in sql.fetchall():
                    return {
                        "product_id": product_info[0],
                        "cat_ids": product_info[1],
                        "ru_content": product_info[2],
                        "en_content": product_info[3],
                        "he_content": product_info[4],
                        "ar_content": product_info[5],
                        "photo_id": product_info[6],
                        "link": product_info[7]
                    }
            elif self.cat_id != None:
                result = []
                sql.execute(f"SELECT *  FROM products ORDER BY product_id ASC")
                for product_info in sql.fetchall():
                    cat_ids = product_info[1].split("||")
                    if self.cat_id in cat_ids:
                        result.append({
                            "product_id": product_info[0],
                            "cat_ids": product_info[1],
                            "ru_content": product_info[2],
                            "en_content": product_info[3],
                            "he_content": product_info[4],
                            "ar_content": product_info[5],
                            "photo_id": product_info[6],
                            "link": product_info[7]
                        })
                return result

def lang(user_id, new_lang=None) -> str:
    sql.execute(f"SELECT * FROM langs WHERE user_id = '{str(user_id)}'")
    if sql.fetchone() is None:
        sql.execute(f"INSERT INTO langs VALUES ('{str(user_id)}', 'None')")
        db.commit()

    if new_lang != None:
        sql.execute(f"UPDATE langs SET lang = '{new_lang}' WHERE user_id = '{str(user_id)}'")
        db.commit()
    else:
        sql.execute(f"SELECT * FROM langs WHERE user_id = '{str(user_id)}'")
        for row in sql.fetchall():
            return row[1]

def get_text(user_id, text_id) -> str:
    return texts.get_text(text_id)[lang(user_id)]

def back(chat_id, callback_data):
    return btn(get_text(chat_id, "back_btn"), callback_data=callback_data)

def user_idToPhone(user_id):
    try:
        user_info = SBDT().CRM(user_id=user_id).get()
        if user_info != None:
            return user_info['phone']
    except psycopg2.OperationalError:
        user_idToPhone(user_id)


def client_crm(phone, user_id=None):
    try:
        if user_id == None:
            sql.execute(f"SELECT * FROM clients_crm WHERE phone = '{str(phone)}'")
            for row in sql.fetchall():
                return row[2]

        elif user_id != None:
            sql.execute(f"SELECT * FROM clients_crm WHERE phone = '{str(phone)}' AND user_id = '{str(user_id)}'")
            if sql.fetchone() is None:
                sql.execute(f"INSERT INTO clients_crm VALUES ('{str(random.randint(111111111, 999999999))}', '{str(phone)}', '{str(user_id)}')")
                db.commit()
            else:
                sql.execute(f"UPDATE clients_crm SET user_id = '{str(user_id)}' WHERE phone = '{str(phone)}'")
                db.commit()
    except psycopg2.OperationalError:
        client_crm(phone, user_id)


def clients_amount(sbdt_client_id) -> int:
    try:
        sql.execute(f"SELECT * FROM clients_crm WHERE user_id = '{str(sbdt_client_id)}'")
        return len(sql.fetchall())
    except psycopg2.OperationalError:
        clients_amount(sbdt_client_id)


def savePhonesListFromFile(filename, added_by):
    """need to add statistics"""
    result = []
    file_content = open(filename, "r").read()
    send(added_by, get_text(added_by, "start_adding_users_from_file_msg"))
    iter_num = 0
    last_sended = 0
    last_msg = None
    global_phones_num = len(file_content.split("\n"))
    for user_info in file_content.split("\n"):
        inf = user_info.split(";")
        for number in inf[1].split("|"):
            number = number.replace("+", "")
            if len(number) > 6:
                if number[0:2] == "05":
                    number = "9725" + number[2:]
                    result.append(number)
                elif number[0:3] == "972":
                    result.append(number)

                normalized_phone = None
                phone = number
                try:
                    int(phone)
                    if phone[:3] == "972":
                        normalized_phone = phone
                    elif phone[0:2] == "05":
                        normalized_phone = "972" + phone[2:]
                except ValueError:
                    pass
                if normalized_phone != None:
                    client_crm(normalized_phone, added_by)
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
        iter_num = iter_num + 1
        if last_msg != None:
            bot.delete_message(added_by, last_msg.chat.id)

        if last_sended != iter_num//10:
            last_sended = iter_num//10
            last_msg = send(added_by, f"Saved: {str(iter_num)} of {str(global_phones_num)}")


def download_file(message):
    file_name = message.document.file_name
    file_id = message.document.file_name
    file_id_info = bot.get_file(message.document.file_id)
    downloaded_file = bot.download_file(file_id_info.file_path)
    src = file_name
    with open("c22.csv", 'wb') as new_file:
        new_file.write(downloaded_file)
