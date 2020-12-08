def p1():
    with open('input.txt') as data:
        max_seat_id = -1
        for line in data:
            line = line.strip()
            lo = 0
            hi = 127
            row = 0
            for i in range(7):
                mid = lo + (hi - lo) / 2
                if line[i] == 'F':
                    hi = mid
                    row = lo
                else:
                    lo = mid + 1
                    row = hi

            col_lo = 0
            col_hi = 7
            col = 0
            for i in range(7, 10):
                col_mid = col_lo + (col_hi - col_lo) / 2
                if line[i] == 'L':
                    col_hi = col_mid
                    col = col_lo
                else:
                    col_lo = col_mid + 1
                    col = col_hi
            seat_id = row * 8 + col
            if seat_id > max_seat_id:
                max_seat_id = seat_id
        return max_seat_id

def p2():
    with open('input.txt') as data:
        all_seats = []
        for line in data:
            line = line.strip()
            lo = 0
            hi = 127
            row = 0
            for i in range(7):
                mid = lo + (hi - lo) / 2
                if line[i] == 'F':
                    hi = mid
                    row = lo
                else:
                    lo = mid + 1
                    row = hi

            col_lo = 0
            col_hi = 7
            col = 0
            for i in range(7, 10):
                col_mid = col_lo + (col_hi - col_lo) / 2
                if line[i] == 'L':
                    col_hi = col_mid
                    col = col_lo
                else:
                    col_lo = col_mid + 1
                    col = col_hi
            seat_id = row * 8 + col
            all_seats += [seat_id]
        all_seats = sorted(all_seats)

        for i in range(len(all_seats)-1):
            if all_seats[i+1] - all_seats[i] == 2:
                return all_seats[i] + 1

print p1()
print p2()