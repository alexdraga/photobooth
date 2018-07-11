# -*- coding: utf-8 -*-
import json

from config import bot_settings, errors_log, flickr_settings, unknown_log
from config.dictionary import CommonMessages, BotSystemMessages, CommandMessages, SettingsMessages, \
    UserMessages, FileMessages, HelpMessages
from photocollector.driver import PhotoCollectorDriver
from telegram.abstract_processors import AbstractProcessors


class TelegramProcessor(AbstractProcessors):
    PCD = PhotoCollectorDriver()

    def do_stop(self, message):
        self.answer_message(message, CommonMessages.BYE)
        self.stopped = True

    def do_pause(self, message):
        if not bot_settings.paused:
            self.answer_message(message, CommonMessages.DO_PAUSE)
            bot_settings.paused = True
        else:
            self.answer_message(message, CommonMessages.ALREADY_PAUSED)

    def do_resume(self, message):
        if bot_settings.paused:
            self.answer_message(message, CommonMessages.DO_RESUME)
            bot_settings.paused = False
        else:
            self.answer_message(message, CommonMessages.ALREADY_WORKING)

    def _do_approve(self, message):
        chat_id = message["chat_id"]
        title = message["title"]
        self.answer_message(message, CommonMessages.LETS_GO)
        bot_settings.group_chat_id = chat_id
        bot_settings.group_chat_name = title
        bot_settings.paused = False

    def approve_command(self, message):
        from_id = message["from_id"]
        chat_id = message["chat_id"]
        if bot_settings.is_admin(from_id):
            if chat_id < 0:
                self._do_approve(message)
            else:
                self.answer_message(message, CommonMessages.NOT_GROUP_CHAT)
        elif bot_settings.answer_forbidden:
            self.answer_message(message, CommonMessages.ACCESS_VIOLATION_MESSAGES)

    def do_add_admin(self, message):
        if len(message["text"].split()) > 1:
            admin_to_add = message["text"].split()[1]
            if not admin_to_add.isdigit():
                self.answer_message(message, UserMessages.WRONG_USER_ID)
            else:
                if bot_settings.is_admin(int(admin_to_add)):
                    self.answer_message(
                        message,
                        UserMessages.DUPLICATE_USER_ID)
                else:
                    bot_settings.add_admin_id(int(admin_to_add))
                    self.admin_message(
                        UserMessages.NEW_ADMIN_WAS_ADDED.format(
                            user_id=admin_to_add,
                            nickname=self.get_username(admin_to_add)))
                    self.send_message(admin_to_add, UserMessages.HELLO_NEW_ADMIN)
        else:
            self.answer_message(message,
                                CommandMessages.NO_USER_ID)

    def do_set_group_chat(self, message):
        if len(message["text"].split()) > 1:
            group_chat_id = message["text"].split()[1]
            if group_chat_id.startswith("-") and group_chat_id[1:].isdigit():
                bot_settings.group_chat_id = int(group_chat_id)
            else:
                self.answer_message(message, UserMessages.WRONG_USER_ID)
        else:
            self.answer_message(message,
                                CommandMessages.NO_USER_ID)

    def do_delete_admin(self, message):
        if len(bot_settings.admin_ids) == 1:
            self.answer_message(message, UserMessages.CANNOT_DELETE_ADMIN)
        else:
            admin_to_delete = self.get_new_value(
                message,
                UserMessages.DELETE_USER_ID.format(
                    current_ids=self.get_usernames(bot_settings.admin_ids)))
            if not admin_to_delete.isdigit() or int(admin_to_delete) not in bot_settings.admin_ids:
                self.answer_message(message, UserMessages.WRONG_USER_ID)
            else:
                bot_settings.delete_admin_id(int(admin_to_delete))
                self.answer_message(message, UserMessages.USER_DELETED)

    def do_edit_admin_pass(self, message):
        new = self.get_new_value(
            message,
            SettingsMessages.ENTER_NEW_PASS.format(code=bot_settings.admin_passphrase))
        old = bot_settings.admin_passphrase
        if new not in bot_settings.passphrases:
            bot_settings.admin_passphrase = new
            self.answer_message(
                message,
                SettingsMessages.PASS_WAS_CHANGED.format(code1=old,
                                                         code2=new))
        else:
            self.answer_message(
                message,
                SettingsMessages.DUPLICATE_PASS)

    def do_cleanadmin(self, message):
        self.answer_message(message, BotSystemMessages.CONFIRM_DELETEION)
        answer = self.wait_for_answer(message["from_id"])
        if answer["text"] == "YES":
            bot_settings.clean_admins()
            self.answer_message(message, BotSystemMessages.ADMIN_CLEARED)
        else:
            self.answer_message(message, BotSystemMessages.OPERATION_CANCELLED)

    def do_chat_message(self, message):
        if bot_settings.group_chat_id is not None:
            message_text = self.extract_text(message)
            self.send_message(
                bot_settings.group_chat_id,
                message_text)

    def do_message(self, message):
        message_text = self.extract_text(message)
        if len(message_text.split()) > 1:
            if message_text.split()[0].isdigit():
                user_id = int(message_text.split()[0])
                message_text = message_text.replace(message_text.split()[0], '').lstrip()
                self.send_message(
                    user_id,
                    message_text)
            else:
                self.answer_message(message,
                                    UserMessages.WRONG_USER_ID)
        else:
            self.answer_message(message,
                                CommandMessages.NO_MESSAGE)

    def do_message_admin(self, message):
        message_text = self.extract_text(message)
        for admin_id in bot_settings.admin_ids:
            self.send_message(admin_id,
                              message_text)

    def do_send_errors(self, message):
        from_id = message["from_id"]
        if len(errors_log.errors_raw):
            self.send_file(from_id,
                           str(errors_log.repr_errors()),
                           'errors.txt')
        else:
            self.answer_message(message,
                                FileMessages.NO_DATA_TO_DISPLAY)

    def do_clean_errors(self, message):
        errors_log.clean_errors()
        self.answer_message(message,
                            BotSystemMessages.ERRORS_CLEARED)

    def do_token(self, message):
        new_token = self.get_new_value(message,
                                       BotSystemMessages.NEW_TOKEN.format(token=bot_settings.bot_token))
        if new_token != "NO":
            if bot_settings.bot_token != new_token:
                bot_settings.bot_token = new_token
                self._reset()
            from_id = message["from_id"]
            self.send_message(from_id, BotSystemMessages.TOKEN_CHANGED)
        else:
            self.answer_message(message, BotSystemMessages.TOKEN_CANCELLED)

    def do_auth_flickr(self, message):
        url = self.PCD.request_tokens()
        self.answer_message(message, url['auth_url'], parse_mode="HTML")
        oauth_verifier = self.wait_for_answer(message["from_id"])["text"]
        if self.PCD.request_auth(oauth_verifier):
            self.answer_message(message, SettingsMessages.AUTH_OK)

    def do_send_unknown(self, message):
        from_id = message["from_id"]
        unknown_message = unknown_log.repr_unknown()
        if len(unknown_message):
            self.send_file(from_id,
                           unknown_message,
                           'unknown.txt')
        else:
            self.answer_message(message,
                                FileMessages.NO_DATA_TO_DISPLAY)

    def do_clean_unknown(self, message):
        unknown_log.unknown_raw = []
        self.answer_message(message,
                            BotSystemMessages.UNKNOWN_CLEARED)

    def _do_disapprove(self, message):
        bot_settings.group_chat_id = None
        bot_settings.group_chat_name = None
        bot_settings.paused = True
        self.answer_message(message, CommonMessages.DISAPPROVE)

    def disapprove_command(self, message):
        from_id = message["from_id"]
        chat_id = message["chat_id"]
        if bot_settings.is_admin(from_id):
            if chat_id < 0:
                if chat_id == bot_settings.group_chat_id:
                    self._do_disapprove(message)
                else:
                    self.answer_message(message, CommonMessages.NO_GROUP_CHAT_MESSAGES)
            else:
                self.answer_message(message, CommonMessages.NOT_GROUP_CHAT)
        elif bot_settings.answer_forbidden:
            self.answer_message(message, CommonMessages.ACCESS_VIOLATION_MESSAGES)

    def do_status(self, message):
        status_message = HelpMessages.STATUS.format(
            paused=HelpMessages.PAUSED[bot_settings.paused],
            chat_id=bot_settings.group_chat_id,
            chat_group_name=bot_settings.group_chat_name
        )
        self.answer_message(message, status_message)

    def do_info(self, message):
        info_message = HelpMessages.INFO.format(
            chat_id=bot_settings.group_chat_id,
            admins=json.dumps(self.get_usernames(bot_settings.admin_ids)),
            admin_passphrase=bot_settings.admin_passphrase,
            time_start=bot_settings.start_time,
            bot_errors=len(errors_log.errors_raw),
            token=bot_settings.bot_token,
            unknown_users=len(unknown_log.unknown_raw))
        self.answer_message(message, info_message, parse_mode="HTML")

    def do_help(self, message):
        from_id = message["from_id"]
        if bot_settings.is_admin(from_id):
            self.answer_message(message, HelpMessages.ADMIN_HELP)
        else:
            self.answer_message(message, HelpMessages.REGULAR_HELP)

    def unknown_command(self, message):
        if bot_settings.answer_unknown:
            self.answer_message(message, CommonMessages.UNKNOWN)

    def process_unknown_user(self, message):
        from_id = message["from_id"]
        if not bot_settings.is_user(from_id):
            unknown_log.log_unknown(message)
            return True
        else:
            return False

    def process_photo_in_group_chat(self, message):
        from_id = message["from_id"]
        chat_id = message["chat_id"]
        if chat_id < 0:
            if chat_id == bot_settings.group_chat_id:
                self._process_photo(message)
            elif bot_settings.is_admin(from_id):
                self.answer_message(message, CommonMessages.NO_GROUP_CHAT_MESSAGES)
            elif bot_settings.answer_forbidden:
                self.answer_message(message, CommonMessages.ACCESS_VIOLATION_MESSAGES)
        elif bot_settings.is_user(from_id):
            self._process_photo(message)
        elif bot_settings.answer_forbidden:
            self.answer_message(message, CommonMessages.ACCESS_VIOLATION_MESSAGES)

    def _process_photo(self, message):
        if not bot_settings.paused:
            if message.get("photo") is not None:
                download_link = self.get_file(message["photo"][-1]["file_id"])
                photo_image = self.session.get(download_link)
                self.PCD.upload_file(message["photo"][-1]["file_id"], photo_image.content)
                return True
            else:
                return False

    def process_new_user(self, message):
        passphrase = message["text"]
        from_id = message["from_id"]
        if passphrase == bot_settings.admin_passphrase:
            if from_id in bot_settings.admin_ids:
                return False
            else:
                bot_settings.add_admin_id(int(from_id))
                self.answer_message(message, UserMessages.HELLO_NEW_ADMIN)
                self.admin_message(
                    UserMessages.NEW_ADMIN_WAS_ADDED.format(user_id=from_id,
                                                            nickname=self.get_username(from_id)))
                return True
        elif passphrase == bot_settings.field_passphrase:
            if from_id in bot_settings.field_ids:
                return False
            else:
                bot_settings.add_field_id(int(from_id))
                self.answer_message(message, UserMessages.HELLO_NEW_USER)
                self.admin_message(
                    UserMessages.NEW_FIELD_WAS_ADDED.format(user_id=from_id,
                                                            nickname=self.get_username(from_id)))
                return True
        elif passphrase == bot_settings.kc_passphrase:
            if from_id in bot_settings.kc_ids:
                return False
            else:
                bot_settings.add_kc_id(int(from_id))
                self.answer_message(message, UserMessages.HELLO_NEW_USER)
                self.admin_message(
                    UserMessages.NEW_KC_WAS_ADDED.format(user_id=from_id,
                                                         nickname=self.get_username(from_id)))
                return True
        else:
            return False

    def do_edit_key(self, message):
        new = self.get_new_value(
            message,
            SettingsMessages.ENTER_NEW_KEY.format(code=flickr_settings.key))
        flickr_settings.key = new
        self.answer_message(
            message,
            SettingsMessages.SETTINGS_WERE_SAVED)
        self.PCD = PhotoCollectorDriver()

    def do_edit_secret(self, message):
        new = self.get_new_value(
            message,
            SettingsMessages.ENTER_NEW_SECRET.format(code=flickr_settings.secret))
        flickr_settings.secret = new
        self.answer_message(
            message,
            SettingsMessages.SETTINGS_WERE_SAVED)
        self.PCD = PhotoCollectorDriver()
