import MetaTrader5 as mt5


mt5.initialize()

ativos = mt5.symbols_total()

if ativos > 0:
    print(f"Total de ativos disponíveis para Trade: {ativos}")
else:
    print("Nenhum ativo encontrado!")

mt5.shutdown()
