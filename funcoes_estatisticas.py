import re
import requests

LISTA_TODOS_JOGOS = []

def extrai_todos_jogos_site():

    global LISTA_TODOS_JOGOS

    url = "https://asloterias.com.br/lista-de-resultados-da-lotofacil"
    response = requests.get(url, verify=False)
    html = response.text
    padrao = r'\d+(?: \d+){14}'
    pattern = re.compile(padrao)
    lista_match = pattern.findall(html)
    for string in lista_match:
        lista_substrings = string.split()
        LISTA_TODOS_JOGOS.append([int(substring) for substring in lista_substrings])


""" analize se existe jogos sorteados expelho

         03 04 05 06 07 08 09 11 13 14 15 17 22 22 25 - espelho.
    Ex : 02 03 04 05 06 07 08 10 12 13 14 16 21 23 24 
         01 02 03 04 05 06 07 09 11 12 13 15 20 21 23 - espelho.
"""
def estatistica_espelho():

    global LISTA_TODOS_JOGOS
    dicio_final = { "Com espelho" : 0, "Não espelho" : 0 }

    for sequencia in LISTA_TODOS_JOGOS :
        if not ( 1 in sequencia and 25 in sequencia ) :
           lista_conj_testar = [ [ v + 1 for v in sequencia ], [ v - 1 for v in sequencia ] ]
           cont = 0
           encontrou = False
           while cont < 2 :
               lista_testar = lista_conj_testar [ cont ]
               for sequencia_ in LISTA_TODOS_JOGOS :
                   if lista_testar == sequencia_ :
                      cont = 2
                      dicio_final["Com espelho"] += 1
                      print("sequencia catalizadora : " +str(sequencia))
                      print("sequencia espelho encontrada : " +str(sequencia_))
                      encontrou = True
                      break
                   else : cont += 1
           if encontrou == False: dicio_final["Não espelho"] += 1

    print(dicio_final)

"""
   Examina o quanto é comum sequências com os números : 01,22,25.
"""
def estatistica_01_22_25() :

    global LISTA_TODOS_JOGOS
    dicio_final = { "encontrou" : 0, "não encontrou" : 0 }

    for sequencia in LISTA_TODOS_JOGOS :
        if 1 in sequencia and 22 in sequencia and 25 in sequencia :
           dicio_final["encontrou"] += 1
        else : dicio_final["não encontrou"] += 1

    print( dicio_final )

"""
   estatística se todas as subsequências de 10 dos jogos sorteados se repetem.
"""
def estatistica_sequencia_dez():

    global LISTA_TODOS_JOGOS
    dicio_final = {"encontrou": 0, "não encontrou": 0}
    inicio = 0
    aux = False

    for sequencia_sorteada in LISTA_TODOS_JOGOS:
        aux = False
        for sequencia_secundaria in [x for x in LISTA_TODOS_JOGOS if x != sequencia_sorteada]:

            if (sequencia_sorteada[inicio:10] == sequencia_secundaria[inicio:10] or
                sequencia_sorteada[inicio:10] == sequencia_secundaria[inicio + 1:10] or
                sequencia_sorteada[inicio:10] == sequencia_secundaria[inicio + 2:10] or
                sequencia_sorteada[inicio:10] == sequencia_secundaria[inicio + 3:10] or
                sequencia_sorteada[inicio:10] == sequencia_secundaria[inicio + 4:10] or
                sequencia_sorteada[inicio:10] == sequencia_secundaria[inicio + 5:10]):
                dicio_final["encontrou"] += 1
                aux = True
                break
                #---------------------------------------------------------------------

            elif (sequencia_sorteada[inicio + 1:10] == sequencia_secundaria[inicio:10] or
                  sequencia_sorteada[inicio + 1:10] == sequencia_secundaria[inicio + 1:10] or
                  sequencia_sorteada[inicio + 1:10] == sequencia_secundaria[inicio + 2:10] or
                  sequencia_sorteada[inicio + 1:10] == sequencia_secundaria[inicio + 3:10] or
                  sequencia_sorteada[inicio + 1:10] == sequencia_secundaria[inicio + 4:10] or
                  sequencia_sorteada[inicio + 1:10] == sequencia_secundaria[inicio + 5:10]):
                dicio_final["encontrou"] += 1
                aux = True
                break
                #---------------------------------------------------------------------

            elif (sequencia_sorteada[inicio + 2:10] == sequencia_secundaria[inicio:10] or
                  sequencia_sorteada[inicio + 2:10] == sequencia_secundaria[inicio + 1:10] or
                  sequencia_sorteada[inicio + 2:10] == sequencia_secundaria[inicio + 2:10] or
                  sequencia_sorteada[inicio + 2:10] == sequencia_secundaria[inicio + 3:10] or
                  sequencia_sorteada[inicio + 2:10] == sequencia_secundaria[inicio + 4:10] or
                  sequencia_sorteada[inicio + 2:10] == sequencia_secundaria[inicio + 5:10]):
                dicio_final["encontrou"] += 1
                aux = True
                break
                #---------------------------------------------------------------------

            elif (sequencia_sorteada[inicio + 3:10] == sequencia_secundaria[inicio:10] or
                  sequencia_sorteada[inicio + 3:10] == sequencia_secundaria[inicio + 1:10] or
                  sequencia_sorteada[inicio + 3:10] == sequencia_secundaria[inicio + 2:10] or
                  sequencia_sorteada[inicio + 3:10] == sequencia_secundaria[inicio + 3:10] or
                  sequencia_sorteada[inicio + 3:10] == sequencia_secundaria[inicio + 4:10] or
                  sequencia_sorteada[inicio + 3:10] == sequencia_secundaria[inicio + 5:10]):
                dicio_final["encontrou"] += 1
                aux = True
                break
                #---------------------------------------------------------------------

            elif (sequencia_sorteada[inicio + 4:10] == sequencia_secundaria[inicio:10] or
                  sequencia_sorteada[inicio + 4:10] == sequencia_secundaria[inicio + 1:10] or
                  sequencia_sorteada[inicio + 4:10] == sequencia_secundaria[inicio + 2:10] or
                  sequencia_sorteada[inicio + 4:10] == sequencia_secundaria[inicio + 3:10] or
                  sequencia_sorteada[inicio + 4:10] == sequencia_secundaria[inicio + 4:10] or
                  sequencia_sorteada[inicio + 4:10] == sequencia_secundaria[inicio + 5:10]):
                dicio_final["encontrou"] += 1
                aux = True
                break
                #---------------------------------------------------------------------

            elif (sequencia_sorteada[inicio + 5:10] == sequencia_secundaria[inicio:10] or
                  sequencia_sorteada[inicio + 5:10] == sequencia_secundaria[inicio + 1:10] or
                  sequencia_sorteada[inicio + 5:10] == sequencia_secundaria[inicio + 2:10] or
                  sequencia_sorteada[inicio + 5:10] == sequencia_secundaria[inicio + 3:10] or
                  sequencia_sorteada[inicio + 5:10] == sequencia_secundaria[inicio + 4:10] or
                  sequencia_sorteada[inicio + 5:10] == sequencia_secundaria[inicio + 5:10]):
                dicio_final["encontrou"] += 1
                aux = True
                break
        if not aux:
            dicio_final["não encontrou"] += 1

    print("Sub-sequências de 10 :" + str ( dicio_final) )

def estatistica_sequencia_onze():

    global LISTA_TODOS_JOGOS
    dicio_final = {"encontrou": 0, "não encontrou": 0}
    inicio = 0
    aux = False

    for sequencia_sorteada in LISTA_TODOS_JOGOS:
        aux = False
        for sequencia_secundaria in [x for x in LISTA_TODOS_JOGOS if x != sequencia_sorteada]:

            if (sequencia_sorteada[inicio:11] == sequencia_secundaria[inicio:11] or
                sequencia_sorteada[inicio:11] == sequencia_secundaria[inicio + 1:11] or
                sequencia_sorteada[inicio:11] == sequencia_secundaria[inicio + 2:11] or
                sequencia_sorteada[inicio:11] == sequencia_secundaria[inicio + 3:11] or
                sequencia_sorteada[inicio:11] == sequencia_secundaria[inicio + 4:11]):
                dicio_final["encontrou"] += 1
                aux = True
                break
                #---------------------------------------------------------------------

            elif (sequencia_sorteada[inicio + 1:11] == sequencia_secundaria[inicio:11] or
                  sequencia_sorteada[inicio + 1:11] == sequencia_secundaria[inicio + 1:11] or
                  sequencia_sorteada[inicio + 1:11] == sequencia_secundaria[inicio + 2:11] or
                  sequencia_sorteada[inicio + 1:11] == sequencia_secundaria[inicio + 3:11] or
                  sequencia_sorteada[inicio + 1:11] == sequencia_secundaria[inicio + 4:11]):
                  dicio_final["encontrou"] += 1
                  aux = True
                  break
                #---------------------------------------------------------------------

            elif (sequencia_sorteada[inicio + 2:11] == sequencia_secundaria[inicio:11] or
                  sequencia_sorteada[inicio + 2:11] == sequencia_secundaria[inicio + 1:11] or
                  sequencia_sorteada[inicio + 2:11] == sequencia_secundaria[inicio + 2:11] or
                  sequencia_sorteada[inicio + 2:11] == sequencia_secundaria[inicio + 3:11] or
                  sequencia_sorteada[inicio + 2:11] == sequencia_secundaria[inicio + 4:11]):
                  dicio_final["encontrou"] += 1
                  aux = True
                  break
                #---------------------------------------------------------------------

            elif (sequencia_sorteada[inicio + 3:11] == sequencia_secundaria[inicio:11] or
                  sequencia_sorteada[inicio + 3:11] == sequencia_secundaria[inicio + 1:11] or
                  sequencia_sorteada[inicio + 3:11] == sequencia_secundaria[inicio + 2:11] or
                  sequencia_sorteada[inicio + 3:11] == sequencia_secundaria[inicio + 3:11] or
                  sequencia_sorteada[inicio + 3:11] == sequencia_secundaria[inicio + 4:11]):
                  dicio_final["encontrou"] += 1
                  aux = True
                  break

            elif (sequencia_sorteada[inicio + 4:11] == sequencia_secundaria[inicio:11] or
                  sequencia_sorteada[inicio + 4:11] == sequencia_secundaria[inicio + 1:11] or
                  sequencia_sorteada[inicio + 4:11] == sequencia_secundaria[inicio + 2:11] or
                  sequencia_sorteada[inicio + 4:11] == sequencia_secundaria[inicio + 3:11] or
                  sequencia_sorteada[inicio + 4:11] == sequencia_secundaria[inicio + 4:11]):
                  dicio_final["encontrou"] += 1
                  aux = True
                  break

        if not aux:
            dicio_final["não encontrou"] += 1

    print("Sub-sequências de 11 :" + str ( dicio_final) )

def estatistica_sequencia_doze():

    global LISTA_TODOS_JOGOS
    dicio_final = {"encontrou": 0, "não encontrou": 0}
    inicio = 0
    aux = False

    for sequencia_sorteada in LISTA_TODOS_JOGOS:
        aux = False
        for sequencia_secundaria in [x for x in LISTA_TODOS_JOGOS if x != sequencia_sorteada]:

            if (sequencia_sorteada[inicio:12] == sequencia_secundaria[inicio:12] or
                sequencia_sorteada[inicio:12] == sequencia_secundaria[inicio + 1:12] or
                sequencia_sorteada[inicio:12] == sequencia_secundaria[inicio + 2:12] or
                sequencia_sorteada[inicio:12] == sequencia_secundaria[inicio + 3:12]):
                dicio_final["encontrou"] += 1
                aux = True
                break
                #---------------------------------------------------------------------

            elif (sequencia_sorteada[inicio + 1:12] == sequencia_secundaria[inicio:12] or
                  sequencia_sorteada[inicio + 1:12] == sequencia_secundaria[inicio + 1:12] or
                  sequencia_sorteada[inicio + 1:12] == sequencia_secundaria[inicio + 2:12] or
                  sequencia_sorteada[inicio + 1:12] == sequencia_secundaria[inicio + 3:12]):
                  dicio_final["encontrou"] += 1
                  aux = True
                  break
                #---------------------------------------------------------------------

            elif (sequencia_sorteada[inicio + 2:12] == sequencia_secundaria[inicio:12] or
                  sequencia_sorteada[inicio + 2:12] == sequencia_secundaria[inicio + 1:12] or
                  sequencia_sorteada[inicio + 2:12] == sequencia_secundaria[inicio + 2:12] or
                  sequencia_sorteada[inicio + 2:12] == sequencia_secundaria[inicio + 3:12]):
                  dicio_final["encontrou"] += 1
                  aux = True
                  break
                #---------------------------------------------------------------------

            elif (sequencia_sorteada[inicio + 3:12] == sequencia_secundaria[inicio:12] or
                  sequencia_sorteada[inicio + 3:12] == sequencia_secundaria[inicio + 1:12] or
                  sequencia_sorteada[inicio + 3:12] == sequencia_secundaria[inicio + 2:12] or
                  sequencia_sorteada[inicio + 3:12] == sequencia_secundaria[inicio + 3:12]):
                  dicio_final["encontrou"] += 1
                  aux = True
                  break

        if not aux:
            dicio_final["não encontrou"] += 1

    print("Sub-sequências de 12 :" + str ( dicio_final) )

def estatistica_sequencia_treze():

    global LISTA_TODOS_JOGOS
    dicio_final = {"encontrou": 0, "não encontrou": 0}
    inicio = 0
    aux = False

    for sequencia_sorteada in LISTA_TODOS_JOGOS:
        aux = False
        for sequencia_secundaria in [x for x in LISTA_TODOS_JOGOS if x != sequencia_sorteada]:

            if (sequencia_sorteada[inicio:13] == sequencia_secundaria[inicio:13] or
                sequencia_sorteada[inicio:13] == sequencia_secundaria[inicio + 1:13] or
                sequencia_sorteada[inicio:13] == sequencia_secundaria[inicio + 2:13]):
                dicio_final["encontrou"] += 1
                aux = True
                break
                #---------------------------------------------------------------------

            elif (sequencia_sorteada[inicio + 1:13] == sequencia_secundaria[inicio:13] or
                  sequencia_sorteada[inicio + 1:13] == sequencia_secundaria[inicio + 1:13] or
                  sequencia_sorteada[inicio + 1:13] == sequencia_secundaria[inicio + 2:13]):
                  dicio_final["encontrou"] += 1
                  aux = True
                  break
                #---------------------------------------------------------------------

            elif (sequencia_sorteada[inicio + 2:13] == sequencia_secundaria[inicio:13] or
                  sequencia_sorteada[inicio + 2:13] == sequencia_secundaria[inicio + 1:13] or
                  sequencia_sorteada[inicio + 2:13] == sequencia_secundaria[inicio + 2:13] or
                  sequencia_sorteada[inicio + 2:13] == sequencia_secundaria[inicio + 3:13]):
                  dicio_final["encontrou"] += 1
                  aux = True
                  break

        if not aux:
            dicio_final["não encontrou"] += 1

    print("Sub-sequências de 13 :" + str ( dicio_final) )

def estatistica_sequencia_quatorze():

    global LISTA_TODOS_JOGOS
    dicio_final = {"encontrou": 0, "não encontrou": 0}
    inicio = 0
    aux = False

    for sequencia_sorteada in LISTA_TODOS_JOGOS:
        aux = False
        for sequencia_secundaria in [x for x in LISTA_TODOS_JOGOS if x != sequencia_sorteada]:

            if (sequencia_sorteada[inicio:14] == sequencia_secundaria[inicio:14] or
                sequencia_sorteada[inicio:14] == sequencia_secundaria[inicio + 1:14]):
                dicio_final["encontrou"] += 1
                aux = True
                break
                #---------------------------------------------------------------------

            elif (sequencia_sorteada[inicio + 1:14] == sequencia_secundaria[inicio:14] or
                  sequencia_sorteada[inicio + 1:14] == sequencia_secundaria[inicio + 1:14]):
                  dicio_final["encontrou"] += 1
                  aux = True
                  break

        if not aux:
            dicio_final["não encontrou"] += 1

    print("Sub-sequências de 14 :" + str ( dicio_final) )

""" Padrão de distância de um número ao outro nas unidades."""
def estatistica_analize_unidades ():

    global LISTA_TODOS_JOGOS
    dicio_final = { x : 0 for x in range(1,10)}

    for sequencia in LISTA_TODOS_JOGOS :
        contador = 0
        for unidade in sequencia :
            if unidade < 10 : contador += 1
        dicio_final [ contador ] += 1

    print( dicio_final)

""" Números repetidos do jogo anterior."""
def estatistica_numeros_anterior() :

    dicio_quantidade     = { v : 0 for v in range( 0, 16 ) }
    dicio_unidade_dezena = { "unidade":0, "dezena":0 }

    cont = 1
    for sequencia in LISTA_TODOS_JOGOS[:-1] :
        repetidos = set(sequencia) & set(LISTA_TODOS_JOGOS[cont])
        dicio_quantidade[len(repetidos)] += 1
        for valor in repetidos :
            if   valor < 10  : dicio_unidade_dezena["unidade"] += 1
            elif valor >= 10 : dicio_unidade_dezena["dezena"] += 1
        cont += 1

    lista_quant = { key : v for key,v in dicio_quantidade.items() if v > 0 }
    print("media_quant : ", lista_quant)
    print(dicio_unidade_dezena)

def estatistica_atrasadas_unidades():

    global LISTA_TODOS_JOGOS
    dicio_final      = { key : {k : 0 for k in range(1, 21) } for key in range(1, 10) }
    listas_excluidas = []

    for unidade in dicio_final.keys() :
        contador = 0
        listas_excluidas.clear()
        for sorteio in [ lista for lista in LISTA_TODOS_JOGOS if lista not in listas_excluidas ]:
            if not unidade in sorteio :
                contador += 1
                listas_excluidas.append ( sorteio )
            elif contador > 0:
                 dicio_final [ unidade ][contador] += 1
                 contador = 0

    dicio_imprimir = {unidade: {k: v for k, v in contadores.items() if v > 0} for unidade, contadores in dicio_final.items()}

    for key in dicio_imprimir.keys() :
      print(f"{key} - {dicio_imprimir[key]}")

def estatistica_atrasadas_dezenas():

    global LISTA_TODOS_JOGOS
    dicio_final      = { key : {k : 0 for k in range(1, 21) } for key in range(10, 26) }
    listas_excluidas = []

    for unidade in dicio_final.keys() :
        contador = 0
        listas_excluidas.clear()
        for sorteio in [ lista for lista in LISTA_TODOS_JOGOS if lista not in listas_excluidas ]:
            if not unidade in sorteio :
                contador += 1
                listas_excluidas.append ( sorteio )
            elif contador > 0:
                 dicio_final [ unidade ][contador] += 1
                 contador = 0

    dicio_imprimir = {unidade: {k: v for k, v in contadores.items() if v > 0} for unidade, contadores in dicio_final.items()}

    for key in dicio_imprimir.keys() :
      print(f"{key} - {dicio_imprimir[key]}")

""" Mostra as atrasadas atualmente. """
def estatistica_atrasadas() :

    global LISTA_TODOS_JOGOS
    dicio_dados = { key : 0 for  key in range( 1, 26)} #guarda o tempo de atraso dos números.

    for key in dicio_dados.keys():
        cont = 0
        aux  =  False
        for sequencia in LISTA_TODOS_JOGOS :
            if key not in sequencia :
               cont += 1
               aux = True
               if cont == 2 :
                  dicio_dados[key] = cont
                  break

            elif aux == True and cont == 1 or aux == False : break

    lista_atrasados = { key:valor for key, valor in dicio_dados.items() if valor == 2 }
    print(lista_atrasados)

def estatistica_evidencia_unidades():

    global LISTA_TODOS_JOGOS
    dicio_dados = { key : {k : 0 for k in range(1, 26) } for key in range(1, 10) }

    for key in dicio_dados.keys():

       contador = 0
       flag_aux = False

       for sequencia in LISTA_TODOS_JOGOS :

           if key in sequencia :
              contador += 1
              flag_aux = True

           elif flag_aux ==  True :
               dicio_dados [ key ][ contador ] += 1
               contador = 0
               flag_aux = False


    dicio_imprimir = {unidade: {k: v for k, v in contadores.items() if v > 0} for unidade, contadores in dicio_dados.items()}

    for key in dicio_imprimir.keys() :
      print(f"{key} - {dicio_imprimir[key]}")


def estatistica_evidencia_dezenas():

    global LISTA_TODOS_JOGOS
    dicio_dados = { key : {k : 0 for k in range(1, 26) } for key in range(10, 26) }

    for key in dicio_dados.keys():

       contador = 0
       flag_aux = False

       for sequencia in LISTA_TODOS_JOGOS :

           if key in sequencia :
              contador += 1
              flag_aux = True

           elif flag_aux ==  True :
               dicio_dados [ key ][ contador ] += 1
               contador = 0
               flag_aux = False


    dicio_imprimir = {unidade: {k: v for k, v in contadores.items() if v > 0} for unidade, contadores in dicio_dados.items()}

    for key in dicio_imprimir.keys() :
      print(f"{key} - {dicio_imprimir[key]}")


#-----------------------------------------------------------------------
def format_sequencia( lista_param ):

    str_result = ""

    for dezena in lista_param :
        if dezena < 10 : str_result += "0" + str ( dezena ) + " "
        else : str_result += str ( dezena ) + " "

    return  str_result.rstrip()

""" analise se as atrasadas mais possíveis de sair, estam relacionadas aos seus proximos, ex : 12, 14 então 13 """
def estatistica_criterio_atrasadas() :

    global LISTA_TODOS_JOGOS

    dicio_final = { "tem":0, "não tem":0}

    indice_sorteios = 1
    for sequencia in LISTA_TODOS_JOGOS [ : -1 ] :

        for indice, valor in enumerate ( sequencia ) :

            if indice + 1 <= 12 :
               if valor + valor + 1 + sequencia[ indice + 2 ] == sequencia[ indice ] :




    print ( dicio_final )

if __name__ == '__main__':

   extrai_todos_jogos_site()
   print("extrai_todos_jogos_site......ok")

   #estatistica_01_22_25() """ Não estou usando no sistema principal."""

   #estatistica_espelho()
   #estatistica_sequencia_dez()
   #estatistica_sequencia_onze()
   #estatistica_sequencia_doze()
   #estatistica_sequencia_treze()
   #estatistica_sequencia_quatorze()
   #estatistica_analize_unidades()
   #estatistica_numeros_anterior()
   #estatistica_atrasadas_unidades()
   #estatistica_atrasadas_dezenas()
   #estatistica_atrasadas()
   #estatistica_evidencia_unidades()
   #estatistica_evidencia_dezenas()
   estatistica_criterio_atrasadas()