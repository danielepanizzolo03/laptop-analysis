import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import pyfiglet
import seaborn as sns
import time #per misurare il tempo di esecuzione del programma 

start_time = time.time()
starttime = time.process_time()

#menù principale 
main_menu = {
    1: "Cambia dataset",
    2: "Mostra le prime righe del dataset",
    3: "Mostra le informazioni sul dataset",
    4: "Calcola le statistiche descrittive del dataset",
    5: "Esegui un'analisi specifica",
    0: "Esci"
}
#menù che si apre solo dopo aver cliccato la voce 5: "Esegui un'analisi specifica"
statistics_menu = {
    1: "Mostra il grafico a torta dei produttori",
    2: "Calcola la mediana",
    3: "Calcola la moda",
    4: "Calcola la varianza",
    5: "Calcola la deviazione standard",
    6: "Calcola la correlazione",
    7: "Calcola la covarianza",
    8: "Voglio vedere il grafico dei produttori come un diagramma a barre",
    9: "Mostra il grafico a torta dei prezzi più elevati",
    10: "Mostra il diagramma a barre dei 4 marchi di computer più costosi",
    11: "Ecco il diagramma a barre della categoria di computer più venduti",
    12: 'Ecco il grafico a torta delle ram più apprezzate dai consumatori',
    13: "Mostra i valori rappresentanti la curtosi e l' asimmettria",
    14: "Boxplot tra Category e Price ", #modo migliore per comprendere la relazione tra una variabile numerica e variabile categoriale è attraverso un boxplot
    15:"Boxplot tra Manufacturer e Price",
    0: "Menu principale"
}


def read_menu_choice(menu):
    print("\nCosa vuoi fare?:")
    for k, v in menu.items():
        print(f"{k}. {v}")

    while True:
        try:
            choice = int(input("Inserisci il numero corrispondente: ")) #richiede un input numerico intero dell'utente
            if choice < 0 or choice >= len(menu): #verifica se l'input fornito è valido 
                raise ValueError()
            #in caso non fosse valido il programma si ferma 
            break
        except ValueError:
            print("Scelta non valida. Riprova.\n") #quello che vediamo a schermo 
    return choice #ci ritorna di reinserire un numero corrispondente


def choose_dataset():
    print("Scegli il  di dataset che vuoi utilizzare: ")

    csv_files = [f for f in os.listdir('.') if f.endswith('.csv')]

    for i, f in enumerate(csv_files):
        print(f"{i}: {f}")

    while True:
        try:
            choice = int(input("Inserisci il numero corrispondente: "))
            #verifica se l'input è valido
            if choice < 0 or choice >= len(csv_files):
                raise ValueError() #eccezzione quando si verifica un errore di tipo valore ad esempio diamo un valore non presente nel menù
            break
        except ValueError:
            #stampa un messaggio di errore in caso l'input non sia valido
            print("Scelta non valida. Riprova.\n")
    return csv_files[choice] #restituisce il file csv scelto dall'utente 


def load_dataset(dataset_path):
    dataset = pd.read_csv("./"+dataset_path)
    return dataset


def show_dataset_info(dataset):
    print('Ecco le informazioni del Dataset: ')
    dataset.info()


def choose_dataset():
    print("Scegli il dataset che vuoi utilizzare: ")
    #ottiene tutti i file di tipo CSV che sono presenti nella directoy che stiamo utilizzando 
    csv_files = [f for f in os.listdir('.') if f.endswith('.csv')]

    #stampa l'elenco dei file numerati per permettere all'utente di scegliere su che file CSV vuole fare l'analisi
    for i, f in enumerate(csv_files):
        print(f"{i}: {f}")

    while True:
        try:
            #chiede all'utente su che file CSV vuole operare 
            choice = int(input("Inserisci il numero corrispondente: "))

            #verifica se la scelta è valida 
            if choice < 0 or choice >= len(csv_files):
                raise ValueError()
            break
        except ValueError:
            print("Scelta non valida. Riprova.\n")
    #restituisce il file scelto dall'utente 
    return csv_files[choice]


def handle_statistics_choice(choice, dataset):
    #verifica se il dataset non ha ancora nessun dato caricato 
    if dataset.empty:
        print("Non è stato caricato nessun dataset!")
        return
    #se il dataset presente dati caricati, estrae le colonne numeriche presenti nel dataset 
    numeric_columns = dataset.select_dtypes(include=[np.number]).columns.tolist()

    if choice == 1:
        show_pie_chart(dataset)
    #questa analisi ovvero di calcolare la mediana, la moda, la varianza, la deviazione standard, la correlazione e la covarianza
    #la possiamo fare solo sui valori di tipo numerico ovvero float64
    #se noi all'interno del nostro menù clicchiamo la voce 3 (Mostra le informazioni del dataset) notiamo che solo la voce Price è di tipo float64
    #il resto sono tutti oggetti
    #questo significa che questi calcoli verranno effettuati solo sulla colonna price 
    #in questo caso potevo inserire più precisamente su dove calcolare queste informazioni ma ho voluto comunque far analizzare colonna per colonna per ragioni di sicurezza
    elif choice in [2, 3, 4, 5, 6, 7] and len(numeric_columns) > 0:
        numeric_dataset = dataset[numeric_columns]
        if choice == 2:
            print("La mediana è: ")
            print(numeric_dataset.median()) #calcola la mediana di price
        elif choice == 3:
            print("La moda è: ")
            print(numeric_dataset.mode()) #calcola la moda di price
        elif choice == 4:
            print("La varianza è: ")
            print(numeric_dataset.var())
        elif choice == 5:
            print("La deviazione standard è: ")
            print(numeric_dataset.std()) #calcola la deviazione standard di price
        elif choice == 6:
            print("La correlazione è: ")
            print(numeric_dataset.corr()) #calcola la correlazione di price 
        elif choice == 7:
            print("La covarianza è: ")
            print(numeric_dataset.cov()) #calcola la covarianza di price 

    elif choice == 8:
        print("Ecco la versione con il diagramma a nastri: ")
        show_diagram(dataset)

    elif choice == 9:
        print("Ecco il grafico a torta dei prezzi più elevati")
        show_pie_chart_expensive_laptop(dataset)

    elif choice == 10:
        print("Ecco il diagramma a barre dei 4 marchi di computer più costosi")
        show_diagram_price(dataset)

    elif choice == 11:
        print('Ecco il diagramma a barre della categoria di computer più vendute')
        show_diagram_category(dataset)

    elif choice == 12:
        print('Il grafico a torta delle RAM più utilizzate.')
        show_pie_chart_RAM(dataset)
    elif choice == 13:
        print("\nEcco i valori rappresentanti la curtosi e l'asimettria della variabile PRICE\n")
        curtosi_asimetria(dataset)
    elif choice == 14:
        print ('Ecco il boxplot per Category e Price')
        boxplot(dataset)
    elif choice == 15:
        print ('Ecco il boxplot per Manufacturer e Price')
        boxplot1(dataset)


    elif choice == 0:
        main(dataset)


# funzione che mostra il grafico a torta dei produttori più presenti all'interno del dataset
def show_pie_chart(dataset):
    print("Ecco il grafico a torta dei produttori: ")
    dataset['Manufacturer'].value_counts().plot(kind='pie', autopct='%1.1f%%', figsize=(10, 10))
    plt.show()
# funzione che mostra il grafico dei laptop più costosi all'interno del dataset

def show_pie_chart_expensive_laptop(dataset):
    print('Ecco il grafico a torta dei computer più costosi: ')
    top_5 = dataset['Price'].value_counts().nlargest(10)
    top_5.plot(kind='pie', figsize=(10, 10))
    plt.show()


#funzione che mostra il grafico a barre (diverso da un istogramma poiché le nostre variabili sono qualitative) dei 5 valori più alti di price

def show_diagram_price(dataset):
   
    
    print('Ecco il diagramma a barre dei 4 valori più alti di Price:')
    colors = ['purple'] #ho scelto il colore 'purple' ma era possibile scegliere un qualsiasi colore
    top_5_prices = dataset.nlargest(5, 'Price') #mi sono creato una variabile 
    #che prende attraverso la funzione nlargest() che è fornita dalla libreria Pandas
    #i 5 valori più alti della colonna 'Price'

#In questo passaggio di implementazione vedevo che prendendo i primi 5 valori e senza mettere keep sul grafico notavo due volte la presenza di due colonne nominate Asus
#Allora tenendo lo stesso i 5 valori ma tenendo solo il primo mi comparirà 4 barre e non dello stesso tipo (ovvero come mi era capitato in precedenza con due colonne denominato ASUS)
#Questo problema dopo aver cercato su Google ho notato che potrebbe essere legato ad un problema con il Dataset stesso 
# Rimuovi prodotti duplicati con lo stesso prezzo massimo, tenendo solo il primo
    top_5_prices = top_5_prices.drop_duplicates(subset='Price', keep='first')

# Aggiungi solo il primo prodotto Lenovo con il prezzo massimo
    top_5_prices = top_5_prices.drop_duplicates(subset='Manufacturer', keep='first')

    plt.figure(figsize=(10, 6))
    plt.bar(top_5_prices.index, top_5_prices['Price'], color=colors)
    plt.xlabel('Prodotti')
    plt.ylabel('Prezzo')
    plt.title('Top 4 Valori più Alti di Prezzo')
    plt.xticks(rotation=45)

# Aggiunge i nomi dei produttori sotto ogni barra
    for i, row in top_5_prices.iterrows():
        plt.text(i, row['Price'], row['Manufacturer'], ha='center', va='bottom')
        #ha="center" allinea orizzontalmente il testo rispetto a "center"--> centro 
        #va="bottom" allinea verticalmente il testo nella parte inferiore della posizione che vogliamo inserire (in questo caso "bottom"-->in fondo)

    plt.show()





def show_diagram_category(dataset):
    print ('Ecco il diagramma a nastri delle categorie di PC più vendute:')
    colors = ['green']
    category_counts = dataset['Category'].value_counts()
    plt.figure(figsize=(10, 6))
    plt.bar(category_counts.index, category_counts.values, color= colors)
    plt.xlabel('Categorie')
    plt.ylabel('Conteggio delle Categorie')
    plt.title('Distribuzione delle Categorie')
    plt.xticks(rotation=45)
    plt.show()

    

def show_diagram(dataset):
    print ('Ecco il diagramma a nastri  dei prodotti più venduti:')
    colors = ['orange']
    manufacturer_counts = dataset['Manufacturer'].value_counts()
    plt.figure(figsize=(10, 6)) #figsize=(10, 6), ad esempio, 
    #indica che la larghezza della figura sarà di 10 pollici e l'altezza sarà di 6 pollici. 
    #Le dimensioni della figura possono essere regolate in base alle tue esigenze per ottenere la visualizzazione desiderata del grafico.
    plt.bar(manufacturer_counts.index, manufacturer_counts.values, color= colors)
    plt.xlabel('Produttori')
    plt.ylabel('Conteggio dei produttori')
    plt.title('Distribuzione dei Produttori')
    plt.xticks(rotation=45)
    plt.show()

def show_pie_chart_RAM(dataset):
    print("Ecco il grafico a torta delle RAM")
    dataset['RAM'].value_counts().plot(kind='pie', autopct='%1.1f%%', figsize=(10, 10))
    plt.title('Distribuzione delle RAM:')
    plt.show()

def curtosi_asimetria(dataset):
    print(f"Curtosi: {dataset['Price'].kurt()}")
    print(f"Asimmetria: {dataset['Price'].skew()}")
    print(f"Curtosi dei conteggi dei valori: {dataset['Price'].value_counts().kurt()}") #misura quanto i conteggi dei valori si discostano dalla distribuzione uniforme.


def boxplot(dataset):
    sns.catplot(x='Category', y = 'Price', data = dataset, kind = 'box', aspect = 1.5)
    plt.title('Boxplot per Category e Price')
    plt.show()

def boxplot1(dataset):
    sns.catplot(x='Manufacturer', y = 'Price', data = dataset, kind = 'box', aspect = 1.5)
    plt.title('Boxplot per Manufacturer e Price')
    plt.show()


def main(dataset=None):
    print("Buongiorno e benvenuti nel programma di Daniele e Nicolas.\n\n")

    dataset_path = None

    while True:
        if dataset is None:
            dataset_path = choose_dataset()
            dataset = load_dataset(dataset_path)
        choice = read_menu_choice(main_menu)

        if choice == 1:
            dataset_path = choose_dataset()
            dataset = load_dataset(dataset_path)

        if choice == 2:
            print("Ecco le prime righe del dataset: ") #elemento molto importante perché ci fa visualizzare le prime n righe di un DATASET
            #Questo ci fa capire come è strutturato e che tipo di analisi possiamo andare a fare 
            print(dataset.head())

        if choice == 3:
            show_dataset_info(dataset)

        if choice == 4:
            print("Ecco le statistiche descrittive del dataset: ")
            print(dataset.describe())

        if choice == 5:
            statistics_choice = read_menu_choice(statistics_menu)
            handle_statistics_choice(statistics_choice, dataset)


        if choice == 0:
        
            print(pyfiglet.figlet_format(

                "Grazie mille per aver utilizzato questo programma\n, A presto.", font="small"))
            
            print('\n\n')
            break

        print('\n')


if __name__ == "__main__":
    main()

endtime = time.process_time()
executiontime = endtime - starttime
print(f"Tempo di esecuzione della CPU: {executiontime} secondi") # restituisce il tempo di CPU trascorso per l'esecuzione effettiva del processo corrente in secondi

end_time = time.time()
execution_time = end_time - start_time
print(f"Tempo di esecuzione: {execution_time} secondi") #mostra a schermo il tempo di esecuzione del programma tra due istanti di tempo in secondi 

