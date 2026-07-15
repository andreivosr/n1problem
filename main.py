from sqlalchemy import create_engine, Column, Integer, String, DateTime, event, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base, relationship


engine = create_engine(
    "mysql+pymysql://root:@localhost/db_loja",
    echo=True
)


#Contar o querrys
contador = 0
@event.listens_for(engine, "before_cursor_execute")
def contar_queries(conn, cursor, statement, parameters, context, executemany):
    global contador
    contador += 1


#Mapear tb_clientes e tb_pedidos
Base = declarative_base()
class Cliente(Base):
    __tablename__ = "clientes"

    cli_codigo = Column(Integer, primary_key=True)
    cli_nome = Column(String(100))
    cli_email = Column(String(100))
    cli_senha_hash = Column(String(150))
    cli_criado_em = Column(DateTime)

    pedidos = relationship("Pedido", back_populates="cliente")

class Pedido(Base):
    __tablename__ = "pedidos"

    ped_codigo = Column(Integer, primary_key=True)
    ped_cli_codigo = Column(Integer, ForeignKey("clientes.cli_codigo"))
    ped_status = Column(String(30))
    ped_total = Column(Integer)
    ped_datacriacao = Column(DateTime)

    cliente = relationship("Cliente", back_populates="pedidos")

Session = sessionmaker(bind=engine)
session = Session()
clientes = session.query(Cliente).all()

#PROBLEMA N+1
for cliente in clientes:
    print(cliente.cli_nome)

    for pedido in cliente.pedidos:
        print(f"Pedido {pedido.ped_codigo} - Total: {pedido.ped_total}")

print("=" * 30)
print()
print(f"Total de queries: {contador}")
print()
print("=" * 30)

session.close()
