# Sistema de Controle de Estacionamento

**Disciplina:** Paradigmas de Programação  
**Professor:** Rodrigo Medeiros Costa  
**Instituição:** Universidade da Amazônia (UNAMA) — Curso de Ciência da Computação  
**Linguagem utilizada:** Python 3  

---

## 👥 Integrantes
- Paulo Eduardo Miranda Mendes - 04159820

---

## 📋 1. Descrição do Problema
O projeto consiste no desenvolvimento de um **Sistema de Controle de Estacionamento** automatizado via terminal. O programa tem como objetivo gerenciar a ocupação de 10 vagas, controlando o fluxo operacional de veículos de forma eficiente e transparente.

- **Entradas:** Matrícula (placa) e modelo do veículo, além dos comandos de navegação do menu e horários gerados automaticamente pelo sistema.
- **Regras de Negócio:**
  - O estacionamento possui capacidade fixa de 10 vagas.
  - O sistema impede o registo de veículos com matrículas duplicadas que já estejam dentro do estacionamento.
  - A cobrança de permanência segue a regra: taxa fixa de R$ 5,00 para a primeira hora, acrescida de R$ 2,00 por cada hora adicional (ou fração), calculada de forma automatizada com base no tempo decorrido.
- **Resultados Esperados:** Recibos detalhados de saída com o valor devido, relatórios atualizados do estado das vagas (livres ou ocupadas), consulta específica de veículos e faturamento total acumulado do dia.

---

## 💻 2. Implementação e o Paradigma Imperativo
A solução foi implementada inteiramente em **Python**, estruturando-se em módulos independentes (`estado.py`, `movimentacoes.py`, `calcular_valor.py`, `listar_vagas.py`, `exibir_faturamento.py`, `consultar_veiculo.py`, `menu.py` e `main.py`). O código evidencia os pilares fundamentais do **paradigma imperativo**:

1. **Sequência de Instruções:** O fluxo do programa executa ordens estritamente sequenciais dentro de cada procedimento e função (ex: ler entrada, calcular o tempo, atualizar o estado e exibir o recibo).
2. **Alteração de Estado (Variáveis e Atribuições):** O estado dos dados globais é armazenado e modificado explicitamente no arquivo `estado.py` através de atribuições diretas nas estruturas de dados (dicionários), alterando o status das vagas de `None` para os dados do veículo e atualizando o acumulador `faturamento_total`.
3. **Estruturas de Decisão (`if / elif / else`):** Utilizadas intensivamente para validar a lotação do estacionamento, checar duplicidade de placas, verificar se um veículo existe antes da saída e determinar as faixas de cálculo de preço.
4. **Estruturas de Repetição (`while` e `for`):** O menu principal roda em um ciclo contínuo `while` até que o utilizador decida sair. Os laços `for` percorrem iterativamente o dicionário de vagas para buscar espaços livres ou localizar veículos específicos.
5. **Procedimentos e Funções:** Modularização rigorosa das responsabilidades do sistema em funções isoladas, garantindo legibilidade, coesão e facilidade de manutenção.

---

## 🧠 3. Reflexão sobre o Desenvolvimento
- **Principais Decisões:** Optou-se por separar a aplicação em múltiplos ficheiros (modularização avançada) em vez de um único script monolítico para demonstrar organização profissional de código e limpeza arquitetural. O uso do módulo nativo `datetime` e `math` facilitou a precisão na gestão temporal e no arredondamento das horas cobradas.
- **Dificuldades Encontradas:** Garantir a sincronização correta do estado global entre ficheiros diferentes em Python exigiu o encapsulamento dos dados por meio de funções de acesso centralizadas, evitando dessincronizações de escopo.
- **Possíveis Melhorias Futuras:** Implementar a persistência de dados utilizando ficheiros (como JSON ou CSV) ou uma base de dados leve (SQLite), permitindo que os registos não sejam perdidos ao encerrar a aplicação.

---

## 🚀 4. Instruções de Execução
Para executar o sistema na sua máquina, siga os passos abaixo:

1. Certifique-se de ter o **Python 3.x** instalado no seu computador.
2. Clone este repositório ou descarregue todos os ficheiros do projeto para uma mesma pasta:
   ```bash
   git clone [https://github.com/emendes19/Sistema-de-Estacionamento.git](https://github.com/emendes19/Sistema-de-Estacionamento.git)
   cd Sistema-de-Estacionamento

---

   ## 🎥 5. Vídeo de Demonstração
O vídeo demonstrando a aplicação em funcionamento está disponível no próprio repositório:

👉 **[Clique aqui para assistir ao vídeo de demonstração](./Paradigmas%20de%20programação.mp4)**