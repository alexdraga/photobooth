# -*- coding: utf-8 -*-
from config import commands
from telegram.processors import TelegramProcessor


class TelegramWorker(TelegramProcessor):
    def process_messages(self):
        for message in self.check_new_messages():
            # Process high-level events:
            # 1. Adding new user by invite code
            # 2. Ignore message if it was received from non-authorized iser
            # 3. Try to enter code from field user
            if self.process_photo_in_group_chat(message):
                continue
            if self.process_new_user(message):
                continue
            if self.process_unknown_user(message):
                continue

            command = self.extract_command(message).lower()
            if command == commands.approve:
                self.approve_command(message)
            elif command == commands.disapprove:
                self.disapprove_command(message)
            elif command == commands.stop:
                self._admin_in_group_chat_command(message, self.do_stop)
            elif command == commands.resume:
                self._admin_in_group_chat_command(message, self.do_resume)
            elif command == commands.pause:
                self._admin_in_group_chat_command(message, self.do_pause)
            elif command == commands.chat_message:
                self._admin_in_group_chat_command(message, self.do_chat_message)
            elif command == commands.message_admin:
                self._admin_in_group_chat_command(message, self.do_message_admin)

            # region Admin commands:
            elif command == commands.set_group_chat:
                self._admin_command(message, self.do_set_group_chat)
            elif command == commands.info:
                self._admin_command(message, self.do_info)
            elif command == commands.add_admin:
                self._admin_command(message, self.do_add_admin)
            elif command == commands.delete_admin:
                self._admin_command(message, self.do_delete_admin)
            elif command == commands.edit_admin_pass:
                self._admin_command(message, self.do_edit_admin_pass)
            elif command == commands.clean_admin:
                self._admin_command(message, self.do_cleanadmin)
            elif command == commands.message:
                self._admin_command(message, self.do_message)
            elif command == commands.token:
                self._admin_command(message, self.do_token)
            elif command == commands.send_errors:
                self._admin_command(message, self.do_send_errors)
            elif command == commands.clean_errors_:
                self._admin_command(message, self.do_clean_errors)
            elif command == commands.send_unknown:
                self._admin_command(message, self.do_send_unknown)
            elif command == commands.clean_unknown:
                self._admin_command(message, self.do_clean_unknown)
            elif command == commands.auth_flickr:
                self._admin_command(message, self.do_auth_flickr)
            elif command == commands.edit_key:
                self._admin_command(message, self.do_edit_key)
            elif command == commands.edit_secret:
                self._admin_command(message, self.do_edit_secret)
            else:
                self.unknown_command(message)
                # endregion
