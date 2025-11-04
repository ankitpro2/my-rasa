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
            # Create a Python script that uses playwright to open Google and search
            script_content = """
from playwright.sync_api import sync_playwright
import time

def search_google():
    with sync_playwright() as p:
        # Launch browser
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        # Navigate to Google
        page.goto("https://www.google.com")
        time.sleep(2)
        
        # Search for "nice things to eat"
        search_box = page.locator('textarea[name="q"], input[name="q"]').first
        search_box.fill("nice things to eat")
        search_box.press("Enter")
        
        # Wait for results to load
        time.sleep(3)
        
        # Keep browser open for a few more seconds
        time.sleep(5)
        
        browser.close()

if __name__ == "__main__":
    search_google()
"""
            
            # Write the script to a temporary file
            with open('/tmp/google_search.py', 'w') as f:
                f.write(script_content)
            
            # Execute the script
            subprocess.Popen(['python', '/tmp/google_search.py'])
            
            dispatcher.utter_message(text="Opening Google and searching for nice things to eat...")
            
        except Exception as e:
            dispatcher.utter_message(text=f"An error occurred: {str(e)}")
        
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
