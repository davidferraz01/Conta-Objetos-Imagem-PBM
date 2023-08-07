import sys

class ProcessarImagem:
  def __init__(self, arquivo_pbm):
    ## Inicia as variaveis que serao utilizadas no Algoritmo. ##
    self.arquivo_pbm = arquivo_pbm
    self.pbm_info = None
    self.largura = None
    self.altura = None
    self.matriz = None

    ##elem_estru refere-se ao elemento estruturate ou máscara
    self.dim_elem_estr = None
    self.dim_borda = None
    self.elem_estr_sem_buraco = None
    self.borda_sem_buraco = None
    self.elem_estr_com_buraco = None  
    self.borda_com_buraco = None
    

  def ler_imagem(self):
    ## Ler o arquivo de imagem e atualiza as variaveis da Classe (pbm_info, largura e altura). ##
    with open(self.arquivo_pbm, "r") as image:
      self.pbm_info = (image.read())
    
    temp = self.pbm_info.split('\n')
    
    dimensoes = temp[2].split()
    self.largura = int(dimensoes[0])
    self.altura = int(dimensoes[1])
  
    return True

  
  def imagem_matriz(self):
    ## Processa a Imagem e cria uma Matrix na qual cada ponto representa um pixel, sendo 1 a cor preta e 0 a cor branca. Ao final, salva a matriz na variavel da Classe e retorna True para sinalizar que o processo foi realizado com sucesso. ##
    matriz = [[0 for i in range(self.largura)] for j in range(self.altura)]
    temp = ''.join(self.pbm_info.split('\n')[3:])
    count = 0
    
    for i in range(self.altura):
      for j in range(self.largura):
        matriz[i][j] = int(temp[count])
        count += 1
        
    self.matriz = matriz
    return True


  def print_matriz(self,matriz):
    ## Algoritmo utilizado para imprimir as Matrizes. Recebe como argumento uma Matriz qualquer e a imprime de maneira organizada para melhorar sua visualizacao. ##
    for j in matriz:
      for i in j:
        print(i, end = " ")
      print()
    print()
    

  def porcao_matriz(self, matriz, x_1,x_2 , y_1,y_2):
    ## Algoritmo auxiliar utilizado na funcao "erosao". Recebe como arumento uma Matriz qualquer e coordenadas na qual deseja-se extrair aquela "porcao" da matriz. Retorna a porcao desejada da matriz. ##
    porcao = []
    aux = []
    for i in range(x_1,x_2):
      for j in range(y_1,y_2):
        aux.append(matriz[i][j])
      porcao.append(aux)
      aux = []
  
    return porcao


  def erosao(self, matriz, elem_estr, dim_elem_estr):
    ## Realiza o processo de erosao de uma matriz qualquer. Recebe como argumento a matriz desejada, o elemento estruturante e a dimensao do mesmo. Tal dimensao sera utilizada para calcular uma constante responsável pelo controle de onde o elemento estruturante irá passar (nesse caso, o elemento estruturante comeca em uma posicao a qual ele encaixa-se por completo no canto mais superior e mais a esquerda possivel, em seguida perocurre a matriz/imagem por completo). Retorna a Matriz erodida. ##
    constante = (dim_elem_estr-1)//2
    
    matriz_erosao = [[0 for i in range(self.largura)] for j in range(self.altura)]
    
    for i in range(constante, self.altura-constante):
      for j in range(constante, self.largura-constante):
        temp = self.porcao_matriz(matriz, i-constante,i+constante+1, j-constante,j+constante+1)
        if temp == elem_estr:
          matriz_erosao[i][j] = 1
        
    return matriz_erosao


  def complementar(self, matriz):
    ## Calcula e retorna o complementar da matriz passada como arumento. ##
    matriz_comp = [[0 for i in range(self.largura)] for j in range(self.altura)]
    for i in range(self.altura):
      for j in range(self.largura):
          if matriz[i][j] == 0:
            matriz_comp[i][j] = 1
          else:
            matriz_comp[i][j] = 0
  
    return matriz_comp


  def intersecao(self, matriz_A, matriz_B):
    ## Calcula e retorna uma Matriz que representa a intersecao de duas matrizes quaisquer, ambas passadas como argumento a funcao ## 
    matriz_inter = [[0 for i in range(self.largura)] for j in range(self.altura)]
    for i in range(self.altura):
      for j in range(self.largura):
        if matriz_A[i][j] == 1 and matriz_A[i][j] == matriz_B[i][j]:
          matriz_inter[i][j] = 1
    
    return matriz_inter


  def hit_or_miss(self, elem_estr1, dim_elem_estr1, elem_estr2, dim_elem_estr2):
    ## Realiza o processo conhecido como Hit or Miss, o qual detecta um determinado formato ou padrão na matriz usando o algoritmo de erosão e um par de elementos estruturantes disjuntos. O resultado final desse processo são os objetos na imagem com o formato em questão reduzidos à um único pixel, sendo possível fazer a contabilidade de elementos encontrados.
    passo_1 = self.erosao(self.matriz, elem_estr1, dim_elem_estr1)

    matriz_comp = self.complementar(self.matriz)
    
    passo_2 = self.erosao(matriz_comp, elem_estr2, dim_elem_estr2)

    passo_3 = self.intersecao(passo_1, passo_2)

    return passo_3

  
  def verifica_ocorrencias(self, matriz):
    ## Algoritmo auxiliar utilizado na funcao "identificar_elementos". Recebe como argumento a saida do algoritmo "hit_or_miss (matriz) e conta quantas ocorrencias foram encontradas. Como por exemplo, quantos objetos sem buracos foram econtrados. Dessa forma, retorna um inteiro que representa isso." ##
    cont = 0
    for i in range(self.altura):
      for j in range(self.largura):
        if matriz[i][j] == 1:
          cont += 1
  
    return cont

  
  def identificar_elementos(self):
    ## Algoritmo principal. Nele conseguimos identificar a quantidade dos objetos numa imagem. Para isso, utiliza funcoes auxiliares, "hit_or_miss e "verifica_ocorrencias". Assim, a partir dos elementos estruturantes definidos anteriormente conseguimos calcular e retornar uma tupla contendo o numero de objetos sem buracos e com buracos, respectivamente.
    elem_sem_buracos = self.hit_or_miss(self.elem_estr_sem_buraco, self.dim_elem_estr, self.borda_sem_buraco, self.dim_borda)
    elem_com_buracos = self.hit_or_miss(self.elem_estr_com_buraco, self.dim_elem_estr, self.borda_com_buraco, self.dim_borda)

    quant_sem_buracos = self.verifica_ocorrencias(elem_sem_buracos)
    quant_com_buracos = self.verifica_ocorrencias(elem_com_buracos)

    return (quant_sem_buracos,quant_com_buracos)



def main():
  if sys.argv[1] == "--help" or sys.argv[1] == "-h":
    print("""
    Conta Objetos
    Identifica a quantidade de Objetos, com e sem buracos, na Imagem desejada.
    Uso: python3 conta_objetos.py <PATH da Imagem>
    """)
    exit()
  else:
    ## Algumas atribuicoes e teste do Algoritmo ##
    PI = ProcessarImagem(sys.argv[1])
    PI.ler_imagem()
    PI.imagem_matriz()
    
    PI.elem_estr_sem_buraco = [
    [1,1,1],
    [1,1,1],
    [1,1,1]
    ]

    PI.borda_sem_buraco = [
      [1,1,1,1,1],
      [1,0,0,0,1],
      [1,0,0,0,1],
      [1,0,0,0,1],
      [1,1,1,1,1]
    ]
    
    PI.elem_estr_com_buraco = [
      [1,1,1],
      [1,0,1],
      [1,1,1]
    ]

    PI.borda_com_buraco = [
      [1,1,1,1,1],
      [1,0,0,0,1],
      [1,0,1,0,1],
      [1,0,0,0,1],
      [1,1,1,1,1]
    ]

    PI.dim_elem_estr = 3
    PI.dim_borda = 5
    
    print("Matriz da Imagem desejada:")
    print("Altura:", PI.altura)
    print("Largura:", PI.largura)
    PI.print_matriz(PI.matriz)

    resultado = PI.identificar_elementos()

    print("Quantidade de Objetos sem Buracos:", resultado[0])
    print("Quantidade de Objetos com Buracos:", resultado[1])


if __name__ == "__main__":
  main()