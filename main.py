import sys
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import (ElementClickInterceptedException,
                                        NoSuchElementException, TimeoutException)
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

SIMILAR_ACCOUNT = "pythonlearnerr"
USERNAME = "0616ingeduardoo"
PASSWORD = "Ed061600126"


class InstaFollower:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.wait = WebDriverWait(self.driver, 15)

    def login(self):
        # This method is confirmed to be working perfectly.
        self.driver.get("https://www.instagram.com/accounts/login/")
        try:
            print("Entering credentials...")
            username_input = self.wait.until(EC.presence_of_element_located((By.NAME, "username")))
            password_input = self.driver.find_element(By.NAME, "password")
            username_input.send_keys(USERNAME)
            password_input.send_keys(PASSWORD)
            time.sleep(1)
            password_input.send_keys(Keys.ENTER)
            try:
                save_info_prompt = WebDriverWait(self.driver, 5).until(
                    EC.element_to_be_clickable((By.XPATH, "//div[text()='Not now']")))
                save_info_prompt.click()
                print("Dismissed 'Save Info' prompt.")
            except TimeoutException:
                print("'Save Info' prompt did not appear, which is fine.")
            try:
                notifications_prompt = WebDriverWait(self.driver, 5).until(
                    EC.element_to_be_clickable((By.XPATH, "//button[text()='Not Now']")))
                notifications_prompt.click()
                print("Dismissed 'Notifications' prompt.")
            except TimeoutException:
                print("'Notifications' prompt did not appear, which is fine.")
            self.wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Search']")))
            print("Login successful. Home page is loaded.")
            return True
        except Exception as e:
            print(f"An critical error occurred during login.")
            self.driver.save_screenshot("login_failure.png")
            print(f"Saved a screenshot as 'login_failure.png' to help you see what the page looked like.")
            return False

    def find_and_scroll_followers(self):
        """Finds the followers pop-up and scrolls it."""
        print(f"\nNavigating to {SIMILAR_ACCOUNT}'s profile page...")
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}/")
        try:
            followers_link = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, f"//a[contains(@href, '/followers/')]")))
            print("Found followers link. Clicking to open the list.")
            followers_link.click()
            self.wait.until(EC.presence_of_element_located((By.XPATH, "//div[@role='dialog']")))
            print("Dialog found, waiting 1 second for content to stabilize...")
            time.sleep(1)

            # THE FIX: Using the class name we discovered.
            scrollable_div_xpath = "//div[contains(@class, 'x1i10hfl')]"
            scrollable_div = self.wait.until(EC.presence_of_element_located((By.XPATH, scrollable_div_xpath)))
            print("SUCCESS! Found the scrollable followers list. Starting to scroll.")

            for i in range(5):
                print(f"Scrolling followers list... {i + 1}/5")
                self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scrollable_div)
                time.sleep(2.5)
            return True
        except TimeoutException:
            print("A step failed while trying to open and scroll the followers list.")
            return False

    def follow_users(self):
        """Finds and clicks follow buttons using a robust JavaScript click."""
        print("\nFinding 'Follow' buttons...")
        try:
            follow_buttons_xpath = "//button[.//div[text()='Follow']]"
            all_buttons = self.driver.find_elements(By.XPATH, follow_buttons_xpath)

            if not all_buttons:
                print("No 'Follow' buttons were found after scrolling.")
                return

            print(f"Found {len(all_buttons)} 'Follow' buttons to click.")

            followed_count = 0
            for button in all_buttons:
                try:
                    # THE FIX: Use a JavaScript click, which is more powerful and reliable.
                    self.driver.execute_script("arguments[0].click();", button)
                    followed_count += 1
                    print(f"Clicked 'Follow' ({followed_count}/{len(all_buttons)}).")
                    time.sleep(1.5)  # A short sleep to not seem too robotic.
                except Exception as e:
                    # DEBUGGING: Print the specific error to see why it failed.
                    print(f"Could not click a button. Skipping. Error: {e}")

        except Exception as e:
            print(f"An error occurred in the follow_users method: {e}")


# --- Main Script Execution (Final Version) ---
bot = InstaFollower()

if bot.login():
    if bot.find_and_scroll_followers():
        bot.follow_users()
    else:
        print("Stopping script because followers could not be found or scrolled.")
else:
    print("Stopping script because login failed.")

print("\nBot has finished its run.")
# bot.driver.quit()