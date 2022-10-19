from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from app.config import DATABASE_URL


def main():
    engine = create_engine(DATABASE_URL)
    session = Session(bind=engine.connect())
    session.execute(
        """
        create table references_table (
        id integer not null primary key,
        title varchar(256),
        descript varchar(256)
        );
        """
    )

    session.execute("""
    create table news_table (
    id integer not null primary key,
    title varchar(256),
    hash int(256),
    link varchar(256)
    );
    """)

    session.execute("""
    create table gum_help_table (
    id integer not null primary key,
    title varchar(256),
    city varchar(256),
    address varchar(256),
    description varchar(256));
    """)


if __name__ == '__main__':
    main()