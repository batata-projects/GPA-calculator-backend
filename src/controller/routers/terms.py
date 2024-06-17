from src.controller.routers._base_router import BaseRouter
from src.controller.schemas import TermQuery
from src.db.dependencies import get_term_dao
from src.db.models import Term

terms_router = BaseRouter[Term](
    prefix="/terms",
    tags=["Terms"],
    name="Term",
    model=Term,
    query=TermQuery,
    get_dao=get_term_dao,
).build_router()
