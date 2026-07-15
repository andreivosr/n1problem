from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

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