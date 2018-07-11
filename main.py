# -*- coding: utf-8 -*-
from traceback import format_exc

from datetime import datetime

from config import errors_log
from telegram.worker import TelegramWorker

bot = TelegramWorker()

current_time = datetime.now()
game_update_next_run = current_time
code_enter_next_run = current_time


while not bot.stopped:
    try:
        bot.process_messages()
    except Exception, e:
        bot.admin_message(format_exc())
        errors_log.log_error(format_exc())
