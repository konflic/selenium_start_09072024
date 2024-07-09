def test_hello_mail_ru(browser):
    browser.get("https://mail.ru/")

    assert "Mail.ru" in browser.title, "Неверный тайтл у сайта"
