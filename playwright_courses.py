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
    context.storage_state(path="browser-state_for_courses.json")

# Использование сохраненного контекста браузера, для попадания сразу на страницу Dashboard

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(
        storage_state="browser-state_for_courses.json")  # Указываем файл с сохраненным состоянием
    page = context.new_page()

    page.goto(" https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

    # Проверяем наличие и текст заголовка "Courses"
    courses_title = page.get_by_test_id('courses-list-toolbar-title-text')
    expect(courses_title).to_be_attached()
    expect(courses_title).to_have_text('Courses')

    # Проверяем наличие и текст блока "There is no results"
    no_results_text = page.get_by_test_id('courses-list-empty-view-title-text')
    expect(no_results_text).to_be_attached()
    expect(no_results_text).to_have_text('There is no results')

    # Проверяем наличие и видимость иконки пустого блока
    icon = page.get_by_test_id('courses-list-empty-view-icon')
    expect(icon).to_be_attached()
    expect(icon).to_be_visible()

    # Проверяем наличие и текст описания блока: "Results from the load test pipeline will be displayed here"
    result_displayed_text = page.get_by_test_id('courses-list-empty-view-description-text')
    expect(result_displayed_text).to_be_attached()
    expect(result_displayed_text).to_have_text('Results from the load test pipeline will be displayed here')

    page.wait_for_timeout(5000)
