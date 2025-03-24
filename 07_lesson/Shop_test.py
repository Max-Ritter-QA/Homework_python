from selenium import webdriver
from Page_Object.MainAvtorPage import MainAvtorPage
from Page_Object.CartPage import CartPage
from Page_Object.FormaPage import FormaPage

def test_calc():
    browser = webdriver.Chrome()
    shop = MainAvtorPage(browser)
    shop.avtorization()

    cart_page = CartPage(browser)
    cart_page.cart()

    forma_total = FormaPage(browser)
    forma_total.forma()
    total = forma_total.total()

    assert total == 'Total: $58.29'
    browser.quit()
