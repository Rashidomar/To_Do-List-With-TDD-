from selenium import webdriver
browser = webdriver.Firefo()
browser.get('http://localhost:8000')
assert 'Django' in browser.title
