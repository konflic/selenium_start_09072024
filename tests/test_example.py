def test_hello_google(browser):
    browser.get("https://mail.ru/")

    assert "Mail.ru" in browser.title, "Неверный тайтл у сайта"
