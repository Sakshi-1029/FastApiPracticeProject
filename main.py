import uvicorn
from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware, db
from fastapi.middleware.cors import CORSMiddleware
from apps.crud.models import ToDo
from apps.crud.schema import Item
from core.config import settings

app = FastAPI()

app.add_middleware(DBSessionMiddleware, db_url=settings.DATABASE_URL)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/healthchecker")
def root():
    return {"message": "Hello World"}


@app.get("/api/getitem/")
def getItems():
    query = db.session.query(ToDo).all()
    return query


@app.post("/api/post/item", response_model=Item)
def postItems(item: Item):
    db_item = ToDo(id=item.id, task=item.task)
    db.session.add(db_item)
    db.session.commit()
    return db_item




# if __name__ == "__main__":
    # uvicorn.run("app.api:app", host="0.0.0.0", port=8081, reload=True)