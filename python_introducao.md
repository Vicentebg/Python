Python 
Titulo: Função print e variáveis

Funçoes que podem ser usadas com o print

sep:
Entrada: print("Brasil ganhou 5 titulos mundiais", sep=" ")
Saída: Brasil ganhou 5 titulos mundiais

Entrada:print("Brasil", "ganhou", 5, "titulos mundiais", sep="-")
Saída: Brasil-ganhou-5-titulos mundiais

Entrada:print("Brasil", "ganhou", 5, "titulos mundiais", sep="")
Saída: Brasilganhou5titulos mundiais

Ou seja o sep é um separador, se separarmos nossas strings com vírgula e adicionarmos algum parametro para o sep iremos ter a saída como os exemplos acima

end:
Entrada: print("Brasil ganhou 5 titulos mundiais", end="\n")
Saída: Brasil ganhou 5 titulos mundiais


Entrada: print("Brasil ganhou 5 titulos mundiais", end="")
Saída: Brasil ganhou 5 titulos mundiais>>>

Entrada: print("Brasil ganhou 5 titulos mundiais", end="END")
Saída: Brasil ganhou 5 titulos mundiaisEND>>>

Podemos observar que o end="\n" cria uma nova linha e quando passamos end="" o console já inicia na mesma linha. O que for definido no end acontecerá no final.

Variáveis:
Vamos definir uma variável como : pais = "Italia", podemos depois rodar o comando type(pais) para ver que tipo é essa váriavel, recebemos <class 'str'> que significa que a classe dela é uma String
Agora vamos definir outra variável como: quantidade = 4, iremos rodar agora type(quantidade) e iremos receber <class 'int'>
Agora realizaremos outro comando:
Entrada: print(pais, "ganhou", quantidade, "titulos mundiais")
Saída: Italia ganhou 4 titulos mundiais

Diferença entre break e continue:
A diferença é que o break, quando for executado, sai do bloco do laço abruptamente, enquanto continue apenas pula para próxima iteração.

![image](https://user-images.githubusercontent.com/19577547/223461887-a9ebddce-20c5-4e08-ad57-56816994267e.png)
