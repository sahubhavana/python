@app.get("/pagination")
def pagination(page: int, limit: int):
    

    start = (page - 1) * limit
    end = start + limit

    return data[start:end]
           
from pydantic import BaseModel

class Student(BaseModel):
    id: int
    name: str
    age: int
    gender:str
    course:str
    branch:str
    marks: float
    city:str     
    
