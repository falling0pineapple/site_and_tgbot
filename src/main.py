import uvicorn 
import asyncio
from aiogram import (Bot, Dispatcher as dp)
from src.config import settings
from src.tgbot_logic.tg_routers import all_tg_routers
from src.database.engine import create_base
from src.apis.site_api.push_post_through_site import router as api_router, app

bot = Bot(token=settings.BOT_TOKEN.get_secret_value())
dp.include_router(router for router in all_tg_routers)
app.include_router(api_router)

async def main_func():
    create_base()
    config = uvicorn.Config(app, host="127.0.0.1", port=8000)
    server = uvicorn.Server(config)
    await asyncio.gather(
        dp.start_polling(bot),
        server.serve()
    )
    
    
if __name__ == "__main__":
    asyncio.run(main_func())