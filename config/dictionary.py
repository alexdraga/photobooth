# -*- coding: utf-8 -*-
from config import commands


class CommonMessages:
    PAUSED = u'Я на паузе.'
    ALREADY_PAUSED = u'Не поверишь. Я и так на паузе'
    ALREADY_WORKING = u'Я тебя сейчас наверное удивлю, но я и так работаю.'
    BYE = [u"Всё, давай, пока!",
           u"Давай, до свидания!",
           u"До скорых встреч, уважаемый."]
    AFFIRMATIVE = [u"Я понял тебя, братан",
                   u"Замётано",
                   u"Так точно"]
    UNKNOWN = u"Я тебя не понимаю"
    NOT_GROUP_CHAT = u"Напиши мне в командном чате, а не в личку."
    DO_PAUSE = u"Так. Не трогаю пока ничего тут"
    DO_RESUME = u"И снова здравствуйте!"
    LETS_GO = u"Воо-оо-оойтии-ии-и в игруу-уу-уу"
    DISAPPROVE = u"Если ты им не доверяешь - значит и я."
    CONNECTION_OK_MESSAGES = u"<b>---Авторизация на сайте успешна!---</b>"
    PLEASE_APPROVE_MESSAGES = u"<b>---Для дальнейшей работы выполни команду /approve в игровом чате---</b>"
    ACCESS_VIOLATION_MESSAGES = u"<b>Данная операция запрещена для вас, уважаемый.</b>"
    NO_GROUP_CHAT_MESSAGES = u"Я не доверяю этой группе людей."
    NOT_FOR_GROUP_CHAT_MESSAGES = [u"Такое лучше писать в личку."]


class BotSystemMessages:
    NEW_TOKEN = u"""Текущий токен: *{token}*\r\n Введи новый токен или *NO* для отмены операции"""
    TOKEN_CHANGED = u"""Токен был изменен"""
    CODE_INTERVAL = u"""Введи новый интервал между кодами *NO* для отмены операции"""
    CODE_INTERVAL_CHANGED = u"""Интервал между кодами был изменён"""
    TOKEN_CANCELLED = u"""Изменение токена отменено"""
    OPERATION_CANCELLED = u"""Операция отменена"""
    CODE_INTERVAL_CANCELLED = u"""Интервал между кодами не был изменён"""
    CONFIRM_DELETEION = u"""Эту операцию нельзя отменить. Для подтверждения напиши *"YES"* """
    ADMIN_CLEARED = u"""Все админы были удалены."""
    FIELD_CLEARED = u"""Все полевые игроки были удалены."""
    KC_CLEARED = u"""Все штабные игроки были удалены."""
    CODES_QUEUE_CLEARED = u"""Очередь кодов очищена."""
    ERRORS_CLEARED = u"""Лог ошибок очищен."""
    UNKNOWN_CLEARED = u"""Лог неопознанных пользователей очищен."""
    MEMORY_CLEARED = u"""Лог заданий и введённых кодов удалён."""
    BOT_WAS_RESET = u"Состояние бота было сброшено на начальное."


class CommandMessages:
    NO_CODE_FOUND = u'_Нет кодов для вбития. Попробуй ещё раз. Формат: /c long code или /cc code 1 code2_'
    DUPLICATE_CODE = u' уже вбил <b>{username}</b>/'
    NO_USER_ID = u"""Нет user id для добавления. Пример:
/addadmin 123456"""
    NO_MESSAGE = u"""Нет user id для сообщения. Пример:
/command 123456"""
    NO_TASK_ID = u"""Нет id уровня. Пример:
/codes 123456"""
    WRONG_LEVEL_ID = u"""Нет сохраненного уровня с указанным id"""
    NO_CODES_ENTERED = u"""История введённых кодов отсутсвует."""
    NO_TASKS_RECEIVED = u"""История полученных заданий отсутсвует."""
    FIELD_TRIED_CODE = u"""<b>{nickname}</b>:
{codes}"""


class SettingsMessages:
    ENTER_NEW_PASS = u"""Текущий инвайт-код: {code}.
Введите новый:"""
    ENTER_NEW_KEY = u"""Текущий key: {code}.
Введите новый:"""
    ENTER_NEW_SECRET = u"""Текущий secret: {code}.
Введите новый:"""
    PASS_WAS_CHANGED = u"""Пароль был изменён с *{code1}* на *{code2}*"""
    DUPLICATE_PASS = u"""Данный пароль уже используется, придумай другой."""
    GIVE_VALUE_NOW = u"""Для изменения параметра в групповом чате необходимо сразу передавать новое значение."""

    GIVE_ME_LOGIN = u"Давай мне свой *логин* для игры."
    GIVE_ME_PASSWORD = u"Давай мне свой *пароль*."
    GIVE_ME_HOST = u"На каком *домене* игра?"
    GIVE_ME_GAME = u"Какой *номер игры*?"
    GIVE_ME_NEW_LOGIN = u"Текущий логин: *{login}*\r\nВведи новый:"
    GIVE_ME_NEW_PASSWORD = u"Текущий пароль: *{password}*\r\nВведи новый:"
    GIVE_ME_NEW_HOST = u"Текущий хост игры: *{host}*\r\nВведи новый:"
    GIVE_ME_NEW_GAME = u"Текущий номер игры: *{game}*\r\nВведи новый:"
    TAG_FIELD = u"""Отмечать ли полевых игроков при получении нового задания?
*YES* - да, *NO* - нет, *CANCEL* - отменить"""
    SEND_TASK_TO_PRIVATE_FIELD = u"""Отсылать ли в личку полю новые задания и подсказки?
*YES* - да, *NO* - нет, *CANCEL* - отменить"""
    LOG_ACTIVITY = u"""Логгировать ли моменты активности?
*YES* - да, *NO* - нет, *CANCEL* - отменить"""
    AUTOHANDBRAKE = u"""Блокировать ли ввод кодов при получении задания с ограничением на ввод?
*ON* - да, *OFF* - нет, *CANCEL* - отменить"""
    AUTH_OK = u"Авторизация на сайте успешна"
    HANDBRAKE = u"""Снять блокировку на ввод кодов или оставить?
*ON* - блокировка включена, *OFF* - блокировка выключена, *CANCEL* - отменить"""
    SETTINGS_WERE_CHANGED = u"---*Настройки бота были изменены!*---"
    SETTINGS_WERE_SAVED = u"Настройки были сохранены"
    SETTINGS_WERE_NOT_SAVED = u"Проблема при записи настроек. Проверьте права доступа."
    SETTINGS_WERE_NOT_CHANGED = u"Настройки не были изменены."
    CONNECTION_PROBLEM = u"---*Проблемы с авторизацией на сайте!*---"
    CONNECTION_RESTORED = u"---*Доступ восстановлен!*---"
    CHECK_SETTINGS = u"---*Проверьте настройки!*---"


class UserMessages:
    HELLO_NEW_USER = u"""Добро пожаловать в ряды нашей доблестной команды.
Для начала рекомендую начать с просмотра доступных команд: /help
*ВНИМАНИЕ!*
Все следующие сообщения, которые ты будешь писать мне в личку - будут автоматически вбиваться в систему.
Будь внимателен!"""
    HELLO_NEW_ADMIN = u"""Добро пожаловать в ряды нашей доблестной команды.
Для начала рекомендую начать с просмотра доступных команд: /help"""

    NEW_ADMIN_WAS_ADDED = u"""Новый админ добавлен: {user_id} : {nickname}."""
    NEW_FIELD_WAS_ADDED = u"""Новый полевой игрок добавлен: {user_id} : {nickname}."""
    NEW_KC_WAS_ADDED = u"""Новый штабной игрок добавлен: {user_id} : {nickname}."""
    DUPLICATE_USER_ID = u"""Такой пользователь уже есть в базе. Добавление прервано."""
    CANNOT_DELETE_ADMIN = u"""Нельзя удалить последнего админа."""
    WRONG_USER_ID = u"""Неверный id пользователя"""
    DELETE_USER_ID = u"""Текущие пользователи:
{current_ids}
Введите id, который нужно удалить."""
    USER_DELETED = u"""Пользователь удалён."""


class FileMessages:
    NO_DATA_TO_DISPLAY = u"Нет данных для отображения."


class HelpMessages:
    STATUS = u"""
Статус дружочка: {paused}
Блокировка кодов: {handbrake}
Активная группа: {chat_id}
Имя группы: {chat_group_name}
Соединение к игровому серверу: {game_connection}
Текущий номер задания: {game_level_id}
Показанные подсказки: {game_hint_id}"""

    INFO = u"""
Активная группа: {chat_id}
Токен: {token}
-------------------------------
Инвайт-код для админов: {admin_passphrase}
Активные админы: {admins}
-------------------------------
Запущен: {time_start}
Ошибок: {bot_errors}
Запросов от неизвестных: {unknown_users}
"""

    PAUSED = {False: u"Активный",
              True: u"На паузе"}

    GAME_CONNECTION = {True: u"Активно",
                       False: u"Ошибка"}

    REGULAR_HELP = u"""
{status}: Показать текущий статус бота
{help}: Вывести помощь
""".format(
        status=commands.status,
        help=commands.help)

    ADMIN_HELP = u"""
*Админ-секция:*
{approve} : Добавить чат в список доверенных
{disapprove} : Удалить чат из списка доверенных
{set_group_chat} : Добавить чат по его id

{info} : Вывести детальную информацию о боте
{token}: Изменить токен бота

{pause} : Прекратить отслеживание заданий и вбитие кодов
{resume} : Возобновить отслеживание заданий и вбитие кодов
{stop} : Закончить работу с ботом

{addadmin}: Добавить нового админа. Необходимо указать id пользователя
{deleteadmin}: Удалить админа по его id
{cleanadmin}: Очистить список админов

{eap}: Изменить инвайт-код для админов

{chat_message}: Вывести объявление в групповой чат
{message}: Написать от имени бота указанному id
{message_admin}: Сделать рассылку в личку всем

{errors}: Отправить лог ошибок
{unknown}: Отправить лог запросов от неизвестных пользователей
{clean_errors}: Очистить лог ошибок
{clean_unknown}: Очистить лог запросов от неизвестных

*Пользовательские функции:*
{regular}
""".format(
        approve=commands.approve,
        disapprove=commands.disapprove,
        set_group_chat=commands.set_group_chat,
        token=commands.token,
        pause=commands.pause,
        stop=commands.stop,
        resume=commands.resume,
        info=commands.info,
        help=commands.help,
        addadmin=commands.add_admin,
        deleteadmin=commands.delete_admin,
        cleanadmin=commands.clean_admin,
        eap=commands.edit_admin_pass,
        message=commands.message,
        chat_message=commands.chat_message,
        message_admin=commands.message_admin,
        errors=commands.send_errors,
        unknown=commands.send_unknown,
        clean_errors=commands.clean_errors_,
        clean_unknown=commands.clean_unknown,
        regular=REGULAR_HELP)
