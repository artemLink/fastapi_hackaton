from fastapi import APIRouter, Body, Depends
from app.forms import book_of_references
from app.models import connect_db, references_table, Base, news_table, gum_help_table

router = APIRouter()


@router.get('/take_references/{pk}')
def index(pk: int, database=Depends(connect_db)):
    req = database.query(references_table).filter(references_table.id == pk).one_or_none()

    return {'title': req.title,
            'descript': req.descript}


@router.get('/take_news/{pk}')
def index(pk: int, database=Depends(connect_db)):
    req = database.query(news_table).filter(news_table.id == pk).one_or_none()

    return {'title': req.title,
            'descript': req.descript,
            'region': req.region}


@router.get('/take_gum/{pk}')
def gum_help(pk: int, database=Depends(connect_db)):
    req = database.query(gum_help_table).filter(gum_help_table.id == pk).one_or_none()

    return {
        'title': req.title,
        'address': req.address,
        'timing': req.timing
    }
