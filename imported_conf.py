import psycopg2


class Notifier:
    def init(self, dbname, user, password, host, port):
        self.conn = psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host,
            port=port
        )

    def set(self, row_id, column, value):
        with self.conn.cursor() as cur:
            cur.execute(
                f"UPDATE notifier SET {column} = %s WHERE row_id = %s",
                (value, row_id)
            )
        self.conn.commit()

    def get(self):
        with self.conn.cursor() as cur:
            cur.execute("SELECT * FROM notifier")
            columns = [desc[0] for desc in cur.description]
            rows = cur.fetchall()
            data = []
            for row in rows:
                data.append(dict(zip(columns, row)))
        return data

    def new(self, row_id, phone, tattoo_date, notif_medic_every_hours, notif_master_every_days, last_medic_notif, last_master_notif, status):
        with self.conn.cursor() as cur:
            cur.execute(
                "INSERT INTO notifier (row_id, phone, tattoo_date, notif_medic_every_hours, notif_master_every_days, last_medic_notif, last_master_notif, status) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                (row_id, phone, tattoo_date, notif_medic_every_hours, notif_master_every_days, last_medic_notif, last_master_notif, status)
            )
        self.conn.commit()

    def remove(self, row_id):
        with self.conn.cursor() as cur:
            cur.execute("DELETE FROM notifier WHERE row_id = %s", (row_id,))
        self.conn.commit()

    def __del__(self):
        self.conn.close()


# Использование класса
notifier = Notifier(dbname="mydb", user="myuser", password="mypassword", host="localhost", port=5432)

# Добавление новой записи
notifier.new(
    row_id="1",
    phone="1234567890",
    tattoo_date="2021-10-01",
    notif_medic_every_hours="2",
    notif_master_every_days="1",
    last_medic_notif="2021-10-01 10:00:00",
    last_master_notif="2021-10-01 10:00:00",
    status="active"
)

# Получение всех записей
data = notifier.get()
print(data)

# Изменение значения поля "phone" для записи с row_id=1
notifier.set(row_id="1", column="phone", value="0987654321")

# Получение всех записей после изменения
data = notifier.get()
print(data)

# Удаление записи с row_id=1
notifier.remove(row_id="1")

# Получение всех записей после удаления
data = notifier.get()
print(data)
