from os.path import exists

from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    # color para la seleccion de un elemento de alguna ventana(ficha, opciones)
    color_selected_element: int = Field(None, env="COLOR_SELECTED_ELEMENT")
    # color para el tablero activo(tablero de fichas o tablero de jugador)
    color_selected_panel: int = Field(None, env="COLOR_SELECTED_PANEL")

    class Config:
        env_file = (
            "user_settings.env" if exists("user_settings.env") else "settings.env"
        )
        env_file_encoding = "utf-8"


settings = Settings()
