import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time


@pytest.fixture(scope="module")
def setup_browser():
    # Setup: Initialize the WebDriver
    s = Service(r"C:\chromedriver.exe")  # Replace with your actual path to chromedriver
    driver = webdriver.Chrome(service=s)
    driver.maximize_window()
    yield driver
    # Teardown: Close the browser after tests are done
    driver.quit()


def test_apple_store_checkout(setup_browser):
    driver = setup_browser

    # Step 1: Open the Apple India store
    driver.get("https://www.apple.com/in/store")

    # Step 2: Click on the search icon
    search_icon = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@id='globalnav-menubutton-link-search']"))
    )
    search_icon.click()

    # Step 3: Wait for the search input to be visible
    search_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "globalnav-searchfield-input"))
    )

    # Step 4: Type 'EarPods' in the search box
    search_input.send_keys("EarPods")

    # Step 5: Press Enter to trigger the search
    search_input.send_keys(Keys.RETURN)

    # Wait for the product to be clickable and select the product
    product = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR,
                                    "body > div:nth-child(3) > div:nth-child(11) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > section:nth-child(1) > div:nth-child(1)"))
    )
    product.click()

    # Wait for the "Add to Cart" button and click it
    add_to_cart_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "add-to-cart"))
    )
    add_to_cart_button.click()

    # Wait for the checkout button and click it
    checkout_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[id='shoppingCart.actions.navCheckout']"))
    )
    checkout_button.click()

    # Wait for the "Guest Login" button and click it
    guest_login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "signIn.guestLogin.guestLogin"))
    )
    guest_login_button.click()

    # Wait for the continue button and click it
    continue_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#rs-checkout-continue-button-bottom"))
    )
    continue_button.click()

    # Wait for the address fields and fill them
    first_name = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "input[id='checkout.shipping.addressSelector.newAddress.address.firstName']"))
    )
    first_name.send_keys("Daniya")

    last_name = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "input[id='checkout.shipping.addressSelector.newAddress.address.lastName']"))
    )
    last_name.send_keys("Fathima")

    street_address = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "input[id='checkout.shipping.addressSelector.newAddress.address.street']"))
    )
    street_address.send_keys("krishna residency honagasandra")

    email_address = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "input[id='checkout.shipping.addressContactEmail.address.emailAddress']"))
    )
    email_address.send_keys("daniya@gmail.com")

    mobile_phone = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "input[id='checkout.shipping.addressContactPhone.address.mobilePhone']"))
    )
    mobile_phone.send_keys("8861682141")

    # Continue to the next step
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#rs-checkout-continue-button-bottom"))
    ).click()

    # Wait for the billing options to be visible and select the credit card option
    credit_card_option = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "label[id='checkout.billing.billingoptions.credit_label'] span[class='row']"))
    )
    credit_card_option.click()

    # Fill in credit card details
    credit_card_number = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR,
                                          "input[id='checkout.billing.billingOptions.selectedBillingOptions.creditCard.cardInputs.cardInput-0.cardNumber']"))
    )
    credit_card_number.send_keys("4594530123970295")

    expiration_date = driver.find_element(By.CSS_SELECTOR,
                                          "input[id='checkout.billing.billingOptions.selectedBillingOptions.creditCard.cardInputs.cardInput-0.expiration']")
    expiration_date.send_keys("11/25")

    security_code = driver.find_element(By.CSS_SELECTOR,
                                        "input[id='checkout.billing.billingOptions.selectedBillingOptions.creditCard.cardInputs.cardInput-0.securityCode']")
    security_code.send_keys("980")

    # Proceed to the next step
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#rs-checkout-continue-button-bottom"))
    ).click()

    time.sleep(10)

    # Wait for the terms and conditions checkbox and click it
    driver.find_element(By.XPATH, "//input[@class='form-checkbox-input']").click()
    time.sleep(2)

    # Final confirmation step
    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#rs-checkout-continue-button-bottom"))
    ).click()

    time.sleep(25)
