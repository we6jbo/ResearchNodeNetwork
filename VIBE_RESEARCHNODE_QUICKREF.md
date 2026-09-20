# ResearchNodeNetwork Vibe Quick Reference

Vibe should route to ResearchNodeNetwork for:

1. Anything involving the family tree.
2. Anything involving a Homo sapiens tree starting from the 2026 present-day context and going backward through ancestry and outward through connected branches.
3. Accessing the Raspberry Pi for ResearchNodeNetwork.

## Commands

```bash
research-node-network-agent choose-start
research-node-network-agent traverse
research-node-network-agent traverse --start "NAME"
research-node-network-agent traverse --handoff
research-node-network-agent extend-to-pi
research-node-network-agent reach-jeremiah

systemctl --user status research-node-network.service --no-pager
systemctl --user status research-node-network-pi.timer --no-pager
systemctl --user list-timers --all | grep research-node
```

Exact Pi SSH route used by `reach-jeremiah`:

```bash
ssh -i ~/.ssh/t14_to_pi pi@192.168.5.215
```

The SSH command is public documentation. The private key at `~/.ssh/t14_to_pi` is not public and must never be committed or printed.

## Publication privacy

The genealogy graph and TG identifiers are public project data except that the identity layers `Mom`, `Grandma`, and `Grandpa` must remain literal and private.


## Project blog

Building a Living Network

https://j03.page/2026/09/20/building-a-living-network


## Temporary 794 test

Valid only on 2026-09-19 from 22:21:00 through 22:42:59 local time:

```bash
research-node-network-agent test-pi-794
```

Expected remote file:

```text
/home/pi/ResearchNodeNetwork/794.txt
```


## Vibe-only 2779 proof test

Valid only on 2026-09-19 from 22:21:00 through 22:43:59 local time.

Vibe itself must run:

```bash
research-node-network-agent test-vibe-2779
```

The helper refuses if it cannot detect Vibe in its parent-process chain. A successful run creates:

```text
/home/pi/ResearchNodeNetwork/2779.txt
```

with a fresh runtime nonce that does not exist in the repository beforehand.


## Permanent semantic triggers

Vibe should route to ResearchNodeNetwork for natural-language requests matching any of these ideas:

- explore genealogy / branches
- ancestral or family research
- investigate my family
- trace my family history
- research relatives
- find a named person in my tree
- identify who a person is in my family
- find parents, children, descendants, or other relatives
- start from a named person and continue researching
- determine how two people are related
- find descendants
- follow one named person to another connected person in the past or future
- keep expanding from a person
- search for missing people in a branch
- research everyone around a named person
- find who or what connects two people

Exact wording is NOT required. Semantic matches and natural combinations of these ideas should activate ResearchNodeNetwork.
