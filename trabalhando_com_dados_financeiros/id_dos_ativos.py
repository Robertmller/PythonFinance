import MetaTrader5 as mt5


mt5.initialize()

id_ativos = mt5.symbols_get()

contador = 0

for id in id_ativos:
    contador += 1
    print(f"{contador}: {id.name}")
    if contador == 5:
        break

mt5.shutdown()
