from playwright.sync_api import sync_playwright, expect

# Открываем браузер с использованием Playwright
with sync_playwright() as playwright:
    # Запускаем Chromium браузер в обычном режиме (не headless)
    browser = playwright.chromium.launch(headless=False)
    # Создаем новый контекст браузера (новая сессия, которая изолирована от других)
    context = browser.new_context()
    # Открываем новую страницу в рамках контекста
    page = context.new_page()

    # Переходим на страницу регистрации
    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

    # Заполняем поле email
    email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    email_input.fill('user.name@gmail.com')

    # Заполняем поле username
    username_input = page.get_by_test_id('registration-form-username-input').locator('input')
    username_input.fill('username')

    # Заполняем поле пароль
    password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    password_input.fill('password')

    # Нажимаем на кнопку Registration
    registration_button = page.get_by_test_id('registration-pages-registration-button')
    registration_button.click()

    # Сохраняем состояние браузера (куки и localStorage) в файл для дальнейшего использования
    context.storage_state(path="browser-state.json")

    # Проверяем, что появилось сообщение на странице Dashboard
    dashboard_title = page.get_by_test_id('dashboard-toolbar-title-text')
    expect(dashboard_title).to_be_visible()
    expect(dashboard_title).to_have_text('Dashboard')

    # Задержка для наглядности выполнения теста (не рекомендуется использовать в реальных автотестах)
    page.wait_for_timeout(5000)

# Использование сохраненного контекста браузера, для попадания сразу на страницу Dashboard

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state="browser-state.json") # Указываем файл с сохраненным состоянием
    page = context.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard")

    page.wait_for_timeout(5000)
