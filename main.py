# from fastapi import FastAPI, Header
# from typing import Optional
#
# app = FastAPI()
#
# @app.get('/')
# async def root():
#     return {'msg': 'Server is running'}
#
# @app.get('/greet/{name}')       # Path Parameter http://127.0.0.1:8000/greet/Ansh
# async def greet(name: str) -> dict:
#     return {'msg': f'Hellow {name}'}
#
# @app.get('/greet')      # Query Parameter http://127.0.0.1:8000/greet?name=Ansh
# async def greet(age: int, name:Optional[str] = 'User') -> dict:
#     return {'msg': f'Hello {name}, age: {age}'}
#
# @app.post('/create_book')
# async def create_book(book_data : BookCreateModel):
#     return {
#         'title' : book_data.title,
#         'author' : book_data.author
#     }
#
#
# @app.get('/get_headers')
# async def get_headers(
#         accept : str = Header(None),
#         content_type : str = Header(None),
#         user_agent : str = Header(None),
#         host : str = Header(None)
# ):
#     request_headers = {
#         'Accept': accept,
#         'Content Type' : content_type,
#         'User agent' : user_agent,
#         'Host' : host
#     }
#
#     return request_headers