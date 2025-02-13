from fastapi import FastAPI
from fastapi.responses import JSONResponse
import json

app = FastAPI()

def baca_data():
    with open("mahasiswa.json", "r") as file:
        data= json.load(file)
    return data

@app.get("/")
def get_data():
    try:
        data = baca_data()  

        nama_dan_umur = [{"nama": mhs["nama"], "umur": mhs["umur"]} for mhs in data]

        result = {
            "semua_data": data,
            "nama_dan_umur": nama_dan_umur
        }

        return JSONResponse(content=result)
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
