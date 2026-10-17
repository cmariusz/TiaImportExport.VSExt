#!/usr/bin/env python3
# cmsoft:managed tia-import - Prepare Workspace of CMsoft Import for TiaPortal updates this file; delete this line to keep your own version
r"""
Open or connect to a TIA Portal project through the local TIA CLI bridge and export it.

Examples:
    python .\Tools\tia_cli_example.py "E:\Projects\TIA\Demo.ap21" --workspace . --pretty
    python .\Tools\tia_cli_example.py --workspace . --pretty
    python .\Tools\tia_cli_example.py --workspace . --project-name Demo --pretty
    python .\Tools\tia_cli_example.py --workspace . --project-name Demo --program-only --log-level error --pretty

Status and CMsoft Import for TiaPortal Output log lines are written to stderr. The final machine-readable
result is written to stdout as JSON. Press Ctrl+C to interrupt the script.
"""

import argparse
import http.client
import json
import sys
from pathlib import Path
from typing import Any, Optional


SCRIPT_DIR = Path(__file__).resolve().parent


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Open or connect to a TIA Portal project through the local TIA CLI bridge and export it into the workspace.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=r"""
Examples:
    python .\Tools\tia_cli_example.py "E:\Projects\TIA\Demo.ap21" --workspace . --pretty
    python .\Tools\tia_cli_example.py --workspace . --pretty
    python .\Tools\tia_cli_example.py --workspace . --project-name Demo --pretty
    python .\Tools\tia_cli_example.py --workspace . --project-name Demo --program-only --log-level error --pretty
""".strip(),
    )
    parser.add_argument("project", nargs="?", help="Optional path to a TIA Portal .ap* project file")
    parser.add_argument(
        "--workspace",
        default=str(SCRIPT_DIR.parent),
        help="Workspace folder containing .tia/cli.json; defaults to the workspace this script is in (the parent of Tools/)",
    )
    parser.add_argument("--project-name", help="Optional TIA Portal project name to select after connecting")
    parser.add_argument("--timeout", type=int, default=0, help="CLI request timeout in milliseconds; 0 disables it")
    parser.add_argument("--program-only", action="store_true", help="Export program objects without hardware configuration")
    parser.add_argument(
        "--hw-format",
        choices=["xml", "cax"],
        help="Override HW config export format for this run",
    )
    parser.add_argument("--skip-prepare", action="store_true", help="Do not call prepare_workspace before connecting")
    parser.add_argument("--log-limit", type=int, default=80, help="Number of recent TIA Output log lines to show; 0 disables log display")
    parser.add_argument(
        "--log-level",
        choices=["debug", "info", "warn", "error", "section", "all"],
        default="all",
        help="Filter displayed TIA Output log lines by level",
    )
    parser.add_argument("--pretty", action="store_true", help="Pretty-print the final JSON result")
    args = parser.parse_args()

    workspace_path = Path(args.workspace).expanduser().resolve()
    project_path = Path(args.project).expanduser().resolve() if args.project else None
    state: dict[str, Any] = {}
    steps: list[dict[str, Any]] = []

    try:
        status(f"Workspace: {workspace_path}")
        if project_path:
            status(f"Project file: {project_path}")
        validate_paths(workspace_path, project_path)
        status("Reading TIA CLI bridge state")
        state = ensure_cli_state(workspace_path)
        status(f"Connected to TIA CLI bridge at {state['host']}:{state['port']}")

        if not args.skip_prepare:
            status("Preparing workspace templates")
            prepare_result = call_tia_bridge(state, "prepare_workspace", {}, args.timeout)
            ensure_success("prepare_workspace", prepare_result)
            steps.append({"command": "prepare_workspace", "result": prepare_result})

        if project_path:
            status("Opening TIA project by file path")
            open_result = call_tia_bridge(state, "open_project", {"filePath": str(project_path)}, args.timeout)
            ensure_success("open_project", open_result)
            steps.append({"command": "open_project", "result": open_result})
        else:
            status("Connecting to TIA Portal")
            connect_result = call_tia_bridge(state, "connect", {}, args.timeout)
            ensure_success("connect", connect_result)
            steps.append({"command": "connect", "result": connect_result})

        if args.project_name and not project_path:
            status(f"Selecting TIA project: {args.project_name}")
            select_result = call_tia_bridge(state, "select_project", {"projectName": args.project_name}, args.timeout)
            ensure_success("select_project", select_result)
            steps.append({"command": "select_project", "result": select_result})
        else:
            status("Reading current TIA project")
            current_result = call_tia_bridge(state, "current_project", {}, args.timeout)
            ensure_success("current_project", current_result)
            steps.append({"command": "current_project", "result": current_result})

        status("Refreshing TIA project structure")
        refresh_result = call_tia_bridge(state, "refresh", {}, args.timeout)
        ensure_success("refresh", refresh_result)
        steps.append({"command": "refresh", "result": refresh_result})

        status("Exporting project into workspace. Press Ctrl+C to stop waiting for the operation.")
        export_payload: dict[str, Any] = {"includeHwConfig": not args.program_only}
        if args.hw_format:
            export_payload["hwConfigFormat"] = args.hw_format
        export_result = call_tia_bridge(state, "export_project", export_payload, args.timeout)
        ensure_success("export_project", export_result)
        steps.append({"command": "export_project", "result": export_result})
        status("Export completed")
        show_output_logs(state, args.log_limit, args.log_level, args.timeout)

        return emit(
            {
                "success": True,
                "workspace": str(workspace_path),
                "projectPath": str(project_path) if project_path else None,
                "projectName": args.project_name,
                "steps": steps,
            },
            args.pretty,
            0,
        )
    except KeyboardInterrupt:
        status("Interrupted by user")
        show_output_logs(state, args.log_limit, args.log_level, args.timeout)
        return emit(
            {
                "success": False,
                "interrupted": True,
                "error": "Interrupted by user",
                "workspace": str(workspace_path),
                "projectPath": str(project_path) if project_path else None,
                "projectName": args.project_name,
                "steps": steps,
            },
            args.pretty,
            130,
        )
    except Exception as error:
        status(f"Failed: {error}")
        show_output_logs(state, args.log_limit, args.log_level, args.timeout)
        return emit(
            {
                "success": False,
                "error": str(error),
                "workspace": str(workspace_path),
                "projectPath": str(project_path) if project_path else None,
                "projectName": args.project_name,
                "steps": steps,
            },
            args.pretty,
            1,
        )


def status(message: str) -> None:
    print(f"[tia-import] {message}", file=sys.stderr, flush=True)


def validate_paths(workspace_path: Path, project_path: Optional[Path]) -> None:
    if not workspace_path.exists():
        raise FileNotFoundError(f"Workspace folder not found: {workspace_path}")
    if project_path:
        if not project_path.exists():
            raise FileNotFoundError(f"TIA project file not found: {project_path}")
        if not project_path.name.lower().endswith(tuple(f".ap{version}" for version in range(10, 30))):
            raise ValueError(f"Expected a TIA Portal .ap* project file, got: {project_path}")


def ensure_cli_state(workspace_path: Path) -> dict[str, Any]:
    state_path = workspace_path / ".tia" / "cli.json"
    if state_path.exists():
        return read_cli_state(state_path)
    raise FileNotFoundError(
        f"TIA CLI state not found: {state_path}. Open this workspace in VS Code with the CMsoft Import for TiaPortal extension active "
        "and switch the CLI bridge on (row CLI Bridge of the Connection view, or the setting tiaImport.cli.enabled)."
    )


def read_cli_state(state_path: Path) -> dict[str, Any]:
    with state_path.open("r", encoding="utf-8") as state_file:
        state = json.load(state_file)
    for key in ("host", "port", "token"):
        if not state.get(key):
            raise ValueError(f"Invalid TIA CLI state file {state_path}: missing {key}")
    return state


def call_tia_bridge(
    state: dict[str, Any],
    command: str,
    payload: dict[str, Any],
    timeout_ms: int,
) -> dict[str, Any]:
    body = json.dumps({"command": command, "args": payload}).encode("utf-8")
    connection = http.client.HTTPConnection(
        str(state["host"]),
        int(state["port"]),
        timeout=timeout_ms / 1000 if timeout_ms > 0 else None,
    )
    try:
        connection.request(
            "POST",
            "/api",
            body=body,
            headers={
                "authorization": f"Bearer {state['token']}",
                "content-type": "application/json; charset=utf-8",
            },
        )
        response = connection.getresponse()
        text = response.read().decode("utf-8")
        try:
            result = json.loads(text)
        except json.JSONDecodeError as exc:
            raise RuntimeError(f"TIA bridge returned invalid JSON for {command}: {text}") from exc
        if response.status >= 400:
            raise RuntimeError(result.get("error") or f"TIA bridge request failed with HTTP {response.status}")
        return result
    finally:
        connection.close()


def show_output_logs(state: dict[str, Any], limit: int, level: str, timeout_ms: int) -> None:
    if not state or limit <= 0:
        return
    try:
        result = call_tia_bridge(
            state,
            "get_logs",
            {"limit": limit, "level": level},
            timeout_ms,
        )
        if result.get("success") is False:
            status(f"Could not read TIA Output logs: {result.get('error', result)}")
            return
        lines = ((result.get("data") or {}).get("lines") or [])
        if not lines:
            status("CMsoft Import for TiaPortal Output log has no matching entries")
            return
        print("\n--- CMsoft Import for TiaPortal Output log ---", file=sys.stderr)
        for line in lines:
            print(line, file=sys.stderr)
        print("--- End CMsoft Import for TiaPortal Output log ---\n", file=sys.stderr)
    except Exception as error:
        status(f"Could not read TIA Output logs: {error}")


def ensure_success(command: str, result: dict[str, Any]) -> None:
    if result.get("success") is False:
        raise RuntimeError(f"{command} failed: {result.get('error', result)}")


def emit(payload: dict[str, Any], pretty: bool, exit_code: int) -> int:
    print(json.dumps(payload, indent=2 if pretty else None))
    return exit_code


if __name__ == "__main__":
    sys.exit(main())
