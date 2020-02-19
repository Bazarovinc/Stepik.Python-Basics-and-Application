class Buffer:
    def __init__(self):
        self.arr = []

    def add(self, *a):
        self.arr += a
        while len(self.arr) >= 5:
            if len(self.arr) >= 5:
                new_arr = []
                s = 0
                for i in range(len(self.arr)):
                    if i < 5:
                        s += self.arr[i]
                    elif i >= 5:
                        new_arr.append(self.arr[i])
                print(s)
                self.arr = new_arr

    def get_current_part(self):
        return (self.arr)

buf = Buffer()
buf.add(1, 2, 3)
print(buf.get_current_part()) # вернуть [1, 2, 3]
buf.add(4, 5, 6) # print(15) – вывод суммы первой пятерки элементов
print(buf.get_current_part()) # вернуть [6]
buf.add(7, 8, 9, 10) # print(40) – вывод суммы второй пятерки элементов
print(buf.get_current_part()) # вернуть []
buf.add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1) # print(5), print(5) – вывод сумм третьей и четвертой пятерк
print(buf.get_current_part())# вернуть [1]