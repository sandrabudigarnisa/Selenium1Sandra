from selenium import webdriver

websites = [
    "https://www.tiket.com",
    "https://www.tokopedia.com",
    "https://www.orangsiber.com",
    "https://www.idejongkok.com",
    "https://kelasotomesyen.com"
]

option = webdriver.ChromeOptions()
option.add_argument('--headless=new')

driver = webdriver.Chrome(options=option)

driver.get(websites[0])
titles = [driver.title]

for url in websites[1:]:
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[-1])
    driver.get(url)
    titles.append(driver.title)

for i, title in enumerate(titles):
    print(f"Tab {i+1}: {title}")
    
driver.quit()
