# PUC - power user curve
Problema proposto para avaliacao de conhecimento.
O Empresa quer entender, de sua base de usuários “premium” (pagantes), qual é o seu
comportamento de uso ao longo do mês: quantos usuários (%) utilizam o app 1 vez ao mês, 2
vezes ao mês, ... até 30 (ou 31, ou 28) dias ao mês. Trata-se da chamada “power user
curve”, um indicador utilizado por várias empresas para entender o engajamento de seus
usuários/clientes.
Os eventos de utilização do app Empresa estão mapeados e queremos ter a “power user curve”
dos nossos usuários. Para fins deste desafio, foi gerada uma fonte de dados.
Esse arquivo JSON contém a lista de usuários do app , contendo o ID e uma lista que
representa o histórico de utilização do app (activities).
A lista (activities) contém 365 registros, que representa os dias do ano (primeiro item 01/01,
último item 31/12). Cada item da lista pode ter o valor “1” ou “0” (1: o usuário utilizou o app; 0: o
usuário não utilizou o app).


## Como Usar?

1. Clone o repositório.
2. Crie um virtualenv com Python 3.5.
3. Ative o virtualenv.
4. Instale as dependências.
6. Execute
   ```console
    python main.py {parametro}
   ```
    Onde se parametro for 0 vai gerar um relatorio da base tratada em arquivo xlsx na raiz do instalacao
    Para gerar o grafico devera passar os meses desejados (numeros inteiros de 1 a 12) separados por um espaco.
    Exemplo: gerar grafico de Maio, junho e julho
   ```console
        python main.py 5 6 7
   ```   
```console
git clone git@github.com:rgrlinux/puc.git puc
cd puc
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python main.py 
```