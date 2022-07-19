import os
import uvicorn
from fastapi import FastAPI

# from app.app import Application
from dotenv import load_dotenv
from configurations.config import Configuration
from modules.router import router as health_check_v1
# from modules.HealthCheck.router import router as health_check_v1
from app.containers import ApplicationContainer

def create_app():
  print("##################### RUN ######################")
  app = FastAPI()
  container = ApplicationContainer()
  # container.config.from_pydantic(Configuration())
  # container.config.app_id.from_env("APP_ID")
  os.environ["API_KEY"] = "secret"
  os.environ["API_TIMEOUT"] = "5"

  container.config.key.from_env("API_KEY")
  container.config.timeout.from_env("API_TIMEOUT")
  app.container = container
  app.include_router(health_check_v1)
  return app

app = create_app()
