import os
import shutil
import subprocess

from src.common.ghidra import Ghidra
from src.common.paths import Paths


class GenerateBinDiff():
    def removeExtension(self, filename):
        base, extension = os.path.splitext(filename)
        return filename[:-1 * len(extension)]

    def run(self, bin_export_1, bin_export_2, bin_diff_db):
        path = Paths()
        analyze_headless_script = os.path.join(path.GHIDRA_PATH, 'analyzeHeadless.bat')
        ghidra_command = [
            "Bindiff",
            "--primary",
            bin_export_1,
            "--secondary",
            bin_export_2,
            "--output_dir",
            path.PROJECT_PATH
        ]
        ghidra_command = ghidra_command
        try:
            import ctypes
            ctypes.windll.kernel32.SetConsoleOutputCP(65001)
        except Exception as e:
            print(f"Failed to set console encoding: {e}")
        process = subprocess.run(ghidra_command, shell=True)

        ret_file = self.removeExtension(bin_export_1) + "_vs_" + self.removeExtension(bin_export_2) + ".BinDiff"
        ret_file = os.path.join(path.PROJECT_PATH, ret_file)
        if not os.path.exists(ret_file):
            raise FileNotFoundError(f"The file '{ret_file}' does not exist.")
        shutil.move(ret_file, bin_diff_db)
