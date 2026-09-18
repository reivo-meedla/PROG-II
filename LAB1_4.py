from abc import ABC, abstractmethod


class Printer(ABC):
    @abstractmethod
    def print(self, document):
        pass


class Scanner(ABC):
    @abstractmethod
    def scan(self, document):
        pass


class MyPrinter(Printer):
    def print(self, document):
        print(f"Printing: {document}")


class Photocopier(Printer, Scanner):
    def print(self, document):
        print(f"Photocopier printing: {document}")

    def scan(self, document):
        print(f"Photocopier scanning: {document}")


class MultiFunctionMachine(Printer, Scanner):
    def __init__(self, printer: Printer, scanner: Scanner):
        self.printer = printer
        self.scanner = scanner

    def print(self, document):
        self.printer.print(document)

    def scan(self, document):
        self.scanner.scan(document)


if __name__ == "__main__":
    printer = MyPrinter()
    photocopier = Photocopier()

    printer.print("Hello from printer")

    photocopier.print("Copy this document")
    photocopier.scan("Scanned document")

    mfm = MultiFunctionMachine(printer, photocopier)
    mfm.print("Delegated print")
    mfm.scan("Delegated scan")