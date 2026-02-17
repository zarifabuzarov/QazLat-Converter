letters = {
'а': 'a',
'ә': 'ə',
'б': 'b',
'в': 'v',
'г': 'g',
'ғ': 'ğ',
'д': 'd',
'е': 'e',
'ж': 'c',
'з': 'z',
'й': 'y',
'к': 'k',
'қ': 'q',
'л': 'l',
'м': 'm',
'н': 'n',
'ң': 'ŋ',
'ө': 'ö',
'п': 'p',
'р': 'r',
'с': 's',
'т': 't',
'ү': 'ü',
'ұ': 'u',
'ф': 'f',
'х': 'x',
'һ': 'h',
'ц': 'ç',
'ч': 'ç',
'ш': 'ş',
'щ': 'ç',
'ъ': '`',
'ы': 'ı',
'і': 'İ',
'ь': '',
'э': 'e',
}

hitri_letter = {
    True: {
        True: {
            'ё':'yö',
            'ю':'yüv',
            'я':'yə',
        },
        False: {
            'ё': 'ö',
            'ю': 'üv',
            'я': 'ə',
        }
    },
    False:{
        True: {
            'ё': 'yo',
            'ю': 'yuv',
            'я': 'ya',
        },
        False: {
            'ё': 'o',
            'ю': 'uv',
            'я': 'a',
        }
    }
}

difto_letter = {
    'у': {
        True: {
        'cc': 'üv',
        'cv': 'üv',
        'vc': 'vü',
        'vv': 'v',
        },
        False: {
        'cc': 'uv',
        'cv': 'uv',
        'vc': 'vu',
        'vv': 'v',
        },
    },
    'о': {
        True: {
            'cc':'ö',
            'cv':'ö',
            'vc':'vö',
            'vv':'v',
        },
        False: {
            'cc':'o',
            'cv':'o',
            'vc':'vo',
            'vv':'v',
        },
    },
}

i_letter = {
    True: {
        'cc': 'iy',
        'cv': 'iy',
        'vc': 'yi',
        'vv': 'y',
    },
    False: {
        'cc': 'ıy',
        'cv': 'ıy',
        'vc': 'yı',
        'vv': 'y',
    }
}

def split_text(text, alphabet):
    check = text.lower()
    words = []
    spaces = []
    word = ''
    space = ''
    start = text[0].lower() in alphabet
    prev = None

    for i, c in enumerate(text):
        curr = check[i] in alphabet
        if curr:
            if prev:
                word += c
            else:
                if space:
                    spaces.append(space)
                word = c
        else:
            if prev:
                if word:
                    words.append(word)
                space = c
            else:
                space += c
        prev = curr

    if curr:
        if word:
            words.append(word)
    else:
        if space:
            spaces.append(space)
    return (words, spaces, start)

def join_text(text):
    words, spaces, start = text
    output = ''
    diff = len(words) - len(spaces)
    end = min(len(words), len(spaces))

    if start:
        for i in range(end):
            output += words[i]
            output += spaces[i]
    else:
        for i in range(end):
            output += spaces[i]
            output += words[i]
    if diff == -1:
        output += spaces[-1]
    elif diff == 1:
        output += words[-1]

    return output

def lis(lst, string):
    return True in [i in string for i in lst]

def sette(lst):
    output = set()
    output.update(lst)
    return list(output)

def issoft(word):
    if lis(hard, word):
        return False
    elif lis(soft, word):
        return True
    return False

def mapvocal(word):
    output = ''
    for i in word:
        if i in difto:
            output += 'd'
        elif i in hitri:
            output += 'h'
        elif i in vocal:
            output += 'v'
        elif i in const:
            output += 'c'
        else:
            output += i
    return output

def mapupper(word):
    return ''.join(['1' if i.isupper() else '0' for i in word])

def reg_correct(reg, word):
    out = ''.join(word)
    if reg.istitle(): return out.title()
    elif reg.islower(): return out.lower()
    elif reg.isupper(): return out.upper()
    else:
        out = ''
        for i, c in enumerate(reg):
            if c.istitle(): out += word[i].title()
            elif c.islower(): out += word[i].lower()
            elif c.isupper(): out += word[i].upper()
        return out

def convert_word(word):
    vocs = mapvocal(word)
    soft = issoft(word)

    output = []

    for i in range(1, len(word)-1):
        c = word[i]

        place = vocs[i-1]+vocs[i+1]

        if c in const or c in vocal:
            output.append(letters[c])

        if c in hitri:
            output.append(hitri_letter[soft][place[0] in 'vd '][c])

        if c in difto:
            char = 'о' if c in 'оө' else 'у'
            tmp = ('v' if place[0] in 'vhdи ' else 'c') + ('v' if place[1] in 'vhdи !' else 'c')
            output.append(difto_letter[char][soft][tmp])

        if c == 'и':
            tmp = ('v' if place[0] in 'vhdи' else 'c') + ('v' if place[1] in 'vdи !' else 'c')
            output.append(i_letter[soft][tmp])
    return output

def convert_text(text):
    outwords, spaces, start = split_text(text, alphabet)

    words = [f' {i.lower()}!' for i in outwords]

    for i in range(len(words)):
        word = convert_word(words[i])
        outwords[i] = reg_correct(outwords[i], word)

    return join_text((outwords, spaces, start))

alphabet = 'аәбвгғдеёжзийкқлмнңоөпрстуүұфхһцчшщъыіьэюя'

soft = 'ә-е-ө-ү-і'.split('-')
hard = 'а-ұ-ы-о'.split('-')

const = 'бвгғджзйкқлмнңпрстфхһцчшщ'
vocal = 'аәеүұыіэ'
hitri = 'ёюя'
difto = 'уоө'
i_let = 'и'

if __name__ == '__main__':
    print(convert_text("Ассалаумағалейкум, достар!"))
