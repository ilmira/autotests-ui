import allure
from playwright.sync_api import Page, expect
from components.base_component import BaseComponent
from elements.button import Button
from elements.text import Text


class CreateCourseToolbarViewComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.create_course_title = Text(page, 'create-course-toolbar-title-text', 'Title')
        self.create_course_button = Button(page, 'create-course-toolbar-create-course-button', 'Button')

    @allure.step('Check visible course toolbar view "{is_create_course_disabled}"')
    def check_visible(self, is_create_course_disabled=True):
        if is_create_course_disabled:
            self.create_course_button.check_disabled()
        else:
            self.create_course_button.check_enabled()

        self.create_course_title.check_visible()
        self.create_course_title.check_have_text('Create course')

    def click_create_course_button(self):
        self.create_course_button.click()
