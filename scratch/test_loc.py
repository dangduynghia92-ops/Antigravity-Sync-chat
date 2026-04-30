from core.video_pipeline import _parse_location_style
loc = _parse_location_style('Chibi Storybook Historical', 'video_styles')
print(f"Length: {len(loc)}")
print(f"Content: [{loc}]")
print(f"Has Mandatory: {'Mandatory' in loc}")
print(f"Has Negative: {'Negative' in loc}")
