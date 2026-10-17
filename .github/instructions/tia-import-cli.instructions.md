---
applyTo: "Tools/**"
description: "CMsoft Import for TiaPortal - the MCP server and the CLI bridge for scripts and agents"
---
<!-- cmsoft:managed tia-import - Prepare Workspace of CMsoft Import for TiaPortal updates this file; delete this line to keep your own version -->
# TIA CLI Bridge Instructions

The CMsoft Import for TiaPortal extension exposes a localhost-only JSON bridge for external scripts and agents.

## MCP Server (preferred for MCP-capable agents)

The extension also runs a built-in **MCP server** (Model Context Protocol, Streamable HTTP) exposing the same `tia_*` capabilities as native MCP tools. It is **enabled by default** (`tiaImport.mcp.enabled`) and starts with the extension.

While running, the extension writes `.tia/mcp.json` in the workspace:

```json
{
  "version": 1,
  "host": "127.0.0.1",
  "port": 58470,
  "token": "...",
  "endpoint": "/mcp",
  "transport": "streamable-http"
}
```

How an agent uses it:

1. Read `.tia/mcp.json` at runtime before every session (never hard-code or commit the port/token).
2. Connect your MCP client to `http://<host>:<port>/mcp` with header `Authorization: Bearer <token>`.
3. Call `tools/list` to discover the 26 `tia_*` tools with their input schemas, then `tools/call`. Start with `tia_connect`, then `tia_list_projects` / `tia_select_project`, `tia_list_devices`, `tia_list_blocks`.
4. `GET /health` (no auth) verifies the server is up and lists the tool names.
5. If `.tia/mcp.json` is missing, the server is stopped — set `tiaImport.mcp.enabled` to `true` or run the **CMsoft Import for TiaPortal: Start MCP Server** command in VS Code.

Safety notes for MCP: `tia_import_*` tools run autonomously (no confirmation dialogs). `tia_download_to_plc` requires `tiaImport.lmTools.allowPlcDownload`; when the PLC asks for authentication, the local user is prompted in VS Code — credentials never pass through the MCP client.

## Companion: CMsoft Viewer for TiaPortal MCP Server (PLC online data)

If the **CMsoft Viewer for TiaPortal** extension is installed alongside CMsoft Import for TiaPortal, it runs its own localhost-only MCP server (Streamable HTTP, same protocol as above) exposing four `tia_viewer_*` tools for **online PLC data** — complementary to this extension's project-side `tia_*` tools. It is enabled by default (`tiaViewer.mcp.enabled`) and starts with the extension.

While running, CMsoft Viewer for TiaPortal writes `.tia/mcp-viewer.json` (same shape as `.tia/mcp.json`):

```json
{
  "version": 1,
  "host": "127.0.0.1",
  "port": 58470,
  "token": "...",
  "endpoint": "/mcp",
  "transport": "streamable-http"
}
```

How an agent uses it:

1. Read `.tia/mcp-viewer.json` at runtime before every session — the port is ephemeral and the token changes on every activation, so never hard-code or commit them. In plain workspaces the file may exist only in the extension's global storage; the workspace copy appears once the workspace is used for TIA work (unless `tiaViewer.mcp.writeWorkspaceStateFile` is disabled). If it is missing, enable `tiaViewer.mcp.enabled` or run the **CMsoft Viewer for TiaPortal: Start MCP Server** command in VS Code.
2. Connect your MCP client to `http://<host>:<port>/mcp` with header `Authorization: Bearer <token>`. `GET /health` (no auth) verifies the server and lists the tool names.
3. Tools (call `tools/list` for the input schemas):
   - `tia_viewer_plc_sessions` — list PLCs with an active online session (the user pressed *Go online* in a CMsoft Viewer for TiaPortal preview panel). All other viewer tools require such a session; when none exists, ask the user to go online first.
   - `tia_viewer_plc_read` — read online variable values (`PlcProgram.Read`). DB members are read only when their *Accessible from HMI/OPC UA* attribute is set (verified against the exported block sources in the workspace).
   - `tia_viewer_plc_write` — write one online variable (requires *Writable from HMI/OPC UA*). Writing affects the running process: the local user confirms every write in a VS Code dialog unless `tiaViewer.lmTools.autoConfirmPlcWrites` is enabled — never try to bypass this gate.
   - `tia_viewer_trend_data` — record/read/clear archived online trend series. Typical autonomous PID tuning: `record` Setpoint/ProcessValue/Output of the PID instance DB → `read` the response → adjust parameters with `tia_viewer_plc_write` → `read` again.

CMsoft Viewer for TiaPortal has **no separate CLI bridge** — its automation surface is the MCP endpoint only. Simple scripts can still call it directly over HTTP JSON (the server answers with plain JSON, no SSE stream required), which covers CLI-style use.

## Language Model Tools (agents running inside VS Code)

Both extensions also register the same tools as **VS Code Language Model Tools**, so an agent running inside VS Code (Copilot Chat / agent mode) calls them directly — no state file, port or token needed. Prefer the LM tools whenever the agent runs in the same VS Code window as TIA Portal; use the MCP servers or the CLI bridge only for external agents and scripts.

- **CMsoft Import for TiaPortal** exposes 26 `tia_*` LM tools — the same commands as in the table below (`connect`, `list_devices`, `import_file`, `compile`, `download_to_plc`, …), named `tia_connect`, `tia_list_devices`, etc. In Copilot Chat they can also be referenced with `#` by their reference names (`#tiaConnect`, `#tiaListDevices`, …).
- **CMsoft Viewer for TiaPortal** exposes its four `tia_viewer_*` PLC online tools (`#plcSessions`, `#plcRead`, `#plcWrite`, `#plcTrendData`) — a surface identical to its MCP server.

The safety gates are identical across LM tools, MCP and CLI: CMsoft Import for TiaPortal `tia_import_*` tools overwrite objects in TIA Portal (confirmed per call unless `tiaImport.lmTools.autoConfirmImports` is enabled), `tia_download_to_plc` stays gated behind `tiaImport.lmTools.allowPlcDownload` and always asks for confirmation, and CMsoft Viewer for TiaPortal PLC writes are confirmed by the local user unless `tiaViewer.lmTools.autoConfirmPlcWrites` is enabled.

## State File

The CLI bridge is **opt-in and disabled by default**. Until it is enabled, no listener runs and no `.tia/` folder is created.

Enable it in any of these ways:

- Click the **CLI Bridge** row in the *TIA Connection* view (toggles between `Off` / `On`).
- Click the **terminal** icon (*CMsoft Import for TiaPortal: Start CLI Bridge*) in the *TIA Connection* view title bar.
- Run the command **CMsoft Import for TiaPortal: Toggle CLI Bridge** from the Command Palette.
- Set `tiaImport.cli.enabled` to `true` in VS Code Settings.

Once enabled, the extension writes:

```json
{
  "version": 1,
  "host": "127.0.0.1",
  "port": 58469,
  "token": "..."
}
```

Default location: `.tia/cli.json` in the workspace.

Rules:

- Read `.tia/cli.json` at runtime before every automation session.
- Do not hard-code the port or token.
- Do not commit `.tia/cli.json`.
- Re-read the state file after VS Code reloads or after the bridge is re-enabled.
- If the file is missing, the bridge is disabled — enable `tiaImport.cli.enabled` and retry.

## Request Shape

Send authenticated requests to `POST /api`:

```json
{
  "command": "list_devices",
  "args": {}
}
```

Use `Authorization: Bearer <token>` from `.tia/cli.json`.

`GET /health` returns available commands and does not require a token.

## Calling the Bridge

Nothing has to be installed — PowerShell is enough:

```powershell
$s = Get-Content .tia\cli.json | ConvertFrom-Json
$h = @{ Authorization = "Bearer $($s.token)" }
Invoke-RestMethod -Method Post -Uri "http://$($s.host):$($s.port)/api" -Headers $h -ContentType 'application/json' `
                  -Body '{"command":"list_devices","args":{}}'
```

`Tools/tia_cli_example.py` is a complete Python client of the same protocol (standard library only).

The extension also ships a command-line helper, `scripts\tia-cli.js` in its installation folder
(`%USERPROFILE%\.vscode\extensions\mariuszczyrnek.tia-import-<version>\`). It runs on the runtime built into VS Code, so no
Node.js is needed: section 13.4 of the user manual (**CMsoft Import for TiaPortal: Open User Manual**) defines a `tia`
PowerShell function for it. Use `tia` only when that function exists in the user's PowerShell; otherwise call the HTTP bridge as above.

```powershell
tia current_project --pretty
tia get_logs --limit 100 --pretty
tia list_devices --pretty
tia open_project --filePath "C:\Projects\Demo.ap21" --pretty
tia download_to_plc --device PLC_1 --scope changes --pretty
tia download_to_plc --device PLC_1 --scope software --username admin --password secret
```

## Commands

Command names mirror the Language Model tools and accept both plain names and `tia_` names:

| Command | Purpose |
| --- | --- |
| `prepare_workspace` | Copy workspace templates and helper files. |
| `connect` | Attach to a running TIA Portal instance or use the extension's normal connection flow. |
| `open_project` | Open a TIA project by `filePath` without showing a project picker. |
| `disconnect` / `close_project` | Disconnect from TIA Portal. |
| `current_project` | Return connection and active project metadata. |
| `list_projects` | List open TIA Portal projects. |
| `select_project` | Select the active project by `projectName`. |
| `refresh` | Refresh the project tree/model. |
| `list_devices` | List devices/controllers. |
| `list_blocks` | List blocks for a selected device. Supports `nameFilter`, `offset`, `limit`. |
| `import_blocks` | Pull selected blocks, or all blocks when `blocks` is omitted. Uses the extension's configured block formats (`tiaImport.exportFormat`, `tiaImport.dbExportFormat`). |
| `export_block` | Pull one block from TIA Portal to local files. |
| `export_device` | Pull all program objects for one device. |
| `export_hw_config` | Pull hardware configuration. Omit `device` for all devices. |
| `export_project` | Pull all devices and optionally HW config. |
| `import_file` | Push one local XML/SCL/s7dcl/xlsx file to TIA Portal. |
| `import_folder` | Push all supported files from a folder. |
| `import_hw_config` | Push HW config `.xml`/`.aml` file or folder. |
| `compile` | Compile PLC software for a device. |
| `download_to_plc` | Download (load) software/hardware into the physical PLC. Args: `device` (required), `scope` (`changes` default / `software` / `hardwareAndSoftware`), optional `username` + `password` for password-protected CPUs (UMAC needs both; legacy access-level protection needs only `password`). **Gated:** requires `tiaImport.lmTools.allowPlcDownload` (same switch as the LM tool / the *PLC Download* row in the TIA Connection view). |
| `get_problems` | Return current diagnostics. |
| `fix_compile_errors` | One import/compile/diagnostics iteration. |
| `export_cross_references` | Export cross-reference data for a PLC. |
| `get_logs` | Return recent extension log entries. |

## Recommended Agent Workflow

1. Call `current_project`.
2. If not connected, call `connect`, then `list_projects` and `select_project` when needed.
3. Call `refresh`, `list_devices`, and `list_blocks` before choosing block IDs or device names.
4. Prefer narrow import/export scopes. For block pulls, use `import_blocks` with `blocks` or `export_block`; both honor the extension's configured file formats.
5. After every import, call `compile` and inspect `get_problems`.
6. Only after a successful compile, call `download_to_plc` (default `scope=changes` downloads just the changed software — the closest equivalent to reloading a single edited block). If the PLC is password-protected, pass `username`/`password` per call; credentials are never stored.
7. Use `get_logs` when TIA Portal or the wrapper reports ambiguous failures.

## Safety

- The bridge binds only to `127.0.0.1`.
- Every `POST /api` request requires the per-session token.
- Write operations modify the active TIA Portal project; keep scopes explicit.
- `download_to_plc` writes to the **physical PLC** and may stop the CPU. It is blocked until the user enables `tiaImport.lmTools.allowPlcDownload` — never try to bypass this gate. Pass `username`/`password` only in the request body, never commit or log them.
- Validate imported/exported PLC changes in TIA Portal before downloading to hardware.
