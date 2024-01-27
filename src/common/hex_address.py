class HexAddress:
    def __init__(self, content):
        '''
        Initializes a HexAddress object.

        Parameters:
        - content (int or str): The content to be transformed into a HexAddress.

        Raises:
        - ValueError: If the content type is unsupported.
        '''
        if isinstance(content, int):
            self.value = content
        elif isinstance(content, str):
            self.value = int(content, 16)
        else:
            raise ValueError("Unsupported Transformation!")

    def to_int(self):
        '''
        Converts the HexAddress to an integer.

        Returns:
        - int: The integer representation of the HexAddress.
        '''
        return self.value

    def to_str(self):
        '''
        Converts the HexAddress to a hexadecimal string.

        Returns:
        - str: The hexadecimal string representation of the HexAddress.
        '''
        return hex(self.value).upper().replace("X", "x")

    def __str__(self):
        '''
        Returns the hexadecimal representation when the object is converted to a string.

        Returns:
        - str: Hexadecimal representation.
        '''
        return self.to_str()
    def __repr__(self):
        return self.to_str()
