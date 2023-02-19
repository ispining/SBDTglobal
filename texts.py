from db_connector import sql, db, pre_DB


pre_DB()
texts = [
    # start_message
    {
        "text_id": "start_message",
        "ru": """<b>Добро пожаловать</b>
Данный бот является ранней версией сайта и приложения. Все инструменты для клиентов и учеников S.B.D.T уже присутствуют и тут! 

Выбери интересующий тебя пункт""",
        "en": """<b>Welcome</b>
This bot is an early version of the site and application. All tools for S.B.D.T clients and students are already here!

Choose the option you are interested in""",
        "he": """<b>ברוך הבא</b>
בוט זה הוא גרסה מוקדמת של האתר והאפליקציה. כל הכלים עבור לקוחות וסטודנטים של S.B.D.T כבר כאן!

""",
        "ar": """<b> مرحبًا </ b>
هذا الروبوت هو نسخة قديمة من الموقع والتطبيق. جميع الأدوات لعملاء وطلاب S.B.D.T موجودة هنا بالفعل!"""
    },

    # client_panel_msg
    {
        "text_id": "client_panel_msg",
        "ru": """<b>Панель Управления (Клиент)</b>

Уважаемый Клиент S.B.D.T,
Данная панель управления индивидуально под нужды твоего бизнеса.
Выбери нужное действие""",
        "en": """<b>Control Panel (Client)</b>

Dear S.B.D.T Customer,
This control panel is individually tailored to the needs of your business.
Choose the right action""",
        "he": """<b>לוח בקרה (לקוח)</b>

לקוח S.B.D.T יקר,
לוח בקרה זה מותאם באופן אישי לצרכי העסק שלך.
בחר את הפעולה הנכונה""",
        "ar": """<b></b>"""
    },

    # client356
    {
        "text_id": "client356",
        "ru": """<b>Панель Управления (Клиент)</b>

Уважаемый Клиент S.B.D.T,
Данная панель управления разработана индивидуально под нужды твоего бизнеса.

Выбери нужное действие""",
        "en": """<b>Control Panel (Client)</b>

Dear S.B.D.T Customer,
This control panel is designed individually for the needs of your business.

Choose an action""",
        "he": """<b>לוח בקרה (לקוח)</b>

לקוח S.B.D.T יקר,
לוח בקרה זה תוכנן באופן אינדיבידואלי לצרכי העסק שלך.

בחר פעולה""",
        "ar": """<b></b>"""
    },

    # not_allowed_to_CP_msg
    {
        "text_id": "not_allowed_to_CP_msg",
        "ru": """ОШИБКА!

Вы не имеете доступа к этой области. 
Это панель управления для действующих клиентов S.B.D.T""",
        "en": """ERROR!

You do not have access to this area.
This is the control panel for current S.B.D.T customers""",
        "he": """שגיאה!

אין לך גישה לאזור זה.
זהו לוח הבקרה ללקוחות S.B.D.T הנוכחיים""",
        "ar": """<b></b>"""
    },

    # not_allowed_to_SP_msg
    {
        "text_id": "not_allowed_to_SP_msg",
        "ru": """ОШИБКА!

Вы не имеете доступа к этой области. 
Сюда может заходить лишь тот, кто проходит уроки по программированию и автоматизации в S.B.D.T""",
        "en": """ERROR!

You do not have access to this area.
Only those who take programming and automation lessons in S.B.D.T can enter here""",
        "he": """שגיאה!

אין לך גישה לאזור זה.
זהו לוח הבקרה ללקוחות S.B.D.T הנוכחיים""",
        "ar": """<b></b>"""
    },

    # client356_customers_msg
    {
        "text_id": "client356_customers_msg",
        "ru": """<b>Клиентская база</b>

Ведение клиенской базы - является одним из самых важных шагов в любом бизнесе. 
Клиент один раз - клиент навсегда. Рассылка публикаций и профессиональных реклам позволит увиличивать колличество клиентов, 
вместо того, чтобы просто старых заменять новыми.

Всего Клиентов в базе: {clients_num}
        """,
        "en": """<b>Client base</b>

Maintaining a customer base is one of the most important steps in any business.
Once a customer, forever customer. Sending publications and professional advertisements will increase the number of customers,
instead of just replacing the old ones with new ones.

Total Clients in the database: {clients_num}""",
        "he": """<b>בסיס לקוחות</b>

שמירה על בסיס לקוחות היא אחד השלבים החשובים ביותר בכל עסק.
פעם לקוח, לקוח לנצח. שליחת פרסומים ופרסומות מקצועיות תגדיל את מספר הלקוחות,
במקום פשוט להחליף את הישנים בחדשים.

סך כל הלקוחות במסד הנתונים: {clients_num}""",
        "ar": """<b></b>"""
    },

    # client356_search_msg
    {
        "text_id": "client356_search_msg",
        "ru": """<b>Поиск по клиентской базе</b>

Всего Клиентов в базе: {clients_num}

Выберите интересующее вас действие
        """,
        "en": """<b>Search by customer base</b>

Total Clients in the database: {clients_num}""",
        "he": """<b>חפש לפי בסיס לקוחות</b>

סך כל הלקוחות במסד הנתונים: {clients_num}""",
        "ar": """<b></b>"""
    },

    # client356_new_client_msg
    {
        "text_id": "client356_new_client_msg",
        "ru": """<b>Добавление нового клиента</b>

Введите номер телефона нового клиента.

Обратите внимание, если номер телефона уже существует в базе данных - номер телефона добавлен не будет.
        """,
        "en": """<b>Adding a new client</b>

Enter the phone number of the new customer.

Please note that if the phone number already exists in the database, the phone number will not be added.""",
        "he": """<b>הוספת לקוח חדש</b>

הזן את מספר הטלפון של הלקוח החדש.

שימו לב שאם מספר הטלפון כבר קיים במאגר, מספר הטלפון לא יתווסף.""",
        "ar": """<b></b>"""
    },

    # new_client_added_msg
    {
        "text_id": "new_client_added_msg",
        "ru": """<b>Клиент добавлен успешно</b>

Клиент был добавлен успешно в систему.
Данный номер телефона с этого момента будет учитываться при рассылках или уведомлениях.
В любой момент вы можете отредактировать данные о данном номере телефона и его владельце.

Вы можете добавить еще номера клиентов, или вернуться назад.
        """,
        "en": """<b>Client added successfully</b>

The client was added successfully to the system.
From now on, this phone number will be taken into account in mailing lists or notifications.
At any time, you can edit the data about this phone number and its owner.

You can add more customer numbers, or go back.""",
        "he": """<b>הלקוח נוסף בהצלחה</b>

הלקוח נוסף בהצלחה למערכת.
מרגע זה, מספר טלפון זה יילקח בחשבון ברשימות תפוצה או בהודעות.
בכל עת, תוכל לערוך את הנתונים לגבי מספר הטלפון הזה והבעלים שלו.

אתה יכול להוסיף מספרי לקוחות נוספים, או לחזור אחורה.""",
        "ar": """<b></b>"""
    },

    # new_client_exists_msg
    {
        "text_id": "new_client_exists_msg",
        "ru": """<b>Ошибка</b>
        
Данный номер уже записан в базе данных. Попробуйте ввести новый номер, или вернитесь назад.
        """,
        "en": """<b>Error</b>
        
This number is already in the database. Try entering a new number, or go back.""",
        "he": """<b>שגיאה</b>
        
המספר הזה כבר נמצא במסד הנתונים. נסה להזין מספר חדש, או חזור אחורה.""",
        "ar": """<b></b>"""
    },

    # users_from_file_saved_msg
    {
        "text_id": "all_users_from_file_saved_msg",
        "ru": """<b>Добавление из файла прошло успешно</b>""",
        "en": """"<b>Adding from file was successful<b>""",
        "he": """<b>ההוספה מהקובץ הצליחה</b>""",
        "ar": """<b></b>"""
    },

    # start_adding_users_from_file_msg
    {
        "text_id": "start_adding_users_from_file_msg",
        "ru": """<b>Начинаем добавление ползователей из файла</b> """,
        "en": """<b>Start adding users from file<b>""",
        "he": """<b>מתחיל להוסיף משתמשים מהקובץ</b>""",
        "ar": """<b></b>"""
    },

    # our_products_msg
    {
        "text_id": "our_products_msg",
        "ru": """<b>Наши продукты</b>
        
Тут мы публикуем проекты, которые уже были сделаны для наших клиентов.
Выберите нужную категорию
        """,
        "en": """<b>Our Products</b>
        
Here we publish projects that have already been made for our clients.""",
        "he": """<b>המוצרים שלנו</b>
        
כאן אנו מפרסמים פרויקטים שכבר נעשו עבור לקוחותינו.""",
        "ar": """<b></b>"""
    },

    # selected_prodcat_msg
    {
        "text_id": "selected_prodcat_msg",
        "ru": """<b>Наши идеи и возможности</b>
        
<b>Выбрана категория:</b> {cat_name}
        """,
        "en": """<b>Our ideas and possibilities</b>
        
<b>Category selected:</b> {cat_name}""",
        "he": """<b>הרעיונות והאפשרויות שלנו</b>
        
<b>הקטגוריה שנבחרה:</b> {cat_name}""",
        "ar": """<b></b>"""
    },

    # take_it_msg
    {
        "text_id": "take_it_msg",
        "ru": """<b>Связатья с нами</b>

Для получения бесплатной консультации, заказа услуг или уроков - свяжитесь с нами, воспользовавшись одной из кнопок ниже.""",
        "en": """<b>Contact Us</b>

For a free consultation and ordering services, contact us using one of the buttons below.""",
        "he": """<b>צור קשר</b>

לייעוץ חינם והזמנת שירותי צרו קשר באחד מהלחצנים למטה.""",
        "ar": """<b></b>"""
    },

    # i_need_specialist_msg
    {
        "text_id": "i_need_specialist_msg",
        "ru": """<b>Поиск специалиста</b>

Опишите, что именно вас интересует. 
Не забудьте указать сферу деятельности и не забывайте о том, что чем больше деталей 
вы тут укажите - тем быстрее мы сможем найти именно того, кто вам нужен""",
        "en": """<b>Search for a specialist</b>

Describe what interests you.
Do not forget to indicate the field of activity and do not forget that the more details
you specify here - the faster we can find exactly the one you need""",
        "he": """<b>חפש מומחה</b>

תאר מה מעניין אותך.
אל תשכחו לציין את תחום הפעילות ואל תשכחו שיותר פרטים
אתה מציין כאן - כך נוכל למצוא מהר יותר בדיוק את מי שאתה צריך""",
        "ar": """<b></b>"""
    },

    # how_to_contact_with_client_msg
    {
        "text_id": "how_to_contact_with_client_msg",
        "ru": """<b>Поиск специалиста</b>

Как наши сотрудники смогут с вами связаться?

Укажите свои контактные данные""",
        "en": """<b>Search for a specialist</b>

How can our staff contact you?

Enter your contact details""",
        "he": """<b>חפש מומחה</b>

איך הצוות שלנו יכול ליצור איתך קשר?

הזן את פרטי הקשר שלך""",
        "ar": """<b></b>"""
    },

    # we_will_contact_you_msg
    {
        "text_id": "we_will_contact_you_msg",
        "ru": """<b>Заявка отправлена</b>

Мы обязательно свяжемся с вами в ближайшие дни. 

Спасибо за обращение 🤗""",
        "en": """<b>Application sent</b>

We will definitely contact you in the coming days.

Thank you for contacting 🤗""",
        "he": """<b><b>האפליקציה נשלחה</b>

בהחלט ניצור איתך קשר בימים הקרובים.

תודה שפנית 🤗</b>""",
        "ar": """<b></b>"""
    },

    # users_adding_send_file_msg
    {
        "text_id": "users_adding_send_file_msg",
        "ru": """<b>Добавление из файла</b>

Отправь CSV файл с номерами телефонов""",
        "en": """<b>Add from file</b>

Send CSV file with phone numbers""",
        "he": """"<b>הוסף מקובץ</b>

שלח קובץ CSV עם מספרי טלפון""",
        "ar": """<b></b>"""
    },

    # search_by_user_id_msg
    {
        "text_id": "search_by_user_id_msg",
        "ru": """<b>Поиск по Идентификатору</b>

Введите Идентификационный номер (id) требуемого пользователя""",
        "en": """<b>Search by ID</b>

Enter the identification number (id) of the required user""",
        "he": """<b>חפש לפי מזהה</b>

הזן את מספר הזיהוי (מזהה) של המשתמש הדרוש""",
        "ar": """<b></b>"""
    },

    # search_by_msg
    {
        "text_id": "search_by_msg",
        "ru": """<b>Поиск</b>

Введите значение {by} требуемого пользователя""",
        "en": """<b>Search</b>

Enter the value {by} of the required user""",
        "he": """<b>חפש</b>

הזן את הערך {by} של המשתמש הדרוש""",
        "ar": """<b></b>"""
    },

    # select_a_user_msg
    {
        "text_id": "select_a_user_msg",
        "ru": """<b>Результаты поиска</b>

Ниже показаны результаты осуществляемого поиска.
Выберите одного из пользователей""",
        "en": """<b>Search results</b>

The results of the search being performed are shown below.
Choose one of the users""",
        "he": """<b>תוצאות חיפוש</b>

תוצאות החיפוש המתבצע מוצגות להלן.
בחר אחד מהמשתמשים""",
        "ar": """<b></b>"""
    },

    # client_356_selected_user_msg
    {
        "text_id": "client_356_selected_user_msg",
        "ru": """<b>Информация о Клиенте</b>

<b>Идентификатор:</b> {user_id}
<b>Имя:</b> {first_name}
<b>Фамилия:</b> {last_name}
<b>Удостоверение:</b> {tz}
<b>Дата рождения:</b> {birth_date}
<b>Откуда знаком:</b> {known_from}
<b>Комментарий:</b> {comment}
<b>Страна:</b> {country}
<b>Город:</b> {city}
<b>Адрес:</b> {address}
<b>Номер телефона:</b> {phone}

""",
        "en": """<b>Client Information</b>

<b>Identifier:</b> {user_id}
<b>Name:</b> {first_name}
<b>Last name:</b> {last_name}
<b>Identity:</b> {tz}
<b>Date of birth:</b> {birth_date}
<b>From:</b> {known_from}
<b>Comment:</b> {comment}
<b>Country:</b> {country}
<b>City:</b> {city}
<b>Address:</b> {address}
<b>Phone number:</b> {phone}""",
        "he": """<b>מידע לקוח</b>

<b>מזהה:</b> {user_id}
<b>שם:</b> {first_name}
<b>שם משפחה:</b> {last_name}
<b>זהות:</b> {tz}
<b>תאריך לידה:</b> {birth_date}
<b>מאת:</b> {known_from}
<b>תגובה:</b> {comment}
<b>מדינה:</b> {country}
<b>עיר:</b> {city}
<b>כתובת:</b> {address}
<b>מספר טלפון:</b> {phone}""",
        "ar": """<b></b>"""
    },

    # user_removed_msg
    {
        "text_id": "user_removed_msg",
        "ru": """
Пользователь удален успешно!
""",
        "en": """User deleted successfully!""",
        "he": """המשתמש נמחק בהצלחה!""",
        "ar": """<b></b>"""
    },

    # whatsapp_ads_msg
    {
        "text_id": "whatsapp_ads_msg",
        "ru": """<b>Рассылка по Ватсап</b>

Отсюда вы можете осущетвить рекламную рассылку по сохраненным номерам.

Выберите интересующее вас действие

""",
        "en": """<b>WhatsApp Newsletter</b>

From here you can send promotional messages to saved numbers.""",
        "he": """ניוזלטר WhatsApp

מכאן תוכל לשלוח הודעות קידום מכירות למספרים שמורים.""",
        "ar": """<b></b>"""
    },

    # client356_edit_content_msg
    {
        "text_id": "client356_edit_content_msg",
        "ru": """<b>Редактирование контента</b>

Ваш текущий контент:
<code>
{content}
</code>
""",
        "en": """<b>Content editing</b>

Your current content:
<code>
{content}
</code>""",
        "he": """<b>עריכת תוכן</b>

התוכן הנוכחי שלך:
<code>
{content}
</code>""",
        "ar": """<b></b>"""
    },

    # edit_content_msg
    {
        "text_id": "edit_content_msg",
        "ru": """<b>Редактирование контента</b>
Отправьте новый желаемый контент""",
        "en": """<b>Content editing</b>
Submit new desired content""",
        "he": """<b>עריכת תוכן</b>
שלח תוכן מבוקש חדש""",
        "ar": """<b></b>"""
    },


    # content_edited_msg
    {
        "text_id": "content_edited_msg",
        "ru": """<b>Новый контент сохранен успешно</b>""",

        "en": """<b>New content saved successfully</b>""",
        "he": """<b>תוכן חדש נשמר בהצלחה</b>""",
        "ar": """<b></b>"""
    },


    # client356_start_advert_msg
    {
        "text_id": "client356_start_advert_msg",
        "ru": """Рассылка начинается
Процесс может занять до 24 часов, так как работает Анти-Блокировочный механизм.
Мы вас оповестим о завершении""",
        "en": """Advert starts
The process may take up to 24 hours due to the Anti-Lock mechanism.
We will notify you when completed.""",
        "he": """<b>הפרסום מתחיל
התהליך עשוי להימשך עד 24 שעות בשל מנגנון Anti-Lock.
אנו נודיע לך בסיום.</b>""",
        "ar": """<b></b>"""
    },


    # only_one_action_can_be_used_msg
    {
        "text_id": "only_one_action_can_be_used_msg",
        "ru": """Видимо, рассылка уже начата. Вы не можете ее начать еще раз, до того, как программа завершит рассылку""",
        "en": """Apparently, the distribution has already begun. You cannot start it again before the program completes the broadcast""",
        "he": """ככל הנראה, ההפצה כבר החלה. לא ניתן להפעיל אותה שוב לפני שהתוכנית תסיים את השידור""",
        "ar": """<b></b>"""
    },


    # contact_us_msg
    {
        "text_id": "contact_us_msg",
        "ru": """<b>Связаться с нами</b>

Выберите подходящюю для вас опцию
        """,
        "en": """<b>Contact us</b>

Choose the option that suits you""",
        "he": """<b>צור קשר</b>

בחר את האפשרות המתאימה לך""",
        "ar": """<b></b>"""
    },


    # prog_lessons_msg
    {
        "text_id": "prog_lessons_msg",
        "ru": """<b>Уроки программирования</b>

Мы предоставляем уроки по программированию.
Ниже перечислены языки программирования, по которым мы имеем возможность предоставить учителей на данный момент.
Данный список будет время от времени пополняться.

Выберите интересующий вас язык программирования
        """,
        "en": """<b>Programming lessons</b>

We provide programming lessons.
The programming languages for which we are currently able to provide teachers are listed below.
This list will be updated from time to time.

Choose the programming language you are interested in""",
        "he": """<b>שיעורי תכנות</b>

אנו מספקים שיעורי תכנות.
שפות התכנות שעבורן אנו יכולים כעת לספק למורים מפורטות להלן.
רשימה זו תתעדכן מעת לעת.

בחר את שפת התכנות שבה אתה מעוניין""",
        "ar": """<b></b>"""
    },

    # prog_python_lessons_msg
    {
        "text_id": "prog_python_lessons_msg",
        "ru": """<b>Python</b>

Уроки программирования на языке Python.
• Курсы для начинающих программистов
• Подготовка к экзаменациям
• Помощь в проектах
• Мастер класс

<b>Групповые занятия:</b>
Минимум учеников: 6
Урок: 50 шек за каждого ученика

<b>Частные занятия:</b>
Одинарный урок: 150шек.
Двойной урок: 200шек.

* Каждый урок длится от часу до двух, в зависимости от успеваемости
* Первый урок бесплатно
        """,
        "en": """<b>Python</b>

Programming lessons in Python.
• Courses for beginner programmers
• Exam preparation
• Assistance in projects

<b>Group lessons:</b>
Minimum students: 6
Lesson: 50 NIS per student

<b>Private lessons:</b>
Single lesson: 150 NIS
Double lesson: 200 NIS

* Each lesson lasts from an hour to two, depending on the progress
* First lesson for free""",
        "he": """<b>Python</b>

שיעורי תכנות בפייתון.
• קורסים למתכנתים מתחילים
• הכנה לבחינה
• סיוע בפרויקטים

<b>שיעורים קבוצתיים:</b>
מינימום סטודנטים: 6
שיעור: 50 ₪ לתלמיד

<b>שיעורים פרטיים:</b>
שיעור בודד: 150 ₪
שיעור זוגי: 200 ₪

* משך כל שיעור בין שעה לשעתיים, תלוי בהתקדמות
* שיעור ראשון בחינם""",
        "ar": """<b></b>"""
    },



    ############################ BUTTONS ############################
    # back_btn
    {
        "text_id": "back_btn",
        "ru": "🔙 Назад",
        "en": "🔙 Back",
        "he": "🔙 חזרה",
        "ar": "🔙 خلف"
    },

    # client_panel_btn
    {
        "text_id": "client_panel_btn",
        "ru": "👨‍💼 Панель Предпринимателя",
        "en": "👨‍💼 Entrepreneur Panel",
        "he": "👨‍💼 איזור בעלי עסקים",
        "ar": "👨‍💼 مجال أصحاب الأعمال"
    },

    # student_panel_btn
    {
        "text_id": "student_panel_btn",
        "ru": "🧑‍🎓 Панель Студента",
        "en": "🧑‍🎓 Student Panel",
        "he": "🧑‍🎓 איזור סטודנטים",
        "ar": "🧑‍🎓 لوحة الطالب"
    },

    # our_products_btn
    {
        "text_id": "our_products_btn",
        "ru": "🌐 Наши продукты",
        "en": "🌐 Our products",
        "he": "🌐 המוצרים משלנו",
        "ar": "🌐 منتجاتنا الخاصة"
    },

    # i_need_specialist_btn
    {
        "text_id": "i_need_specialist_btn",
        "ru": "🔎 Ищу специалиста",
        "en": "🔎 Looking for a specialist",
        "he": "🔎 מחפש איש מקצוע",
        "ar": "🔎 أبحث عن متخصص"
    },

    # our_team_btn
    {
        "text_id": "our_team_btn",
        "ru": "🫂 Наша команда",
        "en": "🫂 Our Team",
        "he": "🫂 הצוות שלנו",
        "ar": "🫂 فريقنا"
    },

    # contact_us_btn
    {
        "text_id": "contact_us_btn",
        "ru": "📱 Связаться с нами",
        "en": "📱 Contact us",
        "he": "📱 צור קשר",
        "ar": "📱 اتصل بنا"
    },

    # my_customers_btn
    {
        "text_id": "my_customers_btn",
        "ru": "🗃️ Мои клиенты",
        "en": "🗃️ My Clients",
        "he": "🗃️ תיק הלקוחות שלי",
        "ar": "🗃️ موكلي"
    },

    # whatsapp_ads_btn
    {
        "text_id": "whatsapp_ads_btn",
        "ru": "📣 Рассылка ватсап",
        "en": "📣 WhatsApp Advertise",
        "he": "📣 פרסום בווטסאפ",
        "ar": "📣 إعلان WhatsApp"
    },

    # set_langs_btn
    {
        "text_id": "set_langs_btn",
        "ru": "🔄 Сменить язык",
        "en": "🔄 Change language",
        "he": "🔄 שנה שפה",
        "ar": "🔄 تغيير اللغة"
    },

    # search_btn
    {
        "text_id": "search_btn",
        "ru": "🔎 Поиск",
        "en": "🔎 Search",
        "he": "🔎 חיפוש",
        "ar": "🔎 يبحث"
    },

    # add_one_by_one_btn
    {
        "text_id": "add_one_by_one_btn",
        "ru": "📁 Добавление по одному",
        "en": "📁 Add one by one",
        "he": "📁 הוסף אחד אחד",
        "ar": "📁 "
    },

    # add_users_from_csv_btn
    {
        "text_id": "add_users_from_csv_btn",
        "ru": "🗂️ Добавление из файла",
        "en": "🗂️ Add from file",
        "he": "🗂️ הוספה מקובץ",
        "ar": "🗂️ أضف واحدًا تلو الآخر"
    },

    # find_by_user_id_btn
    {
        "text_id": "find_by_user_id_btn",
        "ru": "🔎 Искать по Идентификатору",
        "en": "🔎 Find by ID",
        "he": "🔎 חיפוש לפי אי-די",
        "ar": "🔎 البحث عن طريق المعرف"
    },

    # find_by_first_name_btn
    {
        "text_id": "find_by_first_name_btn",
        "ru": "🔎 Искать по Имени",
        "en": "🔎 Find by first name",
        "he": "🔎 חיפוש לפי שם פרטי",
        "ar": "🔎 البحث عن طريق الإسم"
    },

    # find_by_last_name_btn
    {
        "text_id": "find_by_last_name_btn",
        "ru": "🔎 Искать по Фамилии",
        "en": "🔎 Find by last name",
        "he": "🔎 חיפוש לפי שם משפחה",
        "ar": "🔎 البحث بالاسم الأخير"
    },

    # find_by_phone_btn
    {
        "text_id": "find_by_phone_btn",
        "ru": "🔎 Искать по Телефону",
        "en": "🔎 Find by phone",
        "he": "🔎 חיפוש לפי טלפון",
        "ar": "🔎 البحث عن طريق الهاتف"
    },

    # find_by_country_btn
    {
        "text_id": "find_by_country_btn",
        "ru": "🔎 Искать по Стране",
        "en": "🔎 Find by country",
        "he": "🔎 חיפוש לפי מדינה",
        "ar": "🔎 البحث عن طريق الدولة"
    },

    # first_name_btn
    {
        "text_id": "first_name_btn",
        "ru": "Имя",
        "en": "First Name",
        "he": "שם פרטי",
        "ar": "اسم"
    },

    # last_name_btn
    {
        "text_id": "last_name_btn",
        "ru": "Фамилия",
        "en": "Last Name",
        "he": "שם משפחה",
        "ar": "اسم العائلة"
    },

    # phone_btn
    {
        "text_id": "phone_btn",
        "ru": "Телефон",
        "en": "Phone",
        "he": "טלפון",
        "ar": "هاتف"
    },

    # country_btn
    {
        "text_id": "country_btn",
        "ru": "Страна",
        "en": "Country",
        "he": "מדינה",
        "ar": "دولة"
    },

    # city_btn
    {
        "text_id": "city_btn",
        "ru": "Город",
        "en": "City",
        "he": "עיר",
        "ar": "مدينة"
    },

    # address_btn
    {
        "text_id": "address_btn",
        "ru": "Адрес",
        "en": "Address",
        "he": "כתובת",
        "ar": "عنوان"
    },

    # comment_btn
    {
        "text_id": "comment_btn",
        "ru": "Комментарии",
        "en": "Comments",
        "he": "תגובות",
        "ar": "تعليقات"
    },

    # known_from_btn
    {
        "text_id": "known_from_btn",
        "ru": "Откуда знакомы",
        "en": "Known From",
        "he": "מאיכן מכירים",
        "ar": ""
    },

    # take_it_btn
    {
        "text_id": "take_it_btn",
        "ru": "📞 Заказать",
        "en": "📞 Order",
        "he": "📞 הזמן עכשיו",
        "ar": "📞 كيف علمت بذلك"
    },

    # remove_from_db_btn
    {
        "text_id": "remove_from_db_btn",
        "ru": "🗑️ Удалить",
        "en": "🗑️ Remove",
        "he": "🗑️ מחיקה",
        "ar": "🗑️ يزيل"
    },

    # whatsapp_notifier_btn
    {
        "text_id": "whatsapp_notifier_btn",
        "ru": "🔔 Ватсап напоминалка",
        "en": "🔔 WhatsApp notifier",
        "he": "🔔️ התראות ווטסאפ",
        "ar": "🔔 whatsapp يخطر"
    },

    # edit_content_btn
    {
        "text_id": "edit_content_btn",
        "ru": "✏️ Ред. контент",
        "en": "✏️ Edit content",
        "he": "✏️ עריכת תוכן",
        "ar": "✏️ تحرير المحتوى"
    },

    # start_advertise_btn
    {
        "text_id": "start_advertise_btn",
        "ru": "📤 Запустить рассылку",
        "en": "📤 Start advertise",
        "he": "📤 התחל שליחה",
        "ar": "📤 ابدأ الإعلان"
    },

    # prog_lessons_btn
    {
        "text_id": "prog_lessons_btn",
        "ru": "🧑‍🏫 Уроки программирования",
        "en": "🧑‍🏫 Programming lessons",
        "he": "🧑‍🏫 שיעורי תכנות",
        "ar": "🧑‍🏫 "
    }


]

def get_text(text_id) -> dict:
    sql.execute(f"SELECT * FROM texts WHERE text_id = '{text_id}'")
    for row in sql.fetchall():
        return {
            "text_id": row[0],
            "ru": row[1],
            "en": row[2],
            "he": row[3],
            "ar": row[4]
        }

for new_data in texts:
    ru = new_data['ru']
    en = new_data['en']
    he = new_data['he']
    ar = new_data['ar']
    old_data = get_text(new_data['text_id'])
    if old_data == None:
        sql.execute(f"INSERT INTO texts VALUES ('{str(new_data['text_id'])}', 'None', 'None', 'None')")
        db.commit()
        old_data = get_text(new_data['text_id'])

    for lng in ["ru", "en", "he", "ar"]:
        if old_data[lng] != new_data[lng]:
            sql.execute(f"UPDATE texts SET {lng} = '{eval(lng)}' WHERE text_id = '{new_data['text_id']}'")
            db.commit()


set_lang = """
Select your language:
"""

