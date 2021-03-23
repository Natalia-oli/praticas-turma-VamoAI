def complete_series(seq):
    lista_sem_repeticoes = set(seq)
    if len(seq) > len(lista_sem_repeticoes):
      return [0]
    
    maior_numero_da_lista = max(seq)
     list(range(maior_numero_da_lista + 1))