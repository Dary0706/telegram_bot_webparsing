from razdel import sentenize


def pipiska(text: str, limit: int = 1024) -> str:
    text = text.strip()
    text = text.replace('\n', ' ')
    text = ' '.join(text.split())

    if len(text) <= limit:
        return text

    sentences = list(sentenize(text))
    if not sentences:
        return ""

    out_parts = []
    total = 0
    for s in sentences:
        s_text = s.text

        if total + len(s_text) > limit:
            break
        out_parts.append(s_text)
        total += len(s_text)

    return " ".join(out_parts).rstrip()



