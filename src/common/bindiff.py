import sqlite3

from src.common.hex_address import HexAddress


class BinDiffResult:
    def __init__(self, similarity: float, confidence: float, targetAddress: HexAddress):
        self.targetAddress = targetAddress
        self.confidence = confidence
        self.similarity = similarity


class BinDiff:
    def __init__(self, filename):
        # Connect to SQLite database
        self.conn = sqlite3.connect(filename)
        self.cursor = self.conn.cursor()

    def get_result(self, address: HexAddress):
        # Check if address is an integer
        assert isinstance(address, HexAddress), "Address must be an integer."
        address1 = address.to_int()
        # Execute the SQL query
        instruction = self.fetch_from_sqlite(f"SELECT * FROM instruction WHERE address1 = {address1}")
        if instruction is None:
            return None
        basicblock = self.fetch_from_sqlite(f"SELECT * FROM basicblock WHERE id = {instruction['basicblockid']}")
        funct = self.fetch_from_sqlite(f"SELECT * FROM function WHERE id = {basicblock['functionid']}")

        return BinDiffResult(
            funct["similarity"],
            funct["confidence"],
            instruction["address2"]
        )

    def fetch_from_sqlite(self, query: str):
        self.cursor.execute(query)
        result = self.cursor.fetchone()
        column_names = [description[0] for description in self.cursor.description]
        result_dict = {column_name: value for column_name, value in zip(column_names, result)} if result else None
        return result_dict
