(self):
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
