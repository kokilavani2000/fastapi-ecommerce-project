from fastapi import FastAPI

# create  a instance of FastAPI
app = FastAPI(
    title ="my first e-commerce project API",
    description = "This is a simple e-commerce project API built with FastAPI",
    version = "1.0.0",
)



@app.get("/")
def home():
    return {
        "message": "Welcome to my first e-commerce project API!"
    }
