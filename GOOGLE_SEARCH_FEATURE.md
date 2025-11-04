# Google Search Feature Documentation

## Overview
This feature adds the ability for the Rasa chatbot to open Google and search for "nice things to eat" when a user requests it.

## Components Added

### 1. Intent: `search_nice_food`
**Location:** `data/nlu.yml`

This intent recognizes when users want to search for nice food options. Example phrases:
- "search for nice things to eat"
- "find nice food"
- "look for good food"
- "search nice things to eat on google"
- "open google and search for nice food"

### 2. Custom Action: `action_search_google_food`
**Location:** `actions/actions.py`

This custom action uses Playwright to:
1. Launch a Chromium browser
2. Navigate to https://www.google.com
3. Search for "nice things to eat"
4. Wait for results to load
5. Take a screenshot for verification
6. Keep the browser open briefly before closing

The action runs in a separate thread to avoid blocking the Rasa conversation.

### 3. Responses
**Location:** `domain.yml`

Two responses were added:
- `utter_search_started`: Informs the user that the search is starting
- `utter_search_complete`: Confirms the search is complete

### 4. Story: `search_nice_food`
**Location:** `data/stories.yml`

Defines the conversation flow:
1. User expresses intent to search for nice food
2. Bot acknowledges and starts the search
3. Bot executes the search action
4. Bot confirms completion

### 5. Test Story
**Location:** `tests/test_stories.yml`

A test story validates the conversation flow.

## Installation Requirements

### Prerequisites
1. Python 3.8-3.11 (for Rasa compatibility)
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Install Playwright browsers:
   ```bash
   playwright install chromium
   ```

## Usage

### Running the Chatbot

1. Train the model:
   ```bash
   rasa train
   ```

2. Start the action server:
   ```bash
   rasa run actions
   ```

3. In a separate terminal, start the Rasa shell:
   ```bash
   rasa shell
   ```

4. Interact with the bot:
   ```
   User: search for nice things to eat
   Bot: I'm opening Google to search for nice things to eat. Please wait...
   Bot: Opening Google and searching for nice things to eat...
   Bot: I've completed the search on Google for nice things to eat!
   ```

## Technical Details

### Browser Configuration
- **Browser:** Chromium (via Playwright)
- **Mode:** Non-headless by default (set `headless=False` to see the browser)
- **Screenshot:** Saved to `/tmp/google_search_results.png`

### Error Handling
The action includes error handling for:
- Missing Playwright installation
- Browser launch failures
- Network errors
- General exceptions

### Threading
The search runs in a separate thread to prevent blocking the Rasa conversation loop.

## Troubleshooting

### Issue: Playwright not installed
**Solution:** Run `pip install playwright && playwright install chromium`

### Issue: Browser doesn't open
**Solution:** Ensure you have a graphical environment or set `headless=True` in the action code

### Issue: Google blocked
**Solution:** Some networks may block automated access to Google. Try using a VPN or different network.

## Files Modified

1. `domain.yml` - Added intent, responses, and action
2. `data/nlu.yml` - Added training examples for search_nice_food intent
3. `data/stories.yml` - Added conversation flow story
4. `actions/actions.py` - Implemented the custom action
5. `requirements.txt` - Added playwright dependency
6. `tests/test_stories.yml` - Added test story

## Merge Conflicts Resolved

The following merge conflicts were resolved:
- `domain.yml`: Chose proper variable interpolation syntax `{order_status}` and `{product_name}`
- `data/nlu.yml`: Merged duplicate intent definitions
- `data/stories.yml`: Merged story definitions and added happy path story

## Future Enhancements

Potential improvements:
1. Make the search query configurable by extracting entities from user input
2. Parse and return search results to the user
3. Add support for different search engines
4. Implement screenshot capture and image processing
5. Add options for voice search or specific cuisine types
