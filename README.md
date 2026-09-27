Antes de executar, instale o middleware e as ferramentas associadas (nas duas máquinas):


## No Amazon Linux
```
sudo dnf install https://download.zeroc.com/ice/3.7/amzn2023/ice-repo-3.7.amzn2023.noarch.rpm
```

```
sudo dnf install python3-ice ice-compilers
```

## No Ubuntu
```
wget "https://download.zeroc.com/ice/3.8/ubuntu26.04/ice-repo-3.8_1.0.0_all.deb" -O ice-repo.deb
sudo dpkg -i ice-repo.deb
rm ice-repo.deb
sudo apt-get update
```
```
sudo apt-get install python3-zeroc-ice
```
```
sudo apt-get install zeroc-ice-compilers
```

## No Windows / macOS (pip)
```
pip install zeroc-ice
```

Observação: o código original deste repositório é exatamente o do Exemplo 3.21
do livro de Maarten van Steen (*Distributed Systems*). Os métodos novos
descritos abaixo foram acrescentados a ele.

---

# ASR 06 – Novos métodos no objeto remoto

Foram acrescentados **5 métodos novos** à interface `Printer` (em `Printer.ice`),
implementados nos servidores (`server.py`, `server2.py`) e chamados pelos
clientes (`client.py`, `client2.py`):

| Método | O que faz | Exemplo |
|---|---|---|
| `string toUpperCase(string s)` | converte o texto para maiúsculas | `"Hello"` → `"HELLO"` |
| `string reverseString(string s)` | inverte o texto | `"Hello"` → `"olleH"` |
| `int countWords(string s)` | conta as palavras do texto | `"a b c"` → `3` |
| `int add(int a, int b)` | soma dois inteiros | `add(20, 22)` → `42` |
| `double divide(double a, double b) throws DivisionByZero` | divide; lança a **exceção remota** `DivisionByZero` se `b == 0` | `divide(10, 4)` → `2.5` |

A exceção `DivisionByZero` também foi declarada no Slice: ela é lançada no
servidor e capturada no cliente como uma exceção Python comum
(`except Demo.DivisionByZero`).

## Gerar o código Python a partir do Slice

A pasta `Demo/` foi gerada com o **Ice 3.8**. Sempre que `Printer.ice` for
alterado (ou se você usar outra versão do Ice), gere de novo:

```
slice2py Printer.ice
```

## Executar

Servidor (em uma máquina/terminal):
```
python3 server.py        # um objeto:  SimplePrinter
python3 server2.py       # dois objetos: SimplePrinter1 e SimplePrinter2
```

Cliente (em outra máquina/terminal), passando o IP do servidor
(padrão: `localhost`). Lembre de liberar a porta **5678** no firewall /
security group:
```
python3 client.py  <IP_DO_SERVIDOR>
python3 client2.py <IP_DO_SERVIDOR>
```

Saída do `client.py`:
```
Hello World!*
toUpperCase:   HELLO WORLD!
reverseString: !dlroW olleH
countWords:    4
add:           42
divide:        2.5
divide(1, 0): excecao remota DivisionByZero: divisao por zero
```

Saída do servidor (`server.py`):
```
Hello World!
toUpperCase: Hello World!
reverseString: Hello World!
countWords: sistemas distribuidos com ice
add: 20 22
divide: 10.0 4.0
divide: 1.0 0.0
```
