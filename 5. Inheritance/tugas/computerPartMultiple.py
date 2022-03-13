# parent

class processor():
    def __init__(self, jenisProcessor) -> None:
        self.processor = jenisProcessor
    


class penyimpananSementara():
    def __init__(self, ram) -> None:
        self.ram = ram

class penyimpanan():
    def __init__(self, storage) -> None:
        self.storage = storage

class computerPart(processor, penyimpananSementara, penyimpanan):
    def __init__(self, jenisProcessor, ram, storage) -> None:
        processor.__init__(self, jenisProcessor)
        penyimpananSementara.__init__(self, ram)
        penyimpanan.__init__(self, storage)


myPc = computerPart('i5 8420U 2,4Ghz', 'DDR4 4GB','HDD Toshiba 1 TB')

print(f'Laptop dengan processor {myPc.processor}, dengan dilengkapi RAM {myPc.ram} serta penyimpanan {myPc.storage}')