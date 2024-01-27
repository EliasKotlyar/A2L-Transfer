from ghidra.program.model.listing import CodeUnit
from ghidra.program.model.symbol import RefType
from ghidra.program.database import ProgramDB
from ghidra.program.flatapi import FlatProgramAPI

state = getState()  # Assume getState() returns the current program state
currentProgram = state.getCurrentProgram()

flat_api = FlatProgramAPI(currentProgram)


def getReferencesFrom(address):
    return flat_api.getReferencesFrom(address)


def find_data_references_from_address(source_address):
    source_addr = currentProgram.getAddressFactory().getAddress(source_address)

    referred_addresses = []

    references = getReferencesFrom(source_addr)

    for ref in references:

        ref_type = ref.getReferenceType()

        if ref_type.isData():
            to_addr = ref.getToAddress()

            referred_addresses.append(str(to_addr))

    return referred_addresses


import json

filename = "targetmap.json"
f = open(filename, "r")
content = f.read()
# print(content)
content = content.encode('utf-8')
contentJson = json.loads(content)
retArr = {}

for name, address in contentJson.iteritems():
    print(address)
    # Assign Vars:
    result = find_data_references_from_address(address)

    retArr[name] = result[0]

    # break
outputfile = "addressmap.json"
with open(outputfile, 'w') as f:
    # Write the content as JSON to the output file
    json.dump(retArr, f, indent=4)
print(retArr)
