import sys, Ice
import Demo

communicator = Ice.initialize(sys.argv)

# Endereco do servidor: primeiro argumento da linha de comando (padrao: localhost)
host = sys.argv[1] if len(sys.argv) > 1 else "localhost"

base1 = communicator.stringToProxy(f"SimplePrinter1:tcp -h {host} -p 5678")
base2 = communicator.stringToProxy(f"SimplePrinter2:tcp -h {host} -p 5678")
printer1 = Demo.PrinterPrx.checkedCast(base1)
printer2 = Demo.PrinterPrx.checkedCast(base2)
if (not printer1) or (not printer2):
    raise RuntimeError("Invalid proxy")

rep = printer1.printString("Hello World from printer1!")
print(rep)
rep = printer2.printString("Hello World from printer2!")
print(rep)

# Chamadas aos metodos novos (ASR 06), uma em cada objeto remoto
print("printer1.toUpperCase:  ", printer1.toUpperCase("Hello World from printer1!"))
print("printer2.reverseString:", printer2.reverseString("Hello World from printer2!"))
print("printer1.countWords:   ", printer1.countWords("sistemas distribuidos com ice"))
print("printer2.add:          ", printer2.add(20, 22))
print("printer1.divide:       ", printer1.divide(10, 4))
try:
    printer2.divide(1, 0)
except Demo.DivisionByZero as e:
    print("printer2.divide(1, 0): excecao remota DivisionByZero:", e.reason)

communicator.destroy()
