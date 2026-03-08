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
    return os.path.join(".infobot", ".tmp", "tasks", feature)


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


def _ready_for_seq(feature: str, seq: str) -> bool:
    paths = _list_subtasks(feature)
    subtasks_by_seq = {}
    ordered = []
    for p in paths:
        obj = _load_json(p)
        s = str(obj.get("seq") or _seq_from_filename(p))
        s = str(s).zfill(2) if str(s).isdigit() else str(s)
        subtasks_by_seq[s] = obj
        ordered.append((s, obj))
    ordered.sort(key=lambda x: x[0])

    obj = subtasks_by_seq.get(seq)
    if not obj:
        return False
    return _ready(subtasks_by_seq, obj)


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


def cmd_start(feature: str, seq: str, agent_id: str | None = None) -> int:
    seq = str(seq).zfill(2) if str(seq).isdigit() else str(seq)
    base = _tasks_dir(feature)
    path = os.path.join(base, f"subtask_{seq}.json")
    if not os.path.isfile(path):
        _die(f"subtask not found: {path}")

    obj = _load_json(path)
    status = str(obj.get("status", "")).lower()
    if status == "completed":
        _die(f"subtask already completed: {feature} {seq}")
    if status == "in_progress":
        print(f"in_progress\t{feature}\t{seq}")
        return 0
    if status != "pending":
        _die(f"subtask not startable from status: {status}")

    if not _ready_for_seq(feature, seq):
        _die(f"subtask not ready (deps/status): {feature} {seq}")

    obj["status"] = "in_progress"
    obj["started_at"] = _now_iso()
    if agent_id:
        obj["agent_id"] = agent_id
    _write_json_atomic(path, obj)

    print(f"started\t{feature}\t{seq}")
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


def cmd_init(feature: str) -> int:
    if not feature or feature.strip() == "":
        _die("usage: router.sh init <feature>")

    feature = feature.strip()
    base = _tasks_dir(feature)
    os.makedirs(base, exist_ok=True)

    task_path = os.path.join(base, "task.json")
    subtask_path = os.path.join(base, "subtask_01.json")

    if os.path.exists(task_path) or os.path.exists(subtask_path):
        _die(
            "task template already exists (refusing to overwrite): "
            f"{task_path} / {subtask_path}"
        )

    task_obj = {
        "id": feature,
        "name": feature,
        "status": "active",
        "objective": "",
        "context_files": [],
        "reference_files": [],
        "exit_criteria": [],
        "subtask_count": 1,
        "completed_count": 0,
        "created_at": _now_iso(),
    }

    subtask_obj = {
        "id": f"{feature}-01",
        "seq": "01",
        "title": "",
        "status": "pending",
        "depends_on": [],
        "parallel": True,
        "suggested_agent": "CoderAgent",
        "context_files": [],
        "reference_files": [],
        "acceptance_criteria": [],
        "deliverables": [],
    }

    _write_json_atomic(task_path, task_obj)
    _write_json_atomic(subtask_path, subtask_obj)

    print(f"created\t{task_path}")
    print(f"created\t{subtask_path}")
    return 0


def main(argv) -> int:
    if len(argv) < 2:
        _die("usage: router.sh <init|status|start|complete|next|parallel> ...")
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

    if cmd == "start":
        if len(argv) not in (4, 5):
            _die("usage: router.sh start <feature> <seq> [agent_id]")
        feature = argv[2]
        seq = argv[3]
        agent_id = argv[4] if len(argv) == 5 else None
        return cmd_start(feature, seq, agent_id)

    if cmd == "next":
        if len(argv) != 3:
            _die("usage: router.sh next <feature>")
        return cmd_next(argv[2])

    if cmd == "parallel":
        if len(argv) != 3:
            _die("usage: router.sh parallel <feature>")
        return cmd_parallel(argv[2])

    if cmd == "init":
        if len(argv) != 3:
            _die("usage: router.sh init <feature>")
        return cmd_init(argv[2])

    _die(f"unknown command: {cmd}")


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
