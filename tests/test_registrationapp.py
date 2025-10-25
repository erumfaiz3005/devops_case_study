import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time


# Fixture for setting up and tearing down the driver
@pytest.fixture
def setup_teardown():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    yield driver
    driver.quit()


# Test 1: Home page loads correctly
def test_home_page(setup_teardown):
    driver = setup_teardown
    driver.get("http://127.0.0.1:5000/")
    time.sleep(1)
    assert "Welcome to My Website" in driver.page_source
    assert "Home" in driver.title or "My Website" in driver.title


# Test 2: About page loads correctly
def test_about_page(setup_teardown):
    driver = setup_teardown
    driver.get("http://127.0.0.1:5000/about")
    time.sleep(1)
    assert "About" in driver.page_source
    assert "simple 3-page Flask application" in driver.page_source


# Test 3: Contact page loads correctly
def test_contact_page(setup_teardown):
    driver = setup_teardown
    driver.get("http://127.0.0.1:5000/contact")
    time.sleep(1)
    assert "Contact" in driver.page_source
    assert "You can reach out using the form below" in driver.page_source


# Test 4: Navigation links work correctly between pages
def test_navigation_links(setup_teardown):
    driver = setup_teardown
    driver.get("http://127.0.0.1:5000/")

    # Click on About link
    about_link = driver.find_element(By.LINK_TEXT, "About")
    about_link.click()
    time.sleep(1)
    assert "/about" in driver.current_url

    # Click on Contact link
    contact_link = driver.find_element(By.LINK_TEXT, "Contact")
    contact_link.click()
    time.sleep(1)
    assert "/contact" in driver.current_url

    # Click back to Home
    home_link = driver.find_element(By.LINK_TEXT, "Home")
    home_link.click()
    time.sleep(1)
    assert driver.current_url.endswith("/")


# Test 5: Contact form elements exist
def test_contact_form_elements(setup_teardown):
    driver = setup_teardown
    driver.get("http://127.0.0.1:5000/contact")
    time.sleep(1)

    # Verify that form fields exist
    name_field = driver.find_element(By.ID, "name")
    email_field = driver.find_element(By.ID, "email")
    message_field = driver.find_element(By.ID, "message")
    submit_button = driver.find_element(By.TAG_NAME, "button")

    assert name_field is not None
    assert email_field is not None
    assert message_field is not None
    assert submit_button.text.lower() == "send"
