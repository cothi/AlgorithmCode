
hei = []


for i in range(9):

    hei.append(int(input()))

hei.sort()

sum_val = sum(hei)

for a in range(9):
    for b in range(9):
        if a == b:
            continue

        else:
            if sum_val - hei[a] - hei[b] == 100:
                for c in range(9):
                    if c != a and c != b:
                        print(hei[c])

                exit()
