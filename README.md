# 🎮 Tic Tac Toe – Python Kata

Este projeto é uma implementação simples e totalmente funcional do clássico **Jogo da Velha (Tic Tac Toe)** em Python, com testes automatizados usando `pytest`.

---

## 📋 Regras do Jogo

- O jogo tem **duas jogadoras**, representadas por `"X"` e `"O"`.
- A grade do jogo é **3x3**, totalizando **nove campos**.
- Os jogadores **se revezam** ocupando os campos.
- Um jogador **não pode jogar em um campo já ocupado**.
- O jogo termina quando:
  - Todos os campos de **uma linha** forem ocupados por um jogador.
  - Todos os campos de **uma coluna** forem ocupados por um jogador.
  - Todos os campos de **uma diagonal** forem ocupados por um jogador.
  - **Todos os campos forem preenchidos** (empate / velha).

---

✅ Testes Automatizados
Os testes cobrem todas as regras do jogo. Aqui estão os principais testes implementados:

Teste	O que verifica
test_player_x_wins_row	Vitória de X ao preencher uma linha
test_player_o_wins_column	Vitória de O ao preencher uma coluna
test_player_wins_diagonal	Vitória por uma diagonal
test_draw	Empate com todos os campos ocupados
test_switch_turns	Alternância correta entre jogadores
test_block_double_play	Impede jogar duas vezes no mesmo campo
test_game_over_blocks_play	Impede jogadas após o fim do jogo
