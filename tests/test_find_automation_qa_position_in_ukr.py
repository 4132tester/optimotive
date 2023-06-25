from pages.careers import Careers


def test_find_automation_qa_position(browser):
    careers_page = Careers(browser)

    careers_page.open()
    careers_page.select_ukr_offices()

    assert careers_page.position_present_in_ukr('QA Automation Engineer')
