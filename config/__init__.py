from os import path

from config.bot_settings import BotSettingsConfig
from config.commands import CommandsConfig
from config.errors import ErrorsLog
from config.flickr_settings import FlickrSettingsConfig
from config.timeouts import TimeoutsConfig
from config.unknown_log import UnknownLog

bot_settings = BotSettingsConfig(path.join("yaml", "bot_settings.yaml"))
flickr_settings = FlickrSettingsConfig(path.join("yaml", "flickr_settings.yaml"))
commands = CommandsConfig(path.join("yaml", "commands.yaml"))
errors_log = ErrorsLog(path.join("yaml", "errors_log.yaml"))
timeouts = TimeoutsConfig(path.join("yaml", "timeouts.yaml"))
unknown_log = UnknownLog(path.join("yaml", "unknown_log.yaml"))
