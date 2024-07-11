Este é o meu primeiro projeto usando a biblioteca Pygame. Trata-se de uma implementação simples do clássico jogo da cobrinha, onde o objetivo é coletar maçãs e aumentar o comprimento da cobra enquanto evita colisões com seu próprio corpo.

VISÃO GERAL
O jogo consiste em uma cobra que se move em uma tela e deve coletar maçãs para aumentar seu comprimento. A pontuação aumenta com cada maçã coletada. Se a cobra colidir com seu próprio corpo, o jogo termina e oferece a opção de reiniciar.

FUNCIONALIDADES
Música de Fundo: Toca uma música de fundo contínua enquanto o jogo está em execução.
Efeitos Sonoros: Um som é reproduzido quando a cobra coleta uma maçã.
Movimento da Cobra: A cobra se move com as teclas W, A, S, D.
Colisão com Maçã: A cobra cresce e a pontuação aumenta ao colidir com a maçã.
Reinício do Jogo: Após a colisão com o próprio corpo, o jogo exibe uma mensagem de "GAME OVER" e oferece a opção de reiniciar pressionando a tecla R.

RRQUISITOS
Python 3: Certifique-se de ter o Python 3 instalado em seu sistema.
Pygame: Instale a biblioteca Pygame com o comando pip install pygame.
Arquivos de Áudio: O jogo utiliza arquivos de áudio que devem estar no mesmo diretório do script:
03. Underwater Theme.mp3 (Música de fundo) LINK: https://downloads.khinsider.com/game-soundtracks/album/super-mario-bros.-1-3-anthology
smb_1-up.wav (Efeito sonoro de coleta de maçã) LINK: https://themushroomkingdom.net/media/smw/wav

INSTRUÇÕES
Clone ou faça o download do repositório:
git clone <URL_DO_REPOSITORIO>

Instale as dependências:
pip install pygame

Coloque os arquivos de áudio no mesmo diretório do script.
Execute o script:
python nome_do_arquivo.py


CONTROLES
W: Mover para cima
A: Mover para a esquerda
S: Mover para baixo
D: Mover para a direita
R: Reiniciar o jogo (após o "GAME OVER")

CÓDIGO
O código principal do jogo está implementado em Python usando a biblioteca Pygame. O jogo possui as seguintes partes principais:

Inicialização: Configura a tela, a música de fundo e os efeitos sonoros.
Loop Principal: Atualiza o estado do jogo, processa eventos, atualiza a posição da cobra e verifica colisões.
Funções Auxiliares:
aumenta_cobra(): Desenha a cobra na tela.
reiniciar(): Reseta o jogo quando o jogador decide reiniciar.
Exemplo:
Quando a cobra colide com a maçã, a pontuação aumenta e a cobra cresce. Se a cobra colidir com seu próprio corpo, o jogo exibe uma tela de "GAME OVER" e permite ao jogador reiniciar.

CONTRIBUIÇÕES
Sinta-se à vontade para contribuir com melhorias ou correções para este projeto!
