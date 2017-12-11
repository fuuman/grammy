from .lib.sender import Sender

# Configuration ####################

# BOT_TOKEN   - Token of the bot, that should notify someone
BOT_TOKEN = ''

# TELEGRAM_ID - TelegramID, that should be the recipient of the notification
TELEGRAM_ID = ''


def mentionable():
    """
    :return: boolean
    True, if there is something mentionable to notify about
    False, if not
    """
    # need to be implemented
    return False


def notification():
    """
    :return: string
    The notification message.
    """
    # need to be implemented
    return ''

####################################


if __name__ == '__main__':
    if mentionable():
        message = notification()
        Sender(BOT_TOKEN, TELEGRAM_ID).send_message(message)
