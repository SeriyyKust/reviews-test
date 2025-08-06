from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # В дальнейшем можно переключить на считывание переменных окружения
    db_url: str = "sqlite+aiosqlite:///reviews.db"
    db_echo: bool = True


settings = Settings()
