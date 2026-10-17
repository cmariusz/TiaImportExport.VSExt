# CMsoft Import for TiaPortal — VS Code Extension

🌐 **[www.cmsoft.com.pl](https://www.cmsoft.com.pl)** — all CMsoft extensions, the shop and contact

<!-- VERSION-BADGE -->
[![Version](https://img.shields.io/badge/version-4.2.0-blue)](CHANGELOG.md)
<!-- /VERSION-BADGE -->

[![VS Code](https://img.shields.io/badge/VS%20Code-%3E%3D1.95.0-blue?logo=visualstudiocode)](https://code.visualstudio.com/)
[![License: Commercial EULA](https://img.shields.io/badge/License-Commercial%20EULA-blue.svg)](LICENSE.md)
[![Platform: Windows](https://img.shields.io/badge/Platform-Windows-0078D6?logo=windows)](https://www.microsoft.com/windows)
[![Author](https://img.shields.io/badge/Author-CMsoft-orange?logo=linkedin)](https://www.linkedin.com/in/mariusz-czyrnek-a33b87a6)

**Bidirectional bridge between VS Code and Siemens TIA Portal** — import PLC/HMI projects from TIA Portal to local files, edit them with full VS Code + Copilot power, and export changes back. Built on the TIA Portal Openness API.

> 💡 **Tip:** The PLC block **viewer** and **web preview generator** live in the companion **[CMsoft Viewer for TiaPortal](https://marketplace.visualstudio.com/items?itemName=MariuszCzyrnek.tia-viewer)** extension ([GitHub](https://github.com/cmariusz/TiaViewer.VSExt)) — it renders LAD/FBD/SCL/GRAPH blocks, data blocks, UDTs and tag tables from the export folders this extension produces, both inside VS Code and as standalone whole-PLC HTML web previews. The two extensions are built to work together.

> 📖 **User manual:** built into the extension — Command Palette → **CMsoft Import for TiaPortal: Open User Manual** (screenshots, a complete worked example, Copilot / MCP / CLI examples, troubleshooting; works offline).

![CMsoft Import for TiaPortal Overview](Screenshots/Overview.png)

---

## FREE and PRO

| Feature                                                                                                                | FREE                           | PRO          |
| ---------------------------------------------------------------------------------------------------------------------- | ------------------------------ | ------------ |
| Connect to TIA Portal, open projects, browse the project structure                                                     | ✅                             | ✅           |
| Import from TIA Portal to the workspace — program blocks, tag tables, PLC data types, watch tables, technology objects | ✅                             | ✅           |
| Compile the PLC software, compile errors in the PROBLEMS panel                                                         | ✅                             | ✅           |
| Export from the workspace to TIA Portal                                                                                | up to 10 objects per operation | ✅ unlimited |
| Hardware configuration — import from and export to TIA Portal (XML, AutomationML)                                      | ⛔                             | ✅           |
| Software Units, HMI, project library types, languages and project texts                                                | ⛔                             | ✅           |
| Cross-references, download to PLC                                                                                      | ⛔                             | ✅           |
| Copilot Language Model tools (`tia_*`) and the `@tia` chat participant                                                 | ⛔                             | ✅           |
| MCP server for AI agents                                                                                               | FREE operations only           | ✅           |
| CLI bridge for scripts and automation                                                                                  | ⛔                             | ✅           |
| Prepare Workspace (AI instructions, XSD schemas, templates, Tools)                                                     | ⛔                             | ✅           |

- **14-day free trial**, no payment details needed: **CMsoft Import for TiaPortal: Manage License / Subscription** → *Try for free*.
- Subscription (monthly or yearly, renews automatically) or one-time payment: **CMsoft Import for TiaPortal: Buy License** — prices on the [pricing page](https://extensions.cmsoft.com.pl/pricing?product=tia-import). A license covers one Seat (one named user on one activated workstation).
- The license is shown in the shared **CMsoft** status bar item (one item for all installed CMsoft extensions) and in the **License** row of the *Connection* view; both open the license panel. Without a license the extension stays in FREE — nothing is deleted when a trial or a license ends.

---

## Key Features

### Import from TIA Portal (TIA → local files)

| Capability                                 | Description                                                                                                                                                                                                                                                                              |
| ------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Connect to TIA Portal**            | Auto-detect running TIA Portal instances or open a project file (`.ap17/.ap18` /`.ap19` / `.ap20` / `.ap21`)                                                                                                                                                                    |
| **Import Entire Project**            | Import complete project structure with all devices, blocks, tags, UDTs, and HW config                                                                                                                                                                                                    |
| **Import Devices**                   | Import individual devices or all devices in a category (PLCs, HMIs, IO_Devices, Computers)                                                                                                                                                                                               |
| **Import Program Blocks**            | Import OB, FB, FC, F-FB, F-FC, DB blocks in XML, SCL, SD (`.s7dcl` / `.s7res`), or DB source (`.db`) format                                                                                                                                                                        |
| **Import Tag Tables**                | Import PLC tag tables as SimaticML XML or Excel XLSX spreadsheets                                                                                                                                                                                                                        |
| **Import UDTs**                      | Import PLC data types (user-defined types)                                                                                                                                                                                                                                               |
| **Import Watch Tables**              | Import watch and force tables                                                                                                                                                                                                                                                            |
| **Import Technology Objects**        | Import Technology Objects (technological instance DBs: PID, Motion Control axes, counters, …) as SimaticML XML, mirroring the TIA user group structure into`Technology objects/` — per device or automatically with device/project import                                            |
| **Import HMI**                       | Import HMI screens, tags, and connections                                                                                                                                                                                                                                                |
| **Import HW Config**                 | Import hardware configuration as XML or**CAx / AutomationML (`.aml`)**. Mirrors TIA Portal device folders on disk; root IO devices stay flat in `Devices/IO_Devices/`. Toggle format via *Format HW* in the Connection panel.                                                |
| **Import Project Library**           | Import the**Project Library &gt; Types** tree (FBs, FCs, UDTs, …) — per-type format selection: LAD/FBD/STL → `.s7dcl`/`.s7res` (V20+), SCL → `.scl`, UDT/GRAPH/CFC/SFC/DB → `.xml`. Master copies are intentionally not imported.                                     |
| **Import Languages & Project Texts** | Import project language settings (supported / active / editing / reference languages →`languages.json`) and export project texts (Languages & resources) to XLSX workbooks for translation. V21+ writes one workbook with all target languages; V18–V20 write one per language pair. |
| **Project Explorer**                 | Browse the full TIA Portal project hierarchy in the VS Code sidebar                                                                                                                                                                                                                      |

> **HW Config folder layout:** `Import HW Config` mirrors TIA Portal folder structure on disk. Devices at the project root use `Devices/<Category>/<Device>/DeviceConfiguration/`, except root IO devices which keep the legacy flat `Devices/IO_Devices/` layout. Devices placed inside TIA Portal device folders are exported under `Devices/<Category>/<FolderPath>/<Device>/DeviceConfiguration/`.

### Viewing imported blocks — companion extension

The block viewer and web preview generator were moved to the separate **[CMsoft Viewer for TiaPortal](https://marketplace.visualstudio.com/items?itemName=MariuszCzyrnek.tia-viewer)** extension ([source on GitHub](https://github.com/cmariusz/TiaViewer.VSExt)). Install it to render imported blocks (SimaticML XML, `.s7dcl` + `.s7res`, `.db`, `.scl`, `.udt`) as interactive LAD/FBD/SCL/GRAPH diagrams inside VS Code, and to generate a complete offline whole-PLC HTML web preview from the export folders this extension produces.

### Export to TIA Portal (local files → TIA)

| Capability                           | Description                                                                                                                                                                                       |
| ------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Export Blocks**              | Export XML / SCL / SD / DB source files back to TIA Portal                                                                                                                                        |
| **Export Software Unit**       | Export a complete V18+ Software Unit folder (`Units/<UnitName>/{Program blocks, PLC data types, PLC tags}`) back to TIA Portal; creates the unit if missing and applies `_unit.json` metadata |
| **Export Tag Tables**          | Export XML or XLSX tag tables to TIA Portal                                                                                                                                                       |
| **Export Project Texts**       | Push a translated project texts XLSX back into the same TIA project (Languages & resources), with optional source-language update                                                                 |
| **Export UDTs / Watch Tables** | Export data types and watch tables                                                                                                                                                                |
| **Export Technology Objects**  | Export Technology Object XMLs back to TIA Portal (auto-detected by content) — objects are imported into the PLC's root*Technology objects* group                                               |
| **Export HW Config**           | Export hardware configuration as XML or**CAx / AutomationML (`.aml`)** via `CaxProvider`                                                                                                |
| **Unified Export**             | One-click export of an entire device folder in dependency order (UDTs → Blocks → Tags → Watch Tables → Technology Objects → HW)                                                              |
| **Smart Comparison**           | Only overwrite items that actually changed (normalized XML diff; Instance DBs compared by StartValues only)                                                                                       |
| **Orphan Cleanup**             | Auto-delete blocks, groups, tag tables, UDTs and Technology Objects in TIA that no longer exist locally (and orphaned local files on import from TIA)                                             |
| **Dependency Ordering**        | Files sorted automatically: UDT → FB → FC → OB → GlobalDB → InstanceDB                                                                                                                       |
| **Compile after Export**       | Automatically compile PLC software in TIA Portal after export — configurable: Always / Ask / Never                                                                                               |
| **Compile Error Tracking**     | Compile results mapped to VS Code PROBLEMS panel with file and line resolution (network / SCL line mapping)                                                                                       |

### Smart Capabilities

- **Connection health monitoring** — automatic ping-based checks with auto-disconnect on broken connections
- **Know-how protected block detection** — detects and skips placeholder files for protected blocks
- **Instance DB creation** — creates Instance DBs directly via API (no XML import needed)
- **Cancellation support** — cancel long-running operations via VS Code progress UI
- **Status bar** — real-time connection state and project info; the **CMsoft** item lists your CMsoft add-on licenses and the user manuals of the installed CMsoft add-ons (hover for details, click to pick a license and manage it or a manual and open it; **Help: CMsoft Manuals…** in the Command Palette lists the manuals alone)
- **Time-based import progress** — long-running project, device, device-category, and category HW Config imports show a live numeric percentage, weighted work counter, and ETA in both the notification progress UI and the status bar; block imports are weighted by export type (SD, SCL/DB source, XML, UDTs, tag/watch tables) and category HW Config imports are weighted per device with a small safety buffer so very large TIA exports do not look stalled
- **Compile after export** — optional PLC software compilation in TIA Portal after each export (Always / Ask / Never); results shown in OUTPUT panel
- **Compile error tracking** — compile errors and warnings mapped to VS Code PROBLEMS panel with automatic file matching, network-to-line resolution (XML, S7DCL, SCL), and direct navigation to the error location

### Copilot / AI Agent Integration

The extension exposes **26 Language Model Tools** (prefix `tia_`) plus a `@tia` chat participant, so GitHub Copilot (and any other VS Code LM-tool consumer) can drive TIA Portal end-to-end without manual clicks:

- **Connection / discovery** — `tia_connect`, `tia_disconnect`, `tia_list_projects`, `tia_select_project`, `tia_refresh`, `tia_list_devices`, `tia_list_blocks`
- **Pull from TIA → workspace** — `tia_export_block`, `tia_export_device`, `tia_export_project` (entire project), `tia_export_hw_config` (per-device or project-wide HW Config; honours `tiaImport.hwConfigFormat`)
- **Push workspace → TIA** — `tia_import_file`, `tia_import_folder` (blocks, tags, UDTs, watch tables), `tia_import_unit` (complete Software Unit), `tia_import_hw_config` (HW Config XML/AML — required for HW; `tia_import_file` does not handle HW)
- **Languages & project texts** — `tia_get_project_languages` (language settings), `tia_export_project_texts` (project texts to xlsx for translation), `tia_import_project_texts` (re-import translated xlsx into the same project)
- **Compile loop** — `tia_compile`, `tia_get_problems`, `tia_fix_compile_errors` (orchestrates import → compile → diagnostics until clean or `tiaImport.lmTools.maxFixIterations` is reached)
- **Download to PLC** — `tia_download_to_plc` (loads changed software / full program / hardware+software into the physical PLC; **disabled by default** — requires `tiaImport.lmTools.allowPlcDownload`)
- **Analysis** — `tia_export_cross_references` (full PLC cross-reference dump to JSONL/CSV, including unused symbols)

Imports that overwrite existing TIA objects show a confirmation dialog unless `tiaImport.lmTools.autoConfirmImports` is enabled. `tia_download_to_plc` always asks for confirmation and is blocked entirely until `tiaImport.lmTools.allowPlcDownload` is enabled — a download can stop the CPU and overwrite the running program. When TIA Portal must reinitialize data blocks for a download (their values, retain data included, go back to the start values), the row **DB Reinit on Download** of the Connection view (`tiaImport.lmTools.reinitializeDataBlocks`) decides: **Never**, **Ask** (default — you are asked in VS Code) or **Always**. The chat participant `@tia` is registered as `tia.assistant` and has the same toolset available.

### External CLI Bridge

External scripts can drive the same TIA workflows through a localhost-only JSON bridge.

**The bridge is opt-in and disabled by default** — no listener is started and no `.tia/` folder is created until you enable it. Turn it on in any of these ways:

- Click the **CLI Bridge** row in the *TIA Connection* view (toggles between `Off` / `On`).
- Click the **terminal** icon (*CMsoft Import for TiaPortal: Start CLI Bridge*) in the *TIA Connection* view title bar — you will be prompted to enable it.
- Set `tiaImport.cli.enabled` to `true` in VS Code Settings.

Once enabled, the extension writes `.tia/cli.json` in the workspace with the current host, port and per-session bearer token. Scripts must read that file at runtime and send authenticated `POST /api` requests. Do not hard-code or commit the token. Toggling the setting off stops the listener and removes the state file.

The bridge is plain HTTP, so any language works — PowerShell needs nothing else installed:

```powershell
$s = Get-Content .tia\cli.json | ConvertFrom-Json
$h = @{ Authorization = "Bearer $($s.token)" }
Invoke-RestMethod -Method Post -Uri "http://$($s.host):$($s.port)/api" -Headers $h -ContentType 'application/json' `
                  -Body '{"command":"list_blocks","args":{"device":"PLC_1","limit":2}}'
```

For the command line, the extension ships the helper `tia-cli.js`. It runs on the runtime built into VS Code, so no Node.js is needed; the user manual (section 13.4, **CMsoft Import for TiaPortal: Open User Manual**) has a ready-made `tia` PowerShell function for it:

```powershell
tia current_project --pretty
tia open_project --filePath "C:\Projects\Demo.ap21" --pretty
tia import_blocks --device PLC_1 --blocks FB10,FC20 --pretty
tia import_file --device PLC_1 --filePath "C:\Projects\Demo\Block.xml" --overwriteExisting true
tia download_to_plc --device PLC_1 --scope changes --username admin --password secret
```

`download_to_plc` writes to the physical PLC: it is gated by `tiaImport.lmTools.allowPlcDownload` (same switch as the LM tool) and takes `--device` (required), `--scope changes|software|hardwareAndSoftware` (default `changes`) and optional `--username` / `--password` for password-protected CPUs (UMAC needs both). A script cannot answer the data-block reinitialization question: with `tiaImport.lmTools.reinitializeDataBlocks` on `ask` (default) a download that needs it stops without loading anything — set `always` for scripted downloads.

Use `import_blocks` / `tia_import_blocks` to pull blocks from TIA Portal into the workspace; it honours the configured block formats (`tiaImport.exportFormat`, `tiaImport.dbExportFormat`). Use `import_file`, `import_folder` and `import_hw_config` when pushing local files back into TIA Portal.

### MCP Server (for AI agents)

The extension runs a built-in **MCP server** (Model Context Protocol, Streamable HTTP) that exposes the same 26 `tia_*` tools to any MCP client — VS Code Copilot, Claude Desktop, Cursor or custom agents.

**The server is enabled by default** (`tiaImport.mcp.enabled`) and starts with the extension. While running, it writes `.tia/mcp.json` (workspace + extension global storage) with the endpoint URL and a per-session bearer token:

```json
{ "version": 1, "host": "127.0.0.1", "port": 58470, "token": "...", "endpoint": "/mcp", "transport": "streamable-http" }
```

- **VS Code 1.99+** discovers the server automatically (MCP server definition provider) — no configuration needed. Disable it via `tiaImport.mcp.enabled` if you don't want it.
- **External MCP clients**: read `.tia/mcp.json` at runtime (never hard-code or commit the token), connect to `http://<host>:<port>/mcp` with `Authorization: Bearer <token>`, then call `tools/list` / `tools/call`. `GET /health` lists the tool names without auth.
- The server binds to `127.0.0.1` only. Note that `tia_import_*` tools run **autonomously** over MCP (no confirmation dialogs — unlike Copilot LM tools). `tia_download_to_plc` is still gated by `tiaImport.lmTools.allowPlcDownload`, and PLC credentials are prompted from the local user via a masked VS Code input — they never pass through the MCP client. The same goes for the question whether data blocks may be reinitialized (`tiaImport.lmTools.reinitializeDataBlocks`: `ask`).

---

## Requirements

| Requirement          | Version                                         |
| -------------------- | ----------------------------------------------- |
| **OS**         | Windows 10 / 11                                 |
| **TIA Portal** | V17, V18, V19, V20 or V21 with Openness license |
| **.NET**       | .NET Framework 4.8 (part of Windows 10 / 11)    |
| **VS Code**    | ≥ 1.95.0                                       |

Nothing else needs to be installed — no Node.js, npm or build tools: the extension comes ready to run, and VS Code provides its runtime.

> A single VSIX supports **TIA Portal V17, V18, V19, V20 and V21** — pick the active version via the **TIA Portal** entry of the Connection panel (or the `tiaImport.tiaPortalVersion` setting). Newer Openness features degrade gracefully on older versions:
>
> - **SD format** (`.s7dcl` / `.s7res`) requires **V20+**. On V17–V19 the extension automatically falls back to XML for LAD/FBD/STL blocks; SCL blocks continue to export as `.scl`.
> - **Cross-reference dump** (`tia_export_cross_references`) requires **V18+**. **Heads-up:** building a full cross-reference table is performed by TIA Portal itself and can take **several minutes — sometimes 10 min+ on large PLCs** (thousands of blocks, large fault-tolerant projects). Progress is logged line-by-line in the *CMsoft Import for TiaPortal* output channel; the operation is non-blocking, so other imports/compiles continue normally.
> - **Software Units** require **V18+**; on V17 unit commands report `supported:false`.
> - **WinCC Unified** screen/tag-table **groups** and tag-table tag export require **V18+**; on V17 only root-level screens and tag tables are exported.
> - **CAx / AutomationML HW Config** is available on all supported versions.
>
> The Windows user running VS Code must be a member of the **Siemens TIA Openness** user group. See [Adding users to the Siemens TIA Openness user group](https://docs.tia.siemens.cloud/r/en-us/v20/tia-portal-openness-api-for-automation-of-engineering-workflows/basics/installation/adding-users-to-the-siemens-tia-openness-user-group) for details.

---

## Installation

1. Install the extension from VS Code Marketplace (or `code --install-extension MariuszCzyrnek.tia-import`)
2. Make sure TIA Portal is installed with an Openness license
3. Optionally adjust settings via **File → Preferences → Settings → CMsoft Import for TiaPortal**

---

## Usage

### Connecting to TIA Portal

1. Start TIA Portal and open a project
2. Open VS Code in a workspace folder
3. Click the **TIA Portal** icon in the Activity Bar
4. Click **Connect to TIA Portal** or run the command `CMsoft Import for TiaPortal: Connect to TIA Portal`
5. The extension auto-detects running instances; if multiple are found, you pick one

### Importing from TIA Portal

1. Connect to TIA Portal
2. Browse the project structure in the **TIA Project Explorer** sidebar
3. Right-click on any node to import:
   - **Device** — import entire device (all blocks, tags, UDTs, watch tables)
   - **Device Category** — import all devices in a category (e.g. all PLCs)
   - **Block Group** — import a folder with all its blocks
   - **Block** — import a single program block
   - **Tag Tables** — import PLC tag tables (XML or XLSX)
   - **UDTs** — import PLC data types
   - **Watch Tables** — import observation/force tables
   - **Technology Objects** — import technological instance DBs (PID, Motion Control, …) to `Technology objects/`
   - **HMI** — import screens, tags, and/or connections
   - **HW Config** — import hardware configuration
   - **Software Unit** — import a complete V18+ Software Unit (blocks, UDTs, tags) to `Devices/<Category>/<Device>/Units/<UnitName>/`
   - **Languages & resources** — import language settings (`languages.json`) and export project texts to XLSX for translation
4. Files are saved under `TiaExport/Projects/<ProjectName>/Devices/` in your workspace
5. Long-running imports show a time-based progress indicator with percentage, ETA and a numeric `work` counter. Tune the pacing with `tiaImport.importProgress.itemsPerSecond` if your TIA environment is noticeably faster or slower than the default calibration.

### Exporting to TIA Portal

1. Connect to TIA Portal V21
2. In the **VS Code Explorer**, right-click on a file or folder
3. Choose the appropriate export command:
   - **Export Blocks to TIA** — for program blocks (`.xml`, `.scl`, `.s7dcl`, `.db`)
   - **Export Software Unit to TIA Portal** — for a complete Software Unit folder exported from TIA Portal V18+ (`Units/<UnitName>/`)
   - **Export XLSX Tags to TIA Portal** — for XLSX tag tables
   - **Export Project Texts to TIA Portal** — for translated project texts (`.xlsx` under `Languages & resources/`)
   - **Export to TIA - Program and HW** — unified export (program + HW config, incl. `Technology objects`)
   - **Export to TIA - Program without HW** — unified export (program only, incl. `Technology objects`)
   - **Export to TiaPortal: HW Config XML** — hardware configuration
4. Select overwrite mode: *Compare & overwrite changes* or *Force overwrite all*
5. If **Compile after Export** is enabled (`always` or `ask`), the extension compiles PLC software in TIA Portal after a successful export
6. Compile results are shown in the **OUTPUT** panel; errors and warnings appear in the **PROBLEMS** panel with clickable file links

### Viewing local blocks and web previews

Block previews are provided by the companion **[CMsoft Viewer for TiaPortal](https://marketplace.visualstudio.com/items?itemName=MariuszCzyrnek.tia-viewer)** extension: right-click a local SimaticML **XML** block or a **`.s7dcl`** source document to open it in the graphical LAD/FBD/SCL/GRAPH viewer, or right-click a PLC folder and choose **Generate Web Preview** to render a complete offline HTML view of the whole PLC (blocks, data types and tag tables with an `index.html` navigator). No TIA Portal connection is needed — the viewer reads the export files produced by this extension directly.

### Exported Directory Structure

When you connect to TIA Portal (or run the `CMsoft Import for TiaPortal: Prepare Workspace` command), the extension scaffolds the workspace with template files:

```
<Workspace>/
├── .gitignore                        # a section with the TIA-specific ignores
├── CLAUDE.md                         # a section: Claude Code imports .github/instructions/tia-import.instructions.md
├── AGENTS.md                         # a section: open agents.md standard (Cursor / Aider / Codex / Gemini CLI / Jules)
├── .github/
│   ├── copilot-instructions.md       # a section pointing to the instructions below
│   ├── instructions/
│   │   ├── tia-import.instructions.md      # AI coding rules for TIA XML files (all files)
│   │   └── tia-import-cli.instructions.md  # MCP server and CLI bridge (Tools/)
│   ├── ProjectDescription.md         # Living project description (created once)
│   └── Schemas/                      # SimaticML XSD schemas
├── Tools/                            # Utility scripts (README section, tia_cli_example.py, _extractHMI.py, …)
├── UserFiles/                        # Output dir for scripts (git-ignored)
├── TiaExport/
│   ├── .tia-cache/                   # Temporary cache (git-ignored)
│   └── Projects/
│       └── <ProjectName>/
│           ├── Languages & resources/    # languages.json + ProjectTexts_*.xlsx
│           └── Devices/
│               ├── PLCs/
│               │   └── <PLC_Name>/
│               │       ├── DeviceConfiguration/
│               │       │   └── <Device>_HwConfig.xml
│               │       └── <PLC_Software>/
│               │           ├── Program blocks/
│               │           │   ├── Main [OB1].xml
│               │           │   ├── MyFB [FB1].xml
│               │           │   └── SubFolder/
│               │           ├── PLC tags/
│               │           │   └── Default tag table.xlsx
│               │           ├── PLC data types/
│               │           │   └── MyUDT.xml
│               │           ├── Watch and force tables/
│               │           │   └── Watch_1.xml
│               │           └── Technology objects/
│               │               └── PID_Compact_1.xml
│               ├── HMIs/
│               │   └── <HMI_Name>/
│               │       └── <HMI_Software>/
│               │           ├── Screens/
│               │           ├── HMI Tags/
│               │           └── Connections/
│               ├── IO_Devices/
│               │   └── <IO_Device>/
│               │       └── DeviceConfiguration/
│               └── Computers/
```

The template (`Documentation/Templates/`) follows the CMsoft workspace protocol, so the CMsoft add-ons can prepare the same workspace side by side (for example the migrator from MELSEC to TIA Portal next to this extension): each keeps its own files named after it (`.github/instructions/tia-import*.instructions.md`, `Tools/tia_cli_example.py`) and **one section** in `AGENTS.md`, `CLAUDE.md`, `.github/copilot-instructions.md`, `.gitignore` and `Tools/README.md`, between `cmsoft:begin` / `cmsoft:end` markers. Running *Prepare Workspace* again updates this extension's section and files; your own text outside the sections — and a file from which you deleted its `cmsoft:managed` line — is never touched. `ProjectDescription.md`, the schemas and the HMI scripts are only created when missing. Unchanged copies of the templates of earlier versions (`.github/copilot-instructions.md`, `.github/CLI-instruction.md`, `Tools/cli_example.py`, …) are replaced.

`UserFiles/` is always created during workspace preparation, even if the template folder is empty in the packaged extension.

You can also scaffold the workspace manually at any time via `CMsoft Import for TiaPortal: Prepare Workspace` command (available in the Command Palette and in the Connection panel title bar).

### Workspace Templates (`.github/`)

On first connection to TIA Portal (or when you run `CMsoft Import for TiaPortal: Prepare Workspace`), the extension copies template files from `Documentation/Templates/` into your workspace root. The `.github/` directory contains resources that enhance both AI-assisted development and XML validation:

| File / Folder                                 | Purpose                                                                                                                                                                                                                                                                                                                                                                                                                         |
| --------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **`.github/instructions/tia-import.instructions.md`** | Instructions for GitHub Copilot (and other AI assistants) that teach the model how to work with Siemens TIA Portal XML files. Covers SimaticML XML structure,`.s7dcl` / `.s7res` file conventions, MLC ID handling, network titles/comments, and rules for updating `ProjectDescription.md`. Copilot applies them to every file (`applyTo: "**"`); `tia-import-cli.instructions.md` next to it describes the MCP server and the CLI bridge (applied to `Tools/`). |
| **`.github/copilot-instructions.md`** | A section of this extension pointing to the instructions above — next to the sections of the other CMsoft add-ons of the workspace. |
| **`.github/ProjectDescription.md`**   | A living document describing the project's architecture, communication topology, block hierarchy, data structures, and data flow. Created once — it is populated automatically by Copilot when you start analyzing the project (as instructed by `tia-import.instructions.md`). Should be kept up to date when blocks, communication channels, or data structures change. Includes Mermaid diagrams for visual documentation. |
| **`.github/Schemas/`**                | SimaticML XSD schema files (`SW.PlcBlocks.*.xsd`, `SW.Common_v3.xsd`, etc.) copied from `Documentation/Schemas/`. These schemas enable XML validation and IntelliSense for exported TIA Portal block files directly in VS Code.                                                                                                                                                                                           |
| **`.gitignore`**                      | A section with the TIA-specific ignore rules (e.g. `.tia-cache`, `.tia`, `CLAUDE.local.md`, `UserFiles/*`) to keep temporary/cache files out of version control. |
| **`CLAUDE.md`**                       | A section for [Claude Code](https://docs.anthropic.com/claude/docs/claude-code). Uses Claude's native `@<path>` import syntax to import the full ruleset from `.github/instructions/tia-import.instructions.md`, so all AI agents share a single source of truth. Add machine-local notes to `CLAUDE.local.md` (already gitignored). |
| **`AGENTS.md`**                       | A section following the open [agents.md](https://agents.md) standard — read by Cursor, Aider, OpenAI Codex, Gemini CLI, Jules and other AI coding agents. Links to the instructions for the full ruleset and lists the MCP / code-style essentials. |

> **Tip:** Commit the `.github/` directory to your Git repository so that every team member and CI pipeline benefits from the same AI instructions, project documentation, and XML schemas.

---

## Extension Settings

| Setting                                     | Description                                                                                                                                                                                                                                                                                                                                                                              | Default              |
| ------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------- |
| `tiaImport.exportFolderName`              | Folder name for TIA exports                                                                                                                                                                                                                                                                                                                                                              | `TiaExport`        |
| `tiaImport.tiaPortalPath`                 | Path to TIA Portal installation                                                                                                                                                                                                                                                                                                                                                          | `C:\…\Portal V21` |
| `tiaImport.autoConnect`                   | Auto-connect on activation                                                                                                                                                                                                                                                                                                                                                               | `false`            |
| `tiaImport.includeComments`               | Include comments in export                                                                                                                                                                                                                                                                                                                                                               | `true`             |
| `tiaImport.exportFormat`                  | Block export format (`xml` / `sd`)                                                                                                                                                                                                                                                                                                                                                   | `xml`              |
| `tiaImport.tagTableFormat`                | Tag table export format (`xml` / `xlsx`)                                                                                                                                                                                                                                                                                                                                             | `xlsx`             |
| `tiaImport.preserveTimestamps`            | Preserve original timestamps                                                                                                                                                                                                                                                                                                                                                             | `true`             |
| `tiaImport.excludeSystemBlocks`           | Exclude system blocks                                                                                                                                                                                                                                                                                                                                                                    | `true`             |
| `tiaImport.dotnetPath`                    | Path to .NET runtime                                                                                                                                                                                                                                                                                                                                                                     | Auto-detect          |
| `tiaImport.dbExportFormat`                | Global DB export format (`xml` / `db`)                                                                                                                                                                                                                                                                                                                                               | `db`               |
| `tiaImport.udtExportFormat`               | UDT (PLC data type) export format (`udt` / `xml`)                                                                                                                                                                                                                                                                                                                                    | `udt`              |
| `tiaImport.showImportExportDetails`       | Show detailed import/export messages plus wrapper and TIA Openness warnings/errors in the output log                                                                                                                                                                                                                                                                                     | `false`            |
| `tiaImport.importProgress.itemsPerSecond` | Speed multiplier for the time-based import progress model used by project/device/category and category HW Config imports.`1.0` uses the built-in weighted calibration plus a 10% safety buffer; increase it if your TIA exports are faster, decrease it if they are slower.                                                                                                            | `1`                |
| `tiaImport.compileAfterExport`            | Compile PLC software after export (`always` / `ask` / `never`)                                                                                                                                                                                                                                                                                                                     | `ask`              |
| `tiaImport.autoExportCrossReferences`     | Generate cross-reference dump after import (`always` / `ask` / `never`). In `ask` mode the prompt is shown **per PLC** when the dump is about to start and auto-skips after **5 s** if you don't respond. ⚠️ Building the table can take **several minutes — 10 min+ on large PLCs** because TIA Portal computes it itself. Default is therefore `ask`. | `ask`              |

### Block Export Formats

| Format        | Extension                          | Description                                                                                                                                                                                                              |
| ------------- | ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **xml** | `.xml`                           | SimaticML XML — full block data with interface sections, networks, and metadata. Default TIA Portal format.                                                                                                             |
| **sd**  | `.scl` / `.s7dcl` + `.s7res` | SIMATIC Source Documents — auto-selects per programming language: SCL blocks →`.scl` (via `GenerateSource`), LAD/FBD/STL blocks → `.s7dcl` + `.s7res` (via `ExportAsDocuments`). Ideal for version control. |

### Global DB Export Formats

Controlled by `tiaImport.dbExportFormat` (applies only to Global Data Blocks; Instance DBs always use XML):

| Format        | Extension | Description                                                                                                         |
| ------------- | --------- | ------------------------------------------------------------------------------------------------------------------- |
| **xml** | `.xml`  | SimaticML XML — standard TIA Portal format                                                                         |
| **db**  | `.db`   | Text-based`DATA_BLOCK` source via `GenerateSource` API — compact, diff-friendly, importable back to TIA Portal |

### UDT Export Formats

Controlled by `tiaImport.udtExportFormat` (applies to PLC data types):

| Format        | Extension | Description                                                                                                                |
| ------------- | --------- | -------------------------------------------------------------------------------------------------------------------------- |
| **udt** | `.udt`  | Text-based`TYPE ... END_TYPE` source via `GenerateSource` API — compact, diff-friendly, importable back to TIA Portal |
| **xml** | `.xml`  | SimaticML XML — standard TIA Portal format                                                                                |

### Tag Table Export Formats

| Format         | Extension | Description                                                                                                                   |
| -------------- | --------- | ----------------------------------------------------------------------------------------------------------------------------- |
| **xml**  | `.xml`  | SimaticML XML — native TIA Portal format                                                                                     |
| **xlsx** | `.xlsx` | Excel spreadsheet — sheets "Tags" and "Constants", with Siemens-style formatting. Editable in Excel, importable back to TIA. |

---

## Commands

### Import Commands (TIA → local)

| Command                                                     | Description                                                 |
| ----------------------------------------------------------- | ----------------------------------------------------------- |
| `CMsoft Import for TiaPortal: Connect to TIA Portal`                       | Connect / attach to a running TIA Portal instance           |
| `CMsoft Import for TiaPortal: Disconnect from TIA Portal`                  | Disconnect from TIA Portal                                  |
| `CMsoft Import for TiaPortal: Select Project`                              | Select a project from the connected TIA Portal              |
| `CMsoft Import for TiaPortal: Import Entire Project`                       | Import full project structure                               |
| `CMsoft Import for TiaPortal: Refresh Project Structure`                   | Refresh the project tree                                    |
| `CMsoft Import for TiaPortal: Import Device`                               | Import a device with all software                           |
| `CMsoft Import for TiaPortal: Import Block`                                | Import a single block                                       |
| `CMsoft Import for TiaPortal: Import Block Folder`                         | Import a block group/folder                                 |
| `CMsoft Import for TiaPortal: Import Tag Tables`                           | Import all tag tables                                       |
| `CMsoft Import for TiaPortal: Import Tag Table`                            | Import a single tag table                                   |
| `CMsoft Import for TiaPortal: Import Data Types`                           | Import all UDTs                                             |
| `CMsoft Import for TiaPortal: Import Data Type`                            | Import a single UDT                                         |
| `CMsoft Import for TiaPortal: Import Watch Tables`                         | Import all watch tables                                     |
| `CMsoft Import for TiaPortal: Import Watch Table`                          | Import a single watch table                                 |
| `CMsoft Import for TiaPortal: Import Technology Objects`                   | Import all Technology Objects of a device (PID, Motion, …) |
| `CMsoft Import for TiaPortal: Import HMI Screens`                          | Import HMI screens                                          |
| `CMsoft Import for TiaPortal: Import HMI Tags`                             | Import HMI tags                                             |
| `CMsoft Import for TiaPortal: Import HMI Connections`                      | Import HMI connections                                      |
| `CMsoft Import for TiaPortal: Import All HMI Elements`                     | Import all HMI elements                                     |
| `CMsoft Import for TiaPortal: Import HW Configuration`                     | Import full HW configuration                                |
| `CMsoft Import for TiaPortal: Import Device HW Configuration`              | Import HW config for a single device                        |
| `CMsoft Import for TiaPortal: Import Programs for All Devices in Category` | Import all devices in a category                            |
| `CMsoft Import for TiaPortal: Import Languages & Project Texts`            | Import language settings + project texts (xlsx)             |

### Export Commands (local → TIA)

| Command                                     | Description                                        |
| ------------------------------------------- | -------------------------------------------------- |
| `Export Blocks to TIA`                    | Export a block file (XML / SCL / SD) to TIA Portal |
| `Export Blocks to TIA (Folder)`           | Export all blocks in a folder                      |
| `Export to TiaPortal: XML File`           | Export a single XML file (non-block)               |
| `Export to TiaPortal: XML Folder`         | Export an XML folder                               |
| `Export XLSX Tags to TIA Portal`          | Export XLSX tag table to TIA Portal                |
| `Export XLSX Tags to TIA Portal (Folder)` | Export all XLSX tag tables in a folder             |
| `Export Project Texts to TIA Portal`      | Import a project texts xlsx into the TIA project   |
| `Export to TiaPortal: HW Config XML`      | Export HW config (XML/AML)                         |
| `Export to TiaPortal: HW Config Folder`   | Export HW config folder                            |
| `Export to TIA - Program and HW`          | Unified export (program + HW config)               |
| `Export to TIA - Program without HW`      | Unified export (program only, no HW)               |

### Utility Commands

| Command                              | Description                                       |
| ------------------------------------ | ------------------------------------------------- |
| `CMsoft Import for TiaPortal: Show Logs`            | Open the extension output channel                 |
| `CMsoft Import for TiaPortal: Open Settings`        | Open extension settings page                      |
| `CMsoft Import for TiaPortal: Select Export Format` | Switch block export format                        |
| `CMsoft Import for TiaPortal: Format PLC Tags`      | Toggle tag table format (XML/XLSX)                |
| `CMsoft Import for TiaPortal: Prepare Workspace`    | Scaffold workspace (`.github/`, `TiaExport/`) |

---

## How it works

```
VS Code
  └─ CMsoft Import for TiaPortal      the extension and its .NET Framework wrapper, in-process
       └─ TIA Portal Openness API     Siemens.Engineering, installed with TIA Portal
            └─ TIA Portal V17 – V21   on the same computer
```

The extension runs inside VS Code and talks to TIA Portal on the same computer through the official **Siemens TIA Portal Openness API**, loaded in-process by a .NET Framework wrapper that ships with the extension. That is why it works on Windows only and needs the Openness option of TIA Portal and a Windows account in the *Siemens TIA Openness* group.

---

## Documentation

- **User manual — inside the extension.** Installation, setting up TIA Portal Openness, every function with screenshots, a complete worked example with tests, Copilot / MCP / CLI examples, settings, license and troubleshooting. Open it with **CMsoft Import for TiaPortal: Open User Manual** (Command Palette, or the links in the *Get Started* walkthrough and in the empty **Project Structure** view); **CMsoft Import for TiaPortal: Search the User Manual** jumps to a chapter or section; the **CMsoft** status bar item and **Help: CMsoft Manuals…** list it next to the manuals of your other CMsoft add-ons. It works offline: the manual ships in the extension as one Markdown file with its screenshots and opens in VS Code's Markdown preview.
- [TIA Portal Openness API (Siemens)](https://docs.tia.siemens.cloud/r/en-us/v21/tia-portal-openness-api-for-automation-of-engineering-workflows) — official Openness API documentation
- SimaticML XSD schemas for all block types — **Prepare Workspace** copies them into your workspace as `.github/Schemas/` (see *Workspace Templates* above)
- [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) — third-party components and redistribution notes
- [LICENSE.md](LICENSE.md) / [TERMS.md](TERMS.md) / [PRIVACY.md](PRIVACY.md) — license agreement, terms of sale, privacy policy

---

## Third-Party Licensing & Redistribution

- This extension is proprietary commercial software licensed under the [End User License Agreement](LICENSE.md). Versions 3.1.85 and earlier were released under the MIT License and remain MIT-licensed; version 4.0.0 and later are not.
- Redistribution of the extension package by anyone other than the Visual Studio Marketplace and the Open VSX Registry is not permitted.
- Third-party notices for npm/NuGet components are listed in [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md); those components keep their own (open-source) licenses.
- For Siemens Openness components, use and distribution are subject to Siemens package terms; evaluate those terms for your release scenario.
- Do **not** bundle or redistribute `Siemens.Engineering.*` binaries with this extension unless explicitly allowed by Siemens terms.
- End users must provide their own licensed TIA Portal installation and Openness entitlement.

---

## Trademarks

This extension is an independent product. It is **not** developed, endorsed, sponsored by or affiliated with Siemens AG. *TIA Portal*, *SIMATIC*, *STEP 7*, *WinCC* and *Openness* are trademarks or registered trademarks of Siemens AG, used here solely for identification and interoperability purposes; *for TiaPortal* in the name *CMsoft Import for TiaPortal* only states which software the extension works with. *Visual Studio Code* is a trademark of Microsoft Corporation.

---

## Known Issues & Limitations

- **Windows only** — TIA Portal and the Openness API are Windows-only
- **Know-how protected blocks** — cannot be exported; the extension detects and skips placeholder files
- **Windows-forbidden characters in TIA object names** — block, block group, tag table, UDT and watch table names become file/folder names on import, so names containing characters Windows forbids (`\ / : * ? " < > |`) cannot be imported, even though TIA Portal itself allows them. Such items are reported per item in the OUTPUT panel as `... name contains characters not allowed in file names: <name>` and skipped — the rest of the import continues normally. Rename the object in TIA Portal to make it importable.
- **SD format (LAD/FBD)** — only supports LAD/FBD and mixed blocks (no protected blocks)
- **Large projects** — full project import may take several minutes depending on project size

---

## Disclaimer of Liability

The extension is a development and automation tool, and all imports/exports modify engineering data at your own risk.

To the extent permitted by applicable law, the author is not liable for indirect or consequential damages — production downtime, data loss, project corruption or other consequences — resulting from changes made to TIA Portal projects using this extension, and any other liability is limited. Liability that the law does not allow to exclude (for example for damage caused intentionally, or for death or personal injury) and the statutory rights of consumers are not affected.

**You are responsible for all content the extension moves, converts or generates** — program blocks, SCL/LAD/FBD sources, data blocks, UDTs, tag tables, watch tables, technology objects, hardware configuration and project texts — regardless of whether you wrote it, the extension generated it, or an AI assistant (GitHub Copilot, `@tia` chat participant, `tia_*` language model tools, an MCP client) produced it. **AI-generated code is not reviewed or verified by the author.**

Users are fully responsible for validating, testing, and approving all generated or imported changes before deployment to real machines, production lines, or safety-related systems — and for keeping verified project backups before any import, export, synchronisation or PLC download.

These terms are binding as sections 12 (warranty), 13 (liability) and 14 (your content, generated code and safety-critical use) of the [End User License Agreement](LICENSE.md#14-your-content-generated-code-and-safety-critical-use); where this summary and the agreement differ, the agreement applies.

---

## Community — Share Your Scripts & Ideas

This extension ships with a `Tools/` directory for utility scripts and the instructions `.github/instructions/tia-import.instructions.md` that teach AI assistants how to work with TIA Portal projects.

**We encourage you to contribute!** If you have created useful scripts, automation tools, or improvements to the Copilot instructions:

1. **Fork** the [TiaImportExport.VSExt](https://github.com/cmariusz/TiaImportExport.VSExt) repository on GitHub
2. Add your scripts to `Tools/` (with a matching `.md` description)
3. Or propose changes to `.github/instructions/tia-import.instructions.md`
4. **Open a Pull Request** — your contribution will help the entire TIA Portal + VS Code community

Every shared script or instruction improves the experience for all users. Don't hesitate to share even small utilities — they often save the most time!

> By submitting a contribution you confirm that it is your own work and you grant CMsoft a perpetual, worldwide, royalty-free right to use, modify and distribute it as part of this product. Contributions are published under the terms of the [EULA](LICENSE.md); the extension's own source code is not open source.

---

## License

Proprietary commercial software — see the [End User License Agreement](LICENSE.md).
Copyright © 2026 CMsoft. All rights reserved.

**CMsoft** · [office@cmsoft.com.pl](mailto:office@cmsoft.com.pl) · [shop.cmsoft.com.pl](https://shop.cmsoft.com.pl)

| Document                                        | Purpose                                                             |
| ----------------------------------------------- | ------------------------------------------------------------------- |
| [LICENSE.md](LICENSE.md)                         | End User License Agreement (terms of use)                           |
| [TERMS.md](TERMS.md)                             | Terms of sale for paid plans                                        |
| [PRIVACY.md](PRIVACY.md)                         | Privacy policy — no telemetry, no project data leaves your machine |
| [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) | Third-party components and their licenses                           |

**Versions 3.1.85 and earlier** were published under the MIT License. That grant is irrevocable for those versions and is reproduced in section 20 of [LICENSE.md](LICENSE.md). It does not apply to version 4.0.0 or later.
