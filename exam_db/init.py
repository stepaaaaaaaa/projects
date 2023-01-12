from dotenv import load_dotenv
import os


load_dotenv()
def get_evn(key: str) -> str:
    data: str = os.environ.get(key)
    if not data:
        raise KeyError(f"{key} не найден")

    return data