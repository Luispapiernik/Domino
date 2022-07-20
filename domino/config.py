from os.path import exists

from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    # This specify the color used for highlight a element selected in some window
    color_selected_element: int = Field(None, env="COLOR_SELECTED_ELEMENT")
    # This color is used to highlight the active panel/window
    color_selected_panel: int = Field(None, env="COLOR_SELECTED_PANEL")

    info_window_width: int = Field(None, env="INFO_WINDOW_WIDTH")
    tokens_per_player: int = Field(None, env="TOKENS_PER_PLAYER")
    token_max_number: int = Field(None, env="TOKEN_MAX_NUMBER")

    class Config:
        env_file = (
            "user_settings.env" if exists("user_settings.env") else "settings.env"
        )
        env_file_encoding = "utf-8"


settings = Settings()
