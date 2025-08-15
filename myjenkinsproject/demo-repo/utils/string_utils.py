
def normalize_name(name: str) -> str:
    if not isinstance(name, str):
        raise TypeError('name must be a string')
    return ' '.join(part.capitalize() for part in name.strip().split())
