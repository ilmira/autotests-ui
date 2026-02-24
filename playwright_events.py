from playwright.sync_api import sync_playwright, Request, Response


# Логирование запросов
def log_request(request: Request):
    print(f"Request: {request.url}")


# Логирование ответов
def log_response(response: Response):
    print(f"Response: {response.url}")


with sync_playwright() as playwright:
    # Открываем браузер и создаём новую страницу
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    # Добавляем обработчики событий
    page.on("request", log_request)  # Запрос отправлен
    page.on("response", log_response)  # Ответ получен

    # Переходим на страницу входа
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

    # Задержка для завершения всех запросов
    page.wait_for_timeout(3000)


# добавлять и удалять обработчики событий динамически
# listener = lambda request: print(f"Request: {request.url}")
#
# pages.on("request", listener)  # Добавляем обработчик
# pages.remove_listener("request", listener)  # Убираем обработчик

# Если нужно логировать только определённые запросы, то нужно использовать фильтрацию
def log_specific_requests(request):
    if "googleapis.com" in request.url:
        print(f"Filtered request: {request.url}")

# получить дополнительную информацию о содержимом ответа:

def log_response_body(response):
    if response.ok:
        print(f"Response body: {response.body()}")  # Тело ответа
