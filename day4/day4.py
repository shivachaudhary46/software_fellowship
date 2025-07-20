from fastapi import FastAPI

# initalizing object of FastApi 
app = FastAPI()

# adding route 
@app.get("/")
def home():
    return {"hello world"}

@app.get("/users/{user_id}")
def about(user_id):
    return {"user": user_id, "name": "shiva"}

# if __name__ == "__main__":
#     app.run(debug=True)