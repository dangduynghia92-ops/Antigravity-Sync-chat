# AI API Resilience: Multi-Endpoint and Rate-Limit Handling

For content creation systems requiring high availability, a singular API endpoint is a point of failure. The architecture employs a multi-layered resilience strategy.

## Multi-Endpoint Fallback

The **`APIClient`** manages a list of endpoints (e.g., Primary + Fallbacks). Each endpoint entry includes:
- `base_url` (OpenAI-compatible chat/completions).
- `api_key`.
- `flash_model` and `pro_model` identifiers.

### The Switching Logic
1. Attempt a request on the current "Active" endpoint.
2. If hit with a **429 (Rate Limit)** or **Timeout**:
   - Log the failure and mark the endpoint's last failure time.
   - Immediately switch to the next available enabled endpoint in the list.
   - Retry the request.
3. If all endpoints in a round fail: Apply an exponential backoff (e.g., 5s, 10s, 15s) and start a new round of attempts.

## Intelligent Tier Selection

The system supports selecting between **"Flash" (Standard)** and **"Pro" (High-Quality)** models.
- **Automatic Fallback within Endpoint**: If an endpoint is missing a specific "Pro" model ID, it should fallback to its "Flash" model rather than failing the call entirely.
- **Forced Pro-Tier Tasks**: Critical analytical steps (e.g., "Visual Bible" generation or "Narrative Review") should be hard-coded to use the **Pro** tier regardless of user settings to ensure the highest analytical baseline for the rest of the generation.

## Rate-Limit Recovery Popups (Interactive)

When **ALL** endpoints have failed after multiple retry rounds, the system should not simply crash. Instead, it triggers an interactive recovery flow:
1. The background thread blocks and signals the main thread.
2. The UI shows a modal dialog with 3 choices:
   - **🔄 Retry**: Re-enables all disabled endpoints; allows the user to add a *new* API key inline before retrying.
   - **⏭ Skip**: Skips the current failing segment and continues to the next.
   - **⏹ Stop & Save**: Gracefully stops the process and ensures all *already generated* content is saved to disk.
3. Once the user decides, the signal returns the choice to the background thread to resume or terminate.

## Interactive Cancellation (The `stop_check` Pattern)

To ensure the "Stop" button is immediately responsive even during long-running API tasks, the system implements a **`stop_check`** pattern:

1. **The Callback**: Generators and clients accept a `stop_check` callable (e.g., `lambda: self._stop_flag`).
2. **Interruptible Sleep Helper**: Native `time.sleep(N)` is not interruptible. The system uses a helper:
   ```python
   def _interruptible_sleep(seconds, stop_check):
       if not stop_check: 
           time.sleep(seconds); return True
       end_t = time.time() + seconds
       while time.time() < end_t:
           if stop_check(): return False
           time.sleep(min(0.5, end_t - time.time()))
       return True
   ```
3. **The Blocking Call Limitation**: Since standard `requests.post` is synchronous, a stop request cannot interrupt a mid-flight network request. The stop is only detected **between attempts**, **during backoff sleeps**, or **immediately after** the block returns.
4. **Discarding Results**: If `stop_check()` returns true immediately after a 200 response returns, the result is discarded, and the state is NOT saved to disk to prevent corrupted outputs.
