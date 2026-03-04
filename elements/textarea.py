import allure  # Импортируем allure
from playwright.sync_api import Locator, expect
from ui_coverage_tool import ActionType

from elements.base_element import BaseElement
from tools.logger import get_logger  # Импортируем get_logger

logger = get_logger("TEXTAREA")  # Инициализируем logger


class Textarea(BaseElement):
    @property
    def type_of(self) -> str:
        return "textarea"

    def get_locator(self, nth: int = 0, **kwargs) -> Locator:
        return super().get_locator(nth, **kwargs).locator('textarea').first

    def get_raw_locator(self, nth: int = 0, **kwargs) -> str:
        base_xpath = super().get_raw_locator(nth, **kwargs)
        return f"({base_xpath}//textarea)[1]"

    def fill(self, value: str, nth: int = 0, **kwargs):
        step = f'Fill {self.type_of} "{self.name}" to value "{value}"'
        with allure.step(step):
            logger.info(step)
            locator = self.get_locator(nth, **kwargs)
            locator.fill(value)

        # После успешного fill фиксируем покрытие как действие FILL
        self.track_coverage(ActionType.FILL, nth, **kwargs)

    def check_have_value(self, value: str, nth: int = 0, **kwargs):
        step = f'Checking that {self.type_of} "{self.name}" has a value "{value}"'
        with allure.step(step):
            logger.info(step)
            locator = self.get_locator(nth, **kwargs)
            expect(locator).to_have_value(value)

        # После успешного fill фиксируем покрытие как действие FILL
        self.track_coverage(ActionType.VALUE, nth, **kwargs)
