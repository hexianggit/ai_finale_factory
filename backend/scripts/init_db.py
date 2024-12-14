import asyncio
import aiomysql
from urllib.parse import urlparse
from core.config import settings

async def init_database():
    # 解析数据库URL
    url = urlparse(settings.DATABASE_URL)
    host = url.hostname
    port = url.port or 3306
    user = url.username
    password = url.password
    database = url.path.strip('/')

    try:
        # 创建连接
        conn = await aiomysql.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            charset='utf8mb4',
            connect_timeout=60
        )
        
        async with conn.cursor() as cur:
            # 创建数据库（如果不存在）
            await cur.execute(f"CREATE DATABASE IF NOT EXISTS {database} CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci")
            print(f"Database {database} initialized successfully")
            
    except Exception as e:
        print(f"Error initializing database: {e}")
        raise
    finally:
        conn.close()
        await conn.wait_closed()

if __name__ == "__main__":
    asyncio.run(init_database()) 