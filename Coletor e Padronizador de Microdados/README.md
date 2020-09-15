# CDA-squad8
repositório para acompanhar todo trabalho que está sendo feito acerca das dados coletados da COVID-19

# Coletor dos dados

- Coleta todas as bases de microdados possíveis de se coletar. (19 bases, especificadas no TXT dicionário contido no repositório)
- Para gerar a base completa é necessário coletar outras 5 bases manualmente sendo essas:
- - Acre - http://covid19.ac.gov.br/monitoramento/notificacoes/esus
- - Amapá Casos e Amapá Obitos - https://docs.google.com/spreadsheets/d/1BNivdd1qWi5El228SJ0Yk0WevuAUZEJkqhlp67GrgcY/edit#gid=1082917827
- - Mato Grosso do Sul - http://mais.saude.ms.gov.br/sense/app/51c38346-b65d-4f3e-8a80-5111a7a9da76/sheet/18934db3-7aaf-45cf-a762-15e526251abc/state/analysis
- - Santa Catarina - ftp://boavista:dados_abertos@ftp2.ciasc.gov.br/boavista_covid_dados_abertos.csv

Mais informações acerca dos microdados: https://docs.google.com/spreadsheets/d/1BNivdd1qWi5El228SJ0Yk0WevuAUZEJkqhlp67GrgcY/edit?usp=sharing

# Padronizador
Segue o padrão abaixo:

// coloque esse codigo na mesma pasta que o arquivo CSV de micro dados do estado.

// altere para o nome do CSV que deseja padronizar 

// OBS: algumas bases utiliza-se o encoding="latin1"

// o método segue o seguinte padrão: 

// writerow({'nome da coluna da base padrão': coluna['Nome da coluna que contem a informação da base a ser padronizada']

// Exemplo caso a base nao contenha a informação idade: 'idade': N/A

# Exemplo: Padronizador SP

leitor = csv.DictReader(open('SP.csv', 'r',encoding="utf8"), delimiter=';')

with open('padrao.csv', 'a') as padrao_csv:

    escrever = csv.DictWriter(padrao_csv, fieldnames=colunas, delimiter=';', lineterminator='\n')
    
    for coluna in leitor:
        escrever.writerow({'id': contador, 
                            'evolucao_casos': 'CONFIRMADO',
                            'municipio': coluna['nome_munic'],
                            'cod_ibge': coluna['codigo_ibge'],
                            'uf': 'SP',
                            'data_inicio_sintomas': coluna['data_inicio_sintomas'],
                            'idade': coluna['idade'],
                            'faixa_etaria': 'N/A',
                            'sexo': coluna['cs_sexo'],
                            'etnia': 'N/A',
                            'obito': coluna['obito'], 
                            'data_obito': 'N/A'})
                            
        contador = contador+1
