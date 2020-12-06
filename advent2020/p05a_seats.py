class Seat():
    def __init__(self, raw_data) :
        self.row = raw_data[:7]
        self.col = raw_data[7:]
        self.rownum = Seat.row_to_num(self.row)
        self.colnum = Seat.col_to_num(self.col)
        self.sid = self.rownum * 8 + self.colnum

    def row_to_num(row) :
        rowrange_start = 0
        rowrange_end = 2**len(row)
        for i in range(len(row)) :
            if rowrange_start != rowrange_end :
                if row[i] == "F" :
                    rowrange_end = (rowrange_start + rowrange_end) / 2
                if row[i] == "B" :
                    rowrange_start = (rowrange_start + rowrange_end) / 2
        return rowrange_start


    def col_to_num(col) :
        colrange_start = 0
        colrange_end = 2**len(col)
        for i in range(len(col)) :
            if colrange_start != colrange_end :
                if col[i] == "L" :
                    colrange_end = (colrange_start + colrange_end) / 2
                if col[i] == "R" :
                    colrange_start = (colrange_start + colrange_end) / 2
        return colrange_start

    def __str__(self) :
        return f"{self.sid}"

with open("advent2020/p05a_data.txt") as file :
    data = file.read().split("\n")

seats = []
for d in data :
    seats.append(Seat(d))

print(max(seats, key=lambda x: x.sid))
