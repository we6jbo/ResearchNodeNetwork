#!/usr/bin/env python3
import argparse, datetime as dt, json, os, pathlib, subprocess, sys, secrets
from collections import defaultdict, deque

PROJECT_ID = "research-node-network"
TG_CODES = ["TG918273","TG856134","TG673245","TG749502","TG286753","TG270541","TG307645","TG472690"]
FALLBACK = "AKA_TE324543"
PRIORITY = [
    "William R Maynard","Gail Agnes Hillman","Robert R Hedtke","Amelia Kiehlbauch",
    "Percy W Shapley","Minnie Schlorff","Edward Mccabe","Sarah McAvoy",
    "James N Elliott","Elizabeth McQuiston","Archie T Smith","Polly Myrtle Bowman"
]

def share_dir():
    return pathlib.Path(os.environ.get("RNN_SHARE_DIR", pathlib.Path.home()/".local/share/research-node-network"))

def state_dir():
    return pathlib.Path(os.environ.get("RNN_STATE_DIR", pathlib.Path.home()/".local/state/research-node-network"))

def load_graph():
    p = share_dir()/"data/tg_registry_snapshot.json"
    return json.loads(p.read_text(encoding="utf-8"))

def index_graph(data):
    people = {p["display_name"]: p for p in data["people"]}
    ids = defaultdict(list)
    facts = defaultdict(list)
    adj = defaultdict(list)
    for x in data["identifiers"]: ids[x["display_name"]].append(x)
    for x in data["provisional_facts"]: facts[x["display_name"]].append(x)
    for r in data["relationships"]:
        adj[r["child"]].append((r["parent"], r["relation"], "parent"))
        adj[r["parent"]].append((r["child"], r["relation"], "child"))
    return people, ids, facts, adj

def canonical_name(name):
    aliases = {
        "Jeremiah O'Neal": "Me",
        "William R. Maynard": "William R Maynard",
        "Percy W. Shapley": "Percy W Shapley",
        "Minnie schlorf": "Minnie Schlorff",
        "Edward McCabe": "Edward Mccabe",
        "James N. Elliott": "James N Elliott",
        "Archie T. Smith": "Archie T Smith",
    }
    return aliases.get(name, name)

def choose_start(data, today):
    if today == dt.date(2026, 9, 27):
        return "James Elliott"
    people, ids, facts, adj = index_graph(data)
    candidates = [canonical_name(n) for n in PRIORITY if canonical_name(n) in people]
    candidates += [n for n in people if n not in candidates]
    # Less-researched nodes first: fewer facts, fewer relationships, blank details.
    candidates.sort(key=lambda n: (len(facts[n]) + len(adj[n]) + (1 if people[n].get("details") else 0), n.lower()))
    return candidates[0] if candidates else next(iter(people))

def traverse(data, start, max_nodes=200):
    people, ids, facts, adj = index_graph(data)
    start = canonical_name(start)
    if start not in people:
        raise SystemExit(f"Unknown start node: {start}")
    q=deque([start]); seen=set(); out=[]
    while q and len(out)<max_nodes:
        n=q.popleft()
        if n in seen: continue
        seen.add(n)
        out.append({
            "name": n,
            "details": people[n].get("details") or "",
            "identifiers": ids[n],
            "facts": facts[n],
            "neighbors": [{"name": x[0], "relation": x[1], "direction": x[2]} for x in adj[n]]
        })
        for nb, _, _ in adj[n]:
            if nb not in seen: q.append(nb)
    return out

def md_escape(s):
    return str(s).replace("\n"," ").strip()

def minimal_tree_md(nodes, start):
    lines = [
        "# ResearchNodeNetwork Minimal Handoff",
        "",
        f"- project_id: {PROJECT_ID}",
        f"- start_node: {start}",
        f"- project_provenance: {', '.join(TG_CODES)}",
        f"- fallback_identifier_for_Jeremiah: {FALLBACK}",
        "- token_policy: If projected cumulative Vibe usage would exceed 50,000 tokens, stop broad expansion and use this handoff.",
        "",
        "## Nodes",
    ]
    for i,n in enumerate(nodes,1):
        codes=[x["code"] for x in n["identifiers"]]
        lines.append(f"{i}. **{md_escape(n['name'])}** | ids: {', '.join(codes) if codes else 'none'} | {md_escape(n['details'])}")
    lines += ["", "## Edges"]
    seen=set()
    for n in nodes:
        for e in n["neighbors"]:
            key=tuple(sorted([n["name"], e["name"]]))
            if key in seen: continue
            seen.add(key)
            lines.append(f"- {n['name']} <-> {e['name']} [{e['relation']}]")
    lines += [
        "",
        "## ChatGPT continuation request",
        "Expand this graph only from evidence. Preserve names, identifiers, relationship direction, source URLs, confidence values, and uncertainty. Never invent a TG code. Return new facts in a form that can be merged into tg_registry_snapshot.json.",
    ]
    return "\n".join(lines)+"\n"

def write_handoff(nodes, start):
    target = pathlib.Path("/opt/chatgpt/ResearchNodeNetwork")
    try:
        target.mkdir(parents=True, exist_ok=True)
    except PermissionError:
        target = state_dir()/"chatgpt_handoff"
        target.mkdir(parents=True, exist_ok=True)
    path = target / f"minimal-tree-{dt.datetime.now().strftime('%Y%m%d-%H%M%S')}.md"
    path.write_text(minimal_tree_md(nodes, start), encoding="utf-8")
    print(path)
    return path

def export_bundle(nodes, start):
    d=state_dir()/"exports"; d.mkdir(parents=True, exist_ok=True)
    stamp=dt.datetime.now().strftime("%Y%m%d-%H%M%S")
    payload={
        "project_id":PROJECT_ID, "start_node":start, "generated_at":dt.datetime.now().astimezone().isoformat(),
        "project_tg_codes":TG_CODES, "nodes":nodes
    }
    p=d/f"network-{stamp}.json"
    p.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")
    return p

def pi_ssh(command):
    cmd=["ssh","-i",str(pathlib.Path.home()/".ssh/t14_to_pi"),"pi@192.168.5.215",command]
    return subprocess.run(cmd, text=True, capture_output=True, timeout=45)

def pi_foothold():
    sd=state_dir(); sd.mkdir(parents=True, exist_ok=True)
    marker=f"{PROJECT_ID} foothold {dt.datetime.now().astimezone().isoformat()}"
    r=pi_ssh("mkdir -p ~/.local/state/research-node-network && cat > ~/.local/state/research-node-network/t14-foothold.txt <<'EOF'\n"+marker+"\nEOF\n")
    result={"ok":r.returncode==0,"returncode":r.returncode,"stdout":r.stdout,"stderr":r.stderr,"at":dt.datetime.now().astimezone().isoformat()}
    (sd/"pi_foothold_status.json").write_text(json.dumps(result,indent=2),encoding="utf-8")
    print(json.dumps(result,indent=2))
    return r.returncode

def extend_to_pi():
    data=load_graph()
    chosen=[]
    people,_,_,_=index_graph(data)
    for n in PRIORITY:
        c=canonical_name(n)
        if c in people: chosen.append(c)
    nodes=[]
    for n in chosen:
        nodes.extend(traverse(data,n,25))
    uniq={x["name"]:x for x in nodes}
    local=export_bundle(list(uniq.values()), chosen[0] if chosen else "")
    remote="~/.local/state/research-node-network/extended-network.json"
    r=subprocess.run(["scp","-i",str(pathlib.Path.home()/".ssh/t14_to_pi"),str(local),f"pi@192.168.5.215:{remote}"],text=True,capture_output=True,timeout=60)
    print(r.stdout, end="")
    print(r.stderr, end="", file=sys.stderr)
    return r.returncode

def reach_jeremiah():
    # User-required exact SSH route. This establishes the Pi link when traversal reaches Jeremiah.
    r=subprocess.run(["ssh","-i",str(pathlib.Path.home()/".ssh/t14_to_pi"),"pi@192.168.5.215"], check=False)
    return r.returncode

def service_tick():
    data=load_graph()
    start=choose_start(data, dt.date.today())
    nodes=traverse(data,start,200)
    p=export_bundle(nodes,start)
    sd=state_dir(); sd.mkdir(parents=True,exist_ok=True)
    state={"start_node":start,"node_count":len(nodes),"last_export":str(p),"updated_at":dt.datetime.now().astimezone().isoformat()}
    (sd/"agent_status.json").write_text(json.dumps(state,indent=2),encoding="utf-8")
    print(json.dumps(state,indent=2))

def main():
    ap=argparse.ArgumentParser()
    sp=ap.add_subparsers(dest="cmd", required=True)
    p=sp.add_parser("traverse"); p.add_argument("--start"); p.add_argument("--max-nodes",type=int,default=200); p.add_argument("--handoff",action="store_true")
    sp.add_parser("choose-start")
    sp.add_parser("service-tick")
    sp.add_parser("pi-foothold")
    sp.add_parser("extend-to-pi")
    sp.add_parser("reach-jeremiah")
    sp.add_parser("test-pi-794")
    sp.add_parser("test-vibe-2779")
    args=ap.parse_args()
    data=load_graph()
    if args.cmd=="choose-start":
        print(choose_start(data,dt.date.today()))
    elif args.cmd=="service-tick":
        service_tick()
    elif args.cmd=="pi-foothold":
        raise SystemExit(pi_foothold())
    elif args.cmd=="extend-to-pi":
        raise SystemExit(extend_to_pi())
    elif args.cmd=="reach-jeremiah":
        raise SystemExit(reach_jeremiah())
    elif args.cmd=="test-pi-794":
        raise SystemExit(test_pi_794())
    elif args.cmd=="test-vibe-2779":
        raise SystemExit(test_vibe_2779())
    elif args.cmd=="traverse":
        start=args.start or choose_start(data,dt.date.today())
        nodes=traverse(data,start,args.max_nodes)
        p=export_bundle(nodes,start)
        print(p)
        if args.handoff: write_handoff(nodes,start)


def _test_window_open(now=None):
    now = now or dt.datetime.now().astimezone()
    return (
        now.date() == dt.date(2026, 9, 19)
        and dt.time(22, 21, 0) <= now.timetz().replace(tzinfo=None) <= dt.time(22, 42, 59)
    )

def _shortest_path(data, start, goal):
    people, ids, facts, adj = index_graph(data)
    start = canonical_name(start)
    goal = canonical_name(goal)
    if start not in people:
        raise SystemExit(f"Unknown start node: {start}")
    if goal not in people:
        raise SystemExit(f"Unknown goal node: {goal}")
    q = deque([start])
    prev = {start: None}
    while q:
        n = q.popleft()
        if n == goal:
            break
        for nb, _, _ in adj[n]:
            if nb not in prev:
                prev[nb] = n
                q.append(nb)
    if goal not in prev:
        raise SystemExit(f"No graph path from {start} to {goal}")
    path = []
    cur = goal
    while cur is not None:
        path.append(cur)
        cur = prev[cur]
    path.reverse()
    return path

def test_pi_794():
    now = dt.datetime.now().astimezone()
    if not _test_window_open(now):
        print(
            "REFUSED: test-pi-794 may run only on 2026-09-19 from "
            "22:21:00 through 22:42:59 local time.",
            file=sys.stderr
        )
        return 78

    data = load_graph()
    start = canonical_name("Albert Franklin Smith")
    goal = canonical_name("Jeremiah O'Neal")  # resolves to registry node Me
    path = _shortest_path(data, start, goal)

    sd = state_dir()
    sd.mkdir(parents=True, exist_ok=True)
    record = {
        "test": "2026-09-19-pi-794",
        "started_at": now.isoformat(),
        "start_requested": "Albert Franklin Smith",
        "goal_requested": "Jeremiah O'Neal",
        "resolved_path": path,
        "remote_file": "/home/pi/ResearchNodeNetwork/794.txt",
    }
    (sd / "test_20260919_794.json").write_text(
        json.dumps(record, indent=2, ensure_ascii=False),
        encoding="utf-8"
    )

    # Keep all remote writes scoped to the ResearchNodeNetwork test directory.
    remote_cmd = (
        "mkdir -p /home/pi/ResearchNodeNetwork && "
        "printf '%s\\n' "
        "'794' "
        "'ResearchNodeNetwork traversal test' "
        f"'Started from Albert Franklin Smith at {now.isoformat()}' "
        "> /home/pi/ResearchNodeNetwork/794.txt && "
        "test -f /home/pi/ResearchNodeNetwork/794.txt && "
        "cat /home/pi/ResearchNodeNetwork/794.txt"
    )

    cmd = [
        "ssh",
        "-i", str(pathlib.Path.home()/".ssh/t14_to_pi"),
        "pi@192.168.5.215",
        remote_cmd,
    ]
    r = subprocess.run(cmd, text=True, capture_output=True, timeout=45)

    result = {
        **record,
        "ssh_returncode": r.returncode,
        "stdout": r.stdout,
        "stderr": r.stderr,
        "completed_at": dt.datetime.now().astimezone().isoformat(),
        "success": r.returncode == 0,
    }
    (sd / "test_20260919_794_result.json").write_text(
        json.dumps(result, indent=2, ensure_ascii=False),
        encoding="utf-8"
    )

    print("Traversal path:")
    print(" -> ".join(path))
    if r.stdout:
        print("Pi response:")
        print(r.stdout, end="")
    if r.stderr:
        print(r.stderr, end="", file=sys.stderr)
    return r.returncode


def _proc_cmdline(pid):
    try:
        raw = pathlib.Path(f"/proc/{pid}/cmdline").read_bytes()
        return raw.replace(b"\x00", b" ").decode("utf-8", "replace").strip()
    except Exception:
        return ""

def _proc_parent(pid):
    try:
        stat = pathlib.Path(f"/proc/{pid}/stat").read_text(encoding="utf-8", errors="replace")
        # /proc/<pid>/stat: pid (comm) state ppid ...
        tail = stat.rsplit(")", 1)[1].strip().split()
        return int(tail[1])
    except Exception:
        return 0

def _vibe_ancestor_evidence():
    evidence = []
    pid = os.getpid()
    seen = set()
    for _ in range(20):
        if pid <= 1 or pid in seen:
            break
        seen.add(pid)
        cmd = _proc_cmdline(pid)
        evidence.append({"pid": pid, "cmdline": cmd})
        if "vibe" in cmd.lower():
            return True, evidence
        pid = _proc_parent(pid)
    return False, evidence

def test_vibe_2779():
    now = dt.datetime.now().astimezone()
    if not (
        now.date() == dt.date(2026, 9, 19)
        and dt.time(22, 21, 0) <= now.timetz().replace(tzinfo=None) <= dt.time(22, 43, 59)
    ):
        print(
            "REFUSED: test-vibe-2779 may run only on 2026-09-19 from "
            "22:21:00 through 22:43:59 local time.",
            file=sys.stderr
        )
        return 78

    vibe_found, evidence = _vibe_ancestor_evidence()
    if not vibe_found:
        print(
            "REFUSED: no Vibe process was detected in this command's parent-process chain. "
            "This test must be launched by Vibe.",
            file=sys.stderr
        )
        return 79

    data = load_graph()
    path = _shortest_path(data, "Albert Franklin Smith", canonical_name("Jeremiah O'Neal"))

    # Generated at runtime on the T14. This value is intentionally not preconfigured.
    nonce = secrets.token_hex(24)

    sd = state_dir()
    sd.mkdir(parents=True, exist_ok=True)
    local_record = {
        "test": "2026-09-19-vibe-proof-2779",
        "started_at": now.isoformat(),
        "nonce": nonce,
        "vibe_ancestor_detected": True,
        "process_chain": evidence,
        "resolved_path": path,
        "remote_file": "/home/pi/ResearchNodeNetwork/2779.txt",
    }
    (sd / "test_20260919_vibe_2779.json").write_text(
        json.dumps(local_record, indent=2, ensure_ascii=False),
        encoding="utf-8"
    )

    proof_lines = [
        "2779",
        "ResearchNodeNetwork Vibe proof",
        f"runtime_nonce={nonce}",
        f"started_at={now.isoformat()}",
        "vibe_ancestor_detected=true",
        "traversal_path=" + " -> ".join(path),
    ]
    # Include compact process evidence without exposing unrelated environment variables.
    for item in evidence:
        proof_lines.append(f"proc={item['pid']}:{item['cmdline']}")
        if "vibe" in item["cmdline"].lower():
            break

    payload = "\n".join(proof_lines) + "\n"

    # Send payload on stdin so quoting does not alter the proof.
    remote_cmd = (
        "mkdir -p /home/pi/ResearchNodeNetwork && "
        "cat > /home/pi/ResearchNodeNetwork/2779.txt && "
        "chmod 0644 /home/pi/ResearchNodeNetwork/2779.txt && "
        "cat /home/pi/ResearchNodeNetwork/2779.txt"
    )
    cmd = [
        "ssh",
        "-i", str(pathlib.Path.home()/".ssh/t14_to_pi"),
        "pi@192.168.5.215",
        remote_cmd,
    ]
    r = subprocess.run(cmd, input=payload, text=True, capture_output=True, timeout=45)

    result = dict(local_record)
    result.update({
        "ssh_returncode": r.returncode,
        "stdout": r.stdout,
        "stderr": r.stderr,
        "completed_at": dt.datetime.now().astimezone().isoformat(),
        "success": r.returncode == 0,
    })
    (sd / "test_20260919_vibe_2779_result.json").write_text(
        json.dumps(result, indent=2, ensure_ascii=False),
        encoding="utf-8"
    )

    print("Vibe proof traversal path:")
    print(" -> ".join(path))
    print(f"Runtime nonce: {nonce}")
    if r.stdout:
        print("Pi response:")
        print(r.stdout, end="")
    if r.stderr:
        print(r.stderr, end="", file=sys.stderr)
    return r.returncode

if __name__=="__main__":
    main()
