from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    # Открываем браузер и создаем новую страницу
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    # Переходим на страницу входа
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

    # Решение: ожидание загрузки страницы:
    # pages.goto(
    #     "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login",
    #     wait_until='networkidle'  # Ждем завершения сетевых запросов
    # )

    # Пытаемся проверить, что несуществующий локатор виден на странице
    # unknown = pages.locator('#unknown')
    # expect(unknown).to_be_visible()

    # Пытаемся ввести текст в кнопку Login
    # login_button = pages.get_by_test_id('login-pages-login-button')
    # login_button.fill('unknown')

    # Пытаемся изменить текст заголовка
    page.evaluate("""
    const title = document.getElementById('authentication-ui-course-title-text');
    title.textContent = 'New Text';
    """)
