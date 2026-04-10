# Walkthrough — Rate Limit & Timeout Fixes + Gemini Key UI

## Changes Made (Session 2)

### A. `call_gemini_native()` — Rate Limit + 429 Retry

render_diffs(file:///f:/1.%20Edit%20Videos/8.AntiCode/1.Prompt_Image/1.Prompt_Image/core/api_client.py)

**Before:** No rate limiting, no retry on 429, single attempt only.

**After:**
- **Rate limiting**: 2s minimum delay between Gemini native calls (interruptible)
- **429 retry**: Exponential backoff 5s → 10s, max 2 retries per call
- **500+ retry**: Wait 5s then retry, max 2 retries
- **Timeout retry**: Auto-retry on timeout, max 2 retries
- **Status code**: Returns `status_code` in response for caller to distinguish error types
- **`_interruptible_sleep()`**: Sleeps in 0.5s chunks, checks `stop_check` — user can cancel during wait

### B. `historical_verifier.py` — Smart Key Rotation

**Before:** Try all 7 keys with 0 delay between them.

**After:**
- Max 5 keys (don't burn all)
- After 429 error: wait **10s** before next key
- After other errors: wait **3s** before next key
- Logs which key is being tried: `[VERIFY] Switching to key 2/5...`
- Uses `status_code` from `call_gemini_native()` to distinguish error types

### C. `send_request()` — Dynamic Timeout

**Before:** Fixed 60s timeout for all tiers.

**After:**
- **Flash tier**: 60s (unchanged)
- **Pro tier**: 180s (increased from 60s — Pro models need more time for long prompts)

### D. Gemini API Key UI — Header Button + Dialog

**New UI elements:**
- 🔑 Gemini API Key button (amber/orange) in header bar
- Badge showing key count: `(7 keys)`
- Dialog with:
  - Key list (masked: `AIzaSyAh•••••••pHw`)
  - Add key input with paste support
  - 👁/🙈 toggle to show/hide real keys
  - Remove Selected button
  - OK (saves to `gemini_keys.json`) / Cancel

| File | Change |
|---|---|
| [api_client.py](file:///f:/1.%20Edit%20Videos/8.AntiCode/1.Prompt_Image/1.Prompt_Image/core/api_client.py) | `_interruptible_sleep()`, `_gemini_last_call`, 429 retry, `save_gemini_keys()`, dynamic timeout |
| [historical_verifier.py](file:///f:/1.%20Edit%20Videos/8.AntiCode/1.Prompt_Image/1.Prompt_Image/core/historical_verifier.py) | Smart key rotation with 429-aware delays |
| [main_window.py](file:///f:/1.%20Edit%20Videos/8.AntiCode/1.Prompt_Image/1.Prompt_Image/ui/main_window.py) | Gemini Key button + dialog + badge |

## What Was Tested
- All imports pass: `APIClient`, `ProcessController`, `MainWindow`, `historical_verifier`
- `_gemini_last_call` initialized to 0.0
- `_interruptible_sleep` method exists on APIClient
- `load_gemini_keys()` correctly loads 7 keys
- `save_gemini_keys()` function available
