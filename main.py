import pandas as pd
from twilio.rest import Client
import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

account_sid = "AC298d3f49a3b109ebc8dbe02316f49f1e"
auth_token  = "053feafa1f760334b387c287795fefe5"

client = Client(account_sid, auth_token)


month_list = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho']

for mes in month_list:
    print('\n')
    sales_table = pd.read_excel(f'./Dados Excel/{mes}.xlsx')

    if(sales_table['Vendas'] >= 55000).any():
        vendedor = sales_table.loc[sales_table['Vendas'] >= 55000, 'Vendedor'].values[0]
        vendas = sales_table.loc[sales_table['Vendas'] >= 55000, 'Vendas'].values[0]

        vendas_formatado = locale.currency(vendas, grouping=True)
        
        #SMS
        message = client.messages.create(
            to="+5515996212806", 
            from_="+12568184667",
            body=f"Paranbéns {vendedor}, você acabou de bater sua meta de vendas, seu resultado em vendas foi de {vendas_formatado}!\nAcabou de conseguir uma viagem paga com a familia para o final do ano!")
        print(message.sid)

        


