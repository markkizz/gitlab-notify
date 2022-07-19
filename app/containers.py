from dependency_injector import containers, providers

class ApplicationContainer(containers.DeclarativeContainer):
  config = providers.Configuration()

  wiring_config = containers.WiringConfiguration(
    modules=[
      "modules"
    ]
  )