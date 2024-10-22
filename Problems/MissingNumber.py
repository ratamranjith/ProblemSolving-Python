rr = [1, 2, 4,5]

def missing_number(rr):
    count = 1
    for i  in range(0, len(rr)):
        if count == rr[i]:
            count += 1
        else:
            return count
    return count

print(missing_number(rr))