import os


class Paths:
    def __init__(self):
        common_dir = os.path.dirname(os.path.abspath(__file__))
        self.ROOT_DIR = os.path.abspath(os.path.join(common_dir, "../../"))
        self.GHIDRA_PATH = r'C:\Users\Elias\Desktop\med9-new\ghidra_10.3.2_PUBLIC'
        self.PROJECT_PATH = os.path.join(self.ROOT_DIR, "work")
        self.SCRIPT_FOLDER = os.path.join(self.ROOT_DIR, "ghidra-scripts")
