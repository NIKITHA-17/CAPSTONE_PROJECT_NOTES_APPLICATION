from services.api_client import APIClient


class NotesService:

    def __init__(self, token):
        self.client = APIClient()
        self.headers = {
            "x-auth-token": token
        }

    def get_notes(self):
        return self.client.get("/notes", headers=self.headers)

    def delete_note(self, note_id):
        return self.client.delete(f"/notes/{note_id}", headers=self.headers)
    def create_note(self, payload):
        return self.client.post(
            "/notes",
            json=payload,
            headers=self.headers
        )