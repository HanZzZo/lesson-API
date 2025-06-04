from sqlalchemy import create_engine, Column, String, Table, MetaData
from sqlalchemy.orm import sessionmaker

DB_PATH = "sqlite:///countries.db"
engine = create_engine(DB_PATH)
Session = sessionmaker(bind=engine)
metadata = MetaData()

countries_table = Table(
    'countries', metadata,
    Column('code', String, primary_key=True),
    Column('name', String),
    Column('capital', String),
    Column('languages', String),
    Column('continent', String),
)

def init_db():
    metadata.create_all(engine)

def save_countries(countries, continent_name):
    session = Session()
    with engine.begin() as conn:
        # Очистим данные по континенту перед вставкой
        conn.execute(countries_table.delete().where(countries_table.c.continent == continent_name))
        for c in countries:
            langs = ', '.join(l['name'] for l in c['languages']) if c['languages'] else ''
            conn.execute(countries_table.insert().values(
                code=c['code'],
                name=c['name'],
                capital=c.get('capital', ''),
                languages=langs,
                continent=continent_name
            ))
    session.close()
