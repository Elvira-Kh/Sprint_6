import pytest
class TestQuestions:
    @allure.title("Проверка ответов на важные вопросы")
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
    def test_questions(self, driver, question_num, expected_answer):
        main_page = MainPage(driver)
        main_page.click_on_cookie_button()
        main_page.scrolling_to_questions()
        result = main_page.click_on_question_and_get_answer(AnswersText.answer_1, AnswersText.answer_2, question_num)
        assert main_page.check_answer(result, expected_answer)
