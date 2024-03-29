from conftest import driver
from locators.important_questions import ImportantQuestions
from pages.main_page import MainPage
from data import AnswersText
import pytest
import allure

class TestQuestionsMainPage:
    @pytest.mark.parametrize("question_num, expected_answer",
                             [(0, AnswersText.answer_1),
                              (1, AnswersText.answer_2),
                              (2, AnswersText.answer_3),
                              (3, AnswersText.answer_4),
                              (4, AnswersText.answer_5),
                              (5, AnswersText.answer_6),
                              (6, AnswersText.answer_7)
                              ]
    )
    @allure.title("Проверка ответов на важные вопросы")
    def test_questions(self, driver, question_num, expected_answer):
    main_page = MainPage(driver)
    main_page.click_on_cookie_button()
    main_page.scrolling_to_questions()
    result = main_page.click_on_question_and_get_answer(ImportantQuestions.QUESTION_1, ImportantQuestions.ANSWER_1, question_num)
    assert main_page.check_answer(result, expected_answer)


