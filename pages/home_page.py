from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class HomePage(BasePage):

    ADD_NOTE_BUTTON = (By.CSS_SELECTOR, "[data-testid='add-new-note']")
    TITLE_INPUT = (By.ID, "title")
    DESCRIPTION_INPUT = (By.ID, "description")
    SAVE_BUTTON = (By.CSS_SELECTOR, "[data-testid='note-submit']")
    NOTES_LIST = (By.CSS_SELECTOR, ".card")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")

    def click_add_note(self):
        self.click(self.ADD_NOTE_BUTTON)

    def create_note(self, title, description):
        self.click_add_note()
        self.type_text(self.TITLE_INPUT, title)
        self.type_text(self.DESCRIPTION_INPUT, description)
        self.click(self.SAVE_BUTTON)

    def is_note_visible(self, note_title):
        notes = self.driver.find_elements(*self.NOTES_LIST)
        return any(note_title in note.text for note in notes)