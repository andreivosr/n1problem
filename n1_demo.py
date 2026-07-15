from sqlalchemy import event
from sqlalchemy.orm import joinedload, sessionmaker
from models import Cliente
from engine import engine

contador = 0
@event.listens_for(engine, "before_cursor_execute")
def contar_querrys(conn, cursor, statement, parameters, context, executemany):
    global contador
    contador += 1


Session = sessionmaker(bind=engine)
session = Session()


clientes = session.query(Cliente).all()

for cliente in clientes:
    print(cliente.pedidos)
    for pedido in cliente.pedidos:
        print(f"Pedido {pedido.ped_codigo} - Total: {pedido.ped_total}")

print("=" * 30)
print()
print(f"Total de queries: {contador}")
print()
print("=" * 30)

session.close()