from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select, WebDriverWait

# Configure Chrome options to reduce bot detection
options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument(
    "user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
)

driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 15)

try:
    # 1. Open and Maximize Window
    driver.maximize_window()

    # 2. Open Amazon.ca
    driver.get("https://www.amazon.ca")

    # 3. Search for product
    search_box = wait.until(
        EC.element_to_be_clickable((By.ID, "twotabsearchtextbox"))
    )
    search_box.clear()
    search_box.send_keys("leather shoes for men")
    search_box.send_keys(Keys.RETURN)

    # 4. Wait for search results container to load
    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[contains(@class, 's-result-item')]")
        )
    )

    # Scroll incrementally to trigger lazy loading of product items
    for _ in range(3):
        driver.execute_script("window.scrollBy(0, 100);")
        sleep(1)

    # Locate product title links
    xpath_candidates = [
        "//div[@data-component-type='s-search-result']//h2/a",
        "//div[contains(@class, 's-result-item')]//h2/a",
        "//div[@data-component-type='s-search-result']//a[contains(@class, 'a-text-normal')]",
        "//a[contains(@class, 'a-link-normal s-line-clamp')]",
    ]

    search_results = []
    for xpath in xpath_candidates:
        found_elements = driver.find_elements(By.XPATH, xpath)
        visible_elements = [el for el in found_elements if el.is_displayed()]
        if len(visible_elements) >= 4:
            search_results = visible_elements
            break

    if len(search_results) >= 4:
        print(f"Found {len(search_results)} search results. Selecting the 4th item...")
        driver.execute_script("arguments[0].click();", search_results[3])
    else:
        raise Exception(
            f"Only located {len(search_results)} items."
        )

    sleep(3)

    # 5. Select Size & Color
    try:
        size_dropdown_element = driver.find_element(
            By.ID, "native_dropdown_selected_size_name"
        )
        size_dropdown = Select(size_dropdown_element)
        if len(size_dropdown.options) > 1:
            size_dropdown.select_by_index(1)
            sleep(2)
    except Exception:
        try:
            size_tiles = driver.find_elements(
                By.XPATH,
                "//li[contains(@id, 'size_name_') and not(contains(@class, 'swatchUnavailable'))]//button",
            )
            if size_tiles:
                driver.execute_script("arguments[0].click();", size_tiles[0])
                sleep(2)
        except Exception:
            pass

    # 6. Select Quantity (2)
    try:
        qty_element = driver.find_element(By.ID, "quantity")
        Select(qty_element).select_by_value("2")
        sleep(1)
    except Exception:
        pass

    # 7. Add to Cart
    try:
        buybox = driver.find_element(
            By.XPATH, "//div[@id='rightCol'] | //div[@id='buyBoxAccordion']"
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", buybox)
        sleep(1)
    except Exception:
        pass

    add_cart_xpath = (
        "//input[@id='add-to-cart-button'] | "
        "//input[@name='submit.add-to-cart'] | "
        "//button[@id='add-to-cart-button'] | "
        "//span[@id='submit.add-to-cart']//input"
    )
    add_to_cart_btn = wait.until(
        EC.presence_of_element_located((By.XPATH, add_cart_xpath))
    )
    driver.execute_script("arguments[0].click();", add_to_cart_btn)

    print("Product successfully added to cart.")
    sleep(3)

    # 8. Open Cart and Conditionally Reduce Quantity (Only if current quantity == 2)
    driver.get("https://www.amazon.ca/gp/cart/view.html")
    sleep(2)

    try:
        current_qty = None

        # Check for Stepper UI decrement button or text
        decrement_btn_xpath = (
            "//button[@data-a-selector='decrement'] | "
            "//button[@data-action='a-stepper-decrement'] | "
            "//button[contains(@aria-label, 'Decrease quantity')]"
        )
        decrement_buttons = driver.find_elements(By.XPATH, decrement_btn_xpath)

        # 1. Parse quantity from decrement button's aria-label or UI text
        if decrement_buttons and decrement_buttons[0].is_displayed():
            aria_label = decrement_buttons[0].get_attribute("aria-label") or ""
            if "Quantity is 2" in aria_label:
                current_qty = 2
            elif "Quantity is 1" in aria_label:
                current_qty = 1

        # 2. Fallback: Parse quantity from value element
        if current_qty is None:
            value_elements = driver.find_elements(
                By.XPATH, "//span[@data-a-selector='value']"
            )
            for ve in value_elements:
                if ve.text.strip().isdigit():
                    current_qty = int(ve.text.strip())
                    break

        # 3. Fallback: Parse quantity from standard dropdown
        qty_dropdowns = driver.find_elements(By.NAME, "quantity")
        if current_qty is None and qty_dropdowns and qty_dropdowns[0].is_displayed():
            select = Select(qty_dropdowns[0])
            current_qty = int(select.first_selected_option.text.strip())

        print(f"Detected cart quantity: {current_qty}")

        # Perform reduction only if quantity is 2
        if current_qty == 2:
            if decrement_buttons and decrement_buttons[0].is_displayed():
                driver.execute_script("arguments[0].click();", decrement_buttons[0])
                print("Quantity was 2. Successfully decremented to 1.")
                sleep(3)
            elif qty_dropdowns and qty_dropdowns[0].is_displayed():
                Select(qty_dropdowns[0]).select_by_value("1")
                print("Quantity was 2. Updated quantity to 1 via dropdown.")
                sleep(3)
        elif current_qty == 1:
            print("Quantity in cart is 1. Skipping reduction.")
        else:
            print("Could not definitively verify quantity; skipping reduction to prevent accidental item removal.")

    except Exception as e:
        print(f"Error checking/updating cart quantity: {e}")

    # 9. Proceed to Checkout
    checkout_btn = wait.until(
        EC.presence_of_element_located((By.NAME, "proceedToRetailCheckout"))
    )
    driver.execute_script("arguments[0].click();", checkout_btn)
    print("Navigated to checkout screen.")
    sleep(3)

finally:
    driver.quit()
