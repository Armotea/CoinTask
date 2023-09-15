coin_array = input("Введите стороны монетки подряд без пробелов: ")
coin_array = list(coin_array)
lst = []
x = 1
for i in range(0, len(coin_array)):
    if coin_array[i] == "r" and coin_array[i] == coin_array[i-1]:
        x += 1
    else:
        lst .append((coin_array[i - 1], x))
        x = 1
lst.append((coin_array[-1], x))
print(max(lst))