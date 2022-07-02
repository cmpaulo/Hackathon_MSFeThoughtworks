import config
import requests
import json
import pandas as pd


lista = ["Doenças Negligenciadas", "Doença de Chagas", "Noma" ,"Hepatite C" ,"Acesso a Medicamentos","Acesso a Propriedade Intelectual",
                "Crise climática", "Desastres Socioambientais","Desastre Ambiental" ,"Ajuda Humanitária", "Migração","Refugiados"]

def cria_busca(word = "brasil"):

        url = config.urlNewsHot
        texto = word.lower().replace(' ','%20')
        tempo = '&from=2022-06-01&to=2022-06-30&sortBy=popularity&'

        response = requests.get(url+f'?q={texto}&language=pt{tempo}apiKey={config.apiKey}')

        print(response)

        data = pd.DataFrame(response.json()['articles'])

        ndata = data.drop(['source'], axis=1)

        sdata = pd.DataFrame()

        for i in range(len(ndata)):
                source = response.json()['articles'][i]['source']
                sdata.loc[len(sdata),['id','name'] ] = [source['id'],source['name']]

        allinfo = pd.concat([sdata,ndata], axis='columns')

        # salva os dados e manipula em pandas
        allinfo.to_csv(f'response_news_{texto.replace("%20","_")}.csv')


for i in lista:
        print('Buscando por >>>',i)
        cria_busca(i)