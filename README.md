# ResearchNodeNetwork

ResearchNodeNetwork v0.10 is a Qt 6 T14 service plus a filesystem/SSH research helper. It carries a portable export of the supplied TG registry so it can traverse the research graph without requiring the private registry database.

The service itself opens no network port. `network_agent.py` performs explicit SSH/SCP operations only when you invoke the Pi commands or when the 05:43 user timer invokes the foothold command.

## Important commands

```bash
research-node-network-agent choose-start
research-node-network-agent traverse
research-node-network-agent traverse --start "James Elliott" --handoff
research-node-network-agent extend-to-pi
research-node-network-agent reach-jeremiah
systemctl --user status research-node-network.service
systemctl --user status research-node-network-pi.timer
```

`reach-jeremiah` uses exactly `ssh -i ~/.ssh/t14_to_pi pi@192.168.5.215`.

Mistral Vibe 2.25.5 supports project-level `AGENTS.md`; this repository includes one so Vibe can learn the traversal, 50k-token handoff, Pi-link, and schedule rules when the project is trusted and opened as its working directory.


## TG identifiers and privacy layers

The TG identifiers are intentionally embedded directly in the source and portable metadata. They are project provenance identifiers, not credentials.

Relationship-layer labels such as `Mom`, `Grandma`, and `Grandpa` are preserved literally as privacy boundaries and are not automatically expanded to personal names.


## Build timestamp protection

The installer deletes the previous build directory, normalizes source-file timestamps to the current local filesystem time, creates a fresh build directory, configures once, and then builds with Ninja. This avoids Ninja's `build.ninja still dirty after 100 tries` loop when copied/extracted files have timestamps that appear to be in the future or otherwise inconsistent.


## Vibe integration

The installer adds a small ResearchNodeNetwork section to `~/.vibe/AGENTS.md` without replacing any existing user-level Vibe instructions.

For an explicit ResearchNodeNetwork session from any directory:

```bash
vibe-rnn
```

This launches Vibe with `--workdir ~/Projects/ResearchNodeNetwork`, causing the project-level `AGENTS.md` to load.

For ordinary `vibe` sessions elsewhere, the user-level bootstrap only points Vibe at ResearchNodeNetwork when a request involves genealogy, TG/AKA identifiers, node research, or this project.

Before publishing:

```bash
python3 tools/check_publication_safety.py
```


## Persistent Vibe routing

v0.6 expands the user-level Vibe bootstrap so ResearchNodeNetwork is automatically consulted for three trigger classes:

- any family-tree task;
- any Homo sapiens tree/lineage task starting from the 2026 present-day context and expanding backward/outward;
- any ResearchNodeNetwork task requiring the Raspberry Pi.

The durable instructions are merged into `~/.vibe/AGENTS.md`. A copy of the exact project-facing command map is also retained in `VIBE_RESEARCHNODE_QUICKREF.md`.

Use `vibe-rnn` from any directory to start Vibe directly inside this project.


## Project blog

Vibe is instructed to keep this public project reference in context whenever ResearchNodeNetwork is activated:

https://j03.page/2026/09/20/building-a-living-network


## Temporary traversal test

v0.8 includes a strictly date/time-gated validation command:

```bash
research-node-network-agent test-pi-794
```

It can execute only on 2026-09-19 from 22:21:00 through 22:42:59 local time. It computes a graph path from Albert Franklin Smith to Jeremiah O'Neal and, only if the window is open, writes `/home/pi/ResearchNodeNetwork/794.txt` over the existing SSH route.


## Vibe-origin proof test

v0.9 adds `research-node-network-agent test-vibe-2779`. During its narrow 2026-09-19 test window, the command requires a Vibe ancestor process, generates a fresh runtime nonce, follows the Albert Franklin Smith to Jeremiah O'Neal graph path, and writes proof to `/home/pi/ResearchNodeNetwork/2779.txt`.

The nonce is generated at execution time and is not hardcoded into the repository.


## Semantic Vibe routing

v0.10 adds 16 permanent semantic trigger concepts to both the user-level Vibe bootstrap and the project AGENTS instructions. Vibe is instructed to recognize the user's intent rather than exact phrases.

The portable trigger definition is also stored at:

```text
vibe/semantic_triggers.json
```

This allows future project tools to consume the same trigger vocabulary without depending on prose parsing.
