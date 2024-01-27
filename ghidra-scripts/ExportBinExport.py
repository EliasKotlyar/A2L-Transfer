#@author Elias Kotlyar
#@category Tuning
#@keybinding
#@menupath
#@toolbar


from com.google.security.binexport import BinExportExporter
from java.io import File

name = currentProgram.getName()
fullpath = name + ".BinExport"
from ghidra.app.util.exporter import BinaryExporter

bexp = BinExportExporter()
memory = currentProgram.getMemory()
monitor = getMonitor()
domainObj = currentProgram
f = File(fullpath)
bexp.export(f, domainObj, memory, monitor)
