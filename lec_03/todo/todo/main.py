from fastapi import FastAPI
from sqlmodel import SQLModel,create_engine, Field,Session

import settings


#create model(conbined data and table model)
class Todo (SQLModel, table= True):
    id: int | None = Field(default=None,primary_key=True) #None when database creates by itself
    content: str = Field(index= True, min_length=3,max_length = 54) # index will not search the whole data base hence making the process faster
    is_complete :bool = Field()

##create the engine(for the whole application)
connection_string:str = str(settings.DATABASE_URL).replace("postgesql","postgresql+psycopg")
engine = create_engine(connection_string,connect_args={"sslmode":"require"},pool_recycle=300,pool_size = 8,echo= True) #CONVERT python to sql

SQLModel.metadata.create_all(engine)
todo1 : Todo = Todo(content = "first task")
todo2 : Todo = Todo(content = "second task")
 ## session (for each user)
 
session = Session(engine)
# create todo in database
session.add(todo1) #adds just like git add
print(f"after commit {todo1} 🌞") ## must add echo=True in engine
session.add(todo2)
session.commit()
print(f'after commit {todo2} ☀')
session.close()




app = FastAPI()
#get request for the root route
@app.get("/")
async def root():
    return{"hello":"from the otherside"}
#get request for the route test1
@app.get("/test1")
async def test1():
    return{"test1":"if you are seeing this it is working😊"}
