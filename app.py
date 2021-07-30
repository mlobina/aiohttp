from aiohttp import web
import aiopg

from config import DB_DSN
from views import IndexView, UserView, UsersView, AdvertisementView, AdvertisementsView
from models import db


app = web.Application()


async def set_connection():
    """db-объект подключается к базе данных"""

    return await db.set_bind(DB_DSN)


async def disconnect():
    """db-объект отключается от базы данных"""

    return await db.pop_bind().close()


async def orm_engine(app):
    """менеджер для работы с БД"""

    app['db'] = db
    await set_connection()
    await db.gino.create_all()
    yield
    await disconnect()


async def pg_pool(app):
    """создаем пул соединений"""

    async with aiopg.create_pool(DB_DSN) as pool:
        app['pg_pool'] = pool
        yield
        pool.close()


#  регистрация контекста
app.cleanup_ctx.append(orm_engine)
app.cleanup_ctx.append(pg_pool)

#  регистрация путей
app.add_routes([web.get('/', IndexView),
                web.get('/users', UsersView),
                web.get(r'/user/{user_id:\d+}', UserView),
                web.post('/user', UserView),
                web.get('/advertisements', AdvertisementsView),
                web.get(r'/advertisement/{advertisement_id:\d+}', AdvertisementView),
                web.post('/advertisement', AdvertisementView),
                web.patch(r'/advertisement/{advertisement_id:\d+}', AdvertisementView),
                web.delete(r'/advertisement/{advertisement_id:\d+}', AdvertisementView),
                ])
