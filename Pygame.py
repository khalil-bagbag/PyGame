import pandas as pd

data=pd.read_csv('pygame.stats.csv')



def calculatescore(connections):
    succ=0
    while(connections.find('11111')!=-1):
        succ+=1
        connections=connections.replace('11111','',1)
        #print(connections)
    print('Score = ',succ*10)
    return succ*10

def score_jour(score):
    partie_entiere=score // 15 
    jour=partie_entiere*1.5 +1 
    print(jour)
    return jour 

def remise(jour):
    print(45-jour*1.5)
    return 45-jour*1.5

def gagnant(data):
    identifiant,montant_init=0,45
    liste=[]
    for k,v in data.iterrows():
        joined=v['connections'].replace(';','') 
        score=calculatescore(joined)
        jours=score_jour(score)
        montant_calcul=remise(jours)
        #print(k,score,jours,montant_calcul)
        
        
        if (montant_calcul<=montant_init):
            identifiant=k
            montant_init=montant_calcul
            liste.append([k,montant_calcul])
        liste=sorted(liste,key=lambda liste:liste[1])
        c=1
        best=liste[0][1]
    for i in range(1,len(liste)):
        if best==liste[i][1]:
            c+=1
        else:
            break
    liste=liste[:c]
    for i in liste:
        print('Name :', data.iloc[i[0]]['name'],' Username : ',data.iloc[i[0]]['username'])
    return liste 


liste=gagnant(data)













    