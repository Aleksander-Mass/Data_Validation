from fastapi import FastAPI, Path
from typing import Annotated

# 1. Создаем объект приложения
app = FastAPI()

# 2. Главная страница
@app.get("/")
async def read_main() -> dict:
    return {"message": "Главная страница"}

# 3. Страница администратора
@app.get("/user/admin")
async def read_admin():
    return {"message": "Вы вошли как администратор"}

# 4. Страницы пользователей по параметру пути с валидацией
@app.get("/user/{user_id}")
async def read_user(
    user_id: Annotated[
        int,
        Path(
            title="Enter User ID",
            ge=1,
            le=100,
            description="ID пользователя должен быть целым числом от 1 до 100",
            example=1
        )
    ]
):
    return {"message": f"Вы вошли как пользователь № {user_id}"}

# 5. Страницы пользователей с параметрами в пути и валидацией
@app.get("/user/{username}/{age}")
async def read_user_details(
    username: Annotated[
        str,
        Path(
            title="Enter username",
            min_length=5,
            max_length=20,
            description="Имя пользователя должно содержать от 5 до 20 символов",
            example="UrbanUser"
        )
    ],
    age: Annotated[
        int,
        Path(
            title="Enter age",
            ge=18,
            le=120,
            description="Возраст должен быть числом от 18 до 120",
            example=24
        )
    ]
):
    return {"message": f"Информация о пользователе. Имя: {username}, Возраст: {age}"}

# uvicorn main:app --reload