# utils.py

def print_line(char="=", length=100):
    print(char * length)


def format_hypothesis(h):
    return "<" + ", ".join(h) + ">"


def format_G(G):
    if len(G) == 0:
        return "{}"
    return "{ " + ", ".join([format_hypothesis(g) for g in G]) + " }"


def print_find_s_header():
    print(f"{'Step':<6}{'Example':<55}{'Class':<8}{'Hypothesis (h)':<30}")
    print("-" * 100)


def print_candidate_header():
    print(f"{'Step':<6}{'Example':<55}{'Class':<8}{'S Boundary':<30}{'G Boundary'}")
    print("-" * 130)