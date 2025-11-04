# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import subprocess
import time


class ActionSearchGoogleFood(Action):
    """Custom action to open Google and search for nice things to eat"""

    def name(self) -> Text:
        return "action_search_google_food"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        try:
            # Import playwright inside the method to avoid import errors if not installed
            from playwright.sync_api import sync_playwright
            
            # Create a function to search Google
            def search_google():
                with sync_playwright() as p:
                    # Launch browser in headless mode by default
                    # Set headless=False if you want to see the browser
                    browser = p.chromium.launch(headless=False)
                    page = browser.new_page()
                    
                    # Navigate to Google
                    page.goto("https://www.google.com")
                    page.wait_for_load_state("networkidle")
                    
                    # Search for "nice things to eat"
                    # Try to find the search box - Google has different selectors
                    search_box = page.locator('textarea[name="q"], input[name="q"]').first
                    search_box.fill("nice things to eat")
                    search_box.press("Enter")
                    
                    # Wait for results to load
                    page.wait_for_load_state("networkidle")
                    
                    # Take a screenshot for verification
                    page.screenshot(path="/tmp/google_search_results.png")
                    
                    # Keep browser open for a moment
                    page.wait_for_timeout(3000)
                    
                    browser.close()
            
            # Run the search in a separate process to avoid blocking
            import threading
            search_thread = threading.Thread(target=search_google)
            search_thread.start()
            
            dispatcher.utter_message(text="Opening Google and searching for nice things to eat...")
            
        except ImportError:
            dispatcher.utter_message(text="Playwright is not installed. Please install it with: pip install playwright && playwright install chromium")
        except Exception as e:
            dispatcher.utter_message(text=f"An error occurred while searching: {str(e)}")
        
        return []


class ActionCheckOrderStatus(Action):
    """Custom action to check order status"""

    def name(self) -> Text:
        return "action_check_order_status"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # Placeholder implementation
        return []


class ActionAddToCart(Action):
    """Custom action to add items to cart"""

    def name(self) -> Text:
        return "action_add_to_cart"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # Placeholder implementation
        return []
