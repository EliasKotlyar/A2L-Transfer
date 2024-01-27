from src.processes.convert_a2l_to_json import ConvertA2lToJson
from src.processes.create_a2l import CreateA2L
from src.processes.generate_address_map import GenerateAddressMap
from src.processes.generate_bin_diff import GenerateBinDiff
from src.processes.generate_ghidra_project import GenerateGhidaProject
from src.processes.generate_refmap import GenerateRefMap
from src.processes.generate_targetmap import GenerateTargetMap

generateGhidraProject = GenerateGhidaProject()
# Generate Ghida Project for
bin_a = "1K0907115S_0020.bin"
bin_b = "1Q0907115F_0020.bin"
a2l_a = "1K0907115S_0020.a2l"
a2l_b = "1Q0907115F_0020.a2l"
# Step 1
# generateGhidraProject.run(bin_a)
# Step 2
# generateGhidraProject.run(bin_b)
# Step 3:
a2l_json = "a2l.json"
# converter = ConvertA2lToJson()
# converter.run(a2l_a,a2l_json)
# Step 4:
refmap = "refmap.json"
# generateRefMap = GenerateRefMap()
# generateRefMap.run(bin_a)

# Step 5:
bin_diff_db = "bindiff.sqlite"
# bindiff = GenerateBinDiff()
# bindiff.run(bin_a + ".BinExport", bin_b + ".BinExport", bin_diff_db)

# Step 6:
targetmap = "targetmap.json"
# generator = GenerateTargetMap()
# generator.process(refmap, bin_diff_db, targetmap)

# Step 7:
addressmap = "addressmap.json"
# addressmap = GenerateAddressMap()
# addressmap.run(bin_b)

# Step 8:
#a2l_creator = CreateA2L()
#a2l_creator.run(a2l_a, addressmap, a2l_b)
