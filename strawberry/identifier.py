import os
import hashlib
import time
from datetime import datetime

def heapify(array, index, heap_size):
  # calcola l'indice del figlio sinistro
  left_child = 2 * index + 1
  # calcola l'indice del figlio destro
  right_child = 2 * index + 2
  # inizializza l'indice del figlio massimo come quello del nodo corrente
  largest = index

  # se il figlio sinistro esiste e il suo valore è maggiore di quello del nodo corrente, imposta l'indice del figlio massimo come quello del figlio sinistro
  if left_child < heap_size and array[left_child] > array[largest]:
    largest = left_child
  # se il figlio destro esiste e il suo valore è maggiore di quello del nodo corrente, imposta l'indice del figlio massimo come quello del figlio destro
  if right_child < heap_size and array[right_child] > array[largest]:
    largest = right_child

  # se l'indice del figlio massimo è diverso da quello del nodo corrente, scambia i valori e chiama ricorsivamente heapify() per il figlio massimo
  if largest != index:
    array[largest], array[index] = array[index], array[largest]
    heapify(array, largest, heap_size)


# funzione per ordinare i file per hash usando l'algoritmo di ordinamento a cuscino
def heap_sort_hashes(files):
  # crea una copia della lista di file
  copy = files[:]

  # costruisci il cuscino
  for i in range(len(copy) // 2, -1, -1):
    heapify(copy, i, len(copy))

  # estrai gli elementi dal cuscino uno alla volta
  for i in range(len(copy) - 1, 0, -1):
    copy[i], copy[0] = copy[0], copy[i]
    heapify(copy, 0, i)

  # restituisci la lista ordinata
  return copy

def SearchDuplicate(dir: str):
   
    # chiedi all'utente di inserire il percorso della cartella
    if dir !="":
        percorso = dir
    else:
        percorso = input("Inserisci un percorso: ")
    start_time = time.time()
    print(f"Cerco duplicati in {dir}")
    files = []
    # ottiene la lista dei file nella cartella
    files = os.listdir(percorso)


    # ordina i file per hash usando l'algoritmo di ordinamento a cuscino
    files = heap_sort_hashes(files)
    
    # inizializza una variabile per memorizzare l'hash precedente
    previous_hash = None
    previous_file = None
    log = ""
    # cicla attraverso ogni file nella cartella
    for file in files:
        # calcola l'hash del file
        if(os.path.isfile(f"{percorso}/{file}")):
            print(f"Analizzo {file}")
            hash = hashlib.sha1(open(os.path.join(percorso, file), 'rb').read()).hexdigest()
            # se l'hash è uguale all'hash precedente, il file è un duplicato
            if hash == previous_hash:
                print(f'Il file "{percorso}/{file}" è un duplicato di un altro file "{previous_file}" nella cartella')
                log += f"[{file}]\n{previous_file}\n{percorso}/{file}\n\n"
            # altrimenti, aggiorna l'hash precedente
            else:
                previous_hash = hash
                previous_file = f"{percorso}/{file}"
    elapsed_time = time.time() - start_time
    d = datetime.now().strftime("%Y%m%d_%H:%M:%S")
    f = open(f"strawberry_log_{d}.txt", "w")
    f.write(log)
    f.close()
    print('Il tempo trascorso è: {:.2f} secondi'.format(elapsed_time))
    input("Press Enter to continue...")
    exit()
    
