from pydantic import BaseSettings, Field
import os
from dotenv import load_dotenv

load_dotenv()

class Configuration(BaseSettings):
  # app_id: str
  app_id: str = Field(env="app_id")