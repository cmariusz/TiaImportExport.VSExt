# Privacy Policy

**Product:** TIA Portal Import — Visual Studio Code extension (`MariuszCzyrnek.tia-import`)
**Controller:** CmSoft, Kornatka 23, 32-410 Dobczyce, Poland, NIP PL 894-253-07-59 — `office@cmsoft.com.pl`
**Version:** 1.1 — 2026-09-23 (applies to extension version 4.0.0 and later)

---

## 1. Summary

| Question | Answer |
| --- | --- |
| Does the extension collect telemetry or usage analytics? | **No.** |
| Does it send your project files, PLC programs, tags or source code to the Licensor? | **No.** The extension itself keeps everything on your machine. |
| Can project data reach an AI provider? | **Yes, if you connect an AI Assistant** (for example GitHub Copilot or an MCP client). The assistant receives the results of the tools it calls and forwards them to its model provider — see Section 2a. |
| Does it phone home on start-up? | **No.** |
| What leaves your machine? | Only what you explicitly submit when activating a paid plan (Section 3), periodic license validation of paid plans (Section 3), data forwarded by AI Assistants you connect (Section 2a), and requests the Visual Studio Code Marketplace / Open VSX make to deliver updates (Section 5). |

## 2. Data processed locally only

The extension reads and writes files inside your workspace (for example
`TiaExport/`, `.tia/`), reads TIA Portal project data through the Siemens
Openness API, and writes diagnostic messages to the *TIA Portal Import* output
channel. This processing happens **entirely on your computer**. The Licensor has
no access to it.

The optional CLI bridge (`tiaImport.cli.enabled`, disabled by default) starts a
listener bound to `127.0.0.1` only, protected by a per-session token stored in
`.tia/cli.json`. It is not reachable from outside your machine.

The MCP server (`tiaImport.mcp.enabled`, enabled by default — set it to `false`
to stop it) likewise binds to `127.0.0.1` only and is protected by a per-session
token stored in `.tia/mcp.json`. It is not reachable from outside your machine.
AI agents that you explicitly connect to it (for example Copilot, Claude Desktop
or other MCP clients) can invoke the extension's TIA Portal tools through it;
no data is transmitted to the Licensor.

## 2a. Data forwarded by AI Assistants you connect

When you use the extension's Language Model Tools, the `@tia` chat participant
or the MCP server, the AI Assistant you chose calls the extension's tools and
receives their results — for example block sources, tag and device names,
project structure, compile messages or cross-reference data. The AI Assistant
usually sends this content, together with your prompts, to its model provider
(for example Microsoft/GitHub, Anthropic, OpenAI, Google, or a local model you
run yourself).

- This transfer is performed by the AI Assistant, under the provider's terms
  and privacy policy. The Licensor does not receive, see or store this data and
  is neither controller nor processor for it.
- You decide whether an AI Assistant may access a project. Check your
  confidentiality obligations and your customer's requirements before doing so,
  in particular for projects containing personal data (for example operator or
  user names in HMI or UMAC configurations) or know-how of third parties.
- PLC credentials requested by `tia_download_to_plc` are entered in a local
  VS Code input box and are not passed to the AI Assistant.

The extension does not send automatic error reports. Diagnostic logs leave your
machine only if you attach them yourself, for example to a support e-mail or an
issue.

## 3. Data processed when you activate a paid plan

Activation is **optional** and only happens when you explicitly request it. When
you do, the following data may be transmitted to the Licensor or to the payment
provider acting as merchant of record:

| Data | Purpose | Legal basis (GDPR) |
| --- | --- | --- |
| E-mail address you enter | Issuing and delivering the license key, license support | Art. 6(1)(b) — performance of a contract |
| Company / billing data | Invoicing, tax obligations | Art. 6(1)(b) and 6(1)(c) |
| Derived hardware identifier (a one-way hash of machine characteristics — never the raw serial numbers) | Binding the license to the purchased number of seats, preventing abuse | Art. 6(1)(b) and 6(1)(f) — legitimate interest in protecting against unlicensed use |
| Product name, extension version, operating-system version, TIA Portal major versions installed | Issuing a compatible key, technical support | Art. 6(1)(b) |
| License status, activation and deactivation events | Seat management, revocation | Art. 6(1)(b) |
| License Key identifier, hardware identifier hash and extension version sent during periodic online validation (versions that use it) | Confirming that the license is still valid, enforcing the Seat limit | Art. 6(1)(b) and 6(1)(f) |

**No project content is ever transmitted** — no block sources, tag tables, device
names, project names or file contents.

## 4. Retention

- Order and invoicing data: for the period required by tax and accounting law
  (in Poland, 5 years from the end of the tax year).
- Activation records (e-mail, hardware identifier hash, license status): for the
  duration of the license plus 12 months, for renewal and dispute handling.
- Support correspondence: up to 24 months from the last message.

## 5. Recipients and third parties

- **Payment provider / merchant of record** — processes your payment and billing
  data as an independent controller or processor under its own privacy policy;
  identified on the purchase page.
- **Microsoft Corporation (Visual Studio Marketplace)** and **Eclipse Foundation
  AISBL (Open VSX Registry)** — distribute the extension package and process
  download/update requests under their own privacy policies. The Licensor
  receives only aggregated, anonymous install and rating statistics from them.
- **E-mail provider** — used to deliver license keys and support replies.

The current list of service providers that process personal data on the
Licensor's behalf (for example hosting of the license service, e-mail delivery)
is published on the product purchase page and is available on request.
Business Customers are informed by e-mail at least 30 days before a new
processor is added; if they raise a justified objection that cannot be
resolved, they may terminate the affected subscription with a pro-rata refund.

**Data processing agreement.** Where the Licensor processes personal data on
behalf of a Business Customer (for example the names and e-mail addresses of
users to whom the customer assigns Seats), it does so as a processor under
Article 28 GDPR, only for license and Seat administration. A data processing
agreement with the content required by Article 28(3) GDPR is available on
request at `office@cmsoft.com.pl`.

The Licensor does not sell personal data and does not use it for advertising or
profiling.

## 6. International transfers

Data is processed within the European Economic Area wherever possible. If a
processor operates outside the EEA, transfers are based on the European
Commission's Standard Contractual Clauses or an adequacy decision.

## 7. Your rights

You have the right to access, rectify, erase and port your data, to restrict or
object to processing, and to lodge a complaint with a supervisory authority (in
Poland: Prezes Urzędu Ochrony Danych Osobowych, ul. Stawki 2, 00-193 Warszawa).
To exercise any of these rights, write to `office@cmsoft.com.pl`.

Erasing your activation record will deactivate the corresponding license key.

On request, sent from the e-mail address registered with your license, you
receive a copy of your account and license data in a structured,
machine-readable format (JSON) within one month (Articles 15 and 20 GDPR).
Erasure does not cover data that must be retained under tax and accounting law
(Section 4).

## 8. Security

License data is stored encrypted at rest on the Licensor's side. On your
machine, the license key is stored using Visual Studio Code SecretStorage and
the Windows Data Protection API (DPAPI); it is not written to `settings.json`
and is not included in Settings Sync.

The MCP server and CLI bridge tokens in `.tia/` are regenerated for every
session; do not commit them to version control. How to report a security
vulnerability is described in [`SECURITY.md`](SECURITY.md).

## 9. Children

The Software is a professional engineering tool and is not directed at persons
under 16 years of age.

## 10. Changes

This policy may be updated for future versions of the Software. The version and
date at the top of this document indicate the applicable revision. Material
changes will be announced in the [`CHANGELOG.md`](CHANGELOG.md).

## 11. Contact

**CmSoft**
Kornatka 23, 32-410 Dobczyce, Poland
NIP: PL 894-253-07-59
E-mail: `office@cmsoft.com.pl`
Web: <https://www.cmsoft.com.pl>
