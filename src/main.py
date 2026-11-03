import uvicorn 
import asyncio
from aiogram import Bot, Dispatcher
from config import settings
from tgbot_logic.tg_routers import all_tg_routers
from database.engine import create_base
from apis.site_api.push_post_through_site import router as api_router, app

dp = Dispatcher()
bot = Bot(token=settings.BOT_TOKEN)
dp.include_routers(*all_tg_routers)
app.include_router(api_router)


async def main_func():
    create_base()
    uvi_conf = uvicorn.Config(app, host="127.0.0.1", port=8000)#вынести потом значения в .env
    uvi_serv = uvicorn.Server(uvi_conf)
    await asyncio.gather(
        dp.start_polling(bot),
        uvi_serv.serve()
    )
    
if __name__ == "__main__":
    try:
        asyncio.run(main_func())
    except KeyboardInterrupt:
        print('Бот просто отключился') #сделать потом lifespan