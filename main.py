from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException

# Настройки Bitcoin Core
RPC_USER = 'Alzhan'
RPC_PASSWORD = 'Bakt1baev.04'
RPC_HOST = '20.19.35.156'  # Адрес вашего Bitcoin Core
RPC_PORT = 22  # Порт JSON-RPC сервера Bitcoin Core

# Создание экземпляра JSON-RPC клиента для Bitcoin Core
rpc_connection = AuthServiceProxy(f'http://{RPC_USER}:{RPC_PASSWORD}@{RPC_HOST}:{RPC_PORT}')

# Функция для генерации нового адреса
def get_new_address():
    return rpc_connection.getnewaddress()

# Функция для получения баланса
def get_balance():
    return rpc_connection.getbalance()

# Обработчик команды /getnewaddress
def get_new_address_command(update: Update, context: CallbackContext):
    new_address = get_new_address()
    update.message.reply_text(f"New address generated: {new_address}")

# Обработчик команды /getbalance
def get_balance_command(update: Update, context: CallbackContext):
    balance = get_balance()
    update.message.reply_text(f"Current balance: {balance} BTC")

def main():
    # Токен вашего Telegram бота
    token = "6687886732:AAF48TOOxLY-ng1KaeLf9caZvN0YYvqSw5M"
    updater = Updater(token)

    dispatcher = updater.dispatcher

    # Добавление обработчиков команд
    dispatcher.add_handler(CommandHandler("getnewaddress", get_new_address_command))
    dispatcher.add_handler(CommandHandler("getbalance", get_balance_command))

    # Запуск бота
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
