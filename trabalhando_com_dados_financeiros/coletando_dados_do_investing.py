import investpy as inv

# df = inv.get_stock_historical_data(
#     stock='AAPL', country='United States', from_date='01/01/2020', to_date='01/01/2021')


# print(df.head())

buscar_resultado = inv.search_quotes(text='nu', products=['stocks'],
                                     countries=['united states'], n_results=1)

for resultado in buscar_resultado:
    print(f"{resultado}: {resultado.name}")
