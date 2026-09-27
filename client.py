import sys, Ice
import Demo

communicator = Ice.initialize(sys.argv)

# Endereco do servidor: primeiro argumento da linha de comando (padrao: localhost)
host = sys.argv[1] if len(sys.argv) > 1 else "localhost"

base = communicator.stringToProxy(f"SimplePrinter:tcp -h {host} -p 5678")
printer = Demo.PrinterPrx.checkedCast(base)
if not printer:
    raise RuntimeError("Invalid proxy")

print(printer.printString("Hello World!"))

# Chamadas aos metodos novos (ASR 06)
print("toUpperCase:  ", printer.toUpperCase("Hello World!"))
print("reverseString:", printer.reverseString("Hello World!"))
print("countWords:   ", printer.countWords("sistemas distribuidos com ice"))
print("add:          ", printer.add(20, 22))
print("divide:       ", printer.divide(10, 4))
try:
    printer.divide(1, 0)
except Demo.DivisionByZero as e:
    print("divide(1, 0): excecao remota DivisionByZero:", e.reason)

communicator.destroy()
