from typing import Callable, Dict

from py_telegram_bot_api_framework.AHandler import AHandler
from telegram_bot_api import Update, get_entities_by_type, MessageEntityType, API

HandlerFunc = Callable[[Update], bool]


class BotCommandHandler(AHandler):
	def __init__(self, api: API, config: dict):
		self.registered_commands: Dict[str, HandlerFunc] = {}
		super().__init__(api, config)

	def register_command(self, cmd: str, cmd_handler: HandlerFunc):
		self.registered_commands[cmd] = cmd_handler

	def handle(self, update: Update) -> bool:
		msg = update.message
		if msg:
			commands = get_entities_by_type(msg, MessageEntityType.BOT_COMMAND)
			for command in commands:
				# remove bot name from command if any
				cmd = command.split("@")[0]
				cmd_handler = self.registered_commands.get(cmd, False)
				if cmd_handler:
					return cmd_handler(update)

		return False
