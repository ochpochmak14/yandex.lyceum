GLASN = "АаЕеЁёИиОоУуЫыЭэЮюЯя,.;:-"
translated_text = ""


def check() -> bool:
    if (len(translated_text) > 0 and translated_text[len(translated_text) - 1] != " "):
        return True
    return False


def translate(text: str) -> str:
    global translated_text
    for char in text:
        if char not in GLASN:
            if check() and char == " ":
                translated_text += char
            if char != " ":
                translated_text += char
    return translated_text
    