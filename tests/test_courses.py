import pytest
from playwright.sync_api import expect


@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(chromium_page_with_state):
    chromium_page_with_state.goto(" https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

    # Проверяем наличие и текст заголовка "Courses"
    courses_title = chromium_page_with_state.get_by_test_id('courses-list-toolbar-title-text')
    expect(courses_title).to_be_attached()
    expect(courses_title).to_have_text('Courses')

    # Проверяем наличие и текст блока "There is no results"
    no_results_text = chromium_page_with_state.get_by_test_id('courses-list-empty-view-title-text')
    expect(no_results_text).to_be_attached()
    expect(no_results_text).to_have_text('There is no results')

    # Проверяем наличие и видимость иконки пустого блока
    icon = chromium_page_with_state.get_by_test_id('courses-list-empty-view-icon')
    expect(icon).to_be_attached()
    expect(icon).to_be_visible()

    # Проверяем наличие и текст описания блока: "Results from the load test pipeline will be displayed here"
    result_displayed_text = chromium_page_with_state.get_by_test_id('courses-list-empty-view-description-text')
    expect(result_displayed_text).to_be_attached()
    expect(result_displayed_text).to_have_text('Results from the load test pipeline will be displayed here')
