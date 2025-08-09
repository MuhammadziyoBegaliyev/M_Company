from aiogram import BaseMiddleware
from database.db import get_user

class I18nMiddleware(BaseMiddleware):
    async def __call__(self, handler, event, data):
        user_id = event.from_user.id
        user = await get_user(user_id)
        if user:
            lang = user[4]  # language
            if lang == "ru":
                from locales import ru as locale
            else:
                from locales import uz as locale
        else:
            from locales import uz as locale
        data["locale"] = locale.text
        return await handler(event, data)
