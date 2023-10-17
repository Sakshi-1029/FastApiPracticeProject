# from fastapi import FastAPI
# from fastapi_sqlalchemy import db

# from apps.crud.models import ToDo
# from apps.crud.schema import Item

# app = FastAPI()


# @app.get("/api/healthchecker")
# def root():
#     return {"message": "Hello World"}


# @app.get("/api/getitem/")
# def getItems():
#     query = db.session.query(ToDo).all()
#     return query


# @app.post("/api/post/item", response_model=Item)
# def postItems(item: Item):
#     db_item = ToDo(id=item.id, task=item.task)
#     db.session.add(db_item)
#     db.session.commit()
#     return db_item