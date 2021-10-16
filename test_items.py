'''
Тесте кейсй на проверку наличия кнопки добавления в корзину на странице.
'''

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_basket_btn(browser):
    browser.get(link)
    btn = browser.find_element_by_class_name('btn.btn-lg.btn-primary.btn-add-to-basket')
    assert btn is not None




