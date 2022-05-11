from selenium import webdriver

browser = webdriver.Chrome(executable_path=r"C:\228413\przypomnienie\TestDjango\Project\chromedriver.exe")

browser.get("http://127.0.0.1:8080/")

assert 'The' in browser.title