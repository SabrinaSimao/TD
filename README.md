#Projeto final de Design de Software - Tower Defense
Alexandre Young (Yiaaann), Sabrina Simão (SabrinaSimao), Paulo Tozzo (Formulos) e Lucas Chen (chends888)

###Visão Geral:

  Um jogo estilo Tower Defense, onde se protege uma sessão geral da tela de uma invasão de inimigos por meio da construção de estruturas (Towers) limitadas por um recurso limitado

###Estrutura:

  O jogo é apresentado como um mapa particionado em tiles, cada tile pode conter um monstro ou torre.

  O objetivo principal é proteger o Castelo central da invasão de monstros, o Castelo tem uma vida fixa, sendo que o jogador perde o jogo quando a vida do castelo chega a zero

  Cada monstro percorre o mapa a caminho do castelo, procurando invadí-lo, causando dano ao mesmo. Eles tem uma vida fixa e levam dano quando atacados pelas Torres. Monstros causam dano ao castelo quando atingem ele, sendo o dano dependende do tipo específico do monstro atacante

  Torres são criados pelo jogador usando Ouro (recurso limitado) em tiles específicas do mapa, elas tem a função de atacar os monstros dentro de seu alcance para proteger o Castelo central

  O Ouro necessário para construir as torres é obtido por monstro derrotado, com cada espécie de monstro fornecendo uma quantidade diferente de ouro.

###Fluxo de Jogo

  O jogador, vendo o mapa, controla seus recursos disponíveis para eficientemente posicionar torres e proteger seu Castelo. Tentando sobreviver pelo maior tempo possível

  O input do jogo é feito por meio do mouse, clicando nas casas que se deseja construir a Torre, apenas casas vazias podem ser usadas para posicionar torres

  A geração dos monstros é separada em "Waves" que podem ser geradas proceduralmente ou seguindo uma lista fixa, entre cada Wave o jogador tem um tempo de descanso para posicionar as Torres que deseja

  Quando a vida do Castelo chega a zero o jogador perde o jogo

###Como Jogar

 A interface de usuário é separada no mapa central e em um menu lateral, com o menu lateral é possível selecionar as torres a serem construídas, clicar no mapa com uma torre selecionada vai poscionar uma torre na casa, assumindo que você tenha o gold necessário para construí-la
