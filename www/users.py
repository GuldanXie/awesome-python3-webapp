import orm
import  asyncio
from models import User,Blog,Comment

loop=asyncio.get_event_loop()
async def test():
    await orm.create_pool(loop,user='root',password='',db='awesome')

    u=User(name='Test',email='xjm.@example.com',passwd='1234567890',image='about:blank')

    await u.save()

loop.run_until_complete(test())
