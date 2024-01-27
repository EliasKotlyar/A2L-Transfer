# A2L-Transfer Tool

## Overview

A2L-Transfer is a command-line tool designed to simplify the process of creating an A2L file for a given binary file. This tool takes two inputs – a source binary file and an existing A2L file – and generates a new A2L file for a target binary file. 

## Requirements

- Ghidra installed
- BinDiff installed
- BinExport Plugin for Ghidra installed

## Usage

Currently its optimized only for MED9.1 ECUs but it can be adopted to other ECUs as well.
Just adjust main.py for your bins and then run it.
Its recommended to run it step by step, as there might be errors during the process
Thats why the things are commented out

## Terminology:

- **Bin_A** Source Binary where you have a A2L
- **Bin_B** Target where you have dont have a A2L

## Description of the process

- **1. Generating Ghidra Project for Bin_A** 
- This step will generate a new Ghidra Project for the binary. 
- It will then define the memory map using "med9-install.py" and also move the binary to the right location in memory
- It will define all "UndefinedFunctions" using "DefineUndefinedFunctions.py"
- It will use ExportBinExport.py to export the Binary in a BinDiff compatible Format.
- If you are using some other cpu than MED9, you will have to adjust the scripts according to your needs. 
- You can do this steps also manually
- BinDiff Export can be done also using IDA Pro

- **2. Generating Ghidra Project for Bin_B** 
- Step is doing exactly the same as Step1, but for Bin_B 


- **3. Generating a2l.json** 
- This step will take the provided A2L for Bin_A and generate a JSON file out it. Reason is that parsing A2Ls in ghidra is complicated
because its using Python2. It will generate a Json like this:
```json
    "<Variable Name>": {
        "name": "<Variable Name>",
        "description": "Description from A2l",
        "type": "map",
        "addr": "<address of variable>",
        "size": 1 
    },
```

- **4. Generating RefMap.json with help of A2L.json** 
- This step will take the json and use Ghidra to generate a RefMap of all A2L addresses in Bin_A. Refmap will be looking like this:
```json
    "<Variable Name>": {
        "refs": [
            {
                "type": "READ", 
                "addr": "<Address of Instruction which is doing something with the Var in Bin_A>"
            }
        ], 
        "name": "<Variable Name>", 
        "addr": "<Address of the Variable in Memory in Bin_A>"
    }, 
```
- Basically it will parse all accesses to the memory locations(xrefs) from ghidra and output them as JSON

- **5. Generating Bindiff DB**
- This step will run BinDiff with BinExport Files from 1 and 2. This is where all the magic is happening.
- Bindiff will match up the functions together and provide a SQLite DB with the results. It will be used in the next step.
- If its unclear what bindiff is doing, open up the Bindiff Gui and compare the two BinExport files manually.

- **6. Generating Target Instruction Map**
- Now we can iterate over the Refmap.json and try to find matching instructions in BinDiff Database for Bin_B
- It will generate target_instruction_map.json, which will contain the a2l_name and the address of the instruction which read/writes to it in Bin_B
- Attention: This step might take some time(5m). I havent figured out what the performance bottleneck is, but i suspect its the sqlite-database
- Target Map looks like this:
```json
{
    "<Variable Name>": "<Address a instruction which changes the var in Bin_B>",
}
```
- Key is the a2l-name
- value is the address of a instruction where its getting changed in Bin_B 
- The process selects from the list of xrefs a matching instruction which is present in both binaries
- Process can be modified in generate_targetmap.py
  
- **7. Generating Addressmap**
-  We just need to match targetmap to the real addresses of var. This is done by running ghidra on Bin_B
```json
{
    "<Variable Name>": "<Address of the Variable in Memory in Bin_B>",
}
```

- **8. Generating A2L**
- The process will just take 2 files and replace addresses in the target a2l with addresses from targetmap
- Its not very reliable this way as it might overwrite some addr, but i know that and for my hobbiest needs this is enough
- It should be improved, but i usually work with JSONs from 7 anyway :)

## Contributing

We welcome contributions! If you have ideas for improvements, bug fixes, or new features, please open an issue or submit a pull request.

## License

This tool is licensed under the [MIT License](LICENSE). Feel free to use, modify, and distribute it according to the terms of the license.

## Disclaimer

This tool is provided "as is" without any warranty. Use it at your own risk, and always make backups before performing any critical operations.

## Contact

For any questions, issues, or feedback, please create an issue on the [GitHub repository](https://github.com/EliasKotlyar/A2L-Transfer).

---

Thank you for using A2L-Transfer! 