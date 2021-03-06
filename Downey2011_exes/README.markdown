Exercício Aula 08/01/2015
Cristiano Gurgel de Castro <crisgc1@gmail.com>

# Primeiro exercício

Descrição
: Implemente todas essas medidas de dispersão em python e compare com
os resultados e compare com os métodos implementados em www.thinkstats.
com/thinkstats.py 

Resultado
: Foi implementado no script: stats.py

# Exercícios do Livro ThinkStats Cap 1

## Exercício 1.1

O estudo logitudinal acompanha os mesmos indivíduos durante um período de tempo
enquanto que no "cross section study" indivíduos com características semelhantes
mas não os mesmos são analisados

## Exercício 1.2

Apenas uma sequência de passos a ser seguida: os arquivos de dados foram
baixados e também o script pyhton que os interpreta

- Arquivos:
    - survey.py

## Exercício 1.3

Há uma pequena diferença de aproximadamente 13h entre os tempos de gravidez

- Arquivos
    - first.py

# Exercícios do livro ThinkStats Cap 2

## Exercício 2.1

- Arquivos
    - exe\_02-01.py

## Exercício 2.2

O desvio padrão para os primeiros bebês é maior que para o restante dos nascidos
e a diferenã dos DPs é maior que a das médias. Nos casos de nascimento atrasado
para os primeiros bebês, o atraso será provalvelmente bem maior que para o caso
do restante dos bebês. Portanto a percepção de que os primeiros bebês atrasam
mais é ratificada pelos dados.

- Arquivos
    - exe\_02-02.py

## Exercício 2.3

- Arquivos
    - Mode.py

## Exercício 2.4

- Arquivos
    - RemainingLifetime.py

## Exercício 2.5

- Arquivos
    - MeanPmf.py

## Exercício 2.6

- Arquivo
    - risk.py

## Exercício 2.7

- Arquivo
    - conditional.py

## Exercício 2.8

Para apresentar uma matéria no jornal poderia-se fazer uma comparação dos dos
riscos relativos tal qual no exercício 2.6. Mostrando que o risco de um primeiro
bebê nascer atrasado é 65% maior do que o comparado aos outros.

Para acalmar um paciente, poderia-se falar que a diferença em média é de apenas
13h de atraso para os primeiros bebês

Os primeiros bebês nascem mais tarde, mas pouco (apenas 13h a mais de espera).
No entanto, no caso de atraso, geralmente os primeiros bebês atrasam em mais
tempo do que os outros, o que pode levar a percepção de que os primeiros bebês
nascem mais tarde.

# ThinkStats Cap6 Exercícios

## Exercício 6.1

Implementado no arquivo skewness.py. A função Skewness calcula o resultado da
assimetria como aproximadamente -2.9. O que está de acordo com o exibido no
histograma, já que a curva se estende mais "à esquerda" da média. A moda da
curva são 39 semanas

# ThinkStats Cap 7 Exercícios

## Exercício 7.5

Tem-se duas amostras de sangue na cena do crime

AB
: cuja probabilidade na população é 1%

O
: cuja probabilidade na população é 60 %

Logo, analisa-se duas probabilidades

- A probabilidade da evidência dado que o sangue é mesmo do suspeito (P(E|H))
- A probabilidade da evidência dado que o sangue não é do suspeito (P(E|H0))

- P(E|H) = P(sangue é AB), já sabe-se que o sangue do suspeito é O
- P(E|H0) = 2 P(sangue é AB) P(sangue é O), observa-se que é um caso de
  distribuição binomial

Logo a razão entre as probabilidades é P(E|H)/P(E|H0) = 1 / (2P(sangue é O)) = 1
/ 1.2 = 0.833. Logo, ao contrário do que podería-se supor, isso fornece
evidência de que não é o sangue do suspeito na cena do crime


