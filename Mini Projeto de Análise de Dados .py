#!/usr/bin/env python
# coding: utf-8

# # Mini Projeto de Análise de Dados
# 
# 
# ### O que temos?
# 
# Temos os dados de 2019 de uma empresa de prestação de serviços. 
# 
# - CadastroFuncionarios
# - CadastroClientes
# - BaseServiçosPrestados
# 
# Obs1: Para ler arquivos csv, temos o read_csv<br>
# Obs2: Para ler arquivos xlsx (arquivos em excel normais, que não são padrão csv), temos o read_excel
# 
# ### O que queremos saber/fazer?
# 
# 1. Valor Total da Folha Salarial -> Qual foi o gasto total com salários de funcionários pela empresa? <br>
#     Sugestão: calcule o salário total de cada funcionário, salário + benefícios + impostos, depois some todos os salários
#     
#     
# 2. Qual foi o faturamento da empresa?<br>
#     Sugestão: calcule o faturamento total de cada serviço e depois some o faturamento de todos
#     
#     
# 3. Qual o % de funcionários que já fechou algum contrato?<br>
#     Sugestão: na base de serviços temos o funcionário que fechou cada serviço. Mas nem todos os funcionários que a empresa tem já fecharam algum serviço.<br>
#     . Na base de funcionários temos uma lista com todos os funcionários<br>
#     . Queremos calcular Qtde_Funcionarios_Fecharam_Serviço / Qtde_Funcionários_Totais<br>
#     . Para calcular a qtde de funcionários que fecharam algum serviço, use a base de serviços e conte quantos funcionários tem ali. Mas lembre-se, cada funcionário só pode ser contado uma única vez.<br><br>
#     Dica: se você aplicar o método .unique() em uma variável que é apenas 1 coluna de um dataframe, ele vai excluir todos os valores duplicados daquela coluna.<br>
#     Ex: unicos_colunaA = dataframe['colunaA'].unique() te dá como resposta uma lista com todos os itens da colunaA aparecendo uma única vez. Todos os valores repetidos da colunaA são excluidos da variável unicos_colunaA 
#     
#     
# 4. Calcule o total de contratos que cada área da empresa já fechou
# 
# 
# 5. Calcule o total de funcionários por área
# 
# 
# 6. Qual o ticket médio mensal (faturamento médio mensal) dos contratos?<br>
#     Dica: .mean() calcula a média -> exemplo: media_colunaA = dataframe['colunaA'].mean()
# 
# Obs: Lembrando as opções mais usuais de encoding:<br>
# encoding='latin1', encoding='ISO-8859-1', encoding='utf-8' ou então encoding='cp1252'
# 
# Observação Importante: Se o seu código der um erro na hora de importar os arquivos:<br>
# - CadastroClientes.csv
# - CadastroFuncionarios.csv
# 
# Use separador ";" (ponto e vírgula) para resolver e inclua o parâmetro decimal ',' para o pandas identificar os números corretamente

# In[2]:


import pandas as pd
import matplotlib

funcionarios_df = pd.read_csv('CadastroFuncionarios.csv', sep=';', decimal=',')
clientes_df = pd.read_csv('CadastroClientes.csv', sep=';', decimal=',')
servicos_df = pd.read_excel('BaseServiçosPrestados.xlsx')

#  Retirar colunas Estado Civil e Cargo da tabela de funiconários.
# Qndo vc da um drop, vc ten que informar axis para retirar uma coluna; axis = 0 p índice e axis = 1 p coluna.

funcionarios_df = funcionarios_df.drop(['Estado Civil', 'Cargo'], axis=1)
display(funcionarios_df)
display(clientes_df)
display(servicos_df)

# Folha Salarial
# Criando a nova coluna Salário Total.
funcionarios_df['Salario Total'] = funcionarios_df['Salario Base'] + funcionarios_df['Impostos'] + funcionarios_df['Beneficios'] + funcionarios_df['VT'] + funcionarios_df['VR']
print('Total de folha salarial é de R${:,}'.format(sum(funcionarios_df['Salario Total'])))

# Faturamento da Empresa
# Juntando apenas as colunas ID CLinete e Tempo Total de Contrato (Meses) da tabela servico_df,
# com as colunas ID Cliente e Valor Contrato Mensa, da tabela  clientes_df.

faturamento_df = servicos_df[['ID Cliente', 'Tempo Total de Contrato (Meses)']].merge(clientes_df[['ID Cliente', 'Valor Contrato Mensal']])
display(faturamento_df)
print('Faturamento foi de R${:,}'.format(sum(faturamento_df['Tempo Total de Contrato (Meses)'] * faturamento_df['Valor Contrato Mensal'])))

# Percentual de Funcionários que fechou contrato
qtde_funcionarios_fecharam = len(servicos_df['ID Funcionário'].unique())
qtde_funcionarios_totais = len(funcionarios_df['ID Funcionário'])
print('Percentual foi de {:.2%}'.format(qtde_funcionarios_fecharam / qtde_funcionarios_totais))


# Total de Contratos por Área
# value_counts, conta basicamente qntas vezes um valor aparece.
# No merge, primeiro vc põe a tabela que irá receber as informações e depois a que irá dar.

contratos_area_df = servicos_df[['ID Funcionário']].merge(funcionarios_df[['ID Funcionário', 'Area']])
display(contratos_area_df)
qtde_contratos_area = contratos_area_df['Area'].value_counts()
print(qtde_contratos_area)
qtde_contratos_area.plot(kind='bar')


# Total de Funcionários por Área
qtde_funcionarios_area = funcionarios_df['Area'].value_counts()
print(qtde_funcionarios_area)
qtde_funcionarios_area.plot(kind='bar')


# Ticket Médio Mensal
ticket_medio = clientes_df['Valor Contrato Mensal'].mean()
print('O ticket médio mensal é de R${:,.2f}'.format(ticket_medio))


# In[ ]:




