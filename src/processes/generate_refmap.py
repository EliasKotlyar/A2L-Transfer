from src.common.ghidra import Ghidra


class GenerateRefMap():

    def run(self, file):
        ghidra = Ghidra()
        command = [
            '-process',
            file,
            '-noanalysis',
            '-postScript',
            'ExportRefMap.py',
        ]
        ghidra.run_ghidra_headless(command)
