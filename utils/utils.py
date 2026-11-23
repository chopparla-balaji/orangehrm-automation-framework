

def format_locator_text(locator:tuple[str, str], kwargs:dict[str, str]) -> tuple[str, str]:
    return locator[0], locator[1].format(**kwargs)