from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

inlinekeyboard = InlineKeyboardMarkup()
inlinekeyboard.add(InlineKeyboardButton(text="🆕 Новинки", callback_data="news_menu"),
InlineKeyboardButton(text="🚀 Популярное", callback_data="popular_menu"))
inlinekeyboard.add(InlineKeyboardButton(text="🔍 Поиск", callback_data="poisk"),
InlineKeyboardButton(text="🎞️ Подборки", callback_data="collections"))

inlinekeyboard.add(InlineKeyboardButton(text="💡 О боте", callback_data="about"),
InlineKeyboardButton(text="💬 Контакты", callback_data="contacts"))

news_menu_kb = InlineKeyboardMarkup()
news_menu_kb.add(InlineKeyboardButton(text="Фильмы", callback_data="news_films"), InlineKeyboardButton(text="Сериалы", callback_data="news_serials"))
news_menu_kb.add(InlineKeyboardButton(text="ТВ-шоу", callback_data="news_show"))
news_menu_kb.add(InlineKeyboardButton(text="◀️ Назад", callback_data="back"))

sub_menu = InlineKeyboardButton(text="ПОДПИСАТЬСЯ НА КАНАЛ", url='https://t.me/KINOMIKSED')
sub_menunot = InlineKeyboardButton(text="Я ПОДПИСАЛСЯ", callback_data='subchanneldone')
checksubmemu = InlineKeyboardMarkup(row_width=1)
checksubmemu.insert(sub_menu)
checksubmemu.insert(sub_menunot)

popular_menu_kb = InlineKeyboardMarkup()
popular_menu_kb.add(InlineKeyboardButton(text="Фильмы", callback_data="popular_films"), InlineKeyboardButton(text="Сериалы", callback_data="popular_series"))
popular_menu_kb.add(InlineKeyboardButton(text="Мультфильмы", callback_data="popular_cartoon"), InlineKeyboardButton(text="Мультсериалы", callback_data="popular_cartoon_serials"))
popular_menu_kb.add(InlineKeyboardButton(text="Аниме-фильмы", callback_data="popular_anime"), InlineKeyboardButton(text="Аниме-сериалы", callback_data="popular_anime_serials"))
popular_menu_kb.add(InlineKeyboardButton(text="ТВ-шоу", callback_data="popular_show"))
popular_menu_kb.add(InlineKeyboardButton(text="◀️ Назад", callback_data="back"))

inlinekeyboard2 = InlineKeyboardMarkup()
inlinekeyboard2.add(InlineKeyboardButton(text="◀️ Категории", callback_data="categories"),
InlineKeyboardButton(text="🏠 Меню", callback_data="back"))

inlinekeyboard3 = InlineKeyboardMarkup()
inlinekeyboard3.add(InlineKeyboardButton(text="◀️ Категории", callback_data="categories"),
InlineKeyboardButton(text="🏠 Меню", callback_data="back"))

inlinekeyboard4 = InlineKeyboardMarkup()
inlinekeyboard4.add(InlineKeyboardButton(text="◀️ Категории", callback_data="categories"),
InlineKeyboardButton(text="🏠 Меню", callback_data="back"))

inlinekeyboard5 = InlineKeyboardMarkup()
inlinekeyboard5.add(InlineKeyboardButton(text="◀️ Категории", callback_data="categories"),
InlineKeyboardButton(text="🏠 Меню", callback_data="back"))

inlinekeyboard6 = InlineKeyboardMarkup()
inlinekeyboard6.add(InlineKeyboardButton(text="◀️ Категории", callback_data="categories"),
InlineKeyboardButton(text="🏠 Меню", callback_data="back"))

inlinekeyboard7 = InlineKeyboardMarkup()
inlinekeyboard7.add(InlineKeyboardButton(text="◀️ Категории", callback_data="categories"),
InlineKeyboardButton(text="🏠 Меню", callback_data="back"))

inlinekeyboard8 = InlineKeyboardMarkup()
inlinekeyboard8.add(InlineKeyboardButton(text="◀️ Категории", callback_data="categories"),
InlineKeyboardButton(text="🏠 Меню", callback_data="back"))

exit = InlineKeyboardMarkup()
exit.add(InlineKeyboardButton(text="🏠 Главное меню", callback_data="back"))

gotohome = InlineKeyboardMarkup()
gotohome.add(InlineKeyboardButton(text="◀️ Назад", callback_data="back"))

category = InlineKeyboardMarkup()
category.add(InlineKeyboardButton(text="Фильмы", callback_data="films"),
InlineKeyboardButton(text="Сериалы", callback_data="serials"))
category.add(InlineKeyboardButton(text="Аниме-фильмы", callback_data="anime_films"),
InlineKeyboardButton(text="Аниме-сериалы", callback_data="anime_serials"))
category.add(InlineKeyboardButton(text="Мультфильмы", callback_data="cartoon"),
InlineKeyboardButton(text="Мультсериалы", callback_data="cartoon_serials"))
category.add(InlineKeyboardButton(text="ТВ-Шоу", callback_data="tv"))
category.add(InlineKeyboardButton(text="◀️ Назад", callback_data="back"))

contacts = InlineKeyboardMarkup()
contacts.add(InlineKeyboardButton(text="✈️ разраб", url="https://t.me/MIKSIDED"),
InlineKeyboardButton(text="📝 Наш группа", url="https://t.me/KINOMIKSED"))
contacts.add(InlineKeyboardButton(text="◀️ Назад", callback_data="back"))

about = InlineKeyboardMarkup()
# about.add(InlineKeyboardButton(text="🖊️ Вопросы / Ответы", callback_data="faq"))
about.add(InlineKeyboardButton(text="◀️ Назад", callback_data="back"))

search = InlineKeyboardMarkup()
search.add(InlineKeyboardButton(text="🆔 По KinoPoisk ID", callback_data="search_id"))
search.add(InlineKeyboardButton(text="🖊️ По названию", callback_data="categories"))
search.add(InlineKeyboardButton(text="◀️ Назад", callback_data="back"))

go_poisk = InlineKeyboardMarkup()
# about.add(InlineKeyboardButton(text="🖊️ Вопросы / Ответы", callback_data="faq"))
go_poisk.add(InlineKeyboardButton(text="◀️ Назад", callback_data="poisk"))
