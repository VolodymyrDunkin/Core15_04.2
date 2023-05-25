text = "Hello:World:from:Python"


def split_text(text: str) -> tuple[str, str]:
    result = text.split(":")
    
    first_element = result[0]
    second_element = result[1]
    
    return first_element, second_element


print(split_text(text))