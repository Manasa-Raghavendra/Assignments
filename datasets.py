# datasets.py

# Main dataset (Laptop Purchase Prediction)
laptop_dataset = [
    ["High", "Gaming", "Dell",   "16GB", "SSD", "Yes"],
    ["High", "Gaming", "HP",     "16GB", "SSD", "Yes"],
    ["Medium","Study", "Lenovo", "8GB",  "HDD", "No"],
    ["High", "Gaming", "Dell",   "16GB", "HDD", "Yes"],
    ["Low",  "Office", "HP",     "8GB",  "HDD", "No"]
]

# -----------------------------
# Failure Case Datasets
# -----------------------------

# Case 1: Same instance, different labels (contradiction)
case1 = [
    ["High", "Gaming", "Yes"],
    ["High", "Gaming", "No"]
]

# Case 2: Noise / wrong label
case2 = [
    ["High", "Office", "Yes"],
    ["High", "Office", "Yes"],
    ["High", "Office", "No"]
]

# Case 3: OR concept not representable by conjunction hypothesis
case3 = [
    ["High", "Office", "Yes"],
    ["Low", "Gaming", "Yes"],
    ["Low", "Office", "No"]
]

# Case 4: S becomes too general then negative breaks
case4 = [
    ["High", "Gaming", "Yes"],
    ["Low", "Office", "Yes"],
    ["Medium", "Study", "No"]
]

# Case 5: Boundary crossing contradiction
case5 = [
    ["High", "16GB", "Yes"],
    ["Low", "16GB", "No"],
    ["Low", "8GB", "Yes"]
]