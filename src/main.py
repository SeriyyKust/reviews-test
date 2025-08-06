from fastapi import FastAPI
from fastapi.responses import JSONResponse


app = FastAPI()


@app.get(
    path="/test",
    summary="Тестовая ручка для проверки запуска приложения",
)
async def api_create_review():
    return JSONResponse(status_code=200, content={"message": "Приложение запущено"})
