from aiohttp import web

from models import User, Advertisement


class IndexView(web.View):

    async def get(self):
        return web.json_response({'text': 'Welcome to advertise'})


class UserView(web.View):

    async def get(self):
        user_id = int(self.request.match_info['user_id'])
        user = await User.get_or_404(user_id)
        return web.json_response(user.to_dict())

    async def post(self):
        data = await self.request.json()
        user = await User.create_instance(**data)
        return web.json_response(user.to_dict())

    async def delete(self):
        instance_id = int(self.request.match_info['user_id'])
        instance = await User.get_or_404(instance_id)
        await instance.delete()
        return web.json_response({'status': 'deleted'})


class UsersView(web.View):

    async def get(self):
        pool = self.request.app['pg_pool']
        async with pool.acquire() as conn:
            async with conn.cursor() as cursor:
                await cursor.execute('SELECT id, username FROM users')
                users = await cursor.fetchall()
                return web.json_response(users)


class AdvertisementView(web.View):

    async def get(self):
        advertisement_id = int(self.request.match_info['advertisement_id'])
        advertisement = await Advertisement.get_or_404(advertisement_id)
        return web.json_response(advertisement.to_dict())

    async def post(self):
        data = await self.request.json()
        advertisement = await Advertisement.create_instance(**data)
        return web.json_response(advertisement.to_dict())

    async def patch(self):
        instance_id = int(self.request.match_info['advertisement_id'])
        instance = await Advertisement.get_or_404(instance_id)
        data = await self.request.json()
        await instance.update(**data).apply()
        return web.json_response({'status': 'patched'})

    async def delete(self):
        instance_id = int(self.request.match_info['advertisement_id'])
        instance = await Advertisement.get_or_404(instance_id)
        await instance.delete()
        return web.json_response({'status': 'deleted'})


class AdvertisementsView(web.View):

    async def get(self):
        pool = self.request.app['pg_pool']
        async with pool.acquire() as conn:
            async with conn.cursor() as cursor:
                await cursor.execute('SELECT id, title, text FROM advertisements')
                advertisements = await cursor.fetchall()
                return web.json_response(advertisements)

