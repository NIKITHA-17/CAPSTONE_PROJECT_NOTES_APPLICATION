class MCPHelper:

    @staticmethod
    def generate_test_data():

        return {

            "email": "testuser@gmail.com",

            "password": "Test@123"

        }

    @staticmethod
    def analyze_failure(error):

        return (
            f"MCP Failure Analysis: "
            f"Detected Error -> {error}"
        )

    @staticmethod
    def suggest_locator():

        return (
            "Suggested Locator Strategy: "
            "Use ID or CSS Selector for stability"
        )