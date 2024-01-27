from src.common.bindiff import BinDiff
from src.common.hex_address import HexAddress
from src.common.json import read_json_file, write_json_file
from src.common.refmap_parser import parse_json


class GenerateTargetMap:
    def process(self, refmap: str, bindiffdb: str, targetmap: str):
        binDiff = BinDiff(bindiffdb)
        json = read_json_file(refmap)

        variables = parse_json(json)

        retArr = {}
        for a2lvar in variables:
            self.log(f"Parsing Variable {a2lvar.name} : {a2lvar.addr.to_str()}")

            i = 0
            targetAddress = None
            for reference in a2lvar.refs:
                i = i + 1
                self.log(f"Trying Reference {i}")
                if reference.type == "DATA":
                    continue

                result = binDiff.get_result(reference.addr)
                if result is None:
                    self.log(f'Matching instruction not found in bindiff')
                    continue
                if result.similarity < 0.98:
                    self.log(f'Similarity fail: {result.similarity}')
                    continue
                targetAddress = HexAddress(result.targetAddress).to_str()
                break
            if targetAddress:
                self.log2(f"Var found {a2lvar.name}")
                retArr[a2lvar.name] = targetAddress
            else:
                self.log2(f"Var not found {a2lvar.name}")
        write_json_file(targetmap, retArr)

    def log(self, logEntry: str):
        # print(logEntry)
        pass

    def log2(self, logEntry: str):
        print(logEntry)
        pass
