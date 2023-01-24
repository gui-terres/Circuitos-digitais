import collections

def trata_string(string1, string2):
    string1_vetor = list(string1)
    string2_vetor = list(string2)
    string_retorno = ""

    for i in range(0, len(string1_vetor)):
        if string1_vetor[i] == string2_vetor[i]:
            string_retorno += string1_vetor[i]
        elif string1_vetor[i] != string2_vetor[i]:
            string_retorno += "-"

    return string_retorno

def trata_string_2 (string1, string2):
    string_retorno = string1 + "-" + string2

    return string_retorno

def trata_string_3(string1, string2):
    string1_vetor = list(string1)
    string2_vetor = list(string2)
    string_retorno = ""
    diferencas = 0

    for i in range(0, len(string1_vetor)):
        if string1_vetor[i] == string2_vetor[i]:
            string_retorno += string1_vetor[i]
        elif string1_vetor[i] != string2_vetor[i]:
            string_retorno += "-"
            diferencas += 1

    if diferencas != 1 or string_retorno == len(string1_vetor)*'-':
        string_retorno = int(2)

    return string_retorno, diferencas

def separa_mint_dontcare(mintermos, dontcare):
    mintermos = mintermos.split(' ')
    dontcare = dontcare.split(' ')

    return mintermos, dontcare
def mintermos_dontcare(mintermos, dontcare):
    mint_dont = mintermos + dontcare

    for i in range(0, len(mint_dont)):
        mint_dont[i] = int(mint_dont[i])
    mint_dont.sort()
    for i in range(0, len(mint_dont)):
        mint_dont[i] = str(mint_dont[i])

    return mint_dont

def qtd_tracos(string):
    qtd_tracos = 0
    for i in string:
        if i == "-":
            qtd_tracos += 1
    return qtd_tracos

def testa_diferencas(string1, string2):
    string1_vetor = list(string1)
    string2_vetor = list(string2)
    diferencas = 0

    for i in range(0, len(string1_vetor)):
        if string1_vetor[i] != string2_vetor[i]:
            diferencas += 1

    return diferencas

def adiciona_m_mintermos_sep(mintermos):
    for i in range(0, len(mintermos)):
        mintermos[i] = "m" + str(mintermos[i])

    return mintermos

def remove_repetidos (array):
    array_saida = []

    for i in array:
        if i not in array_saida:
            array_saida.append(i)

    return array_saida

def monta_tab_vdd(nroentradas):
    tamanho = 2 ** nroentradas
    coluna_0 = []

    for i in range(0, tamanho):
        coluna_0.append(bin(i).replace("0b", ""))
        while len(coluna_0[i]) < nroentradas:
            coluna_0[i] = "0" + coluna_0[i]

    return coluna_0

def monta_coluna0(nroentradas, mintermos, tabela_vdd):
    g_binario = []
    g_mintermos = []

    for x in range(0, nroentradas+1):
        g_binario.append([])
        g_mintermos.append([])

    casa_vetor = 0

    for item in tabela_vdd:
        qtd_numeros = collections.Counter(item)
        contador = 0

        while contador <= nroentradas:
            if (qtd_numeros['1'] == contador) and (str(casa_vetor) in mintermos):
                g_binario[contador].append(item)
                g_mintermos[contador].append("m" + str(casa_vetor))
            contador = contador + 1
        casa_vetor = casa_vetor + 1

    return g_binario, g_mintermos

def monta_coluna1(nroentradas, g_binario, g_mintermos):
    retorno = []
    retorno2 = []

    for i in range(0, nroentradas+1):
        retorno.append([])
        retorno2.append([])

    for i in range(0, len(g_binario)-1):
      for j in g_binario[i]:
        for k in g_binario[i+1]:
            string_retorno = trata_string(j, k)
            retorno[i].append(string_retorno)

    for i in range(0, len(g_mintermos)-1):
      for j in g_mintermos[i]:
        for k in g_mintermos[i+1]:
            string_retorno = trata_string_2(j, k)
            retorno2[i].append(string_retorno)

    retorno3 = []
    retorno4 = []

    for i in range(0, nroentradas+1):
        retorno3.append([])
        retorno4.append([])

    for i in range(0, len(retorno)):
        qtd = 0
        for j in range(0, len(retorno[i])):
            qtd = qtd_tracos(retorno[i][j])
            if (retorno[i][j] not in retorno3[i]) and qtd == 1:
                retorno3[i].append(retorno[i][j])
                retorno4[i].append(retorno2[i][j])

    return retorno3, retorno4

def monta_coluna_2(nroentradas, g_binario, g_mintermos):
    retorno = []
    retorno2 = []

    for i in range(0, nroentradas+1):
        retorno.append([])
        retorno2.append([])

    for i in range(0, len(g_binario)-1):
        for j in range(0, len(g_binario[i])):
            for k in range(0, len(g_binario[i+1])):
                string_retorno, diferencas = trata_string_3(g_binario[i][j], g_binario[i+1][k])
                if string_retorno != 2:
                    retorno[i].append(string_retorno)
                if diferencas == 1 and string_retorno != 2:
                    retorno2[i].append(g_mintermos[i][j] + '-' + g_mintermos[i+1][k])

    retorno3 = []
    retorno4 = []

    for i in range(0, nroentradas+1):
        retorno3.append([])
        retorno4.append([])

    for i in range(0, len(retorno)):
        for j in range(0, len(retorno[i])):
            if retorno[i][j] not in retorno3[i]:
                retorno3[i].append(retorno[i][j])
                retorno4[i].append(retorno2[i][j])

    return retorno3, retorno4

def completa_coluna2(g_binario, g_mintermos, col2_b, col2_m):
    array_final = []
    array_final2 = []

    for i in range(0, len(g_binario) - 2):
        for j in range(0, len(g_binario[i])):
            diferenca = []
            for k in range(0, len(g_binario[i + 1])):
                diferenca.append(int(testa_diferencas(g_binario[i][j], g_binario[i + 1][k])))
            qtd1s = diferenca.count(1)
            if qtd1s == 0:
                array_final.append(g_binario[i][j])
                array_final2.append(g_mintermos[i][j])

    array_final2_separado = []
    for i in array_final2:
        array_final2_separado.append(i.split('-'))

    col2_b_separado = []
    col2_m_separado = []
    for i in range(0, len(col2_b)):
        for j in range(0, len(col2_b[i])):
            col2_b_separado.append(col2_b[i][j])
            col2_m_separado.append(col2_m[i][j])

    return array_final, array_final2

def separa_array(array1, array2):
    retorno = []
    retorno2 = []

    for i in array1:
        for j in i:
            retorno.append(j)

    for i in array2:
        for j in i:
            retorno2.append(j)

    return retorno, retorno2

def elimina_desnecessario(mint_duplo, g_mintermos, g_binarios):
    mint_duplo_2 = []
    mint_duplo_2_fin = []
    mint_duplo_2_final = []

    for i in range(0, len(mint_duplo)):
        mint_duplo_2.append(mint_duplo[i].split('-'))
    for i in range(0, len(mint_duplo_2)):
        for j in range(0, len(mint_duplo_2[i])):
            mint_duplo_2_fin.append(mint_duplo_2[i][j])
    for i in range(0, len(mint_duplo_2_fin)):
        for j in range(0, len(mint_duplo_2_fin)):
            mint_duplo_2_final.append(mint_duplo_2_fin[i] + "-" + mint_duplo_2_fin[j])

    retorno_mint = []
    retorno_bin = []

    for i in range(0, len(g_mintermos)):
        flag = 0
        for j in range(0, len(mint_duplo_2_final)):
            if g_mintermos[i] == mint_duplo_2_final[j]:
                flag += 1
        if flag == 0:
            retorno_mint.append(g_mintermos[i])
            retorno_bin.append(g_binarios[i])

    return retorno_mint, retorno_bin

def forma_tabcob(bin, bin1, min, min1) -> tuple:
    retorno_b = [*bin, *bin1]
    retorno_m = [*min, *min1]

    for i in range(0, len(retorno_m)):
        retorno_m[i] = retorno_m[i].split("-")

    return retorno_b, retorno_m

def forma_matriz(tabcob_m, mintermos):
    matriz_retorno = []

    for i in range(0, len(mintermos)):
        matriz_retorno.append([])

    for i in range(0, len(mintermos)):
        for j in range(0, len(tabcob_m)):
            flag = 0
            for k in range(0, len(tabcob_m[j])):
                if mintermos[i] == tabcob_m[j][k]:
                    flag += 1
            if flag != 0:
                matriz_retorno[i].append("x")
            else:
                matriz_retorno[i].append("0")

    matriz_retorno_final = []

    for i in range(0, len(tabcob_m)):
        matriz_retorno_final.append([])
    for i in range(0, len(matriz_retorno)):
        for j in range(0, len(tabcob_m)):
            matriz_retorno_final[j].append(matriz_retorno[i][j])

    return matriz_retorno_final, matriz_retorno

def define_linhas_essenciais(matriz_col):
    linhas_essenciais = []

    for i in range(0, len(matriz_col)):
        linhas_ocorrencias = []
        for j in range(0, len(matriz_col[i])):
            if matriz_col[i][j] == "x":
                linhas_ocorrencias.append(j)
        if len(linhas_ocorrencias) == 1:
            linhas_essenciais.append(linhas_ocorrencias[0])

    return linhas_essenciais

def define_linhas_faltantes(mintermos_separados, tabcob_m, linhas_analise):
    retorno = []
    for i in range(0, len(tabcob_m)):
        for j in range(0, len(linhas_analise)):
            if i == linhas_analise[j]:
                retorno.append(tabcob_m[i])

    retorno_definitivo = []
    for i in mintermos_separados:
        flag = 0
        for j in range(0, len(retorno)):
            for k in range(0, len(retorno[j])):
                if i == retorno[j][k]:
                    flag += 1
        if flag == 0:
            retorno_definitivo.append(i)

    retorno_definitivo_2 = []
    for i in range(0, len(tabcob_m)):
        qtd = 0
        for j in range(0, len(tabcob_m[i])):
            for k in retorno_definitivo:
                if k == tabcob_m[i][j]:
                    qtd += 1
        retorno_definitivo_2.append(qtd)

    tudo_certinho = []
    for i in range(0, len(retorno_definitivo_2)):
        if retorno_definitivo_2[i] == len(retorno_definitivo):
            tudo_certinho.append(i)

    indices = []
    indicador = 0
    while indicador == 0:
        maximo = max(retorno_definitivo_2)
        indice = retorno_definitivo_2.index(maximo)
        indices.append(indice)
        retorno_definitivo_2[indice] = 0
        if retorno_definitivo_2 == [0]*len(retorno_definitivo_2):
            indicador = 1

    saida = []
    for i in indices:
        for j in range(0, len(tabcob_m[i])):
            for k in range(0, len(retorno_definitivo)):
                if retorno_definitivo[k] == tabcob_m[i][j]:
                    saida.append(i)
                    retorno_definitivo[k] = 0
        if retorno_definitivo == [0]*len(retorno_definitivo):
            final = remove_repetidos(saida)
            return final

def linhas_essenciais_completas(linhas_essenciais, linhas_faltantes):
    saida = []

    if linhas_essenciais != [] and linhas_essenciais != None:
        for i in range(0, len(linhas_essenciais)):
            if linhas_essenciais[i] not in saida:
                saida.append(linhas_essenciais[i])

    if linhas_faltantes != [] and linhas_faltantes != None:
        for i in range(0, len(linhas_faltantes)):
            flag = 0
            for j in range(0, len(saida)):
                if linhas_faltantes[i] == saida[j]:
                    flag += 1
            if flag == 0:
                saida.append(linhas_faltantes[i])

    return saida

def binarios_para_analisar(linhas_essenciais, tabcob_b):
    binario_final = []
    for i in linhas_essenciais:
        for j in range(0, len(tabcob_b)):
            if i == j:
                binario_final.append(tabcob_b[j])
    return binario_final

def exibe_resposta(binario_final):
    binario_final_2 = []

    for i in binario_final:
        binario_final_2.append(list(i))

    resposta = ""
    for i in range(0, len(binario_final_2)):
        for j in range(0, len(binario_final_2[i])):
            if binario_final_2[i][j] == '0':
                resposta += chr(65 + j) + "'"
            elif binario_final_2[i][j] == '1':
                resposta += chr(65 + j)
        resposta += " + "

    return resposta[:-2]

##############################
nroentradas = int(input("Digite o número de entradas: "))
mintermos = str(input("Digite os mintermos separados por espaço (exemplo: 4 5 6 8 9 10 13): "))
dontcare = str(input("Digite os elementos don't care separados por espaço (exemplo: 0 7 15): "))

"""
Abaixo estão exemplos de mintermos e dontcare. Entre parenteses está o número de elementos

#mintermos = "4 5 6 8 9 10 13" (4)
#dontcare = "0 7 15" (4)

#mintermos = "0 3 4 7 8" (4)
#dontcare = "10 11 12 13 14 15" (4)

#mintermos = "4 8 10 12 13 14" (4)
#dontcare = "3 5 6 9 15" (4)

#mintermos = "6" (3)
#dontcare = "1 2 4 5" (3)

#mintermos = "0 3 6" (3)
#dontcare = "1 2 4" (3)

#mintermos = "0" (5)
#dontcare = "1 2" (5)

"""

mintermos, dontcare = separa_mint_dontcare(mintermos, dontcare)
tabela_vdd = monta_tab_vdd(nroentradas)
mint_dont = mintermos_dontcare(mintermos, dontcare)
coluna_0_b, coluna_0_m = monta_coluna0(nroentradas, mint_dont, tabela_vdd)
coluna_1_b, coluna_1_m = monta_coluna1(nroentradas, coluna_0_b, coluna_0_m)
coluna_2_b, coluna_2_m = monta_coluna_2(nroentradas, coluna_1_b, coluna_1_m)
comp_col2_b, comp_col2_m = completa_coluna2(coluna_1_b, coluna_1_m, coluna_2_b, coluna_2_m)
coluna_2_b_separada, coluna_2_m_separada = separa_array(coluna_2_b, coluna_2_m)
comp_col2_m_org, comp_col2_b_org = elimina_desnecessario(coluna_2_m_separada, comp_col2_m, comp_col2_b)
tabcob_b, tabcob_m = forma_tabcob(comp_col2_b_org, coluna_2_b_separada, comp_col2_m_org, coluna_2_m_separada)
mintermos_separados = adiciona_m_mintermos_sep(mintermos)
matriz_linhas, matriz_colunas = forma_matriz(tabcob_m, mintermos_separados)
linhas_essenciais = define_linhas_essenciais(matriz_colunas)
linhas_faltantes = define_linhas_faltantes(mintermos_separados, tabcob_m, linhas_essenciais)
linhas = linhas_essenciais_completas(linhas_essenciais, linhas_faltantes)
binarios_final = binarios_para_analisar(linhas, tabcob_b)
resultado = exibe_resposta(binarios_final)

print("Mintermos: ", mintermos)
print("Dontcare: ", dontcare)
print("Tabela verdade: ", tabela_vdd)
print("Mintdont: ", mint_dont)
print("Coluna 0 binario: ", coluna_0_b)
print("Coluna 0 mintermos: ", coluna_0_m)
print("Coluna 1 binario: ", coluna_1_b)
print("Coluna 1 mintermos: ", coluna_1_m)
print("Coluna 2 binario: ", coluna_2_b)
print("Coluna 2 mintermos: ", coluna_2_m)
print("Completa coluna 2 binario: ", comp_col2_b)
print("Completa coluna 2 mintermos: ", comp_col2_m)
print("Coluna 2 binaria separada: ", coluna_2_b_separada)
print("Coluna 2 mintermos separada: ", coluna_2_m_separada)
print("Completa coluna 2 binario ajeitada: ", comp_col2_b_org)
print("Completa coluna 2 mintermos ajeitada: ", comp_col2_m_org)
print("Tabela de cobertura binaria: ", tabcob_b)
print("Tabela de cobertura mintermos: ", tabcob_m)
print("Mintermos separados: ", mintermos_separados)
## Pritando matriz ##
print("Matriz em linhas: ")
for i in matriz_linhas:
    print(i)
#####################
print("Matriz em colunas: ", matriz_colunas)
print("Linhas essenciais: ", linhas_essenciais)
print("Linhas faltantes: ", linhas_faltantes)
print("Linhas: ", linhas)
print("Binarios para analisar: ", binarios_final)
print("Resultado: ", resultado)