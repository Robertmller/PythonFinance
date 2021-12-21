import MetaTrader5 as mt5

mt5.initialize()

ativo = "EURUSD"

ativo_selecionado = mt5.symbol_select(ativo, True)

info_ativo = mt5.symbol_info(ativo)

info_do_ativo_como_dicionario = mt5.symbol_info(ativo)._asdict()

for ativo in info_do_ativo_como_dicionario:
    print(f"{ativo}  {info_do_ativo_como_dicionario[ativo]}")


mt5.shutdown()
