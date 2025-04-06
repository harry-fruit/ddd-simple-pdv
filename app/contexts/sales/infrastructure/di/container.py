from dependency_injector import containers, providers
from infrastructure.db.deps import get_db

class Container(containers.DeclarativeContainer):
    db = providers.Resource(get_db)
    