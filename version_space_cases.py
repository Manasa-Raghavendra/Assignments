# version_space_cases.py

from candidate_elimination import candidate_elimination_trace
from utils import print_line

def run_version_space_case(case_data, case_name):
    print_line("=")
    print(f"{case_name}")
    print_line("=")

    S, G = candidate_elimination_trace(case_data)

    if len(G) == 0:
        print("\nFINAL RESULT: ❌ Version Space = EMPTY (No consistent hypothesis exists)")
    else:
        print("\nFINAL RESULT: ✅ Version Space EXISTS")

    print_line("=")