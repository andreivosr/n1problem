from sqlalchemy import create_engine

engine = create_engine(
    "mysql+pymysql://root:@localhost/db_loja",
    echo=True
)
