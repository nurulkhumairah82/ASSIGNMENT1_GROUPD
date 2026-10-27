## Member 1

Name: Siti Nurin Saffiyah Binti Abd Samad (Role 1-Data Steward)

Role: Data Steward (Role 1)

Owned:
- Task 1
- Task 3

Reviewed:
- Task 2

Issue found:
Resolved dictionary key extraction ('records') for raw JSON files and verified zero missing data points.

---

## Member 2

Name: Nur Dayana Anis Binti Azhar

Role: Structures Engineer (Role 2)

Owned: 
- Task 2

Reviewed:
- Task 1
- Task 3

Issue found:
- Mismatched Survey Years
Issue: Income and poverty datasets have different survey timelines.
Resolution: Merged only on matching survey years using (state, date) as the key.
- Nested JSON Structure
Issue: Raw files loaded as a dictionary instead of a list.
Resolution: Extracted the data directly from the "records" key.
- Data Type Differences
Issue: Dates were stored as text, and some older records contained None values.
Resolution: Converted dates to year integers and cleaned missing values.

---

## Member 3

Name: Nur Naajiya Binti Mohd Fauzi

Role: Matrix Analyst A (Role 3)

Owned:
- Task 4.1 Mean and median of state medians
- Task 4.2 Percentage growth in median income
- Task 4.3 Highest and lowest median income state
- Task 4.4 Relative income index
- Task 4.5 States below 0.8 and states with declining index

Reviewed:
- Task 4.6
- Task 4.7
- Task 5.1

Issue found:
Verified matrix dimensions and state ordering before analysis.

---

## Member 4 

Name: Nurul Najwa Binti Mustafa

Role: Matrix Analyst B (Role 4)	

Owned:
- Task 4.6 Regional Mean of Median Incomes
- Task 4.7 Paradox Period Analysis
- Task 5.1 Build State Profile Function

Reviewed:
- Task 4.1 
- Task 4.2 
- Task 4.3
- Task 4.4
- Task 4.5

Issue found:
Validated strict state-to-region mappings, cross-analyzed income-poverty paradox matrices, and ensured native type conversions for JSON-compatible state profiling.

---

##  Member 5

Name: Nurul Khumairah Bt Sawlihim

Role:  Intergration and Test Lead (Role 5)

Owned:
- Task 5.1 Tests
- Task 5.2 Comparison Table and Interpretation

Reviewed:
- Task 5.1

Issue found:
Identifying missing imports and corrected test failures caused by undefined values
