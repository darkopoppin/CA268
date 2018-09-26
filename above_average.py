def above_average(a):
    s = sum(a)
    new_a = [n for n in a if n>s/len(a)]
    return new_a

def main():
    a = [1,1,1,1,1,2]
    print (above_average(a))

if __name__ == '__main__':
    main()
