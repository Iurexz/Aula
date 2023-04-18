Algoritmo "semnome"

Var
n1,n2:inteiro
m1,m2,m3,m:real
n:caractere
rec:real
Inicio
escreval("Digite um número")
leia(n1)
escreval("Digite outro número")
leia(n2)
se (n1>n2) entao
escreval("O Valor ", n1," é maior que ",n2)
senao
escreval("O Valor ",n2," é maior que ",n1)
fimse

escreval(".................................")
escreval("Qual o seu nome?")
leia(n)
escreval("Qual foi a sua média na primeira unidade?")
leia(m1)
escreval("Qual foi a sua média na segunda unidade?")
leia(m2)
escreval("Qual foi a sua média na terceira unidade?")
leia(m3)
m <-(m1+m2+m3)/3
se (m>=7)entao
escreval(n," Foi Aprovado")
senao
se (m<=5)entao
escreval(n," Foi Reprovado")
senao
escreval(n," Foi para a recuperação!")
fimse
fimse



Fimalgoritmo