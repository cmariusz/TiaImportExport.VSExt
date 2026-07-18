# Change Log

All notable changes to the **TIA Portal Import** extension will be documented in this file.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.0.0/) and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [3.0.103] - 2026-07-18

### Added

- **Languages & resources support** — new `Languages & resources` node in the Project Explorer with inline icons and right-click actions for project languages and project texts:
  - **Import Languages & Project Texts from TIA** — reads the project language settings (supported / active languages, editing and reference language) into `languages.json` and exports project texts to `Projects/<Project>/Languages & resources/` as Excel workbooks ready for translation. On TIA Portal V21+ a single `ProjectTexts_<source>.xlsx` with all target languages is written; on V18–V20 one workbook per source-target language pair is produced (older Openness API exposes only the pairwise export overload).
  - **Export Project Texts to TIA Portal** — pushes a (translated) project texts workbook back into the same TIA project, with an optional source-language update. Available from the tree node, from the VS Code Explorer context menu on `.xlsx` files under `Languages & resources/`, and via the Command Palette. As in the TIA Portal UI, texts can only be re-imported into the project they were exported from.
- **Copilot tools for languages & project texts** — three new Language Model Tools (25 total): `tia_get_project_languages` (read language settings), `tia_export_project_texts` (project texts to xlsx) and `tia_import_project_texts` (xlsx re-import with user confirmation). The CLI bridge mirrors them as `get_project_languages`, `export_project_texts` and `import_project_texts`.

## [3.0.97] - 2026-07-18

### Fixed

- **Project selection crash with `EngineeringObjectDisposedException` (TIA Portal V19)** — "Connect to TIA Portal" auto-selection could fail on large/deep hardware configurations after ~30 s, even though TIA Portal kept running ([issue #5](https://github.com/cmariusz/TiaImportExport.VSExt/issues/5)). `ProjectStructureBuilder.BuildDeviceStructure` walked the `DeviceItems` tree three separate times while holding live Openness enumerators open across recursion and per-node IPC calls (`GetService`/`GetAttribute`), so TIA Portal could recycle the enumerator session mid-walk. The device tree is now scanned in a single pass with every level materialized (`ToList()`), and PLC/HMI software structures are built only after the walk finishes, so no device-item enumerator stays open while block/tag enumerations run. This also cuts most of the redundant IPC round-trips during project selection.
- **Automatic retry when TIA Portal recycles an Openness session** — `TiaConnectionManager` now catches `EngineeringObjectDisposedException` while building the project structure, re-fetches the project and retries (up to 3 attempts) before failing, in both `SelectProjectAsync` and `OpenProjectFromPath`.

### Thanks

- Special thanks to [@KaiserFranz-98](https://github.com/KaiserFranz-98) for the outstanding bug report in [issue #5](https://github.com/cmariusz/TiaImportExport.VSExt/issues/5) — complete with a full stack trace, timing analysis, an accurate suspected root cause and a suggested fix. Reports of this quality make debugging a pleasure.

## [3.0.63] - 2026-07-07

### Fixed

- **HMI screen export error reporting** — WinCC Unified devices that cannot be exported through the TIA Portal Openness API now return a clear error message instead of being silently skipped with an empty error dialog.
- **Empty error message in "Import HMI screens" command** — `importHmiScreensCommand` now falls back to the first detailed message from the .NET wrapper when `result.error` is blank, so the user sees why the import failed.

### Changed

- **WinCC Unified screen export fallback** — `ExportUnifiedScreen` now attempts the classic `Screen.Export(FileInfo, ExportOptions)` method via reflection before trying directory-based export variants. This aligns the Unified path with the official Siemens Openness example for classic HMI panels when the runtime type supports it.

## [3.0.56] - 2026-06-22

### Fixed

- **HW Config export path for devices inside TIA Portal folders** — importing hardware configuration for PLCs, HMIs and IO devices placed in TIA Portal device folders now writes files to the correct mirrored workspace path: `Devices/<Category>/<FolderPath>/<Device>/DeviceConfiguration`. Previously foldered PLCs landed directly under `Devices/<Category>/<Device>/DeviceConfiguration` because the TypeScript callers ignored `folderPath`.
- **TIA folder structure for IO devices** — IO devices inside TIA Portal folders are now exported with their folder hierarchy preserved (`Devices/IO_Devices/<FolderPath>/<Device>/DeviceConfiguration`) instead of being flattened into `Devices/IO_Devices/`. Root IO devices still use the legacy flat layout for backward compatibility.

### Changed

- **Unified HW Config path builder** — all HW Config import callers now use the shared `buildDeviceHwConfigPath` helper, which centralizes the decision between legacy flat IO layout and per-device folder-mirrored layout.

## [3.0.46] - 2026-06-22

### Added

- **Export complete Software Unit to TIA Portal** — right-click a `Units/<UnitName>/` folder in VS Code Explorer and choose **Export Software Unit to TIA Portal** to push the entire unit back to TIA Portal V18+. The command reads `_unit.json`, creates the Software Unit if it does not exist, applies metadata (`author`, `comment`, `namespacePreset`), imports `Program blocks`, `PLC data types` and `PLC tags`, and cleans up orphaned items that no longer exist locally.
- **Software Unit export Copilot tool** — new Language Model Tool `tia_import_unit` lets Copilot push a complete Software Unit folder into TIA Portal in one call. The folder path is optional and auto-detected when the workspace contains a single unit export.

### Fixed

- **CLI Bridge toggle respects workspace settings** — `TIA Import: Toggle CLI Bridge` now flips `tiaImport.cli.enabled` at the same configuration level where it is currently defined (workspace or global), so the On/Off state in the Connection panel updates correctly even when the setting is overridden in workspace settings.
- **ACT preview mirror for Software Units** — importing Software Units with `tiaImport.exportFormat` set to `sd` now writes the parallel XML preview mirror into `Units/<UnitName>/.tiaPreview/Program blocks/...` instead of the device-level `.tiaPreview` folder. `findPreviewXmlForS7dcl` resolves unit paths correctly so the Automation Compare Tool can open LAD/FBD block previews inside Software Units. Fixed a bridge issue where the `s7dclPreviewXmlEnabled` flag was not passed to the .NET export call.
- **Software Unit tag table format** — `tiaImport.tagTableFormat` is now honored when exporting Software Units. When set to `xlsx`, tag tables inside `Units/<UnitName>/PLC tags/` are exported as `.xlsx` (XML sources are removed), matching the behavior for device-level tag tables.
- **Devices inside TIA Portal folders** — PLC/HMI/IO devices placed inside device folders are now discovered, displayed in the Project Structure tree under their folder path, and can be imported/exported. Device exports on disk follow the folder hierarchy: `Devices/<Category>/<FolderPath>/<Device>`. `FindDevice` resolves devices regardless of whether they are at the project root or inside a `DeviceGroup`.
- **Per-device HW Config for foldered PLCs** — `ImportDeviceHwConfig` now uses the shared `IDeviceLocator`, so it can resolve PLCs inside `DeviceGroups`. It also exports only the selected device instead of falling back to a project-wide HW Config export.

## [3.0.11] - 2026-06-17

### Changed

- **CLI bridge is now opt-in** — `tiaImport.cli.enabled` defaults to `false`. The localhost JSON listener no longer starts on activation and no `.tia/cli.json` state file is created until the user explicitly enables it. The setting is now hot-reloadable: toggling it on starts the bridge immediately and toggling it off stops the listener and removes the state file.

### Added

- **CLI Bridge toggle in the TIA Connection view** — a new `CLI Bridge On/Off` row sits next to *TIA Portal Vxx* / *Log Details*. Clicking it (or running `TIA Import: Toggle CLI Bridge`) flips `tiaImport.cli.enabled` without opening Settings.
- **Start CLI Bridge action in the view title bar** — the terminal icon (`TIA Import: Start CLI Bridge`) is visible on the Connection view before connecting to TIA Portal. When the bridge is disabled, it shows an info prompt with **Enable now** / **Open Settings** actions; when enabled, it confirms the bridge is running.
- **Friendly guidance when the bridge is off** — external scripts that try to use the bridge while it's disabled still get the existing `.tia/cli.json not found` error pointing them at `tiaImport.cli.enabled`; users invoking the action from the palette now get an actionable dialog instead of a silent no-op.
- **ACT preview: per-network XML actions** — right-clicking a network in the embedded Automation Compare Tool preview now exposes new actions on the underlying SimaticML XML:
  - **Open XML in network *N*** opens the source `.xml` file and jumps the editor to the matching `<SW.Blocks.CompileUnit>` (the Nth network in document order), so the user can inspect or hand-edit that exact network without scrolling.
  - **Clear logic in network *N*** replaces only the `<NetworkSource>...</NetworkSource>` body of the selected network with a self-closing `<NetworkSource />`, preserving the network envelope (title, comment, programming language). The preview refreshes in-place after the file is saved. Useful for producing clean stubs before re-import to TIA Portal.
  - These actions live alongside the existing **Remove network *N***. All three editors are text-based (they do not re-serialize the document through a generic XML library), so unrelated formatting is preserved and `git diff` review and TIA Portal round-trips stay clean.

## [3.0.0] - 2026-06-10

Major version bump for the external automation CLI bridge and script-driven TIA Portal workflows.

### Added

- **Local JSON CLI bridge for external scripts** — the extension can now expose a localhost-only authenticated API for PowerShell, Python, Node.js and other automation clients. When `tiaImport.cli.enabled` is true, the bridge writes the active host, port and per-session token to `.tia/cli.json`; clients call `POST /api` with `Authorization: Bearer <token>`. The packaged helper is available as `npm run tia:cli -- <command>`.
- **Headless project open from CLI** — `open_project --filePath "C:\Projects\Demo.ap21"` opens a TIA Portal project directly by path without showing the project picker, then refreshes the extension model for subsequent CLI operations.
- **CLI-friendly project and diagnostics commands** — external scripts can now call `current_project`, `prepare_workspace`, `get_logs`, `connect`, `disconnect` / `close_project`, device/block discovery, import/export, compile, diagnostics and cross-reference commands through the same bridge.
- **Example Python automation client** — `Documentation/Templates/Tools/cli_example.py` demonstrates reading `.tia/cli.json`, authenticating against the bridge and driving project export from an external script.

### Changed

- **CLI block import honours extension file-format settings** — `import_blocks` / `tia_import_blocks` now pulls selected blocks, or all blocks from a device, using the configured `tiaImport.exportFormat`, `tiaImport.dbExportFormat` and SD preview mirror behavior instead of forcing XML. `import_file` and `import_folder` remain the workspace-to-TIA push commands.
- **CLI documentation and workspace templates refreshed** — README, generated CLI instructions and Copilot workspace instructions now describe the bridge state file, authentication model, command aliases and the distinction between pulling blocks from TIA and pushing local files back to TIA.
- **Native dependency detection hardened for modern VS Code/Electron** — the startup checker validates the actual `electron-edge-js` payload (`lib/edge.js` and `edge_nativeclr.node`) and accepts future compatible versions via the minimal dependency range `electron-edge-js >=8.2.2`.

---

## [2.0.146] - 2026-06-01

### Fixed

- **TIA Portal V18 project selection with WinCC Unified references** — selecting/opening projects on some V18 installations no longer fails with `TypeLoadException` for `Siemens.Engineering.HmiUnified.HmiSoftware`. Project structure discovery now detects WinCC Unified software without a hard runtime dependency on that optional/version-sensitive Openness type, while preserving Unified HMI tree discovery on newer compatible runtimes.

---

## [2.0.144] - 2026-06-01

### Changed

- **Log Details available before connecting** — the connection panel now shows the `Log Details` toggle immediately after extension startup, before a TIA Portal connection or project selection is available.
- **Expanded wrapper/TIA diagnostics** — when `Log Details` is enabled, bridge calls now include wrapper and TIA Openness warning/error details in the `TIA Portal Import` log, including exception details, compiler warning/error summaries and failed project-selection context.

### Fixed

- **Project selection diagnostics** — failed project selection now logs the wrapper error and, when available, the projects visible through TIA Openness so name mismatches are easier to diagnose.

---

## [2.0.141] - 2026-06-01

### Fixed

- **Flat HW export layout for IO devices** — importing HW configuration from TIA Portal no longer leaves redundant per-device folders under `Devices/IO_Devices` when the actual `.aml` / HW files are written directly into the flat IO devices folder. Empty stale IO device folders are cleaned up safely, while folders containing user files or previous exports are preserved.

---

## [2.0.134] - 2026-05-29

### Fixed

- **Offline native module handling** — the extension no longer attempts `npm install` when pre-built Electron binaries are already bundled in the VSIX but fail to load. `npm install` and `npm reinstall` are now skipped entirely when there is no internet access (DNS lookup to `registry.npmjs.org` is used to detect offline state). A clear diagnostic message is shown instead, listing the bundled Electron versions and suggesting an extension update as the offline fix.

### Changed

- **Improved offline error messages** — when native module repair fails in offline mode, the output now shows which Electron versions are bundled (`35–40`) and which version the current VS Code requires, making it easier to diagnose compatibility issues without internet access.
- **Smaller multi-version VSIX package** — shared .NET wrapper dependencies are now deduplicated into `dotnet/TiaOpennessWrapper/bin/Release/net48/common/` after building V18–V21 wrappers. Version-specific folders now ship only their own `TiaOpennessWrapper.dll`, while the runtime resolver loads common DLLs from the shared folder.
- **Windows x64 native payload trimming** — VSIX packaging now excludes unused `darwin`, `ia32`, and `arm64` native binaries from `edge-js` and `electron-edge-js`, while keeping Windows x64 offline binaries for Electron 35–40.

---

## [2.0.127] - 2026-05-28

### Fixed

- **ACT preview startup after multiline Network comments** — embedded Automation Compare Tool previews no longer stay on the `Loading...` screen after the Network comment line-break handling change. The generated webview script now keeps newline escape sequences valid before ACT's Angular renderer mounts.

---

## [2.0.123] - 2026-05-28

### Fixed

- **FBD row layout in ACT previews** — embedded Automation Compare Tool previews now detect the rendered diagram language per network and keep FBD operand labels on a single line, restoring the original FBD row layout while preserving the LAD wrapping fix.
- **Multiline Network comments in ACT previews** — manual line breaks in Network comments are preserved in the embedded Automation Compare Tool view, matching the multiline layout shown in TIA Portal.

### Changed

- **LAD-only operand wrapping** — long operand label wrapping and collision avoidance now apply only inside `lad-network` diagrams; FBD networks still show expanded full names and enriched tooltips without generated multiline SVG rows.

---

## [2.0.119] - 2026-05-27

### Added

- **Variable comments in ACT tooltips** — embedded Automation Compare Tool previews now parse SimaticML member comments from the opened XML file and append them to LAD/FBD operand tooltips.
- **Compact ACT preview controls** — the embedded ACT toolbar now includes quick toggles for Overview, Interface, Attributes and a Network collapse/expand-all action.

### Changed

- **Cleaner default ACT preview layout** — Overview, Interface, Attributes and the ACT status/title bar are hidden by default so the network diagram gets more usable space.
- **Readable long LAD/FBD symbols** — full operand names are wrapped into compact SVG lines with collision avoidance and a background stroke so long symbols remain visible without covering contacts and coils.

---

## [2.0.106] - 2026-05-11

### Added

- **Time-based numeric import progress for large TIA imports** — project imports, single-device imports and category program imports now show a live numeric percentage, ETA and `work` counter in the VS Code notification progress UI and in the status bar, so long-running exports no longer look frozen while TIA Portal is busy.
- **Time-based progress for category HW Config imports** — `TIA Import: Import HW Config for All Devices in Category` now uses the same progress UI, calibrated from real multi-device hardware-import timings instead of a simple `100 / deviceCount` step.

### Changed

- **Progress estimation is weighted by artifact type** — SD LAD/FBD/STL blocks, SCL/DB source exports, XML exports, ACT XML preview mirrors, UDTs, tag tables and watch tables now contribute different costs to the ETA model, with an additional 10% safety buffer to keep estimates from being too optimistic on large projects.
- **New tuning setting `tiaImport.importProgress.itemsPerSecond`** — lets you scale the built-in progress calibration up or down for faster or slower TIA environments without changing the weight model.

---

## [2.0.99] - 2026-05-11

### Added

- **Embedded ACT diff for Git revisions** — right-click a local `.xml` SimaticML file or `.s7dcl` SD block and choose **TIA Import: Compare with Git Revision in ACT** to pick two revisions from the working tree / recent Git history and open a graphical Automation Compare Tool diff directly inside VS Code. The compare view uses the same embedded ACT webview as the single-file preview and passes both files to the installed ACT renderer as `leftFile` / `rightFile` globals.

### Changed

- **Safer ACT compare fallback** — revision files are materialized under `%TEMP%/tia-act-compare/` with ACT-friendly names, `.s7dcl` comparisons resolve through committed `.tiaPreview/*.xml` mirrors, and external ACT launch remains available only as fallback / `embedMode=external`. The external process path now strips VS Code Electron environment variables so ACT does not start in Node mode.

---

## [2.0.88] - 2026-05-11

### Added

- **Stale preview detection for `.s7dcl` LAD/FBD preview** — opening `TIA Import: Preview XML with Automation Compare Tool` for an `.s7dcl` file now validates whether the cached XML mirror is older than the source SD files (`.s7dcl` / `.s7res`). When staleness is detected, the preview is blocked by default to avoid showing outdated logic and a modal warning explains that the block should be re-exported from TIA Portal.

### Changed

- **Safe fallback flow for stale mirrors** — users can still explicitly continue via **Open Stale XML Anyway**, while **Show Logs** jumps directly to the extension output channel with contextual staleness details (source path and timestamps).

---

## [2.0.70] - 2026-05-08

### Added

- **Graphical LAD / FBD viewer for local SimaticML XML** — program blocks exported from TIA Portal can now be displayed as **interactive LAD or FBD network diagrams** directly inside VS Code, without launching TIA Portal. Right-click a `.xml` block in the Explorer and choose **TIA Import: Preview XML with Automation Compare Tool**: every network is rendered with the same layout TIA Portal uses (instructions, contacts/coils for LAD, function boxes for FBD, wire routing, operand wiring), so block logic can be reviewed and reasoned about offline by humans and AI agents alike. The renderer is the installed SIMATIC Automation Compare Tool, embedded into a VS Code webview panel.
- **Dark-theme support for the embedded SIMATIC Automation Compare Tool preview** — the in-VS-Code ACT preview panel now follows the active VS Code color theme. All ACT surfaces (Overview sidebar, Interface / Attributes tables, Options pane, tabs, splitters) are repainted with `--vscode-*` colors and the LAD/FBD diagram canvas, block bodies, wires and SVG operand text are inverted into a dark palette so block contours and labels stay readable on the dark background.
- **Full operand label expansion in LAD/FBD networks** — ACT renders truncated operand names like `#ManMs…gToRun`, but keeps the full name in a child SVG `<title>` element. The webview now walks the rendered SVG (with a `MutationObserver` to cover lazy-rendered networks) and replaces each truncated `<tspan>` text with the full name, so `#ManMsgL1ToL2.oCountMsgToRun` is shown verbatim. Long input labels that previously got clipped on the left are now displayed fully — the diagram is shifted right with a left margin and parents have `overflow: visible`, with horizontal scroll on the outer split-area as a fallback when the network is wider than the panel.

### Changed

- **Prerequisite emphasised in README** — the *Previewing local SimaticML XML* section and the *Requirements* table now link directly to the Siemens Support download page for the [SIMATIC Automation Compare Tool](https://support.industry.siemens.com/cs/document/109797235/simatic-automation-compare-tool-?dti=0&lc=en-PL). The extension does not bundle ACT; you must install it separately to use the preview.

---

## [2.0.0] - 2026-05-06

Major version bump consolidating the autonomous-agent feature wave.

### Added

- **TIA Portal V18 support** — V18 is now selectable in the TIA Portal version picker (Connection panel and `tiaImport.tiaPortalVersion` setting). The .NET wrapper is built against V18/V19/V20/V21 references and the cross-reference dump (which requires V18+) works on every supported version.
- **`tia_export_cross_references` Language Model tool** — dump the full cross-reference table for a PLC into AI-friendly files. Writes:
  - `cross-references.jsonl` — one JSON record per usage location, streamable for LLM context windows. Fields: `symbol`, `symbolType`, `symbolPath`, `symbolAddress`, `usedIn`, `usedInPath`, `usedInType`, `usedInDevice`, `usedInAddress`, `access`, `referenceLocation`, `referenceType`, `referencedAsName`, `locationName`, `locationAddress`.
  - `cross-references.csv` — flat RFC 4180 CSV with the same columns, deterministic sort, ready to load into pandas / Excel / `Import-Csv`.
  - `unused-symbols.csv` — objects with no references (dead-code detection).
  - Defaults to `<workspace>/TiaExport/Projects/<ProjectName>/Devices/PLCs/<Device>/CrossReferences/`.
  - Uses `Siemens.Engineering.CrossReference.CrossReferenceService` (requires TIA Portal V18+).
- **Setting `tiaImport.autoExportCrossReferences`** (`always` / `ask` / `never`, default `ask`) — controls automatic cross-reference dump after a device or project import. In `ask` mode the prompt is shown **per PLC** at the moment the dump would start, never during plain block imports, and **auto-skips after 5 s** if you don't respond so the rest of the import can run unattended. ⚠️ Generating cross-references is performed by TIA Portal itself and can take **several minutes — sometimes 10 min+ on large PLCs** (thousands of blocks, fault-tolerant projects); progress is streamed line-by-line into the *TIA Portal Import* output channel.
- Total LM tool count is now **18** (`tia_*`). The `tia_export_cross_references` tool is also long-running for the same reason — don't impose short client-side timeouts.

### Changed

- README, CHANGELOG and copilot-instructions updated to reflect the 4 supported TIA Portal versions (V18, V19, V20, V21) and the new auto-export setting.

---

## [1.0.223] - 2026-05-06

### Added

- **Multi-agent instruction files in workspace template** — `TIA Import: Prepare Workspace` now scaffolds two extra files alongside `.github/copilot-instructions.md`:
  - **`CLAUDE.md`** — picked up automatically by [Claude Code](https://docs.anthropic.com/claude/docs/claude-code). Uses Claude's native `@.github/copilot-instructions.md` import syntax to re-export the existing ruleset, so Claude and Copilot share one source of truth.
  - **`AGENTS.md`** — follows the open [agents.md](https://agents.md) standard supported by Cursor, Aider, OpenAI Codex, Gemini CLI, Jules and other AI coding agents.
- **`CLAUDE.local.md` is git-ignored** in the template `.gitignore` so per-machine overrides never get committed.

### Changed

- README **Workspace Templates** section documents the new files.

---

## [1.0.221] - 2026-05-06

### Added

- **Full UI ↔ Copilot parity for Language Model Tools** — every workflow available from the UI is now reachable from Copilot / `@tia` chat participant. Three new tools bring the total to **17**:
  - **`tia_export_project`** — export every device in the active project (program blocks, tag tables, UDTs, watch tables) plus optionally HW configuration in a single call. Equivalent of the UI command **TIA Import: Import Entire Project**. Inputs: `includeHwConfig?` (default `true`), `hwConfigFormat?` (`xml` | `cax`). Returns per-device results with `programOk` / `hwOk` flags.
  - **`tia_import_hw_config`** — push HW Config from the workspace into TIA Portal. Accepts a single `.xml` / `.aml` file or a folder (`Devices/<Cat>/<Dev>/DeviceConfiguration/` or flat `Devices/IO_Devices/`). **Required** for HW Config — the existing `tia_import_file` does not handle HW Config files because they go through a separate `HwConfigBridgeMixin` endpoint. Honours `tiaImport.hwConfigFormat` and supports `overwriteExisting` / `updateExisting` / `importNetworkConfig` / `skipIfIdentical`. Force-overwrite triggers a confirmation dialog unless `tiaImport.lmTools.autoConfirmImports` is enabled.
  - **`tia_refresh`** — re-read the project structure from TIA Portal (devices, blocks, tag tables) into the in-memory cache. Use after the user changed something in TIA Portal between tool calls.

### Changed

- **`@tia` chat participant** now advertises all 17 tools (added `tia_export_project`, `tia_import_hw_config`, `tia_refresh` to `TIA_TOOL_NAMES`).
- **`.github/copilot-instructions.md`** (and the workspace template under `Documentation/Templates/`) updated to document the new tools and clarify that HW Config must be pushed via `tia_import_hw_config`, not `tia_import_file`.
- **README** gained a *Copilot / AI Agent Integration* subsection summarising the LM tool surface.

---

## [1.0.215] - 2026-05-04

### Added

- **Import Project Library &gt; Types** — three new commands on the Library node in the project tree:
  - `TIA Import: Import Library Types` — export the entire Project Library Types tree
  - `TIA Import: Import Library Folder` — export a single user folder (recursive)
  - `TIA Import: Import Library Type` — export a single library type
    Files land under `<workspace>/<projectName>/Library/Types/...`, mirroring the in-project folder structure. Master copies are intentionally not exported.

### Changed

- **Per-type format selection for Project Library export** honours the configured `tiaImport.exportFormat`:
  - LAD/FBD/STL (and their F-variants) → `.s7dcl` / `.s7res` via `LibraryTypeVersion.ExportAsDocuments` (TIA Portal V20+).
  - SCL → `.scl` via `PlcExternalSourceSystemGroup.GenerateSource` (same path as normal SCL block export).
  - UDT / GRAPH / CFC / SFC / DB / non-block types → `.xml` via `LibraryTypeVersion.Export` (with an Info message naming the reason).
- **Format decision is driven by the block's `ProgrammingLanguage`**, not by `LibraryType.GetSupportedExportFormats()` (which is empty for many types and was previously forcing every library type to XML).

### Fixed

- **No more empty per-type subdirectories** when SD export fails — the directory is created on-demand inside the SD branch and rolled back on failure, with automatic XML fallback.
- **Whitelist of SD-compatible languages** prevents `ExportAsDocuments` failures for SCL / GRAPH / CFC / SFC / DB blocks that were previously routed into the SD path.

---

## [1.0.197] - 2026-04-30

### Added

- **TIA Portal version selector in the Connection panel** — new top-most entry "**TIA Portal**" shows the currently selected major version (V19/V20/V21) and opens a quick-pick to switch versions without diving into Settings. The selection is persisted in `tiaImport.tiaPortalVersion`; the existing change-listener prompts for a window reload to apply it.
- New command `TIA Import: Select TIA Portal Version` (`tia-import.selectTiaPortalVersion`).

### Changed

- **Wrapper build script skips V17** — `scripts/build-dotnet-all.ps1` now ignores reference assemblies under `dotnet/refs/V17/` (V17 is no longer a supported target). V18 is also out of scope; only V19/V20/V21 are built.

---

## [1.0.172] - 2026-04-30

### Fixed

- **Per-version .NET wrapper binaries** — V19/V20 installations no longer fail to load the extension with `Could not load file or assembly 'Siemens.Engineering.Base, Version=21.0.0.0'`. The wrapper is now built once per supported TIA Portal major version (V19 → `Siemens.Engineering.dll`, V20 → `Siemens.Engineering.dll`, V21 → `Siemens.Engineering.Base.dll` family) and shipped under `dotnet/TiaOpennessWrapper/bin/Release/net48/V<n>/`. The bridge picks the binary matching `tiaImport.tiaPortalVersion` at activation time.
- **`tiaPortalPath` auto-refresh on version change** — switching the TIA Portal version now automatically clears `tiaImport.tiaPortalPath` if it was pointing at the previous version's default install folder, so the auto-detected path for the newly selected version takes effect after the reload.

### Changed

- **Default TIA Portal version is now V21.**
- New `scripts/build-dotnet.js` build orchestrator: iterates over V19/V20/V21 and builds each only when the corresponding `C:\Program Files\Siemens\Automation\Portal V<n>\PublicAPI\V<n>\net48` directory is present, skipping missing installations gracefully (Siemens NuGet does not bundle reference assemblies — they are resolved from the local TIA install).
- `TiaOpennessWrapper.csproj` no longer appends the framework moniker twice to the output path; binaries land directly in `bin\Release\net48\V<n>\`.

### Notes

- This VSIX ships with the V21 wrapper only because V19/V20 binaries can only be produced on machines with TIA Portal V19/V20 installed. To enable V19 or V20, install the corresponding TIA Portal version and run `npm run build:dotnet` before packaging.

---

## [1.0.171] - 2026-04-30

### Added

- **TIA Portal V19 / V20 backward compatibility** — extension now supports TIA Portal V19, V20 and V21 with a single binary. Version is selected via `tiaImport.tiaPortalVersion` (V18 is no longer offered, since SD-format paths require V20+ and V18 lacks several APIs used internally).
- **`TiaCapabilities` runtime gating** — new helper in the .NET wrapper that exposes the initialized TIA Portal version and feature flags (e.g. `SupportsSdFormat` for V20+). Used to guard newer Openness APIs and degrade gracefully on older versions.

### Changed

- **SD format auto-fallback on V19** — when `exportFormat="sd"` is selected on TIA Portal V19, LAD/FBD/STL blocks are now exported as XML instead of `.s7dcl`/`.s7res` (the `ExportAsDocuments` API was added in V20). SCL blocks continue to use `GenerateSource` (`.scl`) which is available on V19.
- **SD import blocked with clear error on V19** — exporting `.s7dcl` files back to a V19 project now returns an explicit error message ("SD format requires V20+") instead of failing inside the Openness call.
- **UI strings de-versioned** — removed hardcoded `V21` from progress titles and command descriptions in the export commands; the active TIA Portal version is shown in the status bar.

### Internal

- `TiaConnector.GetInitializedVersionNumber()` exposed for capability checks.
- `tsconfig.json` now excludes `test/` from the compilation root so unit tests don't break the production build.

---

## [1.0.164] - 2026-04-27

### Added

- **CAx (AutomationML) format for HW Config** — bidirectional HW configuration transfer between TIA Portal and the workspace using `CaxProvider` (`.aml` files). New TIA→Workspace project- and device-level export and Workspace→TIA `.aml` import paths via the dedicated `HwConfigCaxService`.
- **`Format HW` toggle in Connection panel** — switch HW Config format between **XML** and **CAx (AutomationML)** with a single click; the choice is persisted in the new `tiaImport.hwConfigFormat` setting and used by all HW import/export commands.

### Changed

- **CAx logs streamed to Output panel** — CAx import/export no longer writes `*_CaxImport.log` / `*_CaxExport.log` files in the workspace. The provider log is captured to a temporary file, emitted line-by-line into the `TIA Portal Import` Output channel, and the temp file is deleted afterwards.
- **`Import HW Config` (device category)** — now respects the global `Format HW` setting; previously it always produced XML output regardless of the selection.

---

## [1.0.141] - 2026-04-22

### Changed

- **TIA project opening flow** - Improved project opening and loading when connecting to TIA Portal, making the connection flow more reliable.
- **Block export sorting** - Improved block ordering during export to TIA Portal so dependencies are processed in a more stable sequence.

---

## [1.0.127] - 2026-03-28

### Changed

- **Copilot instructions update** - Refined `.github/copilot-instructions.md` guidance for TIA Portal Openness API usage, including required API XML references, key HW classes, common navigation patterns, block export format rules, and build command reminders.

---

## [1.0.126] - 2026-03-17

### Fixed

- **`UserFiles/` workspace scaffold** — `InitWorkspace` now always creates `UserFiles/` in the workspace root, even when `Documentation/Templates/UserFiles/` is empty and not included in the VSIX package.

---

## [1.0.123] - 2026-03-16

### Fixed

- **Instance DB import comparison (TIA → workspace)** — Instance DBs now use the same StartValue-based comparison as export-to-TIA. Previously, full normalized XML diff was used during import, which reported false differences in FB-inherited interface structure (IDs, timestamps, ordering). Now only non-default StartValues are compared, matching the export logic. Re-importing previously exported IDBs no longer shows spurious changes.

---

## [1.0.102] - 2026-03-16

### Added

- **`Tools/` workspace directory** — Utility scripts (Python, PowerShell, etc.) are now scaffolded into the workspace on first connection. Each script has a matching `.md` description file with usage instructions and dependencies.
- **`UserFiles/` workspace directory** — Default output location for files generated by `Tools/` scripts (Excel reports, CSV exports, logs). Excluded from TIA Portal import and version control.
- **Community contribution call** — README now includes a section encouraging users to share their utility scripts and `copilot-instructions.md` improvements via Pull Requests on GitHub.

---

## [1.0.101] - 2026-03-12

### Fixed

- **`.db` export to TIA Portal** — Fixed error "Sources from DB can only be exported when the target file has the extension '.db'" when using "Check and overwrite differences" mode. The temporary file used for block comparison now uses the same extension as the source file (`.db`, `.scl`, etc.) instead of a hardcoded `.scl`.

---

## [1.0.98] - 2026-03-11

### Added

- **Global Data Block source export (`.db`)** — Global DBs can now be exported as text-based `DATA_BLOCK` source files (`.db`) via the `GenerateSource` API, in addition to the standard XML format. Controlled by `tiaImport.dbExportFormat` setting (default: `db`). Instance DBs always use XML.
- **Export `.db` files back to TIA Portal** — `.db` source files are imported via the SCL external source path (`PlcExternalSourceSystemGroup`). Context menu "Export Blocks to TIA" now available for `.db` files.
- **`tiaImport.showImportExportDetails` setting** — toggle the detailed "Import Details" / "Export Details" log section on or off (default: off). Real-time messages are always shown during operations; the details section repeats them for reference when enabled.
- **"Log Details" toggle** in the Connection panel tree view for quick access to the above setting.

### Changed

- Default DB export format changed from `xml` to `db` (source file).

### Fixed

- Orphan cleanup no longer deletes blocks imported from `.db` files — added `*.db` to local name detection.

---

## [1.0.89] - 2026-03-11

### Fixed

- `Connect to TIA Portal` now auto-selects and loads the project immediately when exactly one running TIA project is available.
- Removed duplicate PLC tree level in Project Explorer for single-PLC devices where device label and PLC software label are identical.

---

## [1.0.53] - 2026-02-18

### Changed

- Internal improvements and stability fixes

---

## [1.0.0] - 2026-01-01

### Added

- Initial stable release
- Bidirectional TIA Portal ↔ VS Code bridge via Openness API
- Full project import: blocks, tag tables, UDTs, watch tables, HMI, HW config
- Export to TIA Portal V21 with smart comparison and orphan cleanup
- Multiple export formats: XML (SimaticML), SD (`.s7dcl`/`.scl`), XLSX (tag tables)
- Project Explorer tree view with context menus
- Status bar connection indicator with health monitoring
- Workspace scaffolding with `.gitignore` and `.github/` templates
- Dependency-aware import ordering (UDT → FB → FC → OB → DB)
- Unified device export command
- HMI support (screens, tags, connections)
- Hardware configuration import/export (XML, AML, CAx)
- Compile after export with configurable mode (Always / Ask / Never)
- Compile error tracking in VS Code PROBLEMS panel with file and line resolution
- Instance DB creation directly via API (no XML import required)
- Know-how protected block detection (detects and skips placeholders)
- Cancellation support for long-running operations
