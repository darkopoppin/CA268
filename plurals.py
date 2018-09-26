def get_plural(s):
    if s[-2:] in ['sh','ch'] or s[-1] in ['x','s','z','o']:
        return s + 'es'
    elif s[-1] == 'y' and s[-2] not in ['a','e','o','i','u']:
        return s[:-1] + 'ies'
    elif s[-1] == 'f':
        return s[:-1] + 'ves'
    elif s[-2:] == 'fe':
        return s[:-2] + 'ves'
    else:
        return s + 's'

def main():
    a = ["beach", "fish", "fox", "bus", "fez", "potato", "fairy", "lady", "boy", "elf", "knife", "fog", "tissue"]
    for word in a:
        print(get_plural(word))

if __name__ == '__main__':
    main()

