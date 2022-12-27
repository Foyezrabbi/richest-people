from fastapi import FastAPI

app = FastAPI()

richest_people_list = {
    "Elon Musk": "12 B",
    "Mark": "10 B"
}

@app.get("/richest-people")
def richest_people():
    return richest_people_list