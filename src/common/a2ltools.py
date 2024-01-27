
def get_c_type_size(type):
    type_size_mapping = {
        'UBYTE': 1,
        'SBYTE': 1,
        'SWORD': 2,
        'UWORD': 2,
        'ULONG': 4,
        'SLONG': 4,
        'UFLOAT': 4,
        'FLOAT32_IEEE': 4,
        # Add more types as needed
    }

    size = type_size_mapping.get(type)

    if size is not None:
        return size
    else:
        raise Exception("Not implemented: " + type)


def get_med9_size(type):
    type_size_mapping = {
        'KwbUb': 'UBYTE',
        'KwbUw': 'UWORD',
        'KwbWS8': 'SBYTE',
        'KwbWU16': 'UWORD',
        'KwbWU32': 'ULONG',
        'KwbWU8': 'UBYTE',
        'KwSb': 'SBYTE',
        'KwSw': 'SWORD',
        'KwUb': 'UBYTE',
        'KwUl': 'ULONG',
        'KwUw': 'UWORD',
        'KwWS16': 'SWORD',
        'KwWS32': 'SLONG',
        'KwWS8': 'SBYTE',
        'KwWU16': 'UWORD',
        'KwWU32': 'ULONG',
        'KwWU8': 'UBYTE',
        'KwbUl': 'ULONG',
        '_REC_S1VAL_20_u1' : "UBYTE",
        '_REC_S1VAL_20_s2': "UWORD",
        # MED9.2:
        'KwWR32' : "ULONG",
        'KwbWR32' : "ULONG"
    }

    size = type_size_mapping.get(type)

    if size is not None:
        return size
    else:
        raise Exception("Not implemented: " + type)


def read_a2l_variables(filename):
    '''
    Credits go to: http://nefariousmotorsports.com/forum/index.php?topic=13749.0title=
    Args:
        filename: filenameo of a2l

    Returns: dict of measurements

    '''
    retmaps = {}
    with open(filename, 'r', encoding='latin-1') as fp:
        measurements = fp.read().split("/begin MEASUREMENT")
        # Removes Asap Line
        measurements.pop(0)
        # print("Found: %d measurement(s)" % len(measurements))
        for m in measurements:
            splitted = m.split("\n")
            # Strip array
            splitted = [s.strip() for s in splitted]
            # Remove all void strings
            splitted = [s for s in splitted if s != ""]
            name = splitted[0]
            description = splitted[1]
            size = get_c_type_size(splitted[2])
            ecu_address = [s for s in splitted if s.startswith("ECU_ADDRESS")]
            if (len(ecu_address) > 0):
                ecu_address = ecu_address[0]
                ecu_address = ecu_address.replace('ECU_ADDRESS', '').strip()
            else:
                print("ERROR: Address not found, A2L wrong")

            # elif (l.startswith("ECU_ADDRESS")):
            # addr = l[12:]

            retmaps[name] = {
                'name': name,
                'description': description,
                'type': "dynamic_variable",
                # Read Addr:
                'addr': ecu_address,
                'size': size,
            }

    return retmaps


def read_a2l_static_values(filename):
    '''
    Credits go to: http://nefariousmotorsports.com/forum/index.php?topic=13749.0title=
    Args:
        filename: filenameo of a2l

    Returns: dict of measurements

    '''
    retmaps = {}
    with open(filename, 'r', encoding='latin-1') as fp:
        static_values = fp.read().split("/begin CHARACTERISTIC")
        # Removes Asap Line
        static_values.pop(0)
        # print("Found: %d measurement(s)" % len(measurements))
        for m in static_values:
            splitted = m.split("\n")
            # Strip array
            splitted = [s.strip() for s in splitted]
            # Remove all void strings
            splitted = [s for s in splitted if s != ""]
            name = splitted[0]
            description = splitted[1]
            type = splitted[2]
            ecu_address = splitted[3]
            ecu_address = int(ecu_address, 16)
            ecu_address = ecu_address + 0x400000
            ecu_address = hex(ecu_address)
            if type == "VALUE":
                type = "static_variable"
                size = splitted[4]
                size = get_med9_size(size)
                size = get_c_type_size(size)
            elif type == "VAL_BLK":
                type = "static_variable"
                size = splitted[4]
                size = get_med9_size(size)
                size = get_c_type_size(size)
            elif type == "ASCII":
                type = "static_string"
                size = 1
            elif type == "CURVE":
                type = "map"
                size = 1
            elif type == "MAP":
                type = "map"
                size = 1
            else:
                raise Exception("Not implemented: " + type)

            retmaps[name] = {
                'name': name,
                'description': description,
                'type': type,
                # Read Addr:
                'addr': ecu_address,
                'size': size,
            }

    return retmaps
