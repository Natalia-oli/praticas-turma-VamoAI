def podio_olimpico(tempo_chegada1, tempo_chegada2, tempo_chegada3):
    
    if (tempo_chegada1 < tempo_chegada2) and (tempo_chegada1 < tempo_chegada3) and (tempo_chegada2 < tempo_chegada3):
        return tempo_chegada1, tempo_chegada2, tempo_chegada3
    elif (tempo_chegada1 < tempo_chegada2) and (tempo_chegada1 < tempo_chegada3) and (tempo_chegada3 < tempo_chegada2):
        return tempo_chegada1, tempo_chegada3, tempo_chegada2
    elif (tempo_chegada2 < tempo_chegada1) and (tempo_chegada2 < tempo_chegada3) and tempo_chegada1 < tempo_chegada3:
        return tempo_chegada2, tempo_chegada1, tempo_chegada3
    elif (tempo_chegada2 < tempo_chegada1) and (tempo_chegada2 < tempo_chegada3) and tempo_chegada3 < tempo_chegada1:
        return tempo_chegada2, tempo_chegada3, tempo_chegada1
    elif (tempo_chegada3 < tempo_chegada1) and (tempo_chegada3 < tempo_chegada2) and (tempo_chegada2 < tempo_chegada1):
        return tempo_chegada3, tempo_chegada2, tempo_chegada1
    elif (tempo_chegada3 < tempo_chegada1) and (tempo_chegada3 < tempo_chegada2) and (tempo_chegada1 < tempo_chegada2):
        return tempo_chegada3, tempo_chegada1, tempo_chegada2

tempo1 = 2
tempo2 = 3
tempo3 = 1
podio_olimpico(tempo1, tempo2, tempo3)