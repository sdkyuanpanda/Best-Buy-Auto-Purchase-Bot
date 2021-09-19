from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import info

atcList = []

# make sure this path is correct
#PATH = "C:\Program Files (x86)\ChromeDriver\chromedriver.exe"
PATH = "/usr/bin/chromedriver"
driver = webdriver.Chrome(PATH)

def atcBtn():
    atcBtn = driver.find_element_by_css_selector(".add-to-cart-button")

def gtcBtn():
    gtcBtn = driver.find_element_by_css_selector(".go-to-cart-button .btn-secondary")

def gtcBtnwtime():
    gtcBtn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".go-to-cart-button"))
    )

RTX3070LINKS = [
        "https://www.bestbuy.com/site/nvidia-geforce-rtx-3070-8gb-gddr6-pci-express-4-0-graphics-card-dark-platinum-and-black/6429442.p?skuId=6429442",
        "https://www.bestbuy.com/site/gigabyte-nvidia-geforce-rtx-3070-eagle-8gb-gddr6-pci-express-4-0-graphics-card/6437912.p?skuId=6437912",
        "https://www.bestbuy.com/site/nvidia-geforce-rtx-3080-10gb-gddr6x-pci-express-4-0-graphics-card-titanium-and-black/6429440.p?skuId=6429440",
        "https://www.bestbuy.com/site/nvidia-geforce-rtx-3060-ti-8gb-gddr6-pci-express-4-0-graphics-card-steel-and-black/6439402.p?skuId=6439402",
        "https://www.bestbuy.com/site/msi-amd-radeon-rx-6800-16g-16gb-gddr6-pci-express-4-0-graphics-card-black-black/6441020.p?skuId=6441020",
        "https://www.bestbuy.com/site/xfx-amd-radeon-rx-6800-16gb-gddr6-pci-express-4-0-gaming-graphics-card-black/6442077.p?skuId=6442077",
        "https://www.bestbuy.com/site/xfx-amd-radeon-rx-6700-xt-12gb-gddr6-pci-express-4-0-gaming-graphics-card-gray-black/6457624.p?skuId=6457624",
        "https://www.bestbuy.com/site/msi-amd-radeon-rx-6800-xt-16g-16gb-gddr6-pci-express-4-0-graphics-card-black/6440913.p?skuId=6440913",
        "https://www.bestbuy.com/site/xfx-amd-radeon-rx-6800xt-16gb-gddr6-pci-express-4-0-gaming-graphics-card-black/6441226.p?skuId=6441226"
]

idx = 0

driver.get(RTX3070LINKS[idx])

isComplete = False

while not isComplete:
    # find add to cart button
    try:
        atcBtn = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ".add-to-cart-button"))
        )
#        atcBtn = driver.find_element_by_css_selector(".add-to-cart-button")
#using wait
#        atcBtn = WebDriverWait(driver, 10).until(
#            EC.element_to_be_clickable((By.CSS_SELECTOR, ".add-to-cart-button"))
#        )
    except:
        print("Out of Stock - Refreshing")
        idx += 1
        if idx == len(RTX3070LINKS):
            idx = 0
        driver.get(RTX3070LINKS[idx])
        continue


    try:
        # add to cart
        atcBtn.click()
        atcList.append("atc")
        if "atc" in atcList:
            try:
                gtcBtn = WebDriverWait(driver, 10).until(
                        EC.element_to_be_clickable((By.CSS_SELECTOR, ".go-to-cart-button"))
                )
                gtcBtn.click()
                atcList.append("gtc1500")
                print("No Queue, going to checkout")
            except:
                try:
                    atcBtn = WebDriverWait(driver, 2).until(
                            EC.element_to_be_clickable((By.CSS_SELECTOR, ".add-to-cart-button"))
                    )
                    atcBtn.click()
                    print("Missed Queue")
                except:
                    atcBtn = WebDriverWait(driver, 3000).until(
                            EC.element_to_be_clickable((By.CSS_SELECTOR, "add-to-cart-button"))
                    )
                    atcBtn.click()
                    try:
                        gtcBtn = WebDriverWait(driver, 10).until(
                                EC.element_to_be_clickable((By.CSS_SELECTOR, ".go-to-cart-button"))
                        )
                        gtcBtn.click()
                        print("In Queue")
                        atcList.append("atc1500")
                    except:
                        atcBtn.click()
                        try:
                            gtcBtn = WebDriverWait(driver, 10).until(
                                EC.element_to_be_clickable((By.CSS_SELECTOR, ".go-to-cart-button"))
                            )
                            gtcBtn.click()
                            atcList.append("atc1500")
                        except:
                            atcBtn.click()
                            print("there was queue, but we missed it :(")
                        
        
        if "atc1500" in atcList or "gtc1500" in atcList:
            # go to cart and begin checkout as guest
#Try using XPATH
#        checkoutBtn = WebDriverWait(driver, 10).until(
#            EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/main/div/div[2]/div[1]/div/div/span/div/div[2]/div[1]/section[2]/div/div/div[3]/div/div[1]/button"))
#        )
#Try using CSS_SELECTOR
#        checkoutBtn = WebDriverWait(driver, 10).until(
#                EC.element_to_be_clickable((By.CSS_SELECTOR, ".checkout-button"))
#        )
#Try using class name
            checkoutBtn = driver.find_element_by_class_name("btn-lg")
            checkoutBtn.click()
            print("Checking Out")

#         fill in email and password
            emailField = WebDriverWait(driver, 20).until(
                    EC.presence_of_element_located((By.ID, "fld-e"))
            )
            emailField.send_keys("ENTER YOUR EMAIL")
            print("Filled out email")

            pwField = WebDriverWait(driver, 20).until(
                    EC.presence_of_element_located((By.ID, "fld-p1"))
            )
#password fill in
            pwField = driver.find_element_by_id("fld-p1")
            pwField.send_keys("ENTER YOUR BESTBUY ACCOUNT PASSWORD")
            print("Filled out password")

        # click sign in button
            signInBtn = driver.find_element_by_class_name("cia-form__controls__submit")
#        signInBtn = WebDriverWait(driver, 10).until(
#            EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/section/main/div[1]/div/div/div/div/form/div[3]/button"))
#        )
            signInBtn.click()
            print("Signing in")

        # fill in card cvv
            print("Filling out ccv")
            cvvField = WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((By.ID, "credit-card-cvv"))
            )
            cvvField.send_keys("ENTER YOUR CREDIT CARD CVV")
            print("Attempting to place order")

        # place order
            placeOrderBtn = WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".button__fast-track"))
            )
            placeOrderBtn.click()

            isComplete = True
            atcList.clear()
    except:
        # make sure this link is the same as the link passed to driver.get() before looping
        idx += 1
        if idx == len(RTX3070LINKS):
            idx = 0
        driver.get(RTX3070LINKS[idx])
        atcList.clear()
        print("Error - restarting bot")
        continue

print("Order successfully placed")



