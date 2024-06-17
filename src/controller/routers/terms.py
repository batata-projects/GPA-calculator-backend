from src.controller._base.router import BaseRouter
from src.db.dependencies import get_term_dao
from src.db.models import Term

terms_router = BaseRouter[Term](
    prefix="/terms",
    tags=["Terms"],
    name="Term",
    model=Term,
    get_dao=get_term_dao,
).build_router()
