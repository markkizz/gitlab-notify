from fastapi import APIRouter, Depends
from dependency_injector.wiring import inject, Provide
from app.containers import ApplicationContainer
from typing import Type

router = APIRouter()

@router.get("/")
@inject
def index(
  config: ApplicationContainer.config = Depends(Provide[ApplicationContainer.config.test])
):
  print(config)
  return {
    "status": config
  }