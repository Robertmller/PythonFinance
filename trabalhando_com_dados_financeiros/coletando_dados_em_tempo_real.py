import MetaTrader5 as mt5
import time

mt5.initialize()

ativo = "USDCHF"

while(True):
    time.sleep(0.5)
    mt5.symbol_select(ativo)
    print(mt5.symbol_info_tick(ativo).last)

mt5.shutdown()
