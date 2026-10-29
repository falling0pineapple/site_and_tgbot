from tgbot_logic.tg_handlers.start_handler import router as start_router
from tgbot_logic.admins.admin_handlers.admin_handlers import router as admin_handlers_router
from tgbot_logic.admins.admin_handlers.admin_posts import router as admin_post_router


all_tg_routers = [start_router, admin_handlers_router, admin_post_router]