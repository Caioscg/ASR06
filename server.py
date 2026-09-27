import sys, Ice
import Demo

class PrinterI(Demo.Printer):
    def printString(self, s, current=None):
        print(s)
        return s + "*"

    # Metodos novos (ASR 06)
    def toUpperCase(self, s, current=None):
        print("toUpperCase:", s)
        return s.upper()

    def reverseString(self, s, current=None):
        print("reverseString:", s)
        return s[::-1]

    def countWords(self, s, current=None):
        print("countWords:", s)
        return len(s.split())

    def add(self, a, b, current=None):
        print("add:", a, b)
        return a + b

    def divide(self, a, b, current=None):
        print("divide:", a, b)
        if b == 0:
            raise Demo.DivisionByZero("divisao por zero")
        return a / b

communicator = Ice.initialize(sys.argv)

adapter = communicator.createObjectAdapterWithEndpoints("SimpleAdapter", "default -p 5678")
object = PrinterI()
adapter.add(object, Ice.Identity("SimplePrinter"))
adapter.activate()

communicator.waitForShutdown()
