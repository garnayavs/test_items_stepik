from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def test_add_to_basket_button_is_located(browser):
    browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    try:
        WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, 'btn-add-to-basket'))
            )
        time.sleep(10) # чтобы убедиться, что язык верный
    except:
        assert False, f'Кнопка "Добавить в корзину" не найдена.'

    

