from typing import Tuple

from telegram_bot_api import MessageEntityType, MessageEntity, User


def get_prefix(entity_type: MessageEntityType):
	if entity_type == MessageEntityType.BOT_COMMAND:
		return "/"
	if entity_type == MessageEntityType.CASHTAG:
		return "$"
	if entity_type == MessageEntityType.HASHTAG:
		return "#"
	if entity_type == MessageEntityType.MENTION:
		return "@"
	if entity_type == MessageEntityType.TEXT_MENTION:
		return "@"
	return ""


def create_entity(
		offset: int,
		entity_type: MessageEntityType,
		text: str,
		url: str = None,
		user: User = None,
		language: str = None
) -> Tuple[str, MessageEntity]:
	result = f'{get_prefix(entity_type)}{text}'
	entity = MessageEntity(
		type=entity_type,
		offset=offset,
		length=len(result)
	)

	if url:
		assert entity_type == MessageEntityType.TEXT_LINK, "url allowed for 'text_link' only"
		entity.url = url
	if user:
		assert entity_type == MessageEntityType.TEXT_MENTION, "User allowed for 'mention' only"
		entity.user = user
	if language:
		assert entity_type == MessageEntityType.PRE, "language allowed for 'pre' only"
		entity.language = language

	return result, entity
