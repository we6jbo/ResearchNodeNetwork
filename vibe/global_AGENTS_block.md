# WE6JBO Vibe persistent routing instructions

## ResearchNodeNetwork: persistent memory/routing contract

Treat the following rules as persistent working context whenever Vibe Code starts.
This is not conversational memory; this file is the durable source of truth.

### Automatic triggers

Immediately consult ResearchNodeNetwork when the user's task involves ANY of the following:

A. **Anything involving the family tree**
   - genealogy
   - ancestors or descendants
   - relatives and family relationships
   - names, dates, places, evidence, sources, or relationships in the family graph
   - TG or AKA identifiers connected to family-tree research

B. **Anything involving a Homo sapiens tree starting from 2026 and going backward and outward**
   - begin conceptually at the user's 2026 present-day node/context
   - move backward through ancestry, generations, human lineage, and related branches
   - move outward through connected people/branches where the research requires it
   - use ResearchNodeNetwork as the graph/research framework rather than inventing a second family/human-tree system

C. **Accessing the Raspberry Pi for ResearchNodeNetwork**
   - any request to reach, extend, copy, inspect, or continue this research graph on the Pi
   - any ResearchNodeNetwork task that requires the Pi-side graph

### What Vibe must load

For any A/B/C trigger:

1. Read:
   `/home/we6jbo/Projects/ResearchNodeNetwork/AGENTS.md`
2. Treat this as the authoritative project root:
   `/home/we6jbo/Projects/ResearchNodeNetwork`
3. Use the installed command:
   `research-node-network-agent`
4. Do not invent TG identifiers or replace ResearchNodeNetwork with a parallel graph format unless the user explicitly asks.

### Basic ResearchNodeNetwork commands to remember

Choose today's starting research node:

    research-node-network-agent choose-start

Traverse the graph from the selected/default node:

    research-node-network-agent traverse

Traverse from a named node:

    research-node-network-agent traverse --start "NAME"

Create the compact Markdown handoff for ChatGPT when needed:

    research-node-network-agent traverse --handoff

Extend the selected public research branches to the Pi:

    research-node-network-agent extend-to-pi

When traversal reaches Jeremiah O'Neal and the project rule requires the Pi transition:

    research-node-network-agent reach-jeremiah

The exact underlying SSH route is:

    ssh -i ~/.ssh/t14_to_pi pi@192.168.5.215

Check the local background service:

    systemctl --user status research-node-network.service --no-pager

Check the scheduled daily Pi foothold:

    systemctl --user status research-node-network-pi.timer --no-pager

See the next scheduled foothold:

    systemctl --user list-timers --all | grep research-node

### Pi access rules

Use the existing SSH key path; do not copy, print, publish, or alter the private key itself.

ResearchNodeNetwork is port-free. Do not create a TCP/UDP client-server transport for it unless the user's separate client/server permission rule is satisfied.

The scheduled T14-to-Pi foothold is handled by the ResearchNodeNetwork systemd user timer. Do not create a second competing scheduler.

### GitHub/publication rule

ResearchNodeNetwork is intended for GitHub.

Public/GitHub-safe project data includes:
- TG identifiers
- ordinary named people in the genealogy graph
- public genealogy facts and relationships
- research citations/URLs
- portable ResearchNodeNetwork graph metadata
- Vibe instructions and project source

These three identity layers remain private and MUST stay literal:
- `Mom`
- `Grandma` — user's mother's mother
- `Grandpa` — user's mother's grandfather

Do not infer, research, substitute, expose, or publish the personal names behind those three labels unless the user explicitly changes this rule.

Never publish credentials, SSH private keys, API keys, tokens, `.env` secrets, or unrelated private application data.

### Scope rule

For unrelated programming, cybersecurity, writing, or ordinary system tasks, do not load the family graph merely because ResearchNodeNetwork exists. Activate this routing contract when an A/B/C trigger is present.


### ResearchNodeNetwork project blog

Whenever an A/B/C trigger activates ResearchNodeNetwork, also remember this public project reference:

    https://j03.page/2026/09/20/building-a-living-network

Title: `Building a Living Network`

Treat this as public/GitHub-safe project metadata and make it available in relevant summaries or handoffs.


### Temporary test trigger: 2026-09-19 / 794

Only on 2026-09-19 between 22:21:00 and 22:42:59 local time, if the user asks for the `794` ResearchNodeNetwork Pi traversal test, read the project `AGENTS.md` and run:

    research-node-network-agent test-pi-794

Do not run this test outside that exact window.


### Vibe-only proof test: 2779

Only on 2026-09-19 from 22:21:00 through 22:43:59 local time, when the user asks Vibe to prove that Vibe itself traversed ResearchNodeNetwork and reached the Pi, execute:

    research-node-network-agent test-vibe-2779

Do not substitute another shell for Vibe or ask the user to run the command manually; the command intentionally verifies that Vibe is present in its parent-process chain.


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
