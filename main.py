from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/") 
def main():
    return {"hello": "world"}  

if __name__ == "__main__":
    uvicorn.run(app,host='0.0.0.0') 