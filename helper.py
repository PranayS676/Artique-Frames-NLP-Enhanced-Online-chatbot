import re
def extract_session_id(session_str: str):

    match = re.search(r"/sessions/(.*?)/contexts/",session_str)
    if match:
        extracted_string = match.group(1)
        return extracted_string
    return ""

def get_str_from_painting_dict(painting_dict: dict):
    return ", ".join([f"{int(value)} {key}" for key, value in painting_dict.items()])


if __name__ == "__main__":
    print(get_str_from_painting_dict({"da Vinci": 2, "Pollack": 5}))
    print(extract_session_id("projects/food-with-pranay/agent/sessions/db047a60-5083-9b60-0021-38d83ff17bf6/contexts/on"))