import config
import requests
import json
import pandas as pd


lista = ["Aborto","Doenças Negligenciadas", "Doença de Chagas", "Noma" ,"Hepatite C" ,"Acesso a Medicamentos","Acesso a Propriedade Intelectual",
                "Crise climática","Desastre Ambiental" ,"Ajuda Humanitária", "Migração","Refugiados"]

def cria_busca(word = "brasil"):

        url = config.urlNewsHot
        texto = word.lower().replace(' ','%20')
        tempo = '&from=2022-06-05&to=2022-06-02&sortBy=popularity&'
        # print(url+f'?q={texto}&language=pt{tempo}apiKey={config.apiKey}')

        response = requests.get(url+f'?q={texto}&language=pt{tempo}apiKey={config.apiKey}')

        print(response)


        data = pd.DataFrame(response.json()['articles'])

        ndata = data.drop(['source'], axis=1)

        sdata = pd.DataFrame()

        for i in range(len(ndata)):
                source = response.json()['articles'][i]['source']
                sdata.loc[len(sdata),['id','name'] ] = [source['id'],source['name']]

        allinfo = pd.concat([sdata,ndata], axis='columns')
        # print(allinfo[:1].to_json(orient="records"))

        with open(f'resp_news_{texto.replace("%20","_")}.json', 'w') as outff:
                outff.write(allinfo.to_json(orient='records', lines=True))

        # salva os dados e manipula em pandas
        allinfo.to_csv(f'response_news_{texto.replace("%20","_")}.csv')
        

for i in lista[1:]:
        print('Buscando por >>>',i)
        cria_busca(i)