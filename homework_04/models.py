import os
from loguru import logger
import asyncio

from sqlalchemy import (
    Column,
    String,
    Integer,
    ForeignKey,
)

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

# PG_CONN_URI = os.environ.get("SQLALCHEMY_PG_CONN_URI") or "postgresql+asyncpg://username:passwd!@localhost/blog"
# PG_ASYNC_CONN_URI = 'postgresql+asyncpg://username:passwd!@localhost/blog'

PG_ASYNC_CONN_URI = os.environ.get("SQLALCHEMY_PG_CONN_URI") \
                    or "postgresql+asyncpg://username:passwd!@localhost/blog"

engine = create_async_engine(PG_ASYNC_CONN_URI, echo=False)
Base = declarative_base()
Session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

cmd = 'docker compose up -d'


async def create_pg_docker(cmd):
    result = await asyncio.create_subprocess_shell(cmd)
    await result.communicate()


logger.info('____pg docker rdy')


async def created_db_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


async def save_user_in_db(u_data):
    async with Session() as session:
        async with session.begin():
            for user in u_data:
                name = user['name']
                username = user['username']
                email = user['email']
                user = User(name=name, username=username, email=email)
                session.add(user)


async def save_post_in_db(p_data):
    async with Session() as session:
        async with session.begin():
            for post in p_data:
                title = post['title']
                body = post['body']
                user_id = post['userId']
                post = Post(title=title, body=body, user_id=user_id)
                session.add(post)


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, default='', server_default='')
    username = Column(String, nullable=False, default='', server_default='')
    email = Column(String, nullable=False, default='', server_default='')

    posts = relationship('Post', back_populates='user')

    def __str__(self):
        return f'{self.__class__.__name__}(id={self.id}, name={self.name!r}, email={self.email},' \
               f'created_at={self.created_at!r})'

    def __repr__(self):
        return str(self)


class Post(Base):
    __tablename__ = 'posts'

    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable='', default='', server_default='')
    body = Column(String, nullable='', default='', server_default='')

    user = relationship('User', back_populates='posts')

    def __str__(self):
        return f'{self.__class__.__name__}(id={self.id}, title={self.title!r}, body={self.body!r})'

    def __repr__(self):
        return str(self)
