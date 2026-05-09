fp = r'f:\1. Edit Videos\8.AntiCode\1.Prompt_Image\1.Prompt_Image\core\video_pipeline.py'
with open(fp, 'r', encoding='utf-8') as f:
    content = f.read()

old = (
    '      \\"default_stance\\": \\"stands at attention with shield at side\\"\\n\'\n'
    "    '    }\\n'"
)
new = (
    '      \\"default_stance\\": \\"stands at attention with shield at side\\",\\n\'\n'
    '    \'      \\"sheet_prompt\\": \\"Character reference sheet, clean white background. Full body front view of a [faction] [role]. [visual_description]. Standing in [default_stance]. Bold text label: [label].\\"\\n\'\n'
    "    '    }\\n'"
)

if old in content:
    content = content.replace(old, new)
    with open(fp, 'w', encoding='utf-8') as f:
        f.write(content)
    print("OK — added sheet_prompt to Step 2d output format")
else:
    print("NOT FOUND")
    # Debug
    idx = content.find('default_stance')
    if idx > 0:
        print(repr(content[idx:idx+200]))
