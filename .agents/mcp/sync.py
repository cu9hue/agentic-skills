#!/usr/bin/env python3
"""Add the MCP servers in servers.json (and servers.local.json, if present)
to Claude Code, Codex and the Antigravity CLI, at user scope.

Only missing servers are added; existing entries and their logins are left
alone. Pass --dry-run to print the commands instead of running them.
"""
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent


def load_servers():
    servers = json.loads((HERE / "servers.json").read_text())
    local = HERE / "servers.local.json"
    if local.exists():
        servers.update(json.loads(local.read_text()))
    return servers


def claude_existing():
    config = Path.home() / ".claude.json"
    if not config.exists():
        return set()
    return set(json.loads(config.read_text()).get("mcpServers", {}))


def claude_add(name, spec):
    if "url" in spec:
        entry = {"type": "http", "url": spec["url"]}
    else:
        entry = {"type": "stdio", "command": spec["command"],
                 "args": spec.get("args", []), "env": spec.get("env", {})}
    return ["claude", "mcp", "add-json", "-s", "user", name, json.dumps(entry)]


def codex_existing():
    out = subprocess.run(["codex", "mcp", "list", "--json"],
                         capture_output=True, text=True, check=True).stdout
    return {server["name"] for server in json.loads(out)}


def codex_add(name, spec):
    if "url" in spec:
        # `codex mcp add --url` starts an OAuth browser login and blocks on it,
        # so write the entry directly and leave `codex mcp login` to the user.
        config = Path(os.environ.get("CODEX_HOME", Path.home() / ".codex")) / "config.toml"
        block = f'\n[mcp_servers.{name}]\nurl = "{spec["url"]}"\n'
        return lambda: config.open("a").write(block), f"append [mcp_servers.{name}] to {config}"
    env = [f"--env={k}={v}" for k, v in spec.get("env", {}).items()]
    return ["codex", "mcp", "add", name, *env, "--", spec["command"], *spec.get("args", [])]


def agy_add(name, spec):
    # `agy mcp add` adds or updates, so no existence check is needed.
    if "url" in spec:
        return ["agy", "mcp", "add", name, spec["url"]]
    env = [f"--env={k}={v}" for k, v in spec.get("env", {}).items()]
    return ["agy", "mcp", "add", *env, name, "--", spec["command"], *spec.get("args", [])]


AGENTS = {
    "claude": (claude_existing, claude_add),
    "codex": (codex_existing, codex_add),
    "agy": (lambda: set(), agy_add),
}


def main():
    dry_run = "--dry-run" in sys.argv[1:]
    servers = load_servers()
    for agent, (existing, add) in AGENTS.items():
        if not shutil.which(agent):
            print(f"{agent}: not installed, skipped")
            continue
        present = existing()
        for name, spec in servers.items():
            if name in present:
                print(f"{agent}: {name} already configured")
                continue
            step = add(name, spec)
            if isinstance(step, tuple):
                action, label = step
            else:
                action = lambda cmd=step: subprocess.run(
                    cmd, check=True, capture_output=True, text=True, timeout=60)
                label = " ".join(step)
            if dry_run:
                print(f"{agent}: would {label}")
                continue
            action()
            print(f"{agent}: added {name}")
    print("Sign in to OAuth servers once per agent: /mcp in Claude Code, "
          "`codex mcp login <name>` in Codex.")


if __name__ == "__main__":
    main()
