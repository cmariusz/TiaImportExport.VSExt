# Third-Party Notices

This project includes third-party components. Redistribution of this extension should preserve the applicable third-party license notices and terms.

> Informational notice: this file is a practical compliance aid and not legal advice.

## Project License

- Version **4.0.0 and later** of this extension is proprietary commercial software licensed under the End User License Agreement in `LICENSE.md`. It is not open source.
- Versions **3.1.85 and earlier** were released under the MIT License; that grant remains in force for those versions only (reproduced in `LICENSE.md`, section 20).
- The terms of `LICENSE.md` do **not** restrict your rights under the open-source licenses of the third-party components listed below. Where a component's license grants broader rights, that license prevails for that component.

## Runtime dependencies (Node.js)

- `edge-js` (19.3.0) — Apache-2.0
- `electron-edge-js` (40.0.1) — MIT
- `xml2js` (0.6.2) — MIT
- Transitive:
  - `@agracio/edge-cs` (1.3.7) — MIT
  - `edge-cs` (1.2.1) — Apache
  - `nan` (2.25.0) — MIT
  - `sax` (1.4.4) — BlueOak-1.0.0
  - `xmlbuilder` (11.0.1) — MIT

## .NET wrapper dependencies (NuGet)

- `Newtonsoft.Json` (13.0.3) — MIT
- `ClosedXML` (0.95.4) — MIT
- `Microsoft.CSharp` (4.7.0) — MIT
- `Microsoft.VisualBasic` (10.3.0) — Microsoft .NET library license terms (package metadata links to Microsoft license info)
- `DocumentFormat.OpenXml` (2.7.2) — package page does not expose a license expression; treat as Microsoft Open XML SDK terms and verify for your distribution policy
- `ExcelNumberFormat` (1.0.10) — MIT
- `System.*` / `Microsoft.*` platform packages used transitively (for example `System.CodeDom`, `System.Management`, `System.DirectoryServices`, `System.Security.*`) are published by Microsoft and generally distributed under MIT in modern package pages

## Siemens Openness packages (critical)

- `Siemens.Collaboration.Net.TiaPortal.Packages.Openness` (21.0.1765349347)
- `Siemens.Collaboration.Net.TiaPortal.Openness.Resolver` (2.0.1765367256)
- Related transitive `Siemens.Collaboration.*` packages

These packages are provided under Siemens "Royalty-free Software" terms with additional conditions for object code use/distribution and intended use with Siemens products.

### Distribution policy for this extension

1. Do not redistribute `Siemens.Engineering.*` binaries as part of this extension package unless Siemens terms explicitly allow it for your exact scenario.
2. Require end users to have their own valid TIA Portal installation and Openness license.
3. Keep Siemens package notices and terms available to recipients.
4. Verify export-control and regional restrictions where applicable.

## Apache-2.0 components — required notices

`edge-js` and `edge-cs` are distributed under the Apache License, Version 2.0.
A copy of the license is available at <https://www.apache.org/licenses/LICENSE-2.0>
and in the packaged `node_modules/edge-js/` and `node_modules/edge-cs/` folders.
These components are redistributed **unmodified**; no changes were made to their
source files. Their copyright, patent, trademark and attribution notices are
preserved in the packaged files and must not be removed.

## Recommended compliance checklist

- Keep this `THIRD_PARTY_NOTICES.md` file in source and packaged artifacts.
- Preserve the project `LICENSE.md` file.
- Do not remove third-party copyright/license notices from redistributed artifacts.
- Re-run dependency license checks before each release (`npm` and `dotnet`) because dependency graphs can change.
- Reject any new dependency under a copyleft license (GPL / LGPL / AGPL / SSPL) — it is incompatible with shipping this extension under a proprietary EULA.

## Audit basis (current snapshot)

- Node dependencies from `package.json` and installed `node_modules` metadata.
- .NET dependencies from `dotnet/TiaOpennessWrapper/TiaOpennessWrapper.csproj` + `dotnet list package --include-transitive`.
- Public NuGet package pages for license details where exposed.
