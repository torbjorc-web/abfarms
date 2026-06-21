import pandas as pd
import numpy as np
from scipy.stats import chi2_contingency, binom_test

# Task 1: Load and inspect the data
abdata = pd.read_csv('clicks.csv')
print("=== Task 1: Inspect data with .head() ===")
print(abdata.head())
print()

# Task 2: Create contingency table
print("=== Task 2: Contingency table (Xtab) ===")
Xtab = pd.crosstab(abdata.group, abdata.is_purchase)
print(Xtab)
print()

purchases_by_group = Xtab['Yes']
print("Purchases by group:")
print(purchases_by_group)
highest_group = purchases_by_group.idxmax()
print(f"Group with highest purchases: {highest_group}")
print()

# Task 3: Chi-Square Test
print("=== Task 3: Chi-Square Test ===")
chi2, pval, dof, expected = chi2_contingency(Xtab)
print(f"p-value: {pval}")
print(f"Is significant (p < 0.05)? {pval < 0.05}")
print()

# Task 4: Calculate number of visitors
print("=== Task 4: Number of visitors ===")
num_visits = len(abdata)
print(f"num_visits: {num_visits}")
print()

# Task 5: Sales needed at $0.99
print("=== Task 5: Sales needed at $0.99 ===")
num_sales_needed_099 = 1000 / 0.99
print(f"num_sales_needed_099: {num_sales_needed_099}")
print()

# Task 6: Proportion needed at $0.99
print("=== Task 6: Proportion needed at $0.99 ===")
p_sales_needed_099 = num_sales_needed_099 / num_visits
print(f"p_sales_needed_099: {p_sales_needed_099}")
print()

# Task 7: Repeat for $1.99 and $4.99
print("=== Task 7: Sales and proportions for $1.99 and $4.99 ===")
num_sales_needed_199 = 1000 / 1.99
p_sales_needed_199 = num_sales_needed_199 / num_visits
print(f"num_sales_needed_199: {num_sales_needed_199}")
print(f"p_sales_needed_199: {p_sales_needed_199}")

num_sales_needed_499 = 1000 / 4.99
p_sales_needed_499 = num_sales_needed_499 / num_visits
print(f"num_sales_needed_499: {num_sales_needed_499}")
print(f"p_sales_needed_499: {p_sales_needed_499}")
print()

# Task 8: Group A sample size and sales
print("=== Task 8: Group A sample size and sales ===")
samp_size_099 = np.sum(abdata.group == 'A')
sales_099 = np.sum((abdata.group == 'A') & (abdata.is_purchase == 'Yes'))
print(f"samp_size_099: {samp_size_099}")
print(f"sales_099: {sales_099}")
print()

# Task 9: Group B and C sample sizes and sales
print("=== Task 9: Group B and C sample sizes and sales ===")
samp_size_199 = np.sum(abdata.group == 'B')
sales_199 = np.sum((abdata.group == 'B') & (abdata.is_purchase == 'Yes'))
print(f"samp_size_199: {samp_size_199}")
print(f"sales_199: {sales_199}")

samp_size_499 = np.sum(abdata.group == 'C')
sales_499 = np.sum((abdata.group == 'C') & (abdata.is_purchase == 'Yes'))
print(f"samp_size_499: {samp_size_499}")
print(f"sales_499: {sales_499}")
print()

# Task 10: Binomial test for Group A (using binom_test)
print("=== Task 10: Binomial test for Group A ===")
# binom_test returns p-value directly (not an object)
pvalueA = binom_test(sales_099, n=samp_size_099, p=p_sales_needed_099, alternative='greater')
print(f"pvalueA: {pvalueA}")
print(f"Is significant (p < 0.05)? {pvalueA < 0.05}")
print()

# Task 11: Binomial test for Group B
print("=== Task 11: Binomial test for Group B ===")
pvalueB = binom_test(sales_199, n=samp_size_199, p=p_sales_needed_199, alternative='greater')
print(f"pvalueB: {pvalueB}")
print(f"Is significant (p < 0.05)? {pvalueB < 0.05}")
print()

# Task 12: Binomial test for Group C
print("=== Task 12: Binomial test for Group C ===")
pvalueC = binom_test(sales_499, n=samp_size_499, p=p_sales_needed_499, alternative='greater')
print(f"pvalueC: {pvalueC}")
print(f"Is significant (p < 0.05)? {pvalueC < 0.05}")
print()

# Task 13: Final conclusion
print("=== Task 13: Final Conclusion ===")
print(f"pvalueA (Group A, $0.99): {pvalueA} - Significant? {pvalueA < 0.05}")
print(f"pvalueB (Group B, $1.99): {pvalueB} - Significant? {pvalueB < 0.05}")
print(f"pvalueC (Group C, $4.99): {pvalueC} - Significant? {pvalueC < 0.05}")

significant_groups = []
if pvalueA < 0.05:
    significant_groups.append(('A', 0.99))
if pvalueB < 0.05:
    significant_groups.append(('B', 1.99))
if pvalueC < 0.05:
    significant_groups.append(('C', 4.99))

print(f"\nGroups with significantly higher purchase rate than target: {significant_groups}")

if significant_groups:
    best_price = max(significant_groups, key=lambda x: x[1])[1]
    print(f"\n** RECOMMENDED PRICE: ${best_price} **")
    print(f"Brian should charge ${best_price} for the upgrade package.")
else:
    print("\nNo group significantly exceeds target.")
