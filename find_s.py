# find_s.py

from utils import format_hypothesis, print_find_s_header

def find_s_trace(data):
    n_attr = len(data[0]) - 1
    h = ['0'] * n_attr

    print("\nFIND-S ALGORITHM TRACING\n")
    print_find_s_header()

    print(f"{0:<6}{'---':<55}{'---':<8}{format_hypothesis(h):<30}")

    for step, row in enumerate(data, start=1):
        x = row[:-1]
        label = row[-1]

        if label == "Yes":
            for i in range(n_attr):
                if h[i] == '0':
                    h[i] = x[i]
                elif h[i] != x[i]:
                    h[i] = '?'

        print(f"{step:<6}{str(x):<55}{label:<8}{format_hypothesis(h):<30}")

    return h