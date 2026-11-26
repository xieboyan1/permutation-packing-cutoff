# No uniform cutoff for prescribed permutation packings

This note gives a counterexample to the five-term cutoff asked about by Blitvić, Kammoun, and Steingrímsson. It also proves that no fixed number of terms suffices for all pattern lengths. [Original question, Section 7, Question 8](https://arxiv.org/html/2610.29846v1#S7)

## The counterexample

Both patterns have length 20 and overlap 10. The bar separates the two increasing halves.

```text
alpha = (1,2,3,6,7,10,11,14,17,20 | 4,5,8,9,12,13,15,16,18,19)
beta  = (1,2,4,5,8, 9,12,13,16,19 | 3,6,7,10,11,14,15,17,18,20)
```

The count for `j` is the number of permutations of length `10(j+1)` that realize the pattern at the `j` prescribed starts `1, 11, …, 1+10(j−1)`. Other occurrences are allowed.

| Prescribed windows | 1 | 2 | 3 | 4 | 5 | 6 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `alpha` | 1 | 3 | 18 | 172 | 2,313 | **36,000** |
| `beta` | 1 | 3 | 18 | 172 | 2,313 | **38,313** |

## Proof and verification

The proof gives a family of pairs of length `4r+8` and overlap `2r+4` whose counts first differ at `r+3` for every integer `r ≥ 1`. It is currently available as a mathematical proof in LaTeX. [Proof source](paper/no-uniform-cutoff-for-pattern-packings.tex)

Run the concrete counterexample verifier with Python 3. It uses the standard library and exact integer arithmetic.

```sh
python scripts/verify_five_term_cutoff.py
```

The verifier builds the inequalities directly from the two permutations and counts all assignments of ranks that satisfy them. A separate row-based recursion gives the same counts. Lean formalization is pending.
