import pandas as pd
import openpyxl 
import os  
from twilio.rest import Client

account_sid = "TWILIO_ACCOUNT_SID"
auth_token = "TWILIO_AUTH_TOKEN"
client = Client(account_sid, auth_token)

lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

# Generic path - same folder as script or subfolder "arquivos"
caminho_pasta = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'arquivos')

for mes in lista_meses:
    caminho_arquivo = os.path.join(caminho_pasta, f'{mes}.xlsx')
    
    tabela_vendas = pd.read_excel(caminho_arquivo)

    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        print(f'No mês {mes} encontrou alguém que bateu a meta! Vendedor: {vendedor}, Vendas: {vendas}')
        message = client.messages.create(
                              body=f'No mês {mes} encontrou alguém que bateu a meta! Vendedor: {vendedor}, Vendas: {vendas}',
                              from_='+16672200117',
                              to='PHONE_NUMBER')
print(message.sid)
