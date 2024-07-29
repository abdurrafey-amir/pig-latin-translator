def translate(text: str):
    vowels = ('a', 'e', 'i', 'o', 'u')
    rule1 = ('xr', 'yt')

    # Rule 1
    if text[0].lower() in vowels or text[:2].lower() in rule1:
        return text + 'ay'

    # Rule 2
    consonants = ''
    for char in text:
        if char.lower() not in vowels:
            consonants += char
        else:
            break
    return text[len(consonants):] + consonants + 'ay'

    # Rule 3
    if 'qu' in text:
        index = text.index('qu')
        return text[index+2:] + text[:index+2] + 'ay'

    # Rule 4
    if 'y' in text:
        index = text.index('y')
        return text[index+1:] + text[:index+1] + 'ay'
    

inp = ('enter text: ')
translate(inp)