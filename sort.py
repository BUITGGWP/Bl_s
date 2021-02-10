def itc_bubble_sort():
    n = 1
    lenns = int(input())
    a = list(map(int, input().split()))
    spisok = a
    while n < len(spisok):
        for i in range(len(spisok) - n):
            if spisok[i] > spisok[i + 1]:
                spisok[i], spisok[i + 1] = spisok[i + 1], spisok[i]
            print(*spisok)
        n += 1

itc_bubble_sort()
