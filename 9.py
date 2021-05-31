import aiohttp
from aiohttp import web


async def get_food_image(request):
    food_name = request.match_info.get('food')
    url = f"https://foodish-api.herokuapp.com/api/images/{food_name}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as request:
            text = await request.text()
            print(request.status)
            print(text)
            return web.Response(text=text)

if __name__ == '__main__':
    app = web.Application()
    app.add_routes([web.get('/{food}', get_food_image)])
    web.run_app(app)