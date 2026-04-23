
# Find-S and Candidate Elimination Algorithms (Case Study + Implementation)

## 📌 Project Overview
This project is a complete case study and Python implementation of two important **Concept Learning Algorithms** in Machine Learning:

1. **Find-S Algorithm**
2. **Candidate Elimination Algorithm**

In addition to implementation, this project also demonstrates **five situations where the Version Space becomes impossible to obtain** (i.e., Version Space becomes empty).

The project includes:
- Dataset creation (custom dataset, not EnjoySport/PlayTennis)
- Step-by-step tracing output in terminal
- Python implementation of both algorithms
- Failure case simulation for version space collapse
- Detailed explanation for theory and working

---

## 🎯 Aim of the Project
To implement Find-S and Candidate Elimination algorithms and analyze their behavior on:
- Normal consistent dataset
- Five inconsistent datasets where version space becomes empty

---

# 1️⃣ Background Theory

## 1.1 Concept Learning
**Concept Learning** is the task of inferring a boolean-valued function (concept) from training examples.

Each example is described using a set of attributes and a target label.

The target label is usually:
- **Yes (Positive example)**
- **No (Negative example)**

Example:

| Budget | RAM | BuyLaptop |
|--------|-----|----------|
| High   | 16GB| Yes      |

Here, the goal is to learn the concept:
> "Under what conditions will a person buy a laptop?"

---

## 1.2 Hypothesis
A **hypothesis (h)** is a possible rule that predicts the target class.

Example:
h = ⟨High, Gaming, ?, 16GB, ?⟩

Meaning:
- Budget must be High
- Purpose must be Gaming
- Brand can be anything
- RAM must be 16GB
- Storage can be anything

---

## 1.3 Hypothesis Space (H)
The **Hypothesis Space (H)** is the set of all possible hypotheses that the learner can represent.

Example hypotheses in H:
- ⟨High, Gaming, Dell, 16GB, SSD⟩
- ⟨High, ?, ?, 16GB, ?⟩
- ⟨?, Gaming, ?, ?, ?⟩
- ⟨?, ?, ?, ?, ?⟩

---

## 1.4 Version Space (VS)
The **Version Space** is the subset of hypotheses from H that are **consistent with all training examples**.

A hypothesis is consistent if:
- It classifies all positive examples correctly
- It classifies all negative examples correctly

So:

**Version Space = { h ∈ H | h is consistent with training data }**

---

## 1.5 Why Find-S and Candidate Elimination?

### Find-S Algorithm
- Finds the most specific hypothesis that covers all positive examples
- Simple and fast
- Ignores negative examples (may cause incorrect generalization)

### Candidate Elimination Algorithm
- Computes full version space
- Uses both positive and negative examples
- Maintains boundaries:
  - **S boundary**: Most specific consistent hypothesis
  - **G boundary**: Most general consistent hypothesis

---

# 2️⃣ Dataset Used

## Laptop Purchase Prediction Dataset
A custom dataset is used (not EnjoySport/PlayTennis).

### Attributes
| Attribute | Possible Values |
|----------|-----------------|
| Budget   | Low, Medium, High |
| Purpose  | Gaming, Study, Office |
| Brand    | Dell, HP, Lenovo |
| RAM      | 8GB, 16GB |
| Storage  | HDD, SSD |

### Target Attribute
- BuyLaptop ∈ {Yes, No}

---

### Training Dataset

| Budget | Purpose | Brand  | RAM  | Storage | BuyLaptop |
|--------|---------|--------|------|---------|----------|
| High   | Gaming  | Dell   | 16GB | SSD     | Yes      |
| High   | Gaming  | HP     | 16GB | SSD     | Yes      |
| Medium | Study   | Lenovo | 8GB  | HDD     | No       |
| High   | Gaming  | Dell   | 16GB | HDD     | Yes      |
| Low    | Office  | HP     | 8GB  | HDD     | No       |

---

# 3️⃣ Find-S Algorithm

## 3.1 Working Principle
Find-S starts with the most specific hypothesis and generalizes it only when necessary.

### Steps
1. Initialize h with the most specific hypothesis.
2. For each positive example:
   - If hypothesis does not cover the example, generalize minimally.
3. Ignore all negative examples.
4. Final h is the output.

---

## 3.2 Pseudocode
```

Initialize h to most specific hypothesis
For each training example x:
If x is positive:
For each attribute i:
If h[i] is empty:
h[i] = x[i]
Else if h[i] != x[i]:
h[i] = '?'
Return h

```

---

# 4️⃣ Candidate Elimination Algorithm

## 4.1 Working Principle
Candidate Elimination maintains two boundaries:

### S Boundary
Most specific hypothesis consistent with all training examples.

### G Boundary
Most general hypothesis consistent with all training examples.

Version Space lies between S and G.

---

## 4.2 Pseudocode
```

Initialize:
S = most specific hypothesis
G = most general hypothesis

For each training example x:
If x is positive:
Remove from G all hypotheses inconsistent with x
Generalize S minimally to cover x

```
If x is negative:
    Remove from S all hypotheses that cover x
    Specialize G minimally to exclude x
```

Return S and G

```

---

# 5️⃣ Version Space Failure Cases (5 Situations)

Version Space becomes empty when no hypothesis exists that can satisfy all training examples.

This happens due to:

---

## Case 1: Contradictory Labels
Same input has different labels.

Example:
| Budget | Purpose | Buy |
|--------|---------|-----|
| High   | Gaming  | Yes |
| High   | Gaming  | No  |

Result: Version Space = ∅

---

## Case 2: Noise / Wrong Label
Wrong labeling introduces inconsistency.

Example:
| Budget | Purpose | Buy |
|--------|---------|-----|
| High   | Office  | Yes |
| High   | Office  | Yes |
| High   | Office  | No  |

Result: Version Space = ∅

---

## Case 3: Concept Not Representable
If hypothesis space supports only conjunction, OR-based concepts cannot be represented.

Example:
Buy = Yes if Budget = High OR Purpose = Gaming

Result: Version Space = ∅

---

## Case 4: S becomes too general early
Positive examples force S to become completely general.
Then negative examples cannot be excluded.

Result: Version Space = ∅

---

## Case 5: Boundary Crossing
When S and G boundaries cannot be maintained (S becomes more general than G), version space collapses.

Result: Version Space = ∅

---

# 6️⃣ Project Folder Structure

```

FindS_CandidateElimination_CaseStudy/
│
├── datasets.py
├── utils.py
├── find_s.py
├── candidate_elimination.py
├── version_space_cases.py
└── main.py

````

---

# 7️⃣ How to Run This Project

## Step 1: Clone Repository
```bash
git clone <your-repo-link>
cd FindS_CandidateElimination_CaseStudy
````

## Step 2: Run Main Program

```bash
python main.py
```

---

# 8️⃣ Output Explanation

### Find-S Output

* Prints hypothesis update after each training example.

### Candidate Elimination Output

* Prints S and G boundaries update after each training example.

### Failure Case Output

* Shows at which step Version Space becomes empty.

---

# 9️⃣ Technologies Used

* Python 3.x
* Basic terminal output tracing
* No external libraries required

---

# 🔟 Conclusion

This project demonstrates the practical implementation of Find-S and Candidate Elimination algorithms.
It also proves that version space can become empty due to contradictions, noise, and limitations of hypothesis representation.

---

# 📌 Author

Name:Manasa BR
Department: CSE (AI)
College: Maharaja Institute of Technology Mysore

---


