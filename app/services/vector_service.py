def embed(text: str):
    return [float(len(text))]

def similarity(a: list, b: list) -> float:
    if a[0] == 0 or b[0] == 0:
        return 0.0
    return 1.0 - abs(a[0] - b[0]) / max(a[0], b[0], 1.0)