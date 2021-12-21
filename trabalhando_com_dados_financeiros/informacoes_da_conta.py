import MetaTrader5 as mt5
import pandas as pd


mt5.initialize()


informacoes_da_conta = mt5.account_info()

informacoes_da_conta_como_dicionario = informacoes_da_conta._asdict()

for chave in informacoes_da_conta_como_dicionario:
    print(f"{chave} = {informacoes_da_conta_como_dicionario[chave]}")
    print()

data_frame = pd.DataFrame(list(
    informacoes_da_conta_como_dicionario.items()), columns=['propriedade', 'valor'])

print("Informações da conta em Data Frame")
print(data_frame)


mt5.shutdown()
