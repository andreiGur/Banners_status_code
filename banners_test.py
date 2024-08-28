from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import requests

class FunctionsClass:

    @staticmethod
    def build_driver_fun():
    # Set up Selenium WebDriver (assuming Chrome)
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        return driver

    @staticmethod
    def system_sign_in(driver):
        driver.get("http://mobileservicesnow.in")
        driver.maximize_window()
        driver.get("http://mobileservicesnow.in/odds_link_maker.php")
        driver.find_element(By.XPATH, "//*[@id='login']").send_keys("andrei")
        driver.find_element(By.XPATH, "//*[@id='pass']").send_keys("jvQ*U0y0)Flh0n3H")
        driver.find_element(By.XPATH, "//*[@id='main']/div[1]/form/input[3]").click()

    @staticmethod
    def get_status_code(url):
        try:
            # Parse the URL to extract components
            parsed_url = urlparse(url)

            # Select the appropriate connection type (http or https)
            if parsed_url.scheme == "https":
                conn = http.client.HTTPSConnection(parsed_url.netloc)
            else:
                conn = http.client.HTTPConnection(parsed_url.netloc)

            # Make a HEAD request (only fetch headers)
            conn.request("HEAD", parsed_url.path or "/")

            # Get the response
            response = conn.getresponse()

            # Return the status code
            return response.status

        except Exception as e:
            print(f"Error occurred: {e}")
            return None


    @staticmethod
    def request_status_check(url_for_check):
        try:
            response = requests.get(url_for_check)
            return response.status_code
        except requests.RequestException as e:
            print(f"Error checking status for URL {url_for_check}: {e}")
            return None

    @staticmethod
    def telegram_alert(message):
        telega_api_url1 = "https://api.telegram.org/bot5520811460:AAEiMSM8ZozY6EHVEEeTGeX3oyGxdzHRVC0/sendMessage?chat_id=@CloackerNotify&text=%7B"
        telega_api_url2 = "%7D"
        full_url = telega_api_url1 + message + telega_api_url2
        
        driver = FunctionsClass.build_driver_fun()
        driver.get(full_url)
        driver.close()


def main():
    driver = FunctionsClass.build_driver_fun()
    FunctionsClass.system_sign_in(driver)
    time.sleep(2)
    driver.maximize_window()

    driver.get("https://mobileservicesnow.in/upload_9000/upload-9000.php")
    time.sleep(3)
    
    driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div[1]/div[2]/form/div[1]/div[2]").click()
    time.sleep(3)
    
    driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div[1]/div[2]/form/div[1]/div[2]/select/option[2]").click()
    time.sleep(3)
    
    driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div[1]/div[2]/form/div[3]/input[2]").click()
    time.sleep(3)
    
    all_links = driver.find_elements(By.TAG_NAME, "a")
    
    FunctionsClass.telegram_alert("Banners(links) status-check test = START")
    
    for link in all_links:
        href = link.get_attribute("href")
        if href:
            #print("\nLink:")
            #print(href)
            status_code = FunctionsClass.request_status_check(href)
            print("Request status code:")
            print(status_code)
            
            if status_code != 200:
                print("\nLink:")
                print(href)
                FunctionsClass.telegram_alert(f"{link.text} - {href}")
                FunctionsClass.telegram_alert(str(status_code))
            print("\n")
    
    FunctionsClass.telegram_alert("Banners(links) status-check test = END")
    
    driver.close()

if __name__ == "__main__":
    main()
