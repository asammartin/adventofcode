import math

lines = []
columns = []
column_sums = []
column_count = 0
rows = []
row_values = []
row_count = 0

with open("day3-2.data") as f:
    for line in f:
        line = line.strip()
        lines.append(line)
        row_value = 0
        column_count = len(line)
        row_bits = []
        for c in range(column_count):
            if row_count == 0:
                columns.append([])
                column_sums.append(0)
            column_value = int(line[c])
            columns[c].append(column_value)
            column_sums[c] += column_value
            row_bits.append(column_value)
            row_value += column_value * int(math.pow(2, column_count - c - 1))
        rows.append(row_bits)
        row_values.append(row_value)
        row_count += 1


def gte(left, right):
    return left >= right


def lt(left, right):
    return left < right


def get_column_filter(col, valid_rows, operation):
    valid_row_count = 0
    count = 0
    for valid_row_idx in range(len(valid_rows)):
        if valid_rows[valid_row_idx] == 0:
            continue
        valid_row_count += 1
        count += 1 if columns[col][valid_row_idx] == 1 else 0
    midway = valid_row_count / 2
    return 1 if operation(count, midway) else 0


def get_most_common_column_filter(col, valid_rows):
    return get_column_filter(col, valid_rows, gte)


def get_least_common_column_filter(col, valid_rows):
    return get_column_filter(col, valid_rows, lt)


def get_rating(get_common_column_filter):
    valid_rows = []
    for i in range(row_count):
        valid_rows.append(1)
    valid_row_count = row_count
    valid_lines = []
    for row in range(len(valid_rows)):
        if valid_rows[row] == 1:
            valid_lines.append(lines[row])
    for col in range(column_count):
        column_filter = get_common_column_filter(col, valid_rows)
        for row in range(row_count):
            if valid_row_count <= 1:
                break
            if valid_rows[row] == 0:
                continue
            if rows[row][col] != column_filter:
                valid_rows[row] = 0
                valid_row_count -= 1
        valid_lines = []
        for row in range(row_count):
            if valid_rows[row] == 1:
                valid_lines.append(lines[row])
    for i in range(row_count):
        if valid_rows[i] == 1:
            return row_values[i]
    return []


def get_o2_rating():
    return get_rating(get_most_common_column_filter)


def get_co2_rating():
    return get_rating(get_least_common_column_filter)


# print(f'columns: {columns}')
# print(f'column_sums: {column_sums}')
# print(f'rows: {rows}')
# print(f'lines: {lines}')
# print(f'row_values: {row_values}')
# print(f'row_count: {row_count}')
print(f'o2_rating: {get_o2_rating()}')
print(f'co2_rating: {get_co2_rating()}')
print(f'answer: {get_co2_rating() * get_o2_rating()}')
# o2_rating: 509
# co2_rating: 2693
# answer: 1370737
