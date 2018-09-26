def calc_average(a):
    s = sum(a)
    return s/len(a)

def main():
    a = [5,5,6,5]
    print(calc_average(a))

if __name__ == '__main__':
    main()
