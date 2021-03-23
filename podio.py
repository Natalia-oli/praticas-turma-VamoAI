def podio_olimpico(tempo_chegada1, tempo_chegada2, tempo_chegada3):
    if (tempo_chegada1 < tempo_chegada2) and (tempo_chegada1 < tempo_chegada3) and (tempo_chegada2 < tempo_chegada3):
        return( f"1 -{tempo_chegada1} minutos\n"
                f"2 - {tempo_chegada2} minutos\n"
                f"3 - {tempo_chegada3} minutos\n")

    elif (tempo_chegada1 < tempo_chegada2) and (tempo_chegada1 < tempo_chegada3) and (tempo_chegada3 < tempo_chegada2):
        return( f"1 -{tempo_chegada1} minutos\n"
                f"2 - {tempo_chegada3} minutos\n"
                f"3 - {tempo_chegada2} minutos\n")

    elif (tempo_chegada2 < tempo_chegada1) and (tempo_chegada2 < tempo_chegada3) and tempo_chegada1 < tempo_chegada3:
        return( f"1 -{tempo_chegada2} minutos\n"
                f"2 - {tempo_chegada1} minutos\n"
                f"3 - {tempo_chegada3} minutos\n")

    elif (tempo_chegada2 < tempo_chegada1) and (tempo_chegada2 < tempo_chegada3) and tempo_chegada3 < tempo_chegada1:
        return( f"1 -{tempo_chegada2} minutos\n"
                f"2 - {tempo_chegada3} minutos\n"
                f"3 - {tempo_chegada1} minutos\n")
                
    elif (tempo_chegada3 < tempo_chegada1) and (tempo_chegada3 < tempo_chegada2) and (tempo_chegada2 < tempo_chegada1):
        return( f"1 -{tempo_chegada3} minutos\n"
                f"2 - {tempo_chegada2} minutos\n"
                f"3 - {tempo_chegada1} minutos\n")
    elif (tempo_chegada3 < tempo_chegada1) and (tempo_chegada3 < tempo_chegada2) and (tempo_chegada1 < tempo_chegada2):
        return( f"1 -{tempo_chegada3} minutos\n"
                f"2 - {tempo_chegada1} minutos\n"
                f"3 - {tempo_chegada2} minutos\n")

print(podio_olimpico(10, 3, 4))