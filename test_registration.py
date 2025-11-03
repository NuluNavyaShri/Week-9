from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

service = Service("D:\\NAVYA\\devops\\Week-2\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=options)

driver.get("http://localhost:31011")

# Wait for form to load
WebDriverWait(driver, 15).until(
    EC.presence_of_element_located((By.NAME, "full_name"))
)

# Fill form
driver.find_element(By.NAME, "full_name").send_keys("Test User")
driver.find_element(By.NAME, "email").send_keys("testuser@example.com")
driver.find_element(By.NAME, "username").send_keys("testuser")
driver.find_element(By.NAME, "password").send_keys("password123")
driver.find_element(By.NAME, "confirm_password").send_keys("password123")
driver.find_element(By.NAME, "phone").send_keys("9876543210")
driver.find_element(By.NAME, "dob").send_keys("2000-01-01")
driver.find_element(By.NAME, "gender").send_keys("Female")
driver.find_element(By.NAME, "address").send_keys("123 Test Street")

# Scroll to make sure button is visible
submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)

# Wait for button to be clickable
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))

submit_button.click()

print("Form submission test completed successfully.")
driver.quit()

