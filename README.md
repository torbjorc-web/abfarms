# FarmBurg A/B Test Analysis

## Project Overview

This project analyzes the results of a FarmBurg microtransaction A/B test with three pricing groups: A, B, and C. The goal is to determine which price point can generate at least $1000 in weekly revenue while maintaining a statistically significant purchase rate.

## Data File

The analysis uses `clicks.csv`, which contains three columns:

- `user_id`: a unique identifier for each visitor.
- `group`: the experimental group assigned to the visitor (`A`, `B`, or `C`).
- `is_purchase`: whether the visitor made a purchase (`Yes` or `No`).

## Analysis Steps

The analysis follows these steps:

1. Create a contingency table for `group` and `is_purchase`.
2. Run a Chi-Square test to check whether purchase behavior differs across groups.
3. Calculate the number of sales and purchase rates needed to reach the $1000 weekly revenue target at each price point.
4. Run binomial tests for each group to compare observed purchase rates against the target purchase rates.
5. Use the results to determine the best price for the upgrade package.

## Dependencies

This project uses the following Python libraries:

- `pandas`
- `scipy`

## SciPy Version Compatibility

Older versions of SciPy used `binom_test()` for binomial hypothesis tests.  
Newer versions use `binomtest()` instead, and the p-value is read from `.pvalue`.

Example:

```python
from scipy.stats import binomtest

pvalueA = binomtest(sales_099, n=samp_size_099, p=p_sales_needed_099, alternative='greater').pvalue
```

If your environment uses an older SciPy version, `binom_test()` may still work, but it has been deprecated and removed in newer releases. [web:16][web:25][web:29]

## Results

Based on the binomial test results, the recommended price for the FarmBurg upgrade package is **$4.99**.

This is the highest price point that still produces a purchase rate significantly above the target needed to meet the $1000 weekly revenue goal.
