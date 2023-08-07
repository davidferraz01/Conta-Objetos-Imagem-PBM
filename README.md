# Conta Objetos Imagem PBM

Este é um algoritmo desenvolvido em Python para contar objetos em uma imagem binária. Ele identifica a quantidade de objetos com e sem buracos na imagem desejada, lembrando que para fins de simplificação serão considerados como obejtos apenas figuras geométricas quadradras com ou sem "buraco", como pode ser visto nas imagens anexadas a esse repositório. O algoritmo utiliza o processo conhecido como "Hit or Miss", que detecta um determinado formato ou padrão na matriz usando o algoritmo de erosão e um par de elementos estruturantes disjuntos. Esse código fonte foi desenvolvido como parte do estudo realizado na disciplina de Processamento de Imagens.

## Requisitos

Certifique-se de ter o Python 3 instalado em seu sistema.

## Instruções de execução

Para obter instruções sobre a utilização do algoritmo, execute-o com o parâmetro "--help" ou "-h", como mostrado abaixo:

```
python3 conta_objetos.py --help
```

ou

```
python3 conta_objetos.py -h
```

Esse comando irá exibir a seguinte informação no console:

```
Conta Objetos
Identifica a quantidade de Objetos, com e sem buracos, na Imagem desejada.
Uso: python3 conta_objetos.py <PATH da Imagem>
```

Assim, para executar o algoritmo com a imagem desejada, utilize o seguinte comando, substituindo `<PATH da Imagem>` pelo caminho para o arquivo de imagem binária no formato PBM:

```
python3 conta_objetos.py <PATH da Imagem>
```

O algoritmo irá processar a imagem e imprimir a matriz da imagem, juntamente com a quantidade de objetos sem buracos e com buracos encontrados na imagem. Certifique-se de ter definido corretamente os elementos estruturantes `elem_estr_sem_buraco` e `elem_estr_com_buraco`, bem como suas dimensões `dim_elem_estr`.

## Exemplo de utilização

Suponha que você tenha um arquivo de imagem chamado "imagem.pbm" no mesmo diretório do script "conta_objetos.py". Para contar os objetos nessa imagem, execute o seguinte comando:

```
python3 conta_objetos.py imagem.pbm
```

O algoritmo irá processar a imagem e exibir a matriz da imagem, seguida da quantidade de objetos sem buracos e com buracos encontrados.

**Observação 1:** Certifique-se de fornecer um arquivo de imagem válido no formato PBM para obter resultados precisos.

**Observação 2:** No repositório há imagens no formato "pbm" e "jpg" pois o Github não exibe fotos no formato "pbm". Portanto foram adicionados as fotos "jpg" para mostrar como as mesmas são vistas com o auxilio de um programa, como o "Gimp", que suporta o formato original "pbm".
