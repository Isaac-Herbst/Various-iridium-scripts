from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def get_iridium_tabs():
    # Set up Chrome options to point to the Iridium executable
    chrome_options = Options()
    chrome_options.binary_location = 'C:/Program Files/Iridium/iridium.exe'  # Adjust path if necessary

    # Set up the WebDriver service
    service = Service('path/to/chromedriver')  # Adjust the path to where you have placed the chromedriver

    # Start the WebDriver
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    # Retrieve open tabs
    handles = driver.window_handles
    urls = []
    for handle in handles:
        driver.switch_to.window(handle)
        urls.append(driver.current_url)

    driver.quit()
    return urls

def save_urls_to_file(urls, file_path='active_urls.txt'):
    with open(file_path, 'w') as file:
        for url in urls:
            file.write(f"{url}\n")

if __name__ == "__main__":
    urls = get_iridium_tabs()
    save_urls_to_file(urls)
    print(f"Active URLs saved to active_urls.txt")
