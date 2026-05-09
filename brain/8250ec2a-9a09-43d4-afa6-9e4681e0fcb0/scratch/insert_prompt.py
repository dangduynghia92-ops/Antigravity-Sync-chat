import os

fp = r'f:\1. Edit Videos\8.AntiCode\1.Prompt_Image\1.Prompt_Image\core\video_pipeline.py'
with open(fp, 'r', encoding='utf-8') as f:
    content = f.read()

# Find insertion point
marker = 'STEP2_CHARACTERS_SYSTEM_PROMPT'
idx = content.find(marker)
print(f"Marker at char: {idx}")

NEW_PROMPT = '''

# ═══════════════ Step 2d: Crowd Character Sheets ═══════════════
STEP2D_CROWD_PROMPT = (
    "You are a Visual Character Designer creating CHARACTER MODEL SHEETS "
    "for CROWD/EXTRAS characters in animation production.\\n\\n"
    "## INPUT\\n"
    "- A list of `crowd_types` identified from the script (unnamed background characters)\\n"
    "- World Bible `crowd_archetypes` with costume descriptions per faction\\n"
    "- Era and geography context\\n\\n"
    "## YOUR JOB\\n"
    "For each crowd type, create a character sheet with a unique label and detailed visual description.\\n"
    "Use the World Bible\\'s crowd_archetypes as your PRIMARY costume reference. Adapt and expand as needed.\\n\\n"
    "## LABEL CONVENTION\\n"
    "Use this format: `EXT-{Faction}-{Role}-{Variant}`\\n"
    "- `EXT-` prefix is MANDATORY (marks this as a crowd character)\\n"
    "- Faction = short faction name (e.g., Ayyubid, Crusader, Assassin, Templar)\\n"
    "- Role = general role (e.g., Soldier, Guard, Civilian, Merchant)\\n"
    "- Variant = specific type (e.g., Infantry, Cavalry, Sentry, Laborer)\\n"
    "- No age variant needed (crowd characters are archetypes)\\n\\n"
    "Examples: `EXT-Ayyubid-Soldier-Infantry`, `EXT-Crusader-Knight-Heavy`, `EXT-Assassin-Agent-Fidai`\\n\\n"
    "## OUTPUT\\n"
    "Return a JSON object:\\n"
    "```json\\n"
    '{\\n'
    '  \\"characters\\": [\\n'
    '    {\\n'
    '      \\"label\\": \\"EXT-Ayyubid-Soldier-Infantry\\",\\n'
    '      \\"group\\": \\"CROWD\\",\\n'
    '      \\"faction\\": \\"Ayyubid Army\\",\\n'
    '      \\"crowd_type\\": \\"soldier\\",\\n'
    '      \\"visual_description\\": \\"BODY: [height in heads, build]. COSTUME: Head: [headwear]. Upper: [garment]. Lower: [garment]. Feet: [footwear]. Acc: [accessories, weapons].\\",\\n'
    '      \\"default_stance\\": \\"stands at attention with shield at side\\"\\n'
    '    }\\n'
    '  ]\\n'
    '}\\n'
    "```\\n\\n"
    "## RULES\\n"
    "1. Create ONE character sheet per unique crowd type + faction combination\\n"
    "2. `visual_description` MUST follow the format: BODY -> COSTUME (Head -> Upper -> Lower -> Feet -> Acc)\\n"
    "3. Do NOT describe face shape, face color/fill, eye rendering - those are controlled by the art style\\n"
    "4. FACE section: ONLY identity features (beard style, scars, helmet covering face, etc.)\\n"
    "5. Use SPECIFIC materials, colors, and item names - NEVER vague terms\\n"
    "6. If a crowd type exists in multiple factions, create SEPARATE entries per faction\\n"
    "7. `default_stance` describes the character\\'s typical pose/action in one sentence\\n"
    "8. ALL descriptions must be historically accurate for the era and geography\\n\\n"
    "Return ONLY the JSON, no explanation."
)


'''

# Insert before marker
new_content = content[:idx] + NEW_PROMPT + content[idx:]

with open(fp, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Inserted STEP2D_CROWD_PROMPT successfully")
