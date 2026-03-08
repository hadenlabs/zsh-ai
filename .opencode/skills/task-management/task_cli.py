#!/usr/bin/env python3

import json
import os
import sys
from datetime import datetime, timezone
from typing import NoReturn


def _now_iso() -> str:
    return (
        datetime.now(timezone.utc)
        .replace(microsecond=0)
        .isoformat()
        .replace("+00:00", "Z")
    )


def _die(msg: str, code: int = 2) -> NoReturn:
    sys.stderr.write(msg + "\n")
    raise SystemExit(code)


def _tasks_dir(feature: str) -> str:
    return os.path.join(".tmp", "tasks", feature)


def _list_subtasks(feature: str):
    base = _tasks_dir(feature)
    if not os.path.isdir(base):
        _die(f"feature not found: {base}")
    files = []
    for name in os.listdir(base):
        if name.startswith("subtask_") and name.endswith(".json"):
            files.append(os.path.join(base, name))
    files.sort()
    return files


def _load_json(path: str):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def _write_json_atomic(path: str, data):
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, sort_keys=False)
        f.write("\n")
    os.replace(tmp, path)


def _seq_from_filename(path: str) -> str:
    name = os.path.basename(path)
    # subtask_01.json -> 01
    mid = name[len("subtask_") : -len(".json")]
    return mid


def _is_completed(obj) -> bool:
    return str(obj.get("status", "")).lower() == "completed"


def _ready(subtasks_by_seq, obj) -> bool:
    if str(obj.get("status", "")).lower() != "pending":
        return False
    deps = obj.get("depends_on") or []
    if not isinstance(deps, list):
        return False
    for dep in deps:
        dep_seq = str(dep).zfill(2) if str(dep).isdigit() else str(dep)
        dep_obj = subtasks_by_seq.get(dep_seq)
        if not dep_obj or not _is_completed(dep_obj):
            return False
    return True


def cmd_status(feature: str) -> int:
    paths = _list_subtasks(feature)
    rows = []
    for p in paths:
        obj = _load_json(p)
        seq = str(obj.get("seq") or _seq_from_filename(p))
        title = str(obj.get("title") or "")
        status = str(obj.get("status") or "unknown")
        rows.append((seq, status, title))

    for seq, status, title in rows:
        print(f"{seq}\t{status}\t{title}")
    return 0


def cmd_complete(feature: str, seq: str, summary: str) -> int:
    seq = str(seq).zfill(2) if str(seq).isdigit() else str(seq)
    base = _tasks_dir(feature)
    path = os.path.join(base, f"subtask_{seq}.json")
    if not os.path.isfile(path):
        _die(f"subtask not found: {path}")

    obj = _load_json(path)
    obj["status"] = "completed"
    obj["completed_at"] = _now_iso()
    obj["completion_summary"] = summary
    _write_json_atomic(path, obj)
    print(f"completed\t{feature}\t{seq}")
    return 0


def cmd_next(feature: str) -> int:
    paths = _list_subtasks(feature)
    subtasks_by_seq = {}
    ordered = []
    for p in paths:
        obj = _load_json(p)
        seq = str(obj.get("seq") or _seq_from_filename(p))
        seq = str(seq).zfill(2) if str(seq).isdigit() else str(seq)
        subtasks_by_seq[seq] = obj
        ordered.append((seq, obj))
    ordered.sort(key=lambda x: x[0])

    for seq, obj in ordered:
        if _ready(subtasks_by_seq, obj):
            title = str(obj.get("title") or "")
            print(f"{seq}\t{title}")
            return 0
    return 1


def cmd_parallel(feature: str) -> int:
    paths = _list_subtasks(feature)
    subtasks_by_seq = {}
    ordered = []
    for p in paths:
        obj = _load_json(p)
        seq = str(obj.get("seq") or _seq_from_filename(p))
        seq = str(seq).zfill(2) if str(seq).isdigit() else str(seq)
        subtasks_by_seq[seq] = obj
        ordered.append((seq, obj))
    ordered.sort(key=lambda x: x[0])

    any_out = False
    for seq, obj in ordered:
        if bool(obj.get("parallel")) and _ready(subtasks_by_seq, obj):
            title = str(obj.get("title") or "")
            print(f"{seq}\t{title}")
            any_out = True
    return 0 if any_out else 1


def main(argv) -> int:
    if len(argv) < 2:
        _die("usage: router.sh <status|complete|next|parallel> ...")
    cmd = argv[1]

    if cmd == "status":
        if len(argv) != 3:
            _die("usage: router.sh status <feature>")
        return cmd_status(argv[2])

    if cmd == "complete":
        if len(argv) < 5:
            _die('usage: router.sh complete <feature> <seq> "<summary>"')
        feature = argv[2]
        seq = argv[3]
        summary = " ".join(argv[4:]).strip()
        return cmd_complete(feature, seq, summary)

    if cmd == "next":
        if len(argv) != 3:
            _die("usage: router.sh next <feature>")
        return cmd_next(argv[2])

    if cmd == "parallel":
        if len(argv) != 3:
            _die("usage: router.sh parallel <feature>")
        return cmd_parallel(argv[2])

    _die(f"unknown command: {cmd}")


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
