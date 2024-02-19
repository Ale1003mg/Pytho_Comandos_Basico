import Dao_Usuario
import Dto_Usuario
from fastapi import FastAPI
app = FastAPI()


#api server
@app.get("/hello")
def hello():
    return {"Hello Word!"}



