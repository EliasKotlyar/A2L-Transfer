import json
from src.common.hex_address import HexAddress


class Reference:
    def __init__(self, ref_type, addr):
        self.type = ref_type
        self.addr = HexAddress(addr)

    def __repr__(self):
        return f"Reference(type={self.type}, addr={self.addr})"


class A2LVariable:
    def __init__(self, name, addr, refs):
        self.name = name
        self.addr = HexAddress(addr)
        self.refs = refs

    def __repr__(self):
        return f"ParsedObject(name={self.name}, addr={self.addr}, refs={self.refs})"


def parse_json(data):
    objects = []

    for key, value in data.items():
        refs = [
            Reference(ref.get("type"), ref.get("addr"))
            for ref in value.get("refs", [])
        ]

        obj = A2LVariable(value.get("name"), value.get("addr"), refs)
        objects.append(obj)

    return objects
