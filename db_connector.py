import datetime

import iluxaMod as ilm

database = ilm.postgreSQL_connect(user="postgres", password="armageddon", database="client356", host="localhost")
database.init_DB(stages=True, staff=True, stdout=False)
db = database.db
sql = database.sql
stages = database.stages
staff = database.staff
settings = database.settings
TOKEN = open("TOKEN", "r").read()
TGBot = ilm.tgBot(TOKEN)
bot = TGBot.bot
bot.parse_mode = "HTML"
kmarkup = TGBot.kmarkup
btn = TGBot.btn
send = TGBot.send

def pre_DB():
    def texts():
        sql.execute("""CREATE TABLE IF NOT EXISTS texts (
        text_id TEXT PRIMARY KEY,
        ru TEXT,
        en TEXT,
        he TEXT,
        ar TEXT
        )""")
        db.commit()
    def langs():
        sql.execute("""CREATE TABLE IF NOT EXISTS langs (
        user_id TEXT PRIMARY KEY,
        lang TEXT
        )""")
        db.commit()
    def sbdt_crm():
        sql.execute("""CREATE TABLE IF NOT EXISTS sbdt_crm (
        user_id TEXT PRIMARY KEY,
        first_name TEXT,
        last_name TEXT,
        phone TEXT,
        country TEXT,
        city TEXT,
        address TEXT,
        comment TEXT,
        facebook TEXT,
        instagram TEXT,
        linkedin TEXT,
        companies_id TEXT
        )""")
        db.commit()
    def client_crm():
        sql.execute("""CREATE TABLE IF NOT EXISTS clients_crm (
        row_id TEXT PRIMARY KEY,
        phone TEXT,
        user_id TEXT
        )""")
        db.commit()
    def product_cats():
        sql.execute("""CREATE TABLE IF NOT EXISTS product_cats (
        cat_id TEXT PRIMARY KEY,
        ru_name_and_desc TEXT,
        en_name_and_desc TEXT,
        he_name_and_desc TEXT,
        ar_name_and_desc TEXT,
        photo_id TEXT,
        eval_func TEXT
        )""")
        db.commit()
    def products():
        sql.execute("""CREATE TABLE IF NOT EXISTS products (
        product_id TEXT PRIMARY KEY,
        cat_ids TEXT,
        ru_name_and_desc TEXT,
        en_name_and_desc TEXT,
        he_name_and_desc TEXT,
        ar_name_and_desc TEXT,
        photo_id TEXT,
        link TEXT
        )""")
        db.commit()

    for db_init_func in [
        texts,
        langs,
        sbdt_crm,
        client_crm,
        product_cats,
        products
    ]:
        print(f"""[+] Table "{db_init_func.__name__}" init...""", end="")
        t1 = datetime.datetime.now()
        db_init_func()
        t2 = datetime.datetime.now()
        print(f'\r[+] Table "{db_init_func.__name__}" initialized    [{str(t2 - t1).split(":")[-1]} sec]')

