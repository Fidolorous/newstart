from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def init_driver():
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(service=service, options=options)
    return driver

def login(driver, username, password, login_url):
    driver.get(login_url)
    
    # Adjust these selectors to match the login form of your insurance provider's website
    username_field = driver.find_element(By.ID, "username") 
    password_field = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "loginButton")

    username_field.send_keys(username)
    password_field.send_keys(password)
    login_button.click()

    # Wait for login to complete, adjust as necessary
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "dashboard")))

def upload_invoice(driver, invoice_file_path, invoice_category):
    # Navigate to invoice submission section
    driver.get("https://my.allianzcare.com/myhealth/1/home/claims/list")

    # Adjust these selectors to match the invoice submission form
    category_dropdown = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "categoryDropdown"))
    )
    file_upload_input = driver.find_element(By.ID, "fileUploadInput")
    submit_button = driver.find_element(By.ID, "submitButton")

    category_dropdown.send_keys(invoice_category)
    file_upload_input.send_keys(invoice_file_path)
    submit_button.click()

    # Confirm submission, adjust as necessary
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "submissionConfirmation")))

def main():
    driver = init_driver()

    try:
        login_url = "https://my.allianzcare.com/myhealth/1/log"
        username = "gergely.szabo.mk@gmail.com"
        password = "concorde654XX#"
        invoice_file_path = "/path/to/your/invoice.pdf"
        invoice_category = "Healthcare"

        login(driver, username, password, login_url)
        upload_invoice(driver, invoice_file_path, invoice_category)

        print("Invoice submitted successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
