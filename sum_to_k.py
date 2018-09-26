def sum_to_k(a, k):
    i = 0
    while i < len(a)-1:
        j = i + 1
        while j < len(a):
            if a[i] + a[j] == k:
                print (a[i], a[j])
            j += 1
        i += 1

def main():
    a =[1, 6, 7, 8, 9, 10, 2, 3, 4, 5] 
    k = 20
    sum_to_k(a,k)

if __name__ == '__main__':
    main()
