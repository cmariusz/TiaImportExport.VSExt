## CMsoft Import for TiaPortal

- `tia_cli_example.py` / `tia_cli_example.md` — opens or attaches to a TIA Portal project through the CLI bridge
  (`.tia/cli.json`) and exports it into the workspace.
- `_extractHMI.py` / `_extractHMI.md` — extracts the HMI-accessible variables of the exported data blocks to
  Excel.
- `_setStartValueHMI.py` / `_setStartValueHMI.md` — writes start values and comments from an HMI variables
  Excel file back into the exported data blocks.
