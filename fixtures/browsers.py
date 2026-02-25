import pytest
from playwright.sync_api import Playwright, Page

from elements.button import Button
from elements.input import Input


@pytest.fixture
def chromium_page(playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=False)
    yield browser.new_page()
    browser.close()

@pytest.fixture(scope='session')
def initialize_browser_state(playwright: Playwright):
        # Запускаем Chromium браузер в обычном режиме (не headless)
        browser = playwright.chromium.launch(headless=False)
        # Создаем новый контекст браузера (новая сессия, которая изолирована от других)
        context = browser.new_context()
        # Открываем новую страницу в рамках контекста
        page = context.new_page()

        # Переходим на страницу регистрации
        page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

        # Заполняем поле email
        email_input = Input(page, 'registration-form-email-input', 'Email')
        email_input.fill('user.name@gmail.com')

        # Заполняем поле username
        username_input = Input(page, 'registration-form-username-input', 'Username')
        username_input.fill('username')

        # Заполняем поле пароль
        password_input = Input(page, 'registration-form-password-input', 'Password')
        password_input.fill('password')

        # Нажимаем на кнопку Registration
        registration_button = Button(page, 'registration-pages-registration-button', 'Registration')
        registration_button.click()

        # Сохраняем состояние браузера (куки и localStorage) в файл для дальнейшего использования
        context.storage_state(path="browser-state.json")


@pytest.fixture(scope='function')
def chromium_page_with_state(initialize_browser_state, playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(
        storage_state="browser-state.json")  # Указываем файл с сохраненным состоянием
    yield context.new_page()
    browser.close()