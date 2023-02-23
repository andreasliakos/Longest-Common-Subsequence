import random
from itertools import product
from itertools import combinations

def brute_force(X, Y):
    max = 0
    max_subsequense = str()
    # Δημιουργία λίστας με όλους τους πιθανούς συνδιασμούς True - False, 
    # ώστε να πάρουμε και όλες τις υποακολουθίες της πρώτης ακολουθίας
    true_false_list = [x for x in product([True, False], repeat=len(X))]
    for true_false in true_false_list:
        subsequence = str()
        for index, boolean in enumerate(true_false):
            if boolean == True:
                subsequence += X[index]
        if len(subsequence) == 0:
            continue
        # Εύρεση της μέγιστης κοινής υποακολουθίας και του μήκους της
        found = 0
        for letter in Y:
            if letter == subsequence[found]:
                found += 1
            if found == len(subsequence):
                if len(subsequence) > max:
                    max = len(subsequence)
                    max_subsequense = subsequence
                break

    return max, max_subsequense

# Κατασκευή τυχαίων ακολουθιών dna
def create_dna_sequense(n, chars, available_chars):
    dna_sequences = list()
    for _ in range(n):
        new_sequence = str()
        for _ in range(chars):
            new_sequence += available_chars[random.randint(0, 3)]
        dna_sequences.append(new_sequence)
    return dna_sequences



# Longest Common Subsequence Algorithm
def lcs(X, Y):
    length_x = len(X)
    length_y = len(Y)
    table = lcs_table(X, Y)
    if length_x == 0 or length_y == 0:
        return str()
    common_subsequnce = str()
    i_index = length_x
    j_index = length_y
    while i_index >= 0 and j_index >= 0:
        current = table[i_index][j_index]
        up = table[i_index][j_index - 1]
        left = table[i_index - 1][j_index]
        if current > left and current > up:
            common_subsequnce += X[i_index - 1]
            i_index -= 1
            j_index -= 1
        elif current == left:
            i_index -= 1
        elif current == up:
            j_index -= 1
    return len(common_subsequnce), common_subsequnce[::-1]

def lcs_table(X, Y):
    length_X = len(X)
    length_Y = len(Y)
    value = [[0 for _ in range(length_Y + 1)] for _ in range(length_X + 1)]
    for i in range(1, length_X + 1):
        for j in range(1, length_Y + 1):
            if X[i - 1] == Y[j - 1]:
                value[i][j] = value[i - 1][j - 1] + 1
            else:
                value[i][j] = max(value[i - 1][j], value[i][j - 1])
    return value


def main():
    n = 10  # 1000
    chars = 5  # 2000
    available_chars = "AGCT"

    # Create dna sequences
    dna_sequences = create_dna_sequense(
        n=n, chars=chars, available_chars=available_chars
    )

    # Create all combinations and run algorithm
    combs = combinations(dna_sequences, 2)
    max_length = 0
    max_length2 = 0
    result1 = list()
    result2 = list()
    for X, Y in combs:
        max, maxsub = brute_force(X, Y)
        if max > max_length:
            result1 = list()
            result1.append((X, Y, maxsub, max))
            max_length = max
        elif max == max_length:
            result1.append((X, Y, maxsub, max))

        max2, maxsub2 = lcs(X, Y)
        if max2 > max_length2:
            result2 = list()
            result2.append((X, Y, maxsub2, max2))
            max_length2 = max2
        elif max2 == max_length2:
            result2.append((X, Y, maxsub2, max2))

    print(f"\nThe results from brute force algorithm are\n {result1}")
    print(f"\nThe results from  algorithm are Longest Common Subsequence\n {result2}")


if __name__ == "__main__":
    main()
