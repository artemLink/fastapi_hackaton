from fastapi import APIRouter, Body, Depends
from sqlalchemy import func
from app.forms import book_of_references
from app.models import connect_db, references_table, Base, news_table, gum_help_table

router = APIRouter()


@router.get('/api/GetReferences/{id_from}')
def references(id_from: int, database=Depends(connect_db)):
    book = {'content': []}

    count_of_help = database.query(references_table).order_by(references_table.id.desc()).first()
    if count_of_help.id - id_from >= 1:
        req = database.query(references_table).filter(references_table.id > id_from).all()
        for item in req:
            book['content'].append(
                {'title': item.title,
                  'descript': item.descript}
            )
    elif count_of_help.id == 0:
        req = database.query(references_table).all()
        for item in req:
            book['content'].append(
                {{'title': item.title,
                  'descript': item.descript}}
            )
    else:
        return {'content': []}

    return book


@router.get('/api/GetNews/{id_from}')
def news(id_from: int, database=Depends(connect_db)):
    book = {'content': []}
    count_of_news = database.query(news_table).order_by(news_table.id.desc()).first()
    if count_of_news.id - id_from >= 1:
        req = database.query(news_table).filter(news_table.id > id_from).all()
        for item in req:
            book['content'].append(
                {'title': item.title,
                 'link': item.link,
                 'hash': item.hash}
            )
    elif count_of_news.id == 0:
        req = database.query(news_table).all()
        for item in req:
            book['content'].append(
                {'title': item.title,
                 'link': item.link,
                 'hash': item.hash}
            )
    else:
        return {'content': []}

    return book


@router.get('/api/GetGum/{city}')
def gum_help(city: str, database=Depends(connect_db)):
    book = {'content': []}
    items = database.query(gum_help_table).filter(gum_help_table.city == city).all()

    for item in items:
        book['content'].append(
            {
                'title': item.title,
                'description': item.description,
                'city': item.city,
                'address': item.address

            }
        )

    return book
