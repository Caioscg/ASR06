import sys, Ice
import Demo

class PrinterI(Demo.Printer):
    def __init__(self, t):
        self.t = t

    def printString(self, s, current=None):
        print(self.t, s)
        return s + "*"

    # Metodos novos (ASR 06)
    def toUpperCase(self, s, current=None):
        print(self.t, "toUpperCase:", s)
        return s.upper()

    def reverseString(self, s, current=None):
        print(self.t, "reverseString:", s)
        return s[::-1]

    def countWords(self, s, current=None):
        print(self.t, "countWords:", s)
        return len(s.split())

    def add(self, a, b, current=None):
        print(self.t, "add:", a, b)
        return a + b

    def divide(self, a, b, current=None):
        print(self.t, "divide:", a, b)
        if b == 0:
            raise Demo.DivisionByZero("divisao por zero")
        return a / b

communicator = Ice.initialize(sys.argv)

adapter = communicator.createObjectAdapterWithEndpoints("SimpleAdapter", "default -p 5678")
object1 = PrinterI("Object1 says:")
object2 = PrinterI("Object2 says:")
adapter.add(object1, Ice.Identity("SimplePrinter1"))
adapter.add(object2, Ice.Identity("SimplePrinter2"))
adapter.activate()

communicator.waitForShutdown()
