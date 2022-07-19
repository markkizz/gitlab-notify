from __future__ import annotations
from fastapi import FastAPI
from dependency_injector import containers
from typing import Type

from configurations.config import Configuration
from app.containers import ApplicationContainer
# from modules.v1.routers import router as api_v1_router
from modules.HealthCheck.router import router as health_check_v1

class Application:
  def __init__(self, server: Type[FastAPI]) -> None:
    self.server = server
    self.container = ApplicationContainer

    self.routers = []
    return

  def __initialize_configuration(self) -> Application:
    self.container.config.from_pydantic(Configuration())
    return self

  def __initialize_router(self) -> Application:
    self.server.include_router(health_check_v1)
    return self

  def start(self):
    self.__initialize_configuration()
    self.__initialize_router()
    self.container.wire(modules=[__name__])
