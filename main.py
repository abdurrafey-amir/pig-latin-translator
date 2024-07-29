vowels = ['a', 'e', 'i', 'o', 'u']
vowels_y = ['a', 'e', 'i', 'o', 'u', 'y']
specials = ['xr', 'yt']

def translate(text):
    piggyfied = []

    for word in text.split():
        if word[0] in vowels or word[0:2] in specials:
            piggyfied.append(word + 'ay')
            continue

        for pos in range(1, len(word)):
            if word[pos] in vowels_y:
                if word[pos] == 'u' and word[pos - 1] == 'q':
                    pos += 1
                piggyfied.append(word[pos:] + word[:pos] + 'ay')
                break
    return ' '.join(piggyfied)

inp = input('enter text: ')
print('pig-latin translation: ')
print(translate(inp))