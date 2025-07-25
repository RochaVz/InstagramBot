Instagram Follower Bot
This Python script uses the Selenium library to automate the process of following users on Instagram. It logs into a specified account, navigates to the followers list of a target account, and then follows a number of users from that list.

This project is intended for educational purposes to demonstrate web scraping and automation with Selenium.

Features
Secure Login: Logs into an Instagram account and handles common pop-ups like "Save Info" and "Turn on Notifications".
Targeted Following: Navigates to a specified "similar" account to find relevant users to follow.
Dynamic Scrolling: Automatically scrolls through the followers list to load more users.
Robust Following: Clicks the "Follow" button for users in the list.
Resilient and Maintainable: Uses explicit waits and robust selectors to handle page load times and minor UI changes. Includes clear print statements for easy debugging.

How It Works
The script is built around the InstaFollower class, which encapsulates all the bot's functionality into three main methods:
login(): Opens Instagram, enters the user credentials, and handles the various login pop-ups to get to the main feed.
find_and_scroll_followers(): Navigates to the target account's profile page, clicks on their "followers" list to open the pop-up modal, and then scrolls down a set number of times to load more users into the view.
follow_users(): After the list is loaded, this method finds all the "Follow" buttons currently visible and clicks them one by one, with short pauses in between to mimic human behavior and avoid being rate-limited.

Getting Started
Prerequisites
Python 3.x
Google Chrome browser installed
pip (Python package installer)
Installation
Clone the repository or download the script:
Save the main.py file to a new project folder.
Set up a virtual environment (recommended):
Generated sh
# On Windows
python -m venv .venv
.\.venv\Scripts\activate

# On macOS/Linux
python3 -m venv .venv
source .venv/bin/activate
Use code with caution.
Sh
Install the required Python packages:
Generated sh
pip install selenium
Use code with caution.
Sh
Download the correct ChromeDriver:
Selenium requires a WebDriver to interface with the Chrome browser.
Check your Chrome browser version (Settings -> About Chrome).
Download the matching ChromeDriver from the Chrome for Testing availability dashboard.
Unzip the downloaded file and place chromedriver.exe (or chromedriver on macOS/Linux) in your project folder or in a location included in your system's PATH. Note: Newer versions of Selenium can manage this for you, but placing it manually is reliable.
Configuration
Before running the script, you must configure your account details at the top of the main.py file:
Generated python
# The Instagram account whose followers you want to target
SIMILAR_ACCOUNT = "pythonlearnerr" 

# Your Instagram login credentials
USERNAME = "YOUR_INSTAGRAM_USERNAME"
PASSWORD = "YOUR_INSTAGRAM_PASSWORD"
Use code with caution.
Python
Warning: Storing credentials directly in the code is not secure for production applications. For personal projects, ensure this file is kept private.
Running the Script
Once everything is set up and configured, run the script from your terminal:
Generated sh
python main.py
Use code with caution.
Sh
A new Chrome browser window will open and the bot will begin its tasks. You can watch its progress in the terminal output.
Code Overview
Generated python
# Import necessary libraries
import sys
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import (ElementClickInterceptedException,
                                        NoSuchElementException, TimeoutException)
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# --- CONFIGURATION ---
SIMILAR_ACCOUNT = "pythonlearnerr"
USERNAME = "0616ingeduardoo"
PASSWORD = "Ed061600126"

# --- MAIN CLASS ---
class InstaFollower:
    # ... (methods described below) ...

# --- SCRIPT EXECUTION ---
bot = InstaFollower()
if bot.login():
    if bot.find_and_scroll_followers():
        bot.follow_users()
    # ... (error handling) ...
Use code with caution.
Python
Key Methods
__init__(): Initializes the Selenium WebDriver, keeping the browser open after the script finishes (detach option).
login(): A sequential, robust login process that waits for and handles optional pop-ups. It confirms success by finding the "Search" input bar on the main page.
find_and_scroll_followers(): This is the most fragile part of the script. It relies on a specific class name for the scrollable followers list (x1i110hfl). This class name will change over time.
follow_users(): Uses a powerful XPath (//button[.//div[text()='Follow']]) to find "Follow" buttons. This is very stable because it relies on the button's visible text, not on changing class names. It also uses a JavaScript click for higher reliability.
Maintenance and Troubleshooting
Web scraping scripts are fragile because websites like Instagram change their layout and HTML structure frequently.
The most common point of failure will be the find_and_scroll_followers() method.
If the script fails to find the followers list, you will see this error:
A step failed while trying to open and scroll the followers list.
To fix this:
Run the script and let it open the followers list pop-up.
In the Chrome window, right-click on the scrollable area of the list and choose "Inspect".
Find the <div> element that contains the list of followers. Look at its class attribute.
Copy the new class name (e.g., xsome_new_class).
Update the scrollable_div_xpath variable inside the find_and_scroll_followers() method with the new class name:
Generated python
# Before
scrollable_div_xpath = "//div[contains(@class, 'x1i10hfl')]"

# After (example)
scrollable_div_xpath = "//div[contains(@class, 'xsome_new_class')]"
Use code with caution.
Python
This process of inspecting and updating selectors is a fundamental skill for web scraping.
Disclaimer
This script is for educational purposes only. Automating interactions on Instagram may be against their Terms of Service. Use this script responsibly and at your own risk. The author is not responsible for any account restrictions or bans that may occur. Avoid running the bot too frequently or following too many users in a short period.
