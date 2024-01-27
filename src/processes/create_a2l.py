from src.common.a2ltools import read_a2l_static_values, read_a2l_variables
from src.common.ghidra import Ghidra
from src.common.hex_address import HexAddress
from src.common.json import read_json_file


class CreateA2L():

    def run(self, source_a2l, addressmap, target_a2l):
        static_values = read_a2l_static_values(source_a2l)
        dynamic_values = read_a2l_variables(source_a2l)
        allvalues = {**static_values, **dynamic_values}
        # Read A2L:
        with open(source_a2l, 'r', encoding='latin-1') as a2l_r:
            a2l_text = a2l_r.read()
            # Insert values:
        addressmap = read_json_file(addressmap)
        for name, newAddress in addressmap.items():
            oldAddress = HexAddress(allvalues[name]["addr"]).to_str()
            newAddress = HexAddress(newAddress).to_str()
            print(f"Replacing {name} : {oldAddress} -> {newAddress}")
            a2l_text.replace(oldAddress, newAddress)

        # Write A2l:
        with open(target_a2l, 'w', encoding='latin-1') as a2l_w:
            a2l_w.write(a2l_text)
