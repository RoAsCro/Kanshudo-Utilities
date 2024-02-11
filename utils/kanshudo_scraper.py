from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

def scrape_web():
    login_details = []

    with open("../../kanup.txt", "r", encoding="utf-8") as login_data:
        for datum in login_data:
            login_details.append(datum)
    print("Login Details acquired...")

    options = Options()
    options.add_argument("--headless")

    driver = webdriver.Firefox(options=options)


    driver.get("https://www.kanshudo.com/users/sign_in")
    print("At signing page...")


    title = driver.title

    driver.implicitly_wait(0.5)

    email_text_box = driver.find_element(by=By.ID, value="user_email")
    password_text_box = driver.find_element(by=By.ID, value="user_password")
    email_text_box.send_keys(login_details[0])
    password_text_box.send_keys(login_details[1])


    driver.find_element(by=By.NAME, value="commit").click()

    print("Signed in...")



    driver.get("https://www.kanshudo.com/srs")
    print("At flashcard page...")


    no_pages = len(driver.find_elements(By.CLASS_NAME, "details"))

    flashcard_content = ""


    for i in range(no_pages):
        print(f"Extracting set {i}...")

        detail_pages = driver.find_elements(By.CLASS_NAME, "details")
        detail_pages[i].click()
        driver.find_element(by=By.CSS_SELECTOR, value="#download_set i").click()
        wait = WebDriverWait(driver=driver, timeout=30, poll_frequency=1)\
            .until(lambda x: x.find_element(by=By.ID, value="ready").is_displayed())
        
        currentContent = driver.find_element(by=By.ID, value="dcontent").get_attribute("value")
        if currentContent is None:
            raise RuntimeError("Content didn't load")
        flashcard_content += currentContent + "\n"
        driver.get("https://www.kanshudo.com/srs")

    print("Extraction done...")

    with open("./data/text/all.txt", "w", encoding="utf-8") as write:
        write.write(flashcard_content)
    print("Wrinting done...")


    driver.quit()
    print("Program quit")
