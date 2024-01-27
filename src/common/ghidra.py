import os
import subprocess

from src.common.paths import Paths


class Ghidra:

    def run_ghidra_headless(self, command: []):
        path = Paths()
        analyze_headless_script = os.path.join(path.GHIDRA_PATH, 'support', 'analyzeHeadless.bat')
        ghidra_command = [
            analyze_headless_script,
            path.PROJECT_PATH,
            'A2L Transfer',
            '-scriptPath',
            path.SCRIPT_FOLDER,
        ]
        ghidra_command = ghidra_command + command
        try:
            import ctypes
            ctypes.windll.kernel32.SetConsoleOutputCP(65001)
        except Exception as e:
            print(f"Failed to set console encoding: {e}")

        process = subprocess.run(ghidra_command, shell=True)
