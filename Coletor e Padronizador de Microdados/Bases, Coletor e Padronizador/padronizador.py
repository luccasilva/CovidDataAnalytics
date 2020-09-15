import csv
import unicodedata

def removeAcentos(text):
    if text!=None:
        try:
            text = unicode(text, 'utf-8')
        except NameError: # unicode is a default on python 3 
            pass

        text = unicodedata.normalize('NFD', text)\
            .encode('ascii', 'ignore')\
            .decode("utf-8")
        return str(text)
    
    else:
        return "N/A"

###### Padronizador AC ######

leitor = csv.DictReader(open('AC.csv', 'r',encoding="utf8"), delimiter=',')

with open('padrao.csv', 'w') as padrao_csv:
    colunas = ['id', 'evolucao_casos', 'municipio', 'cod_ibge', 'uf', 'data_inicio_sintomas', 'idade', 'faixa_etaria', 'sexo', 'etnia', 'obito', 'data_obito']
    escrever = csv.DictWriter(padrao_csv, fieldnames=colunas, delimiter=';', lineterminator='\n')
    escrever.writeheader()
    contador = 1
    for coluna in leitor:
        escrever.writerow({'id': contador, 
                            'evolucao_casos': removeAcentos(coluna['9']),
                            'municipio': removeAcentos(coluna['7']),
                            'cod_ibge': removeAcentos(coluna['14']),
                            'uf': 'AC',
                            'data_inicio_sintomas': removeAcentos(coluna['0']), #data de notificação
                            'idade': removeAcentos(coluna['8']),
                            'faixa_etaria': 'N/A',
                            'sexo': removeAcentos(coluna['4']),
                            'etnia': removeAcentos(coluna['12']),
                            'obito': 'N/A', 
                            'data_obito': 'N/A'})
        contador = contador+1



###### Padronizador AL ######

leitor = csv.DictReader(open('AL.csv', 'r',encoding="utf8"), delimiter=',')

with open('padrao.csv', 'a') as padrao_csv:
    escrever = csv.DictWriter(padrao_csv, fieldnames=colunas, delimiter=';', lineterminator='\n')
    for coluna in leitor:
        escrever.writerow({'id': contador, 
                            'evolucao_casos': removeAcentos(coluna['classificacao']),
                            'municipio': removeAcentos(coluna['municipio_residencia']),
                            'cod_ibge': 'N/A',
                            'uf': 'AL',
                            'data_inicio_sintomas':removeAcentos( coluna['data_resultado_exame']),
                            'idade': removeAcentos(coluna['idade']),
                            'faixa_etaria': 'N/A',
                            'sexo': removeAcentos(coluna['sexo']),
                            'etnia': removeAcentos(coluna['etnia']),
                            'obito': removeAcentos(coluna['situacao_atual']), 
                            'data_obito': removeAcentos(coluna['data_obito'])})
        contador = contador+1


###### Padronizador AP_casos ######

leitor = csv.DictReader(open('AP_casos.csv', 'r',encoding="utf8"), delimiter=',')

with open('padrao.csv', 'a') as padrao_csv:
    escrever = csv.DictWriter(padrao_csv, fieldnames=colunas, delimiter=';', lineterminator='\n')
    for coluna in leitor:
        escrever.writerow({'id': contador, 
                            'evolucao_casos': removeAcentos(coluna['resultadoTeste']),
                            'municipio': removeAcentos(coluna['municipio']),
                            'cod_ibge': 'N/A',
                            'uf': 'AP',
                            'data_inicio_sintomas':  removeAcentos(coluna['dataNotificacao']),
                            'idade':  removeAcentos(coluna['idade']),
                            'faixa_etaria': 'N/A',
                            'sexo':  removeAcentos(coluna['sexo']),
                            'etnia': removeAcentos(coluna['racaCor']),
                            'obito': 'N/A', 
                            'data_obito': 'N/A'})
        contador = contador+1


###### Padronizador AP_obitos ######

leitor = csv.DictReader(open('AP_obitos.csv', 'r',encoding="utf8"), delimiter=',')

with open('padrao.csv', 'a') as padrao_csv:
    escrever = csv.DictWriter(padrao_csv, fieldnames=colunas, delimiter=';', lineterminator='\n')
    for coluna in leitor:
        escrever.writerow({'id': contador, 
                            'evolucao_casos': 'Confirmado',
                            'municipio': removeAcentos(coluna['Município']),
                            'cod_ibge': 'N/A',
                            'uf': 'AP',
                            'data_inicio_sintomas': 'N/A',
                            'idade': 'N/A',
                            'faixa_etaria':  removeAcentos(coluna['Faixa Etária']),
                            'sexo':  removeAcentos(coluna['Sexo']),
                            'etnia': removeAcentos(coluna['Raça/Cor']),
                            'obito': '1', 
                            'data_obito':  removeAcentos(coluna['Data do Óbito'])})
        contador = contador+1

###### Padronizador AM ######

leitor = csv.DictReader(open('AM.csv', 'r',encoding="utf8"), delimiter=';')

with open('padrao.csv', 'a') as padrao_csv:
    escrever = csv.DictWriter(padrao_csv, fieldnames=colunas, delimiter=';', lineterminator='\n')
    for coluna in leitor:
        escrever.writerow({'id': contador, 
                            'evolucao_casos': removeAcentos(coluna['﻿Resultado']),
                            'municipio': removeAcentos(coluna['MunicipioResidencia']),
                            'cod_ibge':  removeAcentos(coluna['CODIGO MUN NOTIFIC']),
                            'uf': 'AM',
                            'data_inicio_sintomas':  removeAcentos(coluna['dt_sin_pri']),
                            'idade': 'N/A',
                            'faixa_etaria': 'N/A',
                            'sexo':  removeAcentos(coluna['SEXO']),
                            'etnia': removeAcentos(coluna['RACA_COR']),
                            'obito': 'N/A', 
                            'data_obito': 'N/A'})
        contador = contador+1

###### Padronizador DF ######

leitor = csv.DictReader(open('DF.csv', 'r',encoding="utf8"), delimiter=';')

with open('padrao.csv', 'a') as padrao_csv:
    escrever = csv.DictWriter(padrao_csv, fieldnames=colunas, delimiter=';', lineterminator='\n')
    for coluna in leitor:
        escrever.writerow({'id': contador, 
                            'evolucao_casos': 'CONFIRMADO',
                            'municipio': 'N/A',
                            'cod_ibge': 'N/A',
                            'uf':  removeAcentos(coluna['UF']),
                            'data_inicio_sintomas':  removeAcentos(coluna['dataPrimeirosintomas']),
                            'idade': 'N/A',
                            'faixa_etaria':  removeAcentos(coluna['Faixa Etária']),
                            'sexo': 'N/A',
                            'etnia': 'N/A',
                            'obito':  removeAcentos(coluna['Óbito']), 
                            'data_obito': 'N/A'})
        contador = contador+1

###### Padronizador ES ######

leitor = csv.DictReader(open('ES.csv', 'r',encoding='latin-1'), delimiter=';')

with open('padrao.csv', 'a') as padrao_csv:
    escrever = csv.DictWriter(padrao_csv, fieldnames=colunas, delimiter=';', lineterminator='\n')
    for coluna in leitor:
        escrever.writerow({'id': contador, 
                            'evolucao_casos': removeAcentos(coluna['Classificacao']),
                            'municipio': removeAcentos(coluna['Municipio']),
                            'cod_ibge': 'N/A',
                            'uf': 'ES',
                            'data_inicio_sintomas':  removeAcentos(coluna['DataDiagnostico']), #data diagnostico
                            'idade':  removeAcentos(coluna['IdadeNaDataNotificacao']),
                            'faixa_etaria':  removeAcentos(coluna['FaixaEtaria']),
                            'sexo':  removeAcentos(coluna['Sexo']),
                            'etnia': removeAcentos(coluna['RacaCor']),
                            'obito': 'N/A', 
                            'data_obito':  removeAcentos(coluna['DataObito'])})
        contador = contador+1

###### Padronizador GO_casos ######

leitor = csv.DictReader(open('GO_casos.csv', 'r',encoding="utf8"), delimiter=';')

with open('padrao.csv', 'a') as padrao_csv:
    escrever = csv.DictWriter(padrao_csv, fieldnames=colunas, delimiter=';', lineterminator='\n')
    for coluna in leitor:
        escrever.writerow({'id': contador, 
                            'evolucao_casos': removeAcentos(coluna['recuperado']),
                            'municipio': removeAcentos(coluna['municipio']),
                            'cod_ibge':  removeAcentos(coluna['codigo_ibge']),
                            'uf': 'GO',
                            'data_inicio_sintomas':  removeAcentos(coluna['data_inicio_sintomas']),
                            'idade': 'N/A',
                            'faixa_etaria':  removeAcentos(coluna['faixa_etaria']),
                            'sexo':  removeAcentos(coluna['sexo']),
                            'etnia': removeAcentos(coluna['raca_cor']),
                            'obito': 'N/A', 
                            'data_obito': 'N/A'})
        contador = contador+1

###### Padronizador GO_obitos ######

leitor = csv.DictReader(open('GO_obitos.csv', 'r',encoding="utf8"), delimiter=';')

with open('padrao.csv', 'a') as padrao_csv:
    escrever = csv.DictWriter(padrao_csv, fieldnames=colunas, delimiter=';', lineterminator='\n')

    for coluna in leitor:
        escrever.writerow({'id': contador, 
                            'evolucao_casos': 'OBITO',
                            'municipio': removeAcentos(coluna['municipio']),
                            'cod_ibge':  removeAcentos(coluna['codigo_ibge']),
                            'uf': 'GO',
                            'data_inicio_sintomas':  removeAcentos(coluna['data_inicio_sintomas']), #data de notificaÃ§Ã£o
                            'idade': 'N/A',
                            'faixa_etaria':  removeAcentos(coluna['faixa_etaria']),
                            'sexo':  removeAcentos(coluna['sexo']),
                            'etnia': removeAcentos(coluna['raca_cor']),
                            'obito': '1', 
                            'data_obito':  removeAcentos(coluna['data_obito'])})
        contador = contador+1

###### Padronizador MS ######

leitor = csv.DictReader(open('MS.csv', 'r',encoding="latin1"), delimiter=',')

with open('padrao.csv', 'a') as padrao_csv:
    escrever = csv.DictWriter(padrao_csv, fieldnames=colunas, delimiter=';', lineterminator='\n')
    for coluna in leitor:
        escrever.writerow({'id': contador, 
                            'evolucao_casos': removeAcentos(coluna['Status']),
                            'municipio': removeAcentos(coluna['MunicÃ­pio']),
                            'cod_ibge': 'N/A',
                            'uf': 'MS',
                            'data_inicio_sintomas':  removeAcentos(coluna['Data']),
                            'idade': 'N/A',
                            'faixa_etaria':  removeAcentos(coluna['Faixa EtÃ¡ria']),
                            'sexo':  removeAcentos(coluna['Sexo']),
                            'etnia': removeAcentos(coluna['RaÃ§a']),
                            'obito': removeAcentos(coluna['Detalhamento Status']), 
                            'data_obito': 'N/A'})
        contador = contador+1


###### Padronizador MG ######

leitor = csv.DictReader(open('MG.csv', 'r'), delimiter=',')

with open('padrao.csv', 'a') as padrao_csv:
    escrever = csv.DictWriter(padrao_csv, fieldnames=colunas, delimiter=';', lineterminator='\n')

    for coluna in leitor:
        escrever.writerow({'id': contador, 
                            'evolucao_casos': removeAcentos(coluna['CLASSIFICACAO_CASO']),
                            'municipio': removeAcentos(coluna['URS']),
                            'cod_ibge':  removeAcentos(coluna['CODIGO']),
                            'uf': 'MG',
                            'data_inicio_sintomas':  removeAcentos(coluna['DATA_NOTIFICACAO']),
                            'idade':  removeAcentos(coluna['IDADE']),
                            'faixa_etaria':  removeAcentos(coluna['FAIXA_ETARIA']),
                            'sexo':  removeAcentos(coluna['SEXO']),
                            'etnia': removeAcentos(coluna['RACA']),
                            'obito': 'N/A', 
                            'data_obito': 'N/A'})
        contador = contador+1

###### Padronizador PR ######

leitor = csv.DictReader(open('PR.csv', 'r',encoding="utf8"), delimiter=';')

with open('padrao.csv', 'a') as padrao_csv:
    escrever = csv.DictWriter(padrao_csv, fieldnames=colunas, delimiter=';', lineterminator='\n')
    for coluna in leitor:
        escrever.writerow({'id': contador, 
                            'evolucao_casos': 'CONFIRMADO',
                            'municipio': removeAcentos(coluna['MUN_RESIDENCIA']),
                            'cod_ibge':  removeAcentos(coluna['\ufeffIBGE_RES_PR']),
                            'uf': 'PN',
                            'data_inicio_sintomas':  removeAcentos(coluna['DATA_INICIO_SINTOMAS']),
                            'idade':  removeAcentos(coluna['IDADE_ORIGINAL']),
                            'faixa_etaria': 'N/A',
                            'sexo':  removeAcentos(coluna['SEXO']),
                            'etnia': 'N/A',
                            'obito': removeAcentos(coluna['OBITO']), 
                            'data_obito':  removeAcentos(coluna['DATA_OBITO'])})
        contador = contador+1

###### Padronizador PE ######

leitor = csv.DictReader(open('PE.csv', 'r',encoding="utf8"), delimiter=';')

with open('padrao.csv', 'a') as padrao_csv:
    escrever = csv.DictWriter(padrao_csv, fieldnames=colunas, delimiter=';', lineterminator='\n')

    for coluna in leitor:
        escrever.writerow({'id': contador, 
                            'evolucao_casos': removeAcentos(coluna['classe']),
                            'municipio': removeAcentos(coluna['municipio']),
                            'cod_ibge':  removeAcentos(coluna['cd_municipio']),
                            'uf': 'PE',
                            'data_inicio_sintomas': coluna['dt_primeiros_sintomas'], #data de notificaÃ§Ã£o
                            'idade': 'N/A',
                            'faixa_etaria': coluna['faixa_etaria'],
                            'sexo': coluna['Sexo'],
                            'etnia': removeAcentos(coluna['raca']),
                            'obito': 'N/A', 
                            'data_obito': removeAcentos(coluna['dt_obito'])})
        contador = contador+1

###### Padronizador RJ ######

leitor = csv.DictReader(open('RJ.csv', 'r',encoding="utf8"), delimiter=';')

with open('padrao.csv', 'a') as padrao_csv:
    escrever = csv.DictWriter(padrao_csv, fieldnames=colunas, delimiter=';', lineterminator='\n')
    for coluna in leitor:
        escrever.writerow({'id': contador, 
                            'evolucao_casos': removeAcentos(coluna['classificacao']),
                            'municipio': removeAcentos(coluna['municipio_res']),
                            'cod_ibge': 'N/A',
                            'uf': removeAcentos(coluna['uf']),
                            'data_inicio_sintomas': removeAcentos(coluna['dt_sintoma']),
                            'idade': removeAcentos(coluna['idade']),
                            'faixa_etaria': 'N/A',
                            'sexo': removeAcentos(coluna['sexo']),
                            'etnia': 'N/A',
                            'obito': removeAcentos(coluna['evolucao']), 
                            'data_obito': removeAcentos(coluna['dt_obito'])})
        contador = contador+1

###### Padronizador RN_obitos ######

leitor = csv.DictReader(open('RN_obitos.csv', 'r',encoding="utf8"), delimiter=';')

with open('padrao.csv', 'a') as padrao_csv:
    escrever = csv.DictWriter(padrao_csv, fieldnames=colunas, delimiter=';', lineterminator='\n')
    for coluna in leitor:
        escrever.writerow({'id': contador, 
                            'evolucao_casos': 'CONFIRMADOS',
                            'municipio': 'N/A',
                            'cod_ibge': 'N/A',
                            'uf': 'RN',
                            'data_inicio_sintomas': 'N/A',
                            'idade': 'N/A',
                            'faixa_etaria': removeAcentos(coluna['fx_etaria']),
                            'sexo': removeAcentos(coluna['genero']),
                            'etnia': 'N/A',
                            'obito': '1', 
                            'data_obito': removeAcentos(coluna['data_obito'])})
        contador = contador+1

###### Padronizador RN_positivos ######

leitor = csv.DictReader(open('RN_obitos.csv', 'r',encoding="utf8"), delimiter=';')

with open('padrao.csv', 'a') as padrao_csv:
    escrever = csv.DictWriter(padrao_csv, fieldnames=colunas, delimiter=';', lineterminator='\n')
    for coluna in leitor:
        escrever.writerow({'id': contador, 
                            'evolucao_casos': 'CONFIRMADOS',
                            'municipio': 'N/A',
                            'cod_ibge': 'N/A',
                            'uf': 'RN',
                            'data_inicio_sintomas': 'N/A',
                            'idade': 'N/A',
                            'faixa_etaria': removeAcentos(coluna['fx_etaria']),
                            'sexo': removeAcentos(coluna['genero']),
                            'etnia': 'N/A',
                            'obito': 'N/A', 
                            'data_obito': 'N/A'})
        contador = contador+1


###### Padronizador RS ######

leitor = csv.DictReader(open('RS.csv', 'r',encoding='latin1'), delimiter=';')

with open('padrao.csv', 'a') as padrao_csv:
    escrever = csv.DictWriter(padrao_csv, fieldnames=colunas, delimiter=';', lineterminator='\n')
    for coluna in leitor:
        escrever.writerow({'id': contador, 
                            'evolucao_casos': removeAcentos(coluna['EVOLUCAO']),
                            'municipio': removeAcentos(coluna['MUNICIPIO']),
                            'cod_ibge': removeAcentos(coluna['COD_IBGE']),
                            'uf': 'RS',
                            'data_inicio_sintomas': removeAcentos(coluna['DATA_SINTOMAS']),
                            'idade': 'N/A',
                            'faixa_etaria': removeAcentos(coluna['FAIXAETARIA']),
                            'sexo': removeAcentos(coluna['SEXO']),
                            'etnia': removeAcentos(coluna['RACA_COR']),
                            'obito': 'N/A', 
                            'data_obito': removeAcentos(coluna['DATA_INCLUSAO_OBITO'])})
        contador = contador+1


###### Padronizador RO ######

import csv

leitor = csv.DictReader(open('RO.csv', 'r',encoding="utf8"), delimiter=';')

with open('padrao.csv', 'a') as padrao_csv:
    escrever = csv.DictWriter(padrao_csv, fieldnames=colunas, delimiter=';', lineterminator='\n')
    for coluna in leitor:
        escrever.writerow({'id': contador, 
                            'evolucao_casos': removeAcentos(coluna['evolucaoCaso']),
                            'municipio': removeAcentos(coluna['municipio']),
                            'cod_ibge': 'N/A',
                            'uf': 'RO',
                            'data_inicio_sintomas': removeAcentos(coluna['dataInicioSintomas']),
                            'idade': removeAcentos(coluna['idade']),
                            'faixa_etaria': 'N/A',
                            'sexo': removeAcentos(coluna['Sexo']),
                            'etnia': removeAcentos(coluna['racaCor']),
                            'obito': 'N/A', 
                            'data_obito': 'N/A'})
        contador = contador+1


###### Padronizador RR ######

leitor = csv.DictReader(open('RR.csv', 'r',encoding="utf8"), delimiter=';')

with open('padrao.csv', 'a') as padrao_csv:
    escrever = csv.DictWriter(padrao_csv, fieldnames=colunas, delimiter=';', lineterminator='\n')
    for coluna in leitor:
        if coluna['resultadoTeste']=='Positivo':
            escrever.writerow({'id': contador, 
                                'evolucao_casos': removeAcentos(coluna['evolucaoCaso']),
                                'municipio': removeAcentos(coluna['municipio']),
                                'cod_ibge': removeAcentos(coluna['municipioIBGE']),
                                'uf': removeAcentos(coluna['estado']),
                                'data_inicio_sintomas': removeAcentos(coluna['dataInicioSintomas']),
                                'idade': removeAcentos(coluna['idade']),
                                'faixa_etaria': 'N/A',
                                'sexo': removeAcentos(coluna['sexo']),
                                'etnia': 'N/A',
                                'obito': 'N/A', 
                                'data_obito': 'N/A'})
            contador = contador+1

###### Padronizador SC ######

leitor = csv.DictReader(open('SC.csv', 'r',encoding='latin-1'), delimiter=';')

with open('padrao.csv', 'a') as padrao_csv:
    escrever = csv.DictWriter(padrao_csv, fieldnames=colunas, delimiter=';', lineterminator='\n')
    for coluna in leitor:
        escrever.writerow({'id': contador, 
                            'evolucao_casos': 'CONFIRMADO',
                            'municipio': removeAcentos(coluna['municipio']),
                            'cod_ibge': removeAcentos(coluna['codigo_ibge_municipio']),
                            'uf': 'SC',
                            'data_inicio_sintomas': removeAcentos(coluna['data_inicio_sintomas']),
                            'idade': removeAcentos(coluna['idade']),
                            'faixa_etaria': 'N/A',
                            'sexo': removeAcentos(coluna['sexo']),
                            'etnia': removeAcentos(coluna['raca']),
                            'obito': removeAcentos(coluna['obito']), 
                            'data_obito': removeAcentos(coluna['data_obito'])})
        contador = contador+1


###### Padronizador SP ######

leitor = csv.DictReader(open('SP.csv', 'r',encoding="utf8"), delimiter=';')

with open('padrao.csv', 'a') as padrao_csv:
    escrever = csv.DictWriter(padrao_csv, fieldnames=colunas, delimiter=';', lineterminator='\n')
    for coluna in leitor:
        escrever.writerow({'id': contador, 
                            'evolucao_casos': 'CONFIRMADO',
                            'municipio': removeAcentos(coluna['nome_munic']),
                            'cod_ibge': removeAcentos(coluna['codigo_ibge']),
                            'uf': 'SP',
                            'data_inicio_sintomas': removeAcentos(coluna['data_inicio_sintomas']),
                            'idade': removeAcentos(coluna['idade']),
                            'faixa_etaria': 'N/A',
                            'sexo': removeAcentos(coluna['cs_sexo']),
                            'etnia': 'N/A',
                            'obito': removeAcentos(coluna['obito']), 
                            'data_obito': 'N/A'})
        contador = contador+1