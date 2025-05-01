# Don't Remove Credit @Ott_Sandhu, @Baii_Ji
# Ask Doubt on telegram @Baii_Ji





from aiohttp import web
from .route import routes


async def web_server():
    web_app = web.Application(client_max_size=30000000)
    web_app.add_routes(routes)
    return web_app
