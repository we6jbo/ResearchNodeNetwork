# ResearchNodeNetwork instructions for Mistral Vibe 2.25.5

This project is a genealogy/research graph. The project service is local and port-free. Interact with it through files and the `research-node-network-agent` command. Do not create a TCP/UDP listener or client/server transport unless the user separately gives permission and the code `3team`.

## Required startup behavior

1. Read `tg_context_snapshot.json` and `data/tg_registry_snapshot.json`.
2. Run `research-node-network-agent choose-start`.
3. On **2026-09-27**, start at **James Elliott**. On other dates, use the chosen under-researched node.
4. Traverse relationships in both directions. Preserve confidence, permanent/provisional status, aliases, source URLs, and exact source-derived details.
5. Never invent a TG code. Project provenance codes are:
   TG918273, TG856134, TG673245, TG749502, TG286753, TG270541, TG307645, TG472690.
   Jeremiah O'Neal uses the fallback project identifier AKA_TE324543 when an identifier is required.
6. Names that must be included in Pi-extension research include:
   William R Maynard; Gail Agnes Hillman; Robert R Hedtke; Amelia Kiehlbauch;
   Percy W Shapley; Minnie Schlorff; Edward Mccabe; Sarah McAvoy;
   James N Elliott; Elizabeth McQuiston; Archie T Smith; Polly Myrtle Bowman.
7. When traversal reaches **Jeremiah O'Neal** (the portable overlay for registry node `Me`), execute exactly:
   `ssh -i ~/.ssh/t14_to_pi pi@192.168.5.215`
   Use that authenticated SSH path to continue only the ResearchNodeNetwork work on the Pi.
8. The T14's daily 05:43 local-time Pi foothold is maintained by the installed systemd user timer. Check it with:
   `systemctl --user status research-node-network-pi.timer`
9. Between **2026-09-20 10:00 and 16:00 local time**, human intervention is allowed. Outside that window, prefer autonomous, reversible project actions and record unresolved items rather than asking for routine input.
10. If projected cumulative Vibe usage for the research pass would exceed **50,000 tokens**, do not spend the extra tokens. Run:
    `research-node-network-agent traverse --handoff`
    This creates a minimal Markdown graph at `/opt/chatgpt/ResearchNodeNetwork/` when writable, otherwise in the user state directory. Stop broad expansion after writing the handoff.

## Exact handoff structure

The Markdown handoff must contain:
- project_id
- start_node
- project provenance TG codes
- fallback identifier
- a `## Nodes` section: one line per node with name, identifiers, and compact details
- a `## Edges` section: `Name A <-> Name B [relation]`
- a `## ChatGPT continuation request` preserving uncertainty and prohibiting invented TG codes

## Safe boundaries

Only process files and data belonging to this project. Do not intercept browser traffic, credentials, email, unrelated application data, or system-wide network traffic. The Pi connection is SSH only. No application listening port is permitted by this project version.


## GitHub/publication policy

This project is intended to be published to GitHub.

The family-tree graph, ordinary named relatives, research facts, source citations, and TG identifiers are considered public project data and may be committed to the repository.

Exactly three relationship-layer identities remain private:
- `Mom`
- `Grandma` — the user's mother's mother
- `Grandpa` — the user's mother's grandfather

Preserve those labels literally in source, generated Markdown, JSON, logs intended for GitHub, commits, issues, documentation, and research exports. Do not infer, search for, substitute, or publish the personal names behind those three labels unless the user explicitly changes this rule.

TG values are provenance identifiers, not credentials or secrets. They may be embedded directly in source and committed publicly.

## Privacy-layer naming

The registry may intentionally use relationship-layer labels such as `Mom`, `Grandma`, and `Grandpa` instead of a person's public name. Treat those labels as intentional privacy boundaries. Do not infer, replace, expose, or attempt to de-anonymize them unless the user explicitly supplies the corresponding name for this project. Other names and TG identifiers in this project are not treated as secret merely because they are embedded in the source.


## Persistent trigger semantics

When Vibe reaches this project through the user-level ResearchNodeNetwork routing rule, treat the trigger as intentional.

ResearchNodeNetwork owns these domains:

1. Anything involving the family tree.
2. Anything involving a Homo sapiens tree that starts from the 2026 present-day context and expands backward through ancestry/generations and outward through connected branches.
3. ResearchNodeNetwork access to the Raspberry Pi.

Basic command map:

- `research-node-network-agent choose-start`
- `research-node-network-agent traverse`
- `research-node-network-agent traverse --start "NAME"`
- `research-node-network-agent traverse --handoff`
- `research-node-network-agent extend-to-pi`
- `research-node-network-agent reach-jeremiah`
- exact Pi SSH route: `ssh -i ~/.ssh/t14_to_pi pi@192.168.5.215`
- local service status: `systemctl --user status research-node-network.service --no-pager`
- Pi timer status: `systemctl --user status research-node-network-pi.timer --no-pager`

Do not expose or copy the SSH private key. The command path may be documented; the key material may not.


## Project blog reference

When Vibe accesses or activates ResearchNodeNetwork, keep this project blog reference in working context:

- Building a Living Network
- https://j03.page/2026/09/20/building-a-living-network

This URL is public/GitHub-safe project metadata. It may be included in project documentation, research handoffs, and summaries when relevant.


## One-time Pi traversal test — 2026-09-19 only

This test is valid ONLY on **2026-09-19 from 22:21:00 through 22:42:59 local time**.

When the user asks for the `794` traversal test during that window:

1. Start at `Albert Franklin Smith`.
2. Traverse the existing ResearchNodeNetwork graph to `Jeremiah O'Neal` (portable registry node `Me`).
3. Then use the existing SSH path to the Pi.
4. Create:
   `/home/pi/ResearchNodeNetwork/794.txt`
5. The file must contain at least:
   `794`
6. Use:
   `research-node-network-agent test-pi-794`

Outside that exact date/time window, DO NOT perform this test and DO NOT create or modify the Pi test file. Report that the test window is closed.

This is a temporary validation rule. It does not change the permanent daily Pi foothold behavior.


## Vibe-only proof test — 2779 — 2026-09-19

This proof test is valid ONLY on **2026-09-19 from 22:21:00 through 22:43:59 local time**.

When the user asks Vibe to demonstrate that Vibe itself is performing the ResearchNodeNetwork traversal:

1. Vibe must execute:
   `research-node-network-agent test-vibe-2779`
2. The helper independently verifies that a process containing `vibe` exists in its parent-process chain.
3. If Vibe is not detected, the helper refuses to proceed with exit code 79.
4. If Vibe is detected, the helper:
   - computes the graph path from `Albert Franklin Smith` to `Jeremiah O'Neal`;
   - generates a fresh cryptographically random runtime nonce on the T14;
   - connects to the Pi through the existing SSH route;
   - writes `/home/pi/ResearchNodeNetwork/2779.txt`.
5. The Pi file records:
   - `2779`
   - the runtime nonce
   - execution timestamp
   - the resolved traversal path
   - compact parent-process evidence up to the detected Vibe process.

The runtime nonce is deliberately generated only when the test runs. It is not hardcoded in the repository or these instructions.

Outside the allowed window, do not attempt this test.


## Permanent semantic trigger vocabulary

Vibe must route to ResearchNodeNetwork when the user's request reasonably expresses ANY of the concepts below.

IMPORTANT: These are semantic triggers, NOT exact-string commands. The user may use different grammar, synonyms, shortened wording, combinations of words, names added later to the database, or natural conversational phrasing. If the meaning matches one or more concepts below, treat it as a ResearchNodeNetwork request.

1. **Explore genealogy / explore branches**
   Examples include: explore genealogy, explore this branch, look into genealogy, look at another branch, investigate a genealogy branch.

2. **Ancestral research / family research**
   Examples include: ancestral research, research my family, family history research, look into the family, research about the family.

3. **Investigate my family**
   Examples include: investigate my family, investigate this side of my family, investigate these relatives, look deeper into my family.

4. **Trace my family history**
   Examples include: trace my family history, trace this family line, trace where this branch came from, follow the family history.

5. **Research my relatives**
   Examples include: research my relatives, research this relative, look into this family member, find out more about this person in my family.

6. **Find [name] in my tree**
   This applies to names already known and names added later to the database or portable registry.
   Examples include: find Sarah McAvoy, find Albert Franklin Smith in my tree, locate this person in the tree, see whether [name] is in my family graph.

7. **Who is [name] in my family?**
   Examples include: who is [name], where does [name] fit, how is [name] related to me, who was this person in the family.

8. **Find the parents, children, or relatives of [name]**
   Relationship terms are flexible and include parents, children, grandparents, descendants, siblings, spouses, cousins, ancestors, and other family relations.

9. **Start with [name] and keep researching**
   Examples include: start at James Elliott, begin with Sarah McAvoy, research outward from [name], continue from this person.

10. **How are [name] and [name] related?**
    Examples include: connect these two people, find the relationship between them, how do they connect, find a path between [name] and [name].

11. **Find descendants of [name]**
    Examples include: find descendants, follow children or grandchildren, trace later generations from this person.

12. **Follow [name] to [another person in the past or future]**
    This means follow the graph from one named person to any other connected person, whether earlier, later, ancestor, descendant, or otherwise connected.
    Examples include: follow Sarah McAvoy to James Elliott, trace this person to an earlier ancestor, follow Albert Franklin Smith to someone later in the tree.

13. **Keep expanding from this person**
    Examples include: keep going, go outward from here, continue from this person, find everyone connected to this person, expand this branch.

14. **Search for missing people in this branch**
    Examples include: who is missing here, fill in this branch, find the unknown parent, look for missing descendants, find people that should connect here.

15. **Research everyone around [name]**
    Examples include: look around this person, who is connected to [name], research the people around [name], expand from [name], investigate this person's surrounding family network.

16. **Who connects these two people?**
    Examples include: how do these two connect, what is the relationship between them, find the link between [name] and [name], who is between these two, what path joins them.

### Semantic combination rule

Any meaningful combination of vocabulary from the concepts above should also trigger ResearchNodeNetwork when the intent is family-tree, genealogy, lineage, relatives, ancestry, descendants, family relationships, or graph traversal.

Examples that MUST trigger:
- `find how Sarah connects to James`
- `research everyone around Albert`
- `look into this branch`
- `trace my family back from here`
- `find the missing parent`
- `continue from Sarah and follow her descendants`
- `connect these names in my family`
- `investigate this person in my tree`

Do not require exact wording. Do not require the user's phrasing to appear literally in this file.
