import allure  # Импортируем allure
from playwright.sync_api import expect
from ui_coverage_tool import ActionType

from elements.base_element import BaseElement
from tools.logger import get_logger  # Импортируем get_logger

logger = get_logger("BUTTON")  # Инициализируем logger


class Button(BaseElement):
    @property
    def type_of(self) -> str:
        return "button"

    def check_enabled(self, nth: int = 0, **kwargs):
        step = f'Checking that {self.type_of} "{self.name}" is enabled'
        with allure.step(step):
            logger.info(step)
            locator = self.get_locator(nth, **kwargs)
            expect(locator).to_be_enabled()

        # Трекаем видимость как VISIBLE
        self.track_coverage(ActionType.ENABLED, nth, **kwargs)

    def check_disabled(self, nth: int = 0, **kwargs):
        step = f'Checking that {self.type_of} "{self.name}" is disabled'
        with allure.step(step):
            logger.info(step)
            locator = self.get_locator(nth, **kwargs)
            expect(locator).to_be_disabled()

        # Трекаем видимость как VISIBLE
        self.track_coverage(ActionType.DISABLED, nth, **kwargs)
