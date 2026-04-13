# Biography Pipeline Protection Rule

## MANDATORY CHECK
Before modifying ANY shared code or prompt in the narrative pipeline:

1. **Identify if the change touches shared code** — functions used by ALL niches:
   - `_extract_chapter_blueprint()`
   - `_extract_style_for_framework()`
   - `write_from_blueprint()`
   - `research_blueprint_multicall()`
   - `_run_enrich_phase()`
   - `_NICHE_OUTLINE_FIELDS`
   - `_NICHE_PROMPT_MAP`
   - Any function in `rewriter.py` that does NOT have niche-specific branching

2. **If yes → MUST verify biography is unaffected** before applying:
   - Does biography hook still receive FULL blueprint?
   - Does fuzzy search fallback still work for biography?
   - Does research still degrade gracefully (draft fallback) for biography?
   - Are biography-specific fields (`life_phases`, `key_relationships`, `myths_vs_reality`, `dual_nature`) still handled?

3. **Use explicit niche branching** — never change shared behavior:
   ```python
   if _is_battle:
       # battle-specific logic
   elif _is_biography:
       # biography-specific logic
   else:
       raise RuntimeError("Niche not configured — add branch here")
   ```

4. **Never silently remove fallbacks** in shared code. If removing a fallback for one niche, keep it for others.

## Key Files
- `core/rewriter.py` — core pipeline logic
- `ui/script_creation_tab.py` — pipeline orchestration (phase plan, validate, split)
- `styles/narrative_tiểu_sử_nhân_vật.json` — biography style config
- `prompts/system_research_blueprint_biography.txt` — biography research prompt
- `prompts/system_narrative_write_biography.txt` — biography write prompt

## Root Cause (2026-04-13)
Battle v2 was added by modifying shared code instead of adding niche-specific branches.
This broke biography in 4 ways:
1. Hook chapters lost full blueprint (filtered to ~2K chars)
2. Empty filter results crashed instead of fallback
3. Draft failures crashed instead of continuing with partial data
4. Expand failures crashed instead of using draft fallback
