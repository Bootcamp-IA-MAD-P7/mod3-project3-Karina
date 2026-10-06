def clean_output(text: str) -> str:
    return text.strip()


def truncate(text: str, max_chars: int = 2000) -> str:
    return text[:max_chars] + "..." if len(text) > max_chars else text
