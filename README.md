# 🪨📄✂️ Jokenpô em Python (Pedra, Papel e Tesoura)

Um simples e divertido jogo de **Jokenpô (Pedra, Papel e Tesoura)** feito em Python, rodando no terminal.  
O jogador escolhe uma das três opções, o computador escolhe outra aleatoriamente, e o programa determina o vencedor.  
Inclui **animação (JO–KEN–PO)**, **validação de entrada**, **repetição opcional** e uma interface de texto organizada.

---

## ✨ Funcionalidades

- 🎮 Jogo interativo no terminal  
- 🖥️ Escolha aleatória do computador  
- ❗ Validação completa para entradas inválidas  
- 🔁 Possibilidade de jogar várias rodadas  
- 🎉 Indicadores claros de vitória, derrota ou empate  
- ⏳ Pequena animação para simular o “JO-KEN-PÔ”  
- 🧼 Código limpo, indentado e organizado  

---

## 🧠 Lógica do Programa

- Um loop `while True` controla o jogo principal  
- O jogador escolhe entre **0 (Pedra), 1 (Papel), 2 (Tesoura)**  
- O computador escolhe um valor aleatório com `randint`  
- A comparação das jogadas determina quem vence  
- Após cada rodada, o usuário decide se continua ou encerra  
- Entradas inválidas não quebram o programa (tratamento adequado)

---

## ▶️ Como Executar

Certifique-se de ter o Python instalado (versão 3 ou superior).

No terminal:

```bash
python jokenpo.py
```

---

## 📂 Estrutura Recomendada do Arquivo

```
📦 jokenpo-python
 └── jokenpo.py
 └── README.md
```

---

## 🧩 Tecnologias Utilizadas

- **Python 3**
- `random` → para gerar a jogada do computador  
- `time.sleep()` → para animação do "JO-KEN-PÔ"

---

## 📸 Exemplo de Uso

```
------------------------------
         JO-KEN-PÔ
------------------------------
> Escolha:
-------------------
 [0] Pedra
 [1] Papel
 [2] Tesoura
-------------------
> Sua escolha: 1
JO
KEN
PO!!!
------------------------------
Computador jogou: Pedra
Você jogou: Papel
------------------------------
🎉 PARABÉNS, VOCÊ VENCEU!!! 🎉
------------------------------
> Deseja continuar? [S/N]:
```

---

## 📌 Observações

- Projeto ideal para quem está começando em Python  
- Ótimo exercício para treinar condicionais, loops e listas  
- Excelente para portfolio no GitHub  

---

## 📜 Licença

Este projeto é de uso livre para estudo e portfólio.


