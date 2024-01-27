from src.common.ghidra import Ghidra


class GenerateGhidaProject():

    def run(self, file):
        ghidra = Ghidra()
        command = [
            '-import',
            file,
            '-processor',
            'PowerPC:BE:32:MED9',
            '-overwrite',
            '-preScript',
            'med91-install.py',
            '-postScript',
            'DefineUndefinedFunctions.py',
            '-postScript',
            'ExportBinExport.py',
        ]
        ghidra.run_ghidra_headless(command)
