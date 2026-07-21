# TIA Portal Import — VS Code Extension

<!-- VERSION-BADGE -->
[![Version](https://img.shields.io/badge/version-3.0.123-blue)](package.json)
<!-- /VERSION-BADGE -->

[![VS Code](<https://img.shields.io/badge/VS%20Code-%3E%3D1.80.0-blue?logo=visualstudiocode>)](https://code.visualstudio.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Platform: Windows](https://img.shields.io/badge/Platform-Windows-0078D6?logo=windows)](https://www.microsoft.com/windows)
[![Author](<https://img.shields.io/badge/Author-Mariusz%20Czyrnek-orange?logo=linkedin>)](https://www.linkedin.com/in/mariusz-czyrnek-a33b87a6)
[![Donate with PayPal](https://img.shields.io/badge/Donate-PayPal-00457C?logo=paypal&logoColor=white)](https://www.paypal.com/donate/?hosted_button_id=68KF5N2K5QQVY)

**Bidirectional bridge between VS Code and Siemens TIA Portal** — import PLC/HMI projects from TIA Portal to local files, edit them with full VS Code + Copilot power, and export changes back. Built on the TIA Portal Openness API.

If this extension helps your TIA Portal workflow, you can support ongoing development with a voluntary [PayPal donation](https://www.paypal.com/donate/?hosted_button_id=68KF5N2K5QQVY).

![TIA Portal Import Overview](Screenshots/Overview.png)

---

## Key Features

### Import from TIA Portal (TIA → local files)

| Capability                                 | Description                                                                                                                                                                                                                                                                              |
| ------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Connect to TIA Portal**            | Auto-detect running TIA Portal instances or open a project file (`.ap18` /`.ap19` / `.ap20` / `.ap21`)                                                                                                                                                                          |
| **Import Entire Project**            | Import complete project structure with all devices, blocks, tags, UDTs, and HW config                                                                                                                                                                                                    |
| **Import Devices**                   | Import individual devices or all devices in a category (PLCs, HMIs, IO_Devices, Computers)                                                                                                                                                                                               |
| **Import Program Blocks**            | Import OB, FB, FC, F-FB, F-FC, DB blocks in XML, SCL, SD (`.s7dcl` / `.s7res`), or DB source (`.db`) format                                                                                                                                                                        |
| **Import Tag Tables**                | Import PLC tag tables as SimaticML XML or Excel XLSX spreadsheets                                                                                                                                                                                                                        |
| **Import UDTs**                      | Import PLC data types (user-defined types)                                                                                                                                                                                                                                               |
| **Import Watch Tables**              | Import watch and force tables                                                                                                                                                                                                                                                            |
| **Import HMI**                       | Import HMI screens, tags, and connections                                                                                                                                                                                                                                                |
| **Import HW Config**                 | Import hardware configuration as XML or**CAx / AutomationML (`.aml`)**. Mirrors TIA Portal device folders on disk; root IO devices stay flat in `Devices/IO_Devices/`. Toggle format via *Format HW* in the Connection panel.                                                |
| **Import Project Library**           | Import the**Project Library &gt; Types** tree (FBs, FCs, UDTs, …) — per-type format selection: LAD/FBD/STL → `.s7dcl`/`.s7res` (V20+), SCL → `.scl`, UDT/GRAPH/CFC/SFC/DB → `.xml`. Master copies are intentionally not imported.                                     |
| **Import Languages & Project Texts** | Import project language settings (supported / active / editing / reference languages →`languages.json`) and export project texts (Languages & resources) to XLSX workbooks for translation. V21+ writes one workbook with all target languages; V18–V20 write one per language pair. |
| **Project Explorer**                 | Browse the full TIA Portal project hierarchy in the VS Code sidebar                                                                                                                                                                                                                      |

> **HW Config folder layout:** `Import HW Config` mirrors TIA Portal folder structure on disk. Devices at the project root use `Devices/<Category>/<Device>/DeviceConfiguration/`, except root IO devices which keep the legacy flat `Devices/IO_Devices/` layout. Devices placed inside TIA Portal device folders are exported under `Devices/<Category>/<FolderPath>/<Device>/DeviceConfiguration/`.

### Local SimaticML Preview

| Capability                                          | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| --------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Graphical LAD / FBD viewer**                | Render local SimaticML XML program blocks as**interactive LAD or FBD network diagrams** directly in a VS Code panel — no TIA Portal connection required, no manual screenshots. Powered by the installed SIMATIC Automation Compare Tool renderer, embedded inside the editor and themed for the active VS Code color theme (dark and light). Each network is shown as it appears in TIA Portal, with full operand names (truncated labels like `#ManMs…gToRun` are automatically expanded to the full `#ManMsgL1ToL2.oCountMsgToRun`).                                                                                                |
| **Automation Compare Tool preview**           | Open local SimaticML XML code blocks, DBs, PLC tag tables and UDTs in a VS Code preview panel powered by the installed Siemens SIMATIC Automation Compare Tool renderer. External ACT launch remains available as a fallback setting.                                                                                                                                                                                                                                                                                                                                                                                                              |
| **Per-network XML operations in ACT preview** | Right-click any network in the embedded ACT preview to act directly on the underlying SimaticML XML:**Open XML in network *N*** jumps the source `.xml` to the matching `<SW.Blocks.CompileUnit>` for fast inspection / hand-edit, **Clear logic in network *N*** empties just that network's `<NetworkSource>` (preserving title, comment and programming language) so the block can be re-imported as a clean stub, and **Remove network *N*** deletes the whole CompileUnit. Edits are text-based (no XML reformatting) so `git diff` stays small and the file stays round-trippable through TIA Portal Import. |
| **Git revision diff in ACT**                  | Compare a local`.xml` block or `.s7dcl` SD block against another Git revision in the same embedded ACT webview. The command materializes the selected revisions to a temporary folder, resolves `.s7dcl` files through their `.tiaPreview/*.xml` mirrors, and opens a graphical side-by-side ACT diff inside VS Code.                                                                                                                                                                                                                                                                                                                      |

### Export to TIA Portal (local files → TIA)

| Capability                           | Description                                                                                                                                                                                       |
| ------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Export Blocks**              | Export XML / SCL / SD / DB source files back to TIA Portal                                                                                                                                        |
| **Export Software Unit**       | Export a complete V18+ Software Unit folder (`Units/<UnitName>/{Program blocks, PLC data types, PLC tags}`) back to TIA Portal; creates the unit if missing and applies `_unit.json` metadata |
| **Export Tag Tables**          | Export XML or XLSX tag tables to TIA Portal                                                                                                                                                       |
| **Export Project Texts**       | Push a translated project texts XLSX back into the same TIA project (Languages & resources), with optional source-language update                                                                 |
| **Export UDTs / Watch Tables** | Export data types and watch tables                                                                                                                                                                |
| **Export HW Config**           | Export hardware configuration as XML or**CAx / AutomationML (`.aml`)** via `CaxProvider`                                                                                                |
| **Unified Export**             | One-click export of an entire device folder in dependency order (UDTs → Blocks → Tags → Watch Tables → HW)                                                                                    |
| **Smart Comparison**           | Only overwrite items that actually changed (normalized XML diff; Instance DBs compared by StartValues only)                                                                                       |
| **Orphan Cleanup**             | Auto-delete blocks, groups, tag tables, and UDTs in TIA that no longer exist locally                                                                                                              |
| **Dependency Ordering**        | Files sorted automatically: UDT → FB → FC → OB → GlobalDB → InstanceDB                                                                                                                       |
| **Compile after Export**       | Automatically compile PLC software in TIA Portal after export — configurable: Always / Ask / Never                                                                                               |
| **Compile Error Tracking**     | Compile results mapped to VS Code PROBLEMS panel with file and line resolution (network / SCL line mapping)                                                                                       |

### Smart Capabilities

- **Connection health monitoring** — automatic ping-based checks with auto-disconnect on broken connections
- **Know-how protected block detection** — detects and skips placeholder files for protected blocks
- **Instance DB creation** — creates Instance DBs directly via API (no XML import needed)
- **Cancellation support** — cancel long-running operations via VS Code progress UI
- **Status bar** — real-time connection state and project info
- **Time-based import progress** — long-running project, device, device-category, and category HW Config imports show a live numeric percentage, weighted work counter, and ETA in both the notification progress UI and the status bar; block imports are weighted by export type (SD, SCL/DB source, XML, ACT XML preview, UDTs, tag/watch tables) and category HW Config imports are weighted per device with a small safety buffer so very large TIA exports do not look stalled
- **Compile after export** — optional PLC software compilation in TIA Portal after each export (Always / Ask / Never); results shown in OUTPUT panel
- **Compile error tracking** — compile errors and warnings mapped to VS Code PROBLEMS panel with automatic file matching, network-to-line resolution (XML, S7DCL, SCL), and direct navigation to the error location

### Copilot / AI Agent Integration

The extension exposes **25 Language Model Tools** (prefix `tia_`) plus a `@tia` chat participant, so GitHub Copilot (and any other VS Code LM-tool consumer) can drive TIA Portal end-to-end without manual clicks:

- **Connection / discovery** — `tia_connect`, `tia_disconnect`, `tia_list_projects`, `tia_select_project`, `tia_refresh`, `tia_list_devices`, `tia_list_blocks`
- **Pull from TIA → workspace** — `tia_export_block`, `tia_export_device`, `tia_export_project` (entire project), `tia_export_hw_config` (per-device or project-wide HW Config; honours `tiaImport.hwConfigFormat`)
- **Push workspace → TIA** — `tia_import_file`, `tia_import_folder` (blocks, tags, UDTs, watch tables), `tia_import_unit` (complete Software Unit), `tia_import_hw_config` (HW Config XML/AML — required for HW; `tia_import_file` does not handle HW)
- **Languages & project texts** — `tia_get_project_languages` (language settings), `tia_export_project_texts` (project texts to xlsx for translation), `tia_import_project_texts` (re-import translated xlsx into the same project)
- **Compile loop** — `tia_compile`, `tia_get_problems`, `tia_fix_compile_errors` (orchestrates import → compile → diagnostics until clean or `tiaImport.lmTools.maxFixIterations` is reached)
- **Analysis** — `tia_export_cross_references` (full PLC cross-reference dump to JSONL/CSV, including unused symbols)

Imports that overwrite existing TIA objects show a confirmation dialog unless `tiaImport.lmTools.autoConfirmImports` is enabled. The chat participant `@tia` is registered as `tia.assistant` and has the same toolset available.

### External CLI Bridge

External scripts can drive the same TIA workflows through a localhost-only JSON bridge.

**The bridge is opt-in and disabled by default** — no listener is started and no `.tia/` folder is created until you enable it. Turn it on in any of these ways:

- Click the **CLI Bridge** row in the *TIA Connection* view (toggles between `Off` / `On`).
- Click the **terminal** icon (*TIA Import: Start CLI Bridge*) in the *TIA Connection* view title bar — you will be prompted to enable it.
- Set `tiaImport.cli.enabled` to `true` in VS Code Settings.

Once enabled, the extension writes `.tia/cli.json` in the workspace with the current host, port and per-session bearer token. Scripts must read that file at runtime and send authenticated `POST /api` requests. Do not hard-code or commit the token. Toggling the setting off stops the listener and removes the state file.

The packaged helper wraps the bridge:

```powershell
npm run tia:cli -- current_project --pretty
npm run tia:cli -- open_project --filePath "C:\Projects\Demo.ap21" --pretty
npm run tia:cli -- import_blocks --device PLC_1 --blocks FB10,FC20 --pretty
npm run tia:cli -- import_file --device PLC_1 --filePath "C:\Projects\Demo\Block.xml" --overwriteExisting true
```

Use `import_blocks` / `tia_import_blocks` to pull blocks from TIA Portal into the workspace; it honours the configured block formats (`tiaImport.exportFormat`, `tiaImport.dbExportFormat`) and SD preview mirror behavior. Use `import_file`, `import_folder` and `import_hw_config` when pushing local files back into TIA Portal.

---

## Requirements

| Requirement          | Version                                    |
| -------------------- | ------------------------------------------ |
| **OS**         | Windows 10 / 11                            |
| **TIA Portal** | V18, V19, V20 or V21 with Openness license |
| **.NET**       | .NET 8.0 Runtime                           |
| **VS Code**    | ≥ 1.80.0                                  |
| **Node.js**    | 20+ (for building / packaging only)        |

**SIMATIC Automation Compare Tool (ACT)** is optional and must be installed separately from Siemens Support when you want graphical local XML previews or Git revision diffs. The extension does not bundle ACT.

👉 Download: [SIMATIC Automation Compare Tool — Siemens Support (109797235)](https://support.industry.siemens.com/cs/document/109797235/simatic-automation-compare-tool-?dti=0&lc=en-PL)

> A single VSIX supports **TIA Portal V18, V19, V20 and V21** — pick the active version via the **TIA Portal** entry at the top of the Connection panel (or the `tiaImport.tiaPortalVersion` setting). Newer Openness features degrade gracefully on older versions:
>
> - **SD format** (`.s7dcl` / `.s7res`) requires **V20+**. On V18/V19 the extension automatically falls back to XML for LAD/FBD/STL blocks; SCL blocks continue to export as `.scl`.
> - **Cross-reference dump** (`tia_export_cross_references`) requires **V18+**. **Heads-up:** building a full cross-reference table is performed by TIA Portal itself and can take **several minutes — sometimes 10 min+ on large PLCs** (thousands of blocks, large fault-tolerant projects). Progress is logged line-by-line in the *TIA Portal Import* output channel; the operation is non-blocking, so other imports/compiles continue normally.
> - **CAx / AutomationML HW Config** is available on all supported versions.
>
> The Windows user running VS Code must be a member of the **Siemens TIA Openness** user group. See [Adding users to the Siemens TIA Openness user group](https://docs.tia.siemens.cloud/r/en-us/v20/tia-portal-openness-api-for-automation-of-engineering-workflows/basics/installation/adding-users-to-the-siemens-tia-openness-user-group) for details.

---

## Installation

1. Install the extension from VS Code Marketplace (or `code --install-extension mariusz-czyrnek.tia-import`)
2. Make sure TIA Portal is installed with an Openness license
3. Make sure end users of your distributed package also have their own valid TIA Portal + Openness license
4. Optionally adjust settings via **File → Preferences → Settings → TIA Portal Import**

---

## Usage

### Connecting to TIA Portal

1. Start TIA Portal and open a project
2. Open VS Code in a workspace folder
3. Click the **TIA Portal** icon in the Activity Bar
4. Click **Connect to TIA Portal** or run the command `TIA Import: Connect to TIA Portal`
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
   - **Export to TIA - Program and HW** — unified export (program + HW config)
   - **Export to TIA - Program without HW** — unified export (program only)
   - **Export to TiaPortal: HW Config XML** — hardware configuration
4. Select overwrite mode: *Compare & overwrite changes* or *Force overwrite all*
5. If **Compile after Export** is enabled (`always` or `ask`), the extension compiles PLC software in TIA Portal after a successful export
6. Compile results are shown in the **OUTPUT** panel; errors and warnings appear in the **PROBLEMS** panel with clickable file links

### Previewing local SimaticML XML

1. **Install SIMATIC Automation Compare Tool** separately — download it from Siemens Industry Support: [SIMATIC Automation Compare Tool (109797235)](https://support.industry.siemens.com/cs/document/109797235/simatic-automation-compare-tool-?dti=0&lc=en-PL). The extension does not bundle ACT.
2. Leave `tiaImport.automationCompareTool.autoDetect` enabled, or set `tiaImport.automationCompareTool.path` to the ACT executable.
3. In VS Code Explorer, right-click a local SimaticML XML file supported by ACT: code block, DB, PLC tag table or UDT.
4. Choose **TIA Import: Preview XML with Automation Compare Tool**.

The preview command is contributed only to the Explorer right-click menu and does not require a TIA Portal connection. It validates the selected file before the ACT renderer starts; SCL, SD, DB source, hardware config XML, watch/force tables, unknown XML and know-how protected placeholders are rejected with a message. By default `tiaImport.automationCompareTool.embedMode` opens the installed ACT renderer in a VS Code webview panel that **follows the active VS Code color theme** (sidebar, tables, tabs, LAD/FBD diagram canvas and block bodies are repainted in dark mode for readability) and **expands truncated operand labels** in LAD/FBD networks (e.g. `#ManMs…gToRun` becomes the full `#ManMsgL1ToL2.oCountMsgToRun`). Set it to `external` when you want ACT to launch in its own native window. In external mode, `tiaImport.automationCompareTool.argumentsTemplate` follows ACT's documented command line syntax and supports `${file}` plus `${title}`, for example `--uiCulture=en-US --title1 "${title}" "${file}"`.

### Comparing Git revisions in ACT

1. Install SIMATIC Automation Compare Tool and keep `tiaImport.automationCompareTool.embedMode` set to `native` for the in-editor experience.
2. In VS Code Explorer, right-click a supported local `.xml` SimaticML file or a `.s7dcl` SD block.
3. Choose **TIA Import: Compare with Git Revision in ACT**.
4. Pick the left and right revisions from the working tree plus recent Git history.

The diff opens in the same embedded ACT webview used by the single-file preview, so LAD/FBD network changes stay graphical and reviewable inside VS Code. For `.s7dcl` files the command compares the generated `.tiaPreview/*.xml` mirror; commit that mirror together with the SD files if you want historical `.s7dcl` revisions to be available. If the embedded renderer cannot be loaded, or when `tiaImport.automationCompareTool.embedMode` is set to `external`, the command falls back to launching ACT externally with `tiaImport.automationCompareTool.compareArgumentsTemplate` (`${file1}`, `${file2}`, `${title1}`, `${title2}`).

### Exported Directory Structure

When you connect to TIA Portal (or run the `TIA Import: Prepare Workspace` command), the extension scaffolds the workspace with template files:

```
<Workspace>/
├── .gitignore                        # TIA-specific ignores (from template)
├── CLAUDE.md                         # Claude Code instructions (re-exports .github/copilot-instructions.md)
├── AGENTS.md                         # Open agents.md standard (Cursor / Aider / Codex / Gemini CLI / Jules)
├── .github/
│   ├── copilot-instructions.md       # AI coding rules for TIA XML files
│   ├── ProjectDescription.md         # Auto-generated project description
│   └── Schemas/                      # SimaticML XSD schemas
├── Tools/                            # Utility scripts (Python, PS, etc.)
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
│               │           └── Watch and force tables/
│               │               └── Watch_1.xml
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

Template files (`.gitignore`, `.github/`) are only created if they don't already exist — existing files are never overwritten. Templates are maintained in `Documentation/Templates/`.

`UserFiles/` is always created during workspace preparation, even if the template folder is empty in the packaged extension.

You can also scaffold the workspace manually at any time via `TIA Import: Prepare Workspace` command (available in the Command Palette and in the Connection panel title bar).

### Workspace Templates (`.github/`)

On first connection to TIA Portal (or when you run `TIA Import: Prepare Workspace`), the extension copies template files from `Documentation/Templates/` into your workspace root. The `.github/` directory contains resources that enhance both AI-assisted development and XML validation:

| File / Folder                                 | Purpose                                                                                                                                                                                                                                                                                                                                                                                                                         |
| --------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **`.github/copilot-instructions.md`** | Instructions for GitHub Copilot (and other AI assistants) that teach the model how to work with Siemens TIA Portal XML files. Covers SimaticML XML structure,`.s7dcl` / `.s7res` file conventions, MLC ID handling, network titles/comments, and rules for updating `ProjectDescription.md`. These instructions are automatically picked up by Copilot in VS Code.                                                        |
| **`.github/ProjectDescription.md`**   | A living document describing the project's architecture, communication topology, block hierarchy, data structures, and data flow. Initially empty — it is populated automatically by Copilot when you start analyzing the project (as instructed by`copilot-instructions.md`). Should be kept up to date when blocks, communication channels, or data structures change. Includes Mermaid diagrams for visual documentation. |
| **`.github/Schemas/`**                | SimaticML XSD schema files (`SW.PlcBlocks.*.xsd`, `SW.Common_v3.xsd`, etc.) copied from `Documentation/Schemas/`. These schemas enable XML validation and IntelliSense for exported TIA Portal block files directly in VS Code.                                                                                                                                                                                           |
| **`.gitignore`**                      | TIA-specific ignore rules (e.g.`.tia-cache`, `CLAUDE.local.md`) to keep temporary/cache files out of version control.                                                                                                                                                                                                                                                                                                       |
| **`CLAUDE.md`**                       | Instructions for[Claude Code](https://docs.anthropic.com/claude/docs/claude-code). Uses Claude's native `@<path>` import syntax to re-export the full ruleset from `.github/copilot-instructions.md`, so all AI agents share a single source of truth. Add machine-local notes to `CLAUDE.local.md` (already gitignored).                                                                                                  |
| **`AGENTS.md`**                       | Follows the open[agents.md](https://agents.md) standard — read by Cursor, Aider, OpenAI Codex, Gemini CLI, Jules and other AI coding agents. Links to `.github/copilot-instructions.md` for the full ruleset and lists build / test / code-style essentials.                                                                                                                                                                  |

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

### Tag Table Export Formats

| Format         | Extension | Description                                                                                                                   |
| -------------- | --------- | ----------------------------------------------------------------------------------------------------------------------------- |
| **xml**  | `.xml`  | SimaticML XML — native TIA Portal format                                                                                     |
| **xlsx** | `.xlsx` | Excel spreadsheet — sheets "Tags" and "Constants", with Siemens-style formatting. Editable in Excel, importable back to TIA. |

---

## Commands

### Import Commands (TIA → local)

| Command                                                     | Description                                       |
| ----------------------------------------------------------- | ------------------------------------------------- |
| `TIA Import: Connect to TIA Portal`                       | Connect / attach to a running TIA Portal instance |
| `TIA Import: Disconnect from TIA Portal`                  | Disconnect from TIA Portal                        |
| `TIA Import: Select Project`                              | Select a project from the connected TIA Portal    |
| `TIA Import: Import Entire Project`                       | Import full project structure                     |
| `TIA Import: Refresh Project Structure`                   | Refresh the project tree                          |
| `TIA Import: Import Device`                               | Import a device with all software                 |
| `TIA Import: Import Block`                                | Import a single block                             |
| `TIA Import: Import Block Folder`                         | Import a block group/folder                       |
| `TIA Import: Import Tag Tables`                           | Import all tag tables                             |
| `TIA Import: Import Tag Table`                            | Import a single tag table                         |
| `TIA Import: Import Data Types`                           | Import all UDTs                                   |
| `TIA Import: Import Data Type`                            | Import a single UDT                               |
| `TIA Import: Import Watch Tables`                         | Import all watch tables                           |
| `TIA Import: Import Watch Table`                          | Import a single watch table                       |
| `TIA Import: Import HMI Screens`                          | Import HMI screens                                |
| `TIA Import: Import HMI Tags`                             | Import HMI tags                                   |
| `TIA Import: Import HMI Connections`                      | Import HMI connections                            |
| `TIA Import: Import All HMI Elements`                     | Import all HMI elements                           |
| `TIA Import: Import HW Configuration`                     | Import full HW configuration                      |
| `TIA Import: Import Device HW Configuration`              | Import HW config for a single device              |
| `TIA Import: Import Programs for All Devices in Category` | Import all devices in a category                  |
| `TIA Import: Import Languages & Project Texts`            | Import language settings + project texts (xlsx)   |

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
| `TIA Import: Show Logs`            | Open the extension output channel                 |
| `TIA Import: Open Settings`        | Open extension settings page                      |
| `TIA Import: Select Export Format` | Switch block export format                        |
| `TIA Import: Format PLC Tags`      | Toggle tag table format (XML/XLSX)                |
| `TIA Import: Prepare Workspace`    | Scaffold workspace (`.github/`, `TiaExport/`) |

---

## Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                       VS Code Extension                     │
│                                                             │
│  ┌────────────┐  ┌─────────────┐  ┌───────────────────────┐│
│  │  Commands   │  │  Providers  │  │       Utilities       ││
│  │ (import/    │  │ (tree view, │  │ (logger, config,      ││
│  │  export)    │  │  connection)│  │  statusBar, workspace)││
│  └──────┬─────┘  └──────┬──────┘  └───────────────────────┘│
│         │               │                                   │
│  ┌──────▼───────────────▼──────────────────────────────────┐│
│  │              Services Layer                             ││
│  │  tiaConnection · projectImport · tiaOpennessBridge      ││
│  │  blockImport · tagTableImport · udtImport               ││
│  │  watchTableImport · hmiImport                           ││
│  └──────────────────────┬──────────────────────────────────┘│
│                         │  electron-edge-js                 │
└─────────────────────────┼───────────────────────────────────┘
                          │
┌─────────────────────────▼───────────────────────────────────┐
│                  .NET Wrapper (C#)                           │
│                                                             │
│  TiaConnector.cs ─► TiaPortalService.cs                     │
│                         │                                   │
│  ┌──────────────────────┼──────────────────────────────┐    │
│  │  Services/Export/                                   │    │
│  │   Software: BlockExportHandler, TagTableExport,     │    │
│  │     UdtExport, WatchTableExport, SdExportHandler,   │    │
│  │     SclExportHandler, XmlComparisonService           │    │
│  │   HW: HwConfigExportToTia, DeviceExportHelper       │    │
│  ├──────────────────────────────────────────────────────┤    │
│  │  Services/Import/                                   │    │
│  │   Software: BlockImport, TagTableImport, UdtImport, │    │
│  │     WatchTableImport, HmiImport, TagTableXlsx       │    │
│  │   HW: HwConfigImport, DeviceItemHelper              │    │
│  └──────────────────────────────────────────────────────┘    │
│                         │                                   │
│              Siemens.Engineering.dll (TIA Openness API)      │
└─────────────────────────────────────────────────────────────┘
```

The extension uses **electron-edge-js** to call the .NET `TiaOpennessWrapper.dll` in-process from Node.js. The wrapper communicates with TIA Portal via the official **Siemens TIA Portal Openness API** (`Siemens.Engineering` assemblies).

---

## Documentation

- [TIA Portal Openness API (Siemens)](https://docs.tia.siemens.cloud/r/en-us/v21/tia-portal-openness-api-for-automation-of-engineering-workflows) — official Openness API documentation
- [Documentation/API/](Documentation/API/) — XML intellisense files for the Openness API
- [Documentation/Schemas/](Documentation/Schemas/) — SimaticML XSD schemas for all block types
- [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) — third-party components and redistribution notes

---

## Third-Party Licensing & Redistribution

- This extension code is released under [MIT](LICENSE).
- Third-party notices for npm/NuGet components are listed in [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).
- For Siemens Openness components, use and distribution are subject to Siemens package terms; evaluate those terms for your release scenario.
- Do **not** bundle or redistribute `Siemens.Engineering.*` binaries with this extension unless explicitly allowed by Siemens terms.
- End users must provide their own licensed TIA Portal installation and Openness entitlement.

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

The author is not liable for any direct or indirect damages, production downtime, data loss, project corruption, safety incidents, or other consequences resulting from changes made to TIA Portal projects using this extension.

Users are fully responsible for validating, testing, and approving all generated or imported changes before deployment to real machines, production lines, or safety-related systems.

---

## Community — Share Your Scripts & Ideas

This extension ships with a `Tools/` directory for utility scripts and a `copilot-instructions.md` file that teaches AI assistants how to work with TIA Portal projects.

**We encourage you to contribute!** If you have created useful scripts, automation tools, or improvements to the Copilot instructions:

1. **Fork** the [TiaImportExport.VSExt](https://github.com/cmariusz/TiaImportExport.VSExt) repository on GitHub
2. Add your scripts to `Tools/` (with a matching `.md` description)
3. Or propose changes to `.github/copilot-instructions.md`
4. **Open a Pull Request** — your contribution will help the entire TIA Portal + VS Code community

Every shared script or instruction improves the experience for all users. Don't hesitate to share even small utilities — they often save the most time!

---

## License

[MIT](LICENSE) — Copyright (c) 2026 Mariusz Czyrnek
