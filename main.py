# main.py

from datasets import laptop_dataset, case1, case2, case3, case4, case5
from find_s import find_s_trace
from candidate_elimination import candidate_elimination_trace
from version_space_cases import run_version_space_case
from utils import print_line

# ---------------------------
# MAIN DATASET IMPLEMENTATION
# ---------------------------
print_line("=")
print("MAIN DATASET: LAPTOP PURCHASE PREDICTION")
print_line("=")

# Find-S
final_h = find_s_trace(laptop_dataset)
print("\nFinal Find-S Hypothesis:", final_h)

print_line("=")

# Candidate Elimination
S_final, G_final = candidate_elimination_trace(laptop_dataset)
print("\nFinal Specific Boundary (S):", S_final)
print("Final General Boundary (G):", G_final)

print_line("=")

# ---------------------------
# FAILURE CASES IMPLEMENTATION
# ---------------------------
run_version_space_case(case1, "CASE 1: Contradictory Labels (Same instance Yes & No)")
run_version_space_case(case2, "CASE 2: Noisy Dataset (Wrong Label Present)")
run_version_space_case(case3, "CASE 3: OR Concept Not Representable in Hypothesis Space")
run_version_space_case(case4, "CASE 4: S Becomes Fully General then Negative Breaks")
run_version_space_case(case5, "CASE 5: Boundary Crossing Contradiction")