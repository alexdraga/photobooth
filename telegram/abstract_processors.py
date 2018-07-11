# -*- coding: utf-8 -*-
from config import bot_settings
from config.dictionary import CommonMessages
from telegram.driver import TelegramDriver


class AbstractProcessors(TelegramDriver):
    stopped = False

    def __init__(self):
        super(AbstractProcessors, self).__init__()

    def _reset(self):
        self.get_updates()

    def _admin_command(self, message, do_function):
        from_id = message["from_id"]
        chat_id = message["chat_id"]
        if bot_settings.is_admin(from_id):
            if chat_id < 0:
                if chat_id == bot_settings.group_chat_id:
                    self.answer_message(message, CommonMessages.NOT_FOR_GROUP_CHAT_MESSAGES)
                else:
                    self.answer_message(message, CommonMessages.NO_GROUP_CHAT_MESSAGES)
            else:
                do_function(message)
        elif bot_settings.answer_forbidden:
            self.answer_message(message, CommonMessages.ACCESS_VIOLATION_MESSAGES)

    def _admin_in_group_chat_command(self, message, do_function):
        from_id = message["from_id"]
        chat_id = message["chat_id"]
        if bot_settings.is_admin(from_id):
            if chat_id < 0:
                if chat_id == bot_settings.group_chat_id:
                    do_function(message)
                else:
                    self.answer_message(message, CommonMessages.NO_GROUP_CHAT_MESSAGES)
            else:
                do_function(message)
        elif bot_settings.answer_forbidden:
            self.answer_message(message, CommonMessages.ACCESS_VIOLATION_MESSAGES)

    def _user_command(self, message, do_function):
        from_id = message["from_id"]
        chat_id = message["chat_id"]
        if chat_id < 0:
            if chat_id == bot_settings.group_chat_id:
                do_function(message)
            elif bot_settings.is_admin(from_id):
                self.answer_message(message, CommonMessages.NO_GROUP_CHAT_MESSAGES)
            elif bot_settings.answer_forbidden:
                self.answer_message(message, CommonMessages.ACCESS_VIOLATION_MESSAGES)
        elif bot_settings.is_user(from_id):
            do_function(message)
        elif bot_settings.answer_forbidden:
            self.answer_message(message, CommonMessages.ACCESS_VIOLATION_MESSAGES)
