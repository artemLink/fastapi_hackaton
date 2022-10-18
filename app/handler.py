from fastapi import APIRouter, Body, Depends
from sqlalchemy import func
from app.forms import book_of_references
from app.models import connect_db, references_table, Base, news_table, gum_help_table

router = APIRouter()


@router.post('api/GetReferences')
def references(database=Depends(connect_db)):
    book = {'content': []}
    req = database.query(references_table).all()
    for item in req:
        book['content'].append({'title': item.title,
                                'descript': item.descript.split(';')})

    return book


@router.get('api/GetNews/{id_from}')
def news(id_form: int, database=Depends(connect_db)):
    book = {'content': []}
    count_of_news = database.query(news_table).order_by(news_table.id.desc()).first()
    if count_of_news.id - id_form >= 1:
        req = database.query(news_table).filter(news_table.id > id_form).all()
        for item in req:
            book['content'].append(
                {'title': item.title,
                 'descript': item.descript,
                 'region': item.region}
            )
    elif count_of_news.id == 0:
        req = database.query(news_table).all()
        for item in req:
            book['content'].append(
                {'title': item.title,
                 'descript': item.descript,
                 'region': item.region}
            )
    else:
        return {'content': []}

    return book


@router.get('api/GetGum/{city}')
def gum_help(city: str, database=Depends(connect_db)):
    book = {'content': []}
    items = database.query(gum_help_table).filter(gum_help_table.city == city).all()

    for req in items:
        book['content'].append(
            {
                'title': req.title,
                'address': req.address,
                'timing': req.timing
            }
        )

    return book
