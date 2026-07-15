from main import clientes, contador, session

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