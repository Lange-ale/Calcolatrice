#Langellotti Alessio, Pymike
import math
while True:
    print('''
    Benvenuto al programma calcolatrice!
    Creata da Lange;
    Di seguito un elenco delle varie funzioni disponibili:

    -Per effettuare un'Addizione, seleziona 1;
    -Per effettuare una Sottrazione, seleziona 2;
    -Per effettuare una Moltiplicazione numerica, seleziona 3;
    -Per effettuare una Divisone, seleziona 4;
    -Per effettuare un Calcolo Esponenziale, seleziona 5;
    -Per effettuare una Radice quadrata, seleziona 6;
    -Per uscire dal programma puoi digitare ESC;
    ''')

    scelta = input('Inserisci il numero corrispondente all\'operazione selezionata --->  ')

    while scelta != "ESC" and scelta != "esc" and scelta != "Esc" and scelta != "1" and scelta != "2" and scelta != "3" and scelta != "4" and scelta != "5" and scelta != "6":
        print('hai canato a cliccare, riprova')
        scelta = input('Inserisci il numero corrispondente all\'operazione selezionata --->  ')


    if scelta == "1":
        print('\nHai scelto: Addizione\n')
        a = input('Inserisci il Primo Numero -> ')
        b = input('Inserisci il Secondo Numero -> ')
        try:
            risultato = float(a) + float(b)
            while True:
                print(f'il risultato è {risultato}')
                c = input('vuoi aggiungere un altro numero? se non vuoi scrivi no -> ')
                if c=='NO' or c=='No' or c=='no':
                    break
                else:
                    risultato = risultato + float(c)
        except ValueError:
            print('non puoi effettuare addizioni con questi valori')


    elif scelta == "2":
        print('\nHai scelto: Sottrazione\n')
        a = input('Inserisci il Primo Numero -> ')
        b = input('Inserisci il Secondo Numero -> ')
        try:
            risultato = float(a) - float(b)
            while True:
                print(f'il risultato è {risultato}')
                c = input('vuoi sottrarre per un altro numero? se non vuoi scrivi no -> ')
                if c == 'NO' or c == 'No' or c == 'no':
                    break
                else:
                    risultato = risultato - float(c)
        except ValueError:
            print('non puoi effettuare sottrazioni con questi valori')


    elif scelta == "3":
        print('\nHai scelto: Moltiplicazione numerica\n')
        a = input('Inserisci il Primo Numero -> ')
        b = input('Inserisci il Secondo Numero -> ')
        try:
            risultato = float(a) * float(b)
            while True:
                print(f'il risultato è {risultato}')
                c = input('vuoi moltiplicare per un altro numero? se non vuoi scrivi no -> ')
                if c == 'NO' or c == 'No' or c == 'no':
                    break
                else:
                    risultato = risultato * float(c)
        except ValueError:
            print('i valori inseriti non sono numerici')


    elif scelta == "4":
        print('\nHai scelto: Divisione\n')
        a = input('Inserisci il Primo Numero -> ')
        b = input('Inserisci il Secondo Numero -> ')
        try:
            if float(a)==0 and float(b)==0:
                print('La divisione è indeterminata')
            else:
                risultato = float(a) / float(b)
                while True:
                    print(f'il risultato è {risultato}')
                    c = input('vuoi dividere per un altro numero? se non vuoi scrivi no -> ')
                    if c == 'NO' or c == 'No' or c == 'no':
                        break
                    else:
                        risultato = risultato / float(c)
        except ValueError:
                print('i valori inseriti non sono numerici')
        except ZeroDivisionError:
                print('divisione impossibile')


    elif scelta == "5":
        print('\nHai scelto: Calcolo Esponenziale\n')
        a = input('Inserisci il Primo Numero -> ')
        b = input('Inserisci il Secondo Numero -> ')
        try:
            risultato = float(a) ** float(b)
            while True:
                print(f'il risultato è {risultato}')
                c = input('vuoi elevare ancora a potenza il risultato? se non vuoi scrivi no -> ')
                if c == 'NO' or c == 'No' or c == 'no':
                    break
                else:
                    risultato = risultato ** float(c)
        except ValueError:
            print('i valori inseriti non sono numerici')


    elif scelta == "6":
        print('\nHai scelto: Radice quadrata\n')
        try:
            a = float(input('Inserisci il Numero -> '))
            if a<0:
                print('il radicando inserito è negativo quindi la radice è impossibile')
            else:
                radice = math.sqrt(a)
                print(f'il risultato è {radice}')
        except ValueError:
            print('i valori inseriti non sono numerici')


    elif scelta == "ESC" or scelta == "esc" or scelta == "Esc":
        print('''L'applicazione verrà ora chiusa!

**********************************************************************''')
        break



    loop = input('\nDesideri continuare ad usare l\'applicazione? S/N ')
    while loop!="S" and loop!="s" and loop!="N" and loop!="n":
        print('hai canato a cliccare, riprova')
        loop = input('\nDesideri continuare ad usare l\'applicazione? S/N ')
    if loop == "S" or loop == "s":
        print('''Sto tornando al Menù principale!

**********************************************************************''')
        continue
    elif loop =='N'or loop =='n':
        print('''Grazie e arrivederci!

**********************************************************************''')
        break
