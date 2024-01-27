from src.common.ghidra import Ghidra


class GenerateAddressMap():

    def run(self, file):
        ghidra = Ghidra()
        command = [
            '-process',
            file,
            '-noanalysis',
            '-postScript',
            'ExportAddressMap.py',
        ]
        ghidra.run_ghidra_headless(command)
