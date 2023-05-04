from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Запустить бота"),
            types.BotCommand("help", "Информация про тест"),
            types.BotCommand("on_start_burnout_test", "Пройти опрос на тему 'Профессиональное выгорание'"),
        ]
    )
