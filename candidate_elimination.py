# candidate_elimination.py

from utils import format_hypothesis, format_G, print_candidate_header

def candidate_elimination_trace(data):
    n_attr = len(data[0]) - 1

    S = ['0'] * n_attr
    G = [['?'] * n_attr]

    print("\nCANDIDATE ELIMINATION ALGORITHM TRACING\n")
    print_candidate_header()

    print(f"{0:<6}{'---':<55}{'---':<8}{format_hypothesis(S):<30}{format_G(G)}")

    for step, row in enumerate(data, start=1):
        x = row[:-1]
        label = row[-1]

        if label == "Yes":
            # Remove inconsistent hypotheses from G
            G = [g for g in G if all(g[i] == '?' or g[i] == x[i] for i in range(n_attr))]

            # Generalize S minimally
            for i in range(n_attr):
                if S[i] == '0':
                    S[i] = x[i]
                elif S[i] != x[i]:
                    S[i] = '?'

        else:  # Negative example
            new_G = []
            for g in G:
                if all(g[i] == '?' or g[i] == x[i] for i in range(n_attr)):
                    # g covers negative -> specialize it
                    for i in range(n_attr):
                        if g[i] == '?':
                            if S[i] != '?' and S[i] != x[i]:
                                new_h = g.copy()
                                new_h[i] = S[i]
                                new_G.append(new_h)
                else:
                    new_G.append(g)

            G = new_G

        print(f"{step:<6}{str(x):<55}{label:<8}{format_hypothesis(S):<30}{format_G(G)}")

        # If G becomes empty -> version space empty
        if len(G) == 0:
            print("\n❌ Version Space becomes EMPTY at this step.")
            return S, G

    print("\n✅ Version Space exists for this dataset.")
    return S, G