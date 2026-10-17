# _extractHMI.py

Extract HMI-accessible variables from TIA Portal DB/IDB exports to Excel.

## Description

Scans all Data Blocks (GlobalDB, InstanceDB) in the PLC `Program blocks` directory and collects variables that are marked as externally accessible (`ExternalAccessible = true`). Outputs a single Excel file with one row per variable, matching the TIA Portal DB monitor view.

### Supported source formats

| Format         | Extension | Block type                                       |
| -------------- | --------- | ------------------------------------------------ |
| SimaticML XML  | `.xml`  | `SW.Blocks.GlobalDB`, `SW.Blocks.InstanceDB` |
| DB text source | `.db`   | Global Data Blocks                               |

### UDT / FB resolution

- Recursively resolves PLC Data Type (UDT) structures from `PLC data types/` XML definitions.
- For InstanceDBs, reads FB/FC/OB interface declarations (XML and `.s7dcl`/`.s7res`) to inherit comments.
- Expands arrays up to 64 elements with per-index rows.

## Usage

## Installation

Install required Python packages before first run:

```powershell
pip install pyyaml openpyxl
```

If Python reports `ModuleNotFoundError: No module named 'yaml'`, install:

```powershell
pip install pyyaml
```

```powershell
# Auto-detect PLC folder from TiaExport/ in current directory
python Tools\_extractHMI.py

# Explicit PLC folder path
python Tools\_extractHMI.py <plc_base_dir>

# Custom output file
python Tools\_extractHMI.py <plc_base_dir> -o output.xlsx
```

## Output

Default: `UserFiles\HMI_Variables_{plc_name}.xlsx`

The output directory is created automatically if it does not already exist.

### Excel columns

| Column                     | Description                                                     |
| -------------------------- | --------------------------------------------------------------- |
| Name                       | Full dotted path (e.g.`DBName.Struct.Field`)                  |
| Data type                  | SIMATIC type (`Int`, `Real`, `"UdtName"`, `Struct`, …) |
| Start value                | Initial value from the DB definition                            |
| Retain                     | Retentive flag                                                  |
| Accessible from HMI/OPC UA | `ExternalAccessible` attribute                                |
| Writable from HMI/OPC      | `ExternalWritable` attribute                                  |
| Visible in HMI engineering | `ExternalVisible` attribute                                   |
| Setpoint                   | `SetPoint` attribute                                          |
| Comment                    | en-US comment text                                              |

## Dependencies

- `openpyxl` — Excel file generation
- `pyyaml` — `.s7res` multilingual text parsing
