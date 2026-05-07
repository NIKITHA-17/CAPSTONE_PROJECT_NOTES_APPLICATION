import yaml
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
CONFIG_FILE = BASE_DIR / "config" / "config.yaml"


def load_config():
    with open(CONFIG_FILE, "r") as file:
        return yaml.safe_load(file)


config = load_config()

UI_BASE_URL = config["ui"]["base_url"]
API_BASE_URL = config["api"]["base_url"]
BROWSER = config["ui"]["browser"]
TIMEOUT = config["ui"]["timeout"]

TEST_EMAIL = config["test_user"]["email"]
TEST_PASSWORD = config["test_user"]["password"]