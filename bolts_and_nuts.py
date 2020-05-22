# Having 2 arrays of bolt and nut sizes, match pairs
# You cannot compare bolts between bolts or nut with a nut.


def sort(bolts, nuts, depth=1):
    if len(bolts) == len(nuts) == 0:
        return []

    # Take first nut and compare it to every bolt, you should end up with 2 arrays and 1 match
    smaller_bolts, bigger_bolts, smaller_nuts, bigger_nuts = [], [], [], []
    nut = nuts[int(len(nuts) / 2)]

    match = None

    for b in bolts:
        if nut == b:
            match = (nut, b)
        elif nut < b:
            bigger_bolts.append(b)
        else:
            smaller_bolts.append(b)

    _, matchbolt = match

    for n in nuts:
        if n == matchbolt:
            continue
        if n < matchbolt:
            smaller_nuts.append(n)
        else:
            bigger_nuts.append(n)

    print(
        f"DEPTH {depth}. Smaller bolts: {smaller_bolts} nuts: {smaller_nuts} + match {match} +  Bigger bolts: {bigger_bolts} nuts: {bigger_nuts}")
    return sort(smaller_bolts, smaller_nuts, depth + 1) + [match] + sort(bigger_bolts, bigger_nuts, depth + 1)


# Worst case
bolts = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
nuts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(f"Result: {sort(bolts, nuts)}")
