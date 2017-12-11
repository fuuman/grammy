from requests import get


class Sender:
    bot_url = 'https://api.telegram.org/bot{}'
    telegram_id = ''

    def __init__(self, bot_token, telegram_id):
        self.bot_url = self.bot_url.format(bot_token)
        self.telegram_id = telegram_id

    def send_message(self, message, parse_mode='markdown'):
        get("{}/sendMessage?chat_id={}&text={}&parse_mode={}".format(
            self.bot_url,
            self.telegram_id,
            message,
            parse_mode))
