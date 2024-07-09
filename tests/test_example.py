def test_hello_google(browser):
    browser.get("https://google.com")

    assert "Google" in browser.title, "Неверный тайтл у сайта"
