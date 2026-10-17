<!-- cmsoft:managed tia-import - Prepare Workspace of CMsoft Import for TiaPortal updates this file; delete this line to keep your own version -->
# tia_cli_example.py

Example Python client for the CMsoft Import for TiaPortal CLI bridge.

The script reads `.tia/cli.json`, connects to the local authenticated bridge, opens a TIA project by file path or attaches to TIA Portal, optionally selects a project, refreshes the project tree, and exports the project into the workspace.

## Usage

```powershell
python .\Tools\tia_cli_example.py "E:\Projects\TIA\Demo.ap21" --workspace . --pretty
python .\Tools\tia_cli_example.py --workspace . --pretty
python .\Tools\tia_cli_example.py --workspace . --project-name Demo --pretty
python .\Tools\tia_cli_example.py --workspace . --project-name Demo --program-only --log-level error --pretty
```

## Requirements

- VS Code workspace is open with the CMsoft Import for TiaPortal extension active.
- `tiaImport.cli.enabled` is true.
- `.tia/cli.json` exists in the workspace.
- TIA Portal is running or can be attached through the extension's `connect` command.

## Notes

- The script writes status and recent extension logs to stderr.
- The final machine-readable result is written to stdout as JSON.
- Do not commit `.tia/cli.json`; it contains a per-session token.
