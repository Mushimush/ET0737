# MLAI End-Semester Test — Practice Questions

A collection of 65 practice questions with fully worked explanations, covering the whole ET0737 syllabus — Python, NumPy, Pandas, visualization, data preprocessing, model training, and evaluation. Every answer walks through the *why*: the trace, the key rule, and the trap to avoid — so the understanding carries to any question on the topic, not just this one.

Structure — **Part 1** (ML fundamentals): Q1–Q20 concept questions, Q21–Q26 core-pattern drills, B1–B6 bonus. **Part 2** (Python, NumPy/Pandas, workflow & evaluation): Q27–Q59, grouped by topic.

Click any **Answer** block to reveal the explanation, the trace, and the key rule.

---

## Give These Topics Extra Attention

Most of this prep is revision of the labs and tutorials. The topics below got only light coverage there, so treat them as **new material** rather than revision and budget study time accordingly:

| Topic | Where it's covered here |
|---|---|
| File modes `"w"` vs `"a"` for writing and appending | Q32 |
| `try / except / finally` | B2 |
| `A[:,1]` (1D) vs `A[:,1:2]` (2D), Ellipsis `A[...,1]`, and chained `A[1:3][1:3]` indexing | Q34, Q35 |
| Gradient-descent variants: Batch vs Stochastic vs Mini-batch | Q24 |
| Bias-variance trade-off and the bull's-eye diagram | Q53, B5 |
| PCA — what the components are and when to use it | Q11 |
| The validation set and test-set discipline | Q56 |
| Seaborn and how it relates to Matplotlib | Q41 |
| Model versioning (`model_v1.pkl`) | B6 |
| `.str.upper()` / `.str.lower()` for standardizing text values | Q40 |
| "Feature selection" as a named term (vs feature engineering) | Q10 |

Everything else is revision of Labs 2–9 and Tutorials 2–11 — the answers reference the labs' own examples and phrasings so the connection is easy to see.

---

## Study Guide — Concepts Covered

Tick each one as you can confidently explain *why* the answer is what it is.

### Visualization & EDA
- [ ] **Matplotlib labels** — `plt.xlabel()`, `plt.ylabel()`, `plt.title()`; there is no `plt.xaxis()` / `plt.labelx()`
- [ ] **Boxplot & IQR** — outliers fall beyond `Q1 − 1.5×IQR` or `Q3 + 1.5×IQR`; boxplot is THE outlier chart
- [ ] **Univariate distribution** — histogram and boxplot show one numeric variable's distribution; scatter needs two variables
- [ ] **Outliers in data** — one value wildly far from the rest (1.2, 1.4, 1.3, **50.0**); investigate before deleting

### Data Cleaning
- [ ] **Missing data** — `NaN` = missing; `df.isnull()` flags it, `df.isnull().sum()` counts per column
- [ ] **Handling strategies** — `dropna()` removes rows; `fillna(median)` imputes; median resists outliers
- [ ] **Cleaning operations** — remove duplicates, handle missing values, fix inconsistent data (changing algorithms is NOT cleaning)

### Scaling & Encoding
- [ ] **Z-score / Standardization** — `(x − mean) / std`; after `StandardScaler`, mean = 0 and std = 1
- [ ] **Min-Max scaling** — `MinMaxScaler` squeezes values into [0, 1]
- [ ] **Why scale** — features on wildly different ranges (age 18–65 vs salary 2000–20000) so distance-based models aren't dominated by the big-range feature
- [ ] **Who needs scaling** — KNN, SVM, Neural Networks, K-Means, Logistic/Linear with gradient descent. Trees & Random Forests do NOT
- [ ] **Label Encoding** — for **ordinal** categories with a natural order (Primary < Secondary < Diploma < Degree)
- [ ] **One-Hot Encoding** — for **nominal** categories with no order (Country, Colour, Product)

### Feature Selection & PCA
- [ ] **Feature selection** — choosing the most relevant existing features (≠ feature engineering = creating new ones)
- [ ] **PCA** — turns many correlated features into fewer uncorrelated components ranked by variance explained

### Splitting & Leakage
- [ ] **`train_test_split()`** — the sklearn function; `test_size=0.2` = 20% test; `random_state` = reproducible shuffle
- [ ] **Fit scaler on train only** — split FIRST, then `fit` on train, `transform` both; otherwise test info leaks into preprocessing

### Algorithms
- [ ] **Linear Regression** — predicts a continuous number (price, temperature)
- [ ] **Logistic Regression** — predicts class probability for classification (Yes/No, Pass/Fail)
- [ ] **Decision Tree** — naturally models non-linear relationships; no scaling needed; interpretable
- [ ] **Random Forest** — many decision trees on random data/feature subsets; majority vote / average
- [ ] **K-Means** — unsupervised clustering; groups data without labels; K is a hyperparameter you choose

### Overfitting, Underfitting & Bias-Variance
- [ ] **Underfitting** — train AND test both low (e.g. 61% / 59%) = high bias
- [ ] **Overfitting** — train high, test much lower (99% / 62%) = high variance
- [ ] **Fixing tree overfitting** — DECREASE `max_depth` (a deeper tree memorises more)
- [ ] **Bull's-eye diagram** — near centre = low bias; tightly grouped = low variance; good model = both

### Metrics
- [ ] **Recall** — TP / (TP + FN); prioritise when missing a positive is costly (cancer screening)
- [ ] **MSE / RMSE** — regression metrics; RMSE ≥ 0, lower = better, same units as the target
- [ ] **Accuracy / Precision / F1** — classification metrics; never use them for regression

### Training Mechanics
- [ ] **Loss function** — measures prediction error so the optimizer knows what to minimise
- [ ] **Batch GD** — update after seeing ALL samples; **SGD** — update after EVERY sample; **Mini-batch** — update after a small batch (stable + frequent + GPU-friendly)
- [ ] **Hyperparameter vs parameter** — hyperparameter is set BY YOU before training (`n_estimators`, `max_depth`, K); parameters are LEARNED (weights, split thresholds)

### Model Persistence & Python
- [ ] **`joblib.dump` / `joblib.load`** — save/load models; `FileNotFoundError` = wrong path; `NotFittedError` = saved before `fit()`
- [ ] **Model versioning** — `model_v1.pkl`, `model_v2.pkl` — never overwrite the same filename
- [ ] **`try / except / finally`** — `finally` ALWAYS runs, exception or not
- [ ] **NumPy slicing** — 0-indexed, negative indices from the end, `A[:, 0]` = first column

---

###### 1. Which pair of commands correctly labels the **y-axis** and gives the chart a **title**? (Assuming matplotlib has been loaded successfully as `plt`)

- A: `plt.ylabel("Salary")` and `plt.title("Salary by Age")`
- B: `plt.yaxis("Salary")` and `plt.charttitle("Salary by Age")`
- C: `plt.labely("Salary")` and `plt.heading("Salary by Age")`
- D: `plt.axisy("Salary")` and `plt.name("Salary by Age")`

<details><summary><b>Answer</b></summary>
<p>

#### Answer: A

Matplotlib's labelling functions follow one simple naming pattern — and the wrong options are all invented names that *sound* plausible.

**The real API:**

| What you want | Correct command | Fake lookalikes you might see in options |
|---|---|---|
| x-axis label | `plt.xlabel("Age")` | ~~`plt.xaxis()`~~, ~~`plt.labelx()`~~, ~~`plt.axisx()`~~ |
| y-axis label | `plt.ylabel("Salary")` | ~~`plt.yaxis()`~~, ~~`plt.labely()`~~, ~~`plt.axisy()`~~ |
| chart title | `plt.title("...")` | ~~`plt.charttitle()`~~, ~~`plt.heading()`~~ |
| legend | `plt.legend()` | — |
| render the figure | `plt.show()` | — |

**Key Rule:**

> The pattern is `plt.xlabel` / `plt.ylabel` / `plt.title` — *label* comes **after** the axis letter, as one word.

**Why this matters:** the axis-label question can be asked for either axis. If you remember the *pattern* instead of one memorised answer, every version is free marks.

**Full mini-example:**
```python
plt.scatter(df["Age"], df["Salary"])
plt.xlabel("Age")
plt.ylabel("Salary")
plt.title("Salary by Age")
plt.show()
```

</p>
</details>

---

###### 2. A dataset of delivery times has Q1 = 20 minutes and Q3 = 40 minutes. Using the standard boxplot rule, which delivery time would be flagged as an **outlier**?

- A: 65 minutes
- B: 75 minutes
- C: 45 minutes
- D: 10 minutes

<details><summary><b>Answer</b></summary>
<p>

#### Answer: B

The boxplot flags outliers using the **IQR rule**: anything beyond 1.5 × IQR outside the quartiles.

**Compute the fences:**

| Step | Calculation | Result |
|------|-------------|--------|
| IQR | Q3 − Q1 = 40 − 20 | 20 |
| 1.5 × IQR | 1.5 × 20 | 30 |
| Lower fence | Q1 − 30 = 20 − 30 | **−10** |
| Upper fence | Q3 + 30 = 40 + 30 | **70** |

**Check each option:**

| Value | Inside (−10, 70)? | Outlier? |
|-------|-------------------|----------|
| 65 | ✅ Yes | No |
| **75** | ❌ No (75 > 70) | **Yes** |
| 45 | ✅ Yes | No |
| 10 | ✅ Yes | No |

**Key Rule:**

> Outlier if value < **Q1 − 1.5 × IQR** or value > **Q3 + 1.5 × IQR**. This rule is what a **boxplot** draws: the box is Q1–Q3, the whiskers extend to the fences, and dots beyond the whiskers are the outliers.

**Why this matters:** "which chart detects outliers?" gets dressed in many scenarios — salaries, purchase amounts, sensor readings. The reasoning never changes: a pie chart shows composition, a line chart shows trend, a histogram shows distribution shape but has no built-in outlier rule — the boxplot is the chart that literally *draws the IQR rule*. If a question gives you numbers instead, compute the fences like above.

</p>
</details>

---

###### 3. A student collects temperature sensor data from a server room: `22.1, 22.4, 21.9, 480.0`. What is the 480.0 reading, and what should the student do **first**?

- A: A missing value — replace it with NaN
- B: An outlier — investigate whether it is a sensor error or a genuine machine fault before deciding what to do
- C: A duplicate — remove it immediately
- D: Inconsistent data — convert it to the same unit as the others

<details><summary><b>Answer</b></summary>
<p>

#### Answer: B

A value present in the data but **wildly far from the rest** is an **outlier** — and the professional first step is to *investigate*, not to delete.

**Distinguish the four data-quality issues:**

| Issue | What it looks like | This case? |
|-------|--------------------|-----------|
| Missing data | `NaN`, blank cell | ❌ the value exists |
| Duplicate | The same record appears twice | ❌ 480.0 appears once |
| Inconsistent data | `"SG"` vs `"Singapore"`, mixed units | ❌ nothing suggests unit mismatch |
| **Outlier** | One value far outside the normal range | ✅ 480.0 vs ~22 |

**Why "investigate first" beats "delete":** in *equipment monitoring specifically*, a sudden spike might be exactly the thing you're trying to detect — an overheating incident, a real fault. Deleting it as "bad data" could throw away the most important reading in the dataset. (Vibration monitoring is the other classic case — same logic: the spike may BE the fault signal.)

| If investigation shows... | Then... |
|---------------------------|---------|
| Sensor glitch / logging error | Remove or correct it |
| Genuine overheating event | **Keep it** — it may be the signal, not noise |

**Key Rule:**

> An outlier is a data point far from the rest of the distribution. Detect it visually with a **boxplot** (IQR rule) — then decide *based on domain knowledge* whether to remove, cap, or keep it.

**Why this matters:** This mirrors the mini-project marking too — groups that deleted outliers blindly lost the justification mark; groups that argued their decision kept it.

</p>
</details>

---

###### 4. A feature is transformed with `StandardScaler`. After the transformation, the feature will have approximately:

- A: Mean = 0 and standard deviation = 1
- B: Mean = 1 and standard deviation = 0
- C: Minimum = 0 and maximum = 1
- D: All values between −1 and +1

<details><summary><b>Answer</b></summary>
<p>

#### Answer: A

`StandardScaler` performs **Standardization** (Z-score scaling):

```
z = (x − mean) / std
```

Subtracting the mean centres the data at **0**; dividing by the standard deviation rescales the spread to **1**.

**Common trap — options C and D describe Min-Max scaling, not Standardization:**

| Scaler | Formula | Result |
|--------|---------|--------|
| **StandardScaler** | `(x − mean) / std` | mean 0, std 1, values NOT bounded — can be −3, +5, etc. |
| **MinMaxScaler** | `(x − min) / (max − min)` | squeezed into [0, 1] exactly |

**Worked example** — Ages `[20, 30, 40]`, mean = 30, std ≈ 8.16:

| Raw | Z-score |
|-----|---------|
| 20 | (20−30)/8.16 ≈ **−1.22** |
| 30 | 0 |
| 40 | ≈ **+1.22** |

Note the −1.22: standardized values routinely go beyond ±1 — that's why D is wrong.

**Key Rule:**

> Standardization answers "how many standard deviations from the mean is this value?" — which puts *all* features on a comparable scale regardless of their original units.

**Why this matters:** "why convert to Z-scores?" has several legitimate answers — similar scale across features, removing measurement-unit effects, helping distance/gradient-based algorithms — and on a Select-ALL they can all be true at once. The one kind of option that is *never* true: anything promising accuracy ("makes prediction 100% accurate") — **no preprocessing step guarantees accuracy.**

</p>
</details>

---

###### 5. A team applies StandardScaler to every feature before trying four models. Which model's performance will be **least affected** by the scaling?

- A: K-Nearest Neighbours
- B: Support Vector Machine
- C: Decision Tree
- D: Neural Network (MLP)

<details><summary><b>Answer</b></summary>
<p>

#### Answer: C

A Decision Tree asks questions like `salary > 5000?` — it compares one feature against a threshold at a time. Rescaling the feature just rescales the threshold; the tree makes **exactly the same splits** either way.

**Who cares about scaling and why:**

| Model | Needs scaling? | Why |
|-------|----------------|-----|
| KNN | ✅ Yes | Uses **distance** — a feature ranging 2000–20000 drowns out one ranging 18–65 |
| SVM | ✅ Yes | Margin/distance-based |
| Neural Network | ✅ Yes | Gradient descent converges far better on similar-scale inputs |
| K-Means | ✅ Yes | Distance-based clustering |
| Linear/Logistic Regression (gradient descent) | ✅ Helps | Speeds up and stabilises convergence |
| **Decision Tree / Random Forest** | ❌ No | Threshold splits are unaffected by monotonic rescaling |

**Key Rule:**

> Scaling matters for models that measure **distances** or train by **gradient descent**. It does not matter for models that make **threshold splits** (trees, forests).

**Why this matters:** "why scale?" questions reward the fairness idea — features should contribute on comparable scales — and the drowning example above is the mechanism behind that phrase. Understanding *who* needs it also earned marks in the mini-project viva.

</p>
</details>

---

###### 6. A DataFrame column `Age` contains `[22, NaN, 26, NaN, 31]`. Which command fills the missing values with the column's **median**? (Assuming pandas is imported and `df` is loaded)

- A: `df["Age"].fillna(df["Age"].median())`
- B: `df["Age"].dropna(df["Age"].median())`
- C: `df["Age"].replace(NaN, "median")`
- D: `df["Age"].isnull().median()`

<details><summary><b>Answer</b></summary>
<p>

#### Answer: A

`fillna(value)` replaces every `NaN` with the value you pass in — here, the median of the non-missing entries.

**Why the others fail:**

| Option | Problem |
|--------|---------|
| B | `dropna()` **removes** rows — it doesn't take a fill value; passing one is wrong usage |
| C | `NaN` isn't a bare name you can type (it's `np.nan`), and `"median"` is a **string literal**, not a computed number |
| D | `isnull()` returns True/False flags; taking their median gives you a number between 0 and 1, and fills nothing |

**The two standard strategies:**

| Strategy | Code | When |
|----------|------|------|
| Remove rows | `df.dropna()` | Few missing rows, plenty of data |
| Impute | `df["Age"].fillna(df["Age"].median())` | Keep the rows; median is robust to outliers |

**Why median and not mean?** One billionaire in a salary column drags the *mean* up dramatically; the *median* barely moves. Filling with the median avoids importing outlier distortion into your imputed values.

**Key Rule:**

> `isnull()` **finds** missing values → `isnull().sum()` **counts** them → `dropna()` / `fillna()` **handle** them. Find → count → handle.

**Why this matters:** find, count, and handle are each fair game as separate questions. Knowing the full pipeline covers every variant.

</p>
</details>

---

###### 7. What is the difference between `df.isnull().sum()` and `df.isnull().sum().sum()`?

- A: They are identical
- B: The first counts missing values per column; the second gives one grand total for the whole DataFrame
- C: The first counts missing values; the second removes them
- D: The first works on numbers, the second on strings

<details><summary><b>Answer</b></summary>
<p>

#### Answer: B

Each `.sum()` collapses one dimension.

**Trace with a 3×2 example:**

```python
df:
   Age   City
0   21    NY
1  NaN   NaN
2   25    LA
```

| Expression | Output | Meaning |
|------------|--------|---------|
| `df.isnull()` | table of True/False | flag each cell |
| `df.isnull().sum()` | `Age 1, City 1` | count per **column** (True counts as 1) |
| `df.isnull().sum().sum()` | `2` | grand total for the whole DataFrame |

**Key Rule:**

> `isnull()` returns a Boolean mask; summing a Boolean mask counts the `True`s. First `.sum()` → per column. Second `.sum()` → across columns.

**Why this matters:** "count the missing values in every column" has exactly one real spelling — `df.isnull().sum()`. Lookalikes in the `df.missing()` / `df.checknull()` / `df.na()` family are **invented methods that do not exist in pandas**. If you've actually typed the real one in labs, fakes are easy to spot.

</p>
</details>

---

###### 8. A neural network requires all input features to be in the range **[0, 1]**. Which Scikit-learn class should be used?

- A: `StandardScaler`
- B: `MinMaxScaler`
- C: `RobustScaler`
- D: `Normalizer`

<details><summary><b>Answer</b></summary>
<p>

#### Answer: B

`MinMaxScaler` maps each feature into an exact range — [0, 1] by default:

```
x_scaled = (x − min) / (max − min)
```

The minimum lands exactly on 0, the maximum exactly on 1, everything else proportionally in between.

**The scaler family:**

| Class | What it does | Output range |
|-------|--------------|--------------|
| `StandardScaler` | Z-score: `(x − mean)/std` | Unbounded (mean 0, std 1) |
| **`MinMaxScaler`** | Rescale to a fixed range | **[0, 1]** |
| `RobustScaler` | Like StandardScaler but uses median/IQR | Unbounded, resistant to outliers |
| `Normalizer` | Rescales each **row** to unit length | Per-sample, not per-feature — rarely what you want |

**Key Rule:**

> Want mean 0 / std 1 → `StandardScaler`. Want a fixed [0, 1] range → `MinMaxScaler`. Both are fitted on **training data only**, then used to transform both sets.

**Why this matters:** "which class performs Standardization?" has one real answer — `StandardScaler` — and invented lookalikes (`NormalizeScaler`, `FeatureScaler`, `DataScaler`) do the rounds as distractors. Between this question and Q4 you know both real scalers, what each produces, and how to spot fakes.

</p>
</details>

---

###### 9. A dataset has two categorical columns: `Education` (Primary, Secondary, Diploma, Degree) and `Country` (Singapore, Malaysia, Thailand). Which encoding pairing is most appropriate?

- A: Label-encode both
- B: One-hot encode both
- C: Label-encode `Education`, one-hot encode `Country`
- D: One-hot encode `Education`, label-encode `Country`

<details><summary><b>Answer</b></summary>
<p>

#### Answer: C

The deciding question is: **does the category have a natural order?**

| Column | Natural order? | Type | Right encoding |
|--------|----------------|------|----------------|
| Education | ✅ Primary < Secondary < Diploma < Degree | **Ordinal** | Label Encoding (0, 1, 2, 3) — the numbers *mean* something |
| Country | ❌ Singapore is not "more than" Malaysia | **Nominal** | One-Hot Encoding (separate 0/1 column per country) |

**What goes wrong if you swap them:**

- Label-encoding `Country` as Singapore=0, Malaysia=1, Thailand=2 tells the model Thailand = 2 × Malaysia and that Singapore < Malaysia < Thailand. A linear model will happily learn from this **fake order** — a real, silent bug.
- One-hot encoding `Education` isn't *wrong*, but it **throws away** the genuine order information (and adds columns needlessly).

**Key Rule:**

> **Ordered categories → Label/Ordinal Encoding. Unordered categories → One-Hot Encoding.** The test is always: "would sorting these categories by their number make sense?"

**Why this matters:** a common variant lists several features (colours, countries, product names, qualification levels) and asks which suits Label Encoding — run the order test on each candidate: qualifications have a natural ladder; the rest are nominal. Same rule, whichever direction it's asked.

**Reconciling with Lab 6's code:** the lab implements ordinal encoding with `.map({'Low': 1, 'Medium': 2, 'High': 3})` (you write the order yourself) and reserves sklearn's `LabelEncoder` class for target labels — because `LabelEncoder` assigns numbers *alphabetically*, which may not be your intended order. For the exam, "Label Encoding" means the concept: ordered categories → meaningful integers. Lab 6's own warning is the same rule: "Never label-encode nominal data — it invents a fake order (Food > Electronics)."

</p>
</details>

---

###### 10. A team starts with 50 features. Team member A picks the 12 features most correlated with the target and discards the rest. Team member B multiplies `height × width` to create a new `area` column. What did each member do?

- A: A did feature selection; B did feature engineering
- B: A did feature engineering; B did feature selection
- C: Both did feature selection
- D: A did scaling; B did encoding

<details><summary><b>Answer</b></summary>
<p>

#### Answer: A

Two different "feature" activities that the exam loves to swap:

| Activity | Definition | Example |
|----------|------------|---------|
| **Feature selection** | Choosing the most relevant **existing** features, discarding the rest | Keep 12 of 50 columns by correlation / importance |
| **Feature engineering** | **Creating new** features from existing ones | `area = height × width`, extracting `year` from a date |
| Feature extraction / PCA | Transforming features into new combined dimensions | hundreds of columns → 20 principal components |
| Scaling | Changing the range of numeric features | StandardScaler, MinMaxScaler |
| Encoding | Converting categories to numbers | One-hot, label encoding |

**Key Rule:**

> Selection = **subset** of what you have. Engineering = **new columns** you compute. PCA = **transformed** dimensions (neither original subset nor hand-made).

**Why this matters:** definition questions here love to plant "creating new features from existing features" as the trap option — that's the definition of feature *engineering*. Know both definitions and the trap becomes the giveaway.

</p>
</details>

---

###### 11. After applying PCA to a dataset of 300 highly-correlated numerical features, the resulting principal components are:

- A: Uncorrelated with each other, and ordered by how much variance they explain
- B: Copies of the 500 original features, sorted alphabetically
- C: Categorical labels for clustering
- D: Identical to the original features but scaled to [0, 1]

<details><summary><b>Answer</b></summary>
<p>

#### Answer: A

PCA (Principal Component Analysis) rotates the data into a **new coordinate system** where:

1. Each principal component is a **weighted combination** of the original features (not a copy of any one of them),
2. The components are mutually **uncorrelated** — the redundancy between correlated features is squeezed out,
3. They are **ranked by explained variance** — PC1 captures the most variation, PC2 the next most, and so on.

Because the ranking concentrates the information into the first components, you can keep the first k (e.g. 20 of 300) and discard the rest with little information loss → **dimensionality reduction**.

**When PCA is the right tool:**

| Situation | Why PCA fits |
|-----------|--------------|
| Hundreds of features, many highly correlated | Correlated features carry duplicated information — PCA compresses it |
| Model is slow / overfitting due to dimensionality | Fewer dimensions = faster and less variance |
| You want to visualise high-dimensional data | Plot PC1 vs PC2 |

**What PCA is NOT:** it is not encoding (that's for categories), not scaling (though you should scale *before* PCA), and not supervised — it never looks at the target.

**Key Rule:**

> Many correlated numeric features → **PCA**. When a question describes hundreds of correlated numeric features and asks for the right preprocessing: encoding is for categories, scaling doesn't reduce anything — **PCA** is the technique that addresses correlation + dimensionality together.

</p>
</details>

---

###### 12. What is the effect of this line? (Assuming sklearn is loaded and `X`, `y` exist)

```python
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
```

- A: 20% of the data goes to the test set, and the split is reproducible — rerunning gives the same rows in each set
- B: 20% of the data goes to the training set
- C: The data is split into 42 equal parts
- D: The model is trained 42 times on 20% of the data

<details><summary><b>Answer</b></summary>
<p>

#### Answer: A

**Each parameter decoded:**

| Parameter | Meaning |
|-----------|---------|
| `test_size=0.2` | **20% → test set**, remaining 80% → training set |
| `random_state=42` | Seeds the shuffle — the same "random" split every run (42 is just a convention; any fixed number works) |
| Return order | `X_train, X_test, y_train, y_test` — train before test, X before y |

**Why `random_state` matters:** without it, every rerun shuffles differently — your accuracy changes between runs and nobody can reproduce your results. With it, teammates (and markers) get identical splits.

**Key Rule:**

> `train_test_split()` is the sklearn function for splitting — lookalikes in the `split_dataset()` / `data_split()` / `split_train_test()` family **do not exist**. Note the word order: **train**, then **test**.

**Why this matters:** Also remember *why* we split at all — the test set simulates unseen data. Evaluating on training data is like grading students on questions they've already seen with the answers.

</p>
</details>

---

###### 13. Which workflow correctly applies a StandardScaler without data leakage?

- A: Fit the scaler on the full dataset, then split into train and test
- B: Split first; fit the scaler on the training set only; transform both training and test sets with it
- C: Split first; fit one scaler on train and a separate scaler on test
- D: Fit the scaler on the test set, since that's the data being predicted

<details><summary><b>Answer</b></summary>
<p>

#### Answer: B

The scaler *learns* something from the data it's fitted on — the mean and standard deviation. If those statistics are computed on data that includes the test set, information about the test set has **leaked** into preprocessing, and your evaluation becomes optimistically biased.

**The correct sequence:**

```python
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)   # LEARN mean/std from train only
X_test_scaled  = scaler.transform(X_test)        # APPLY the same mean/std — no fitting!
```

**Why each wrong option is wrong:**

| Option | Problem |
|--------|---------|
| A | Test rows influence the mean/std → leakage. The core fact: splitting first *prevents test-set information influencing preprocessing* |
| C | Two different scalers = train and test measured on different rulers — the model sees inconsistently-scaled inputs |
| D | Backwards — the test set must stay untouched until evaluation |

**Key Rule:**

> **`fit` on train, `transform` on both.** Anything that *learns* from data (scaler, encoder, imputer, the model itself) must learn from the training set only.

**Why this matters:** This exact principle decided marks in the mini-project — groups that fitted preprocessing on the full dataset before splitting inflated their scores without realising. On paper it's easier: recognise the principle in whatever words it arrives.

</p>
</details>

---

###### 14. A weather agency wants two models: one to predict **tomorrow's temperature in °C**, and one to predict **whether it will rain (Yes/No)**. Which algorithm pairing is appropriate?

- A: Linear Regression for temperature; Logistic Regression for rain
- B: Logistic Regression for temperature; Linear Regression for rain
- C: K-Means for temperature; PCA for rain
- D: Linear Regression for both

<details><summary><b>Answer</b></summary>
<p>

#### Answer: A

Match the algorithm to the **type of output**:

| Target | Task type | Algorithm |
|--------|-----------|-----------|
| Temperature in °C — any continuous number | **Regression** | Linear Regression |
| Rain Yes/No — one of two classes | **Classification** | Logistic Regression |

**The naming trap:** *Logistic Regression* has "Regression" in its name but is a **classifier**. It fits a linear score, squashes it through the sigmoid function into a probability between 0 and 1, and applies a threshold to output a class.

**The full comparison (worth knowing cold):**

| | Linear Regression | Logistic Regression |
|---|---|---|
| Predicts | Continuous numerical values | Class **probabilities** → converted to class labels |
| Output range | Any number (−∞, +∞) | Probability (0, 1) |
| Example | Price, temperature, salary | Spam/not-spam, diabetes Yes/No, Pass/Fail |
| Loss minimised | MSE | Cross-entropy (log loss) |

**Key Rule:**

> Continuous number → Linear Regression. Category/Yes-No → Logistic Regression. The sentence to internalise: *Linear Regression predicts continuous numerical values, while Logistic Regression estimates class probabilities that can be converted into class labels.*

**Why this matters:** the same rule gets dressed as medical diagnoses, price predictions, and pass/fail classifiers. One question — *what does one prediction look like?* — answers them all.

</p>
</details>

---

###### 15. A logistic regression model outputs `predict_proba` = 0.83 for a patient. With the default threshold of 0.5, what does this mean?

- A: The model estimates an 83% probability of the positive class, so the patient is classified as positive
- B: The model is 83% accurate
- C: The patient's blood sugar is 0.83
- D: The model needs 83 more training samples

<details><summary><b>Answer</b></summary>
<p>

#### Answer: A

Logistic regression's raw output is a **probability**, not a class. The class label comes from applying a **threshold**:

| Step | Value |
|------|-------|
| Model's probability for the positive class | 0.83 |
| Threshold | 0.5 |
| 0.83 ≥ 0.5? | Yes → predict **positive** (e.g. "has diabetes") |

**Probability vs accuracy — don't confuse them:**

| Concept | What it describes |
|---------|-------------------|
| `predict_proba` = 0.83 | The model's confidence **for this one patient** |
| Accuracy = 83% | How often the model is right **across a whole test set** |

**Why the threshold matters:** it's adjustable. Lower it to 0.3 and the model flags more patients as positive — recall goes up, precision goes down. That knob is exactly how one mini-project group deliberately traded precision for recall in their churn model.

**Key Rule:**

> Logistic Regression = linear score → sigmoid → **probability** → threshold → **class label**. That two-stage output ("estimates class probabilities that can be converted into class labels") is the phrase the EST comparison question rewards.

</p>
</details>

---

###### 16. Why does a Decision Tree NOT require feature scaling, while KNN does?

- A: Decision Trees split on one feature at a time using threshold comparisons, which are unaffected by the feature's scale; KNN computes distances, which are dominated by large-range features
- B: Decision Trees automatically scale features internally
- C: KNN doesn't actually require scaling either
- D: Decision Trees only accept categorical features

<details><summary><b>Answer</b></summary>
<p>

#### Answer: A

**The tree's view:** every node asks a question like `salary > 5000?`. If you rescale salary to [0, 1], the tree simply learns `salary > 0.31?` — **the same rows go left and right**. Order is preserved, so splits are preserved.

**KNN's view:** the distance between two customers is computed across all features at once:

```
distance² = (age₁ − age₂)² + (salary₁ − salary₂)²
```

With age ∈ [18, 65] and salary ∈ [2000, 20000], the salary term is thousands of times larger — age effectively **vanishes** from the distance. Scaling restores a fair contribution from each feature.

**The Decision Tree's advantage over Logistic Regression — claim check:**

| Claim | True? |
|-------|-------|
| Can naturally model **non-linear relationships** | ✅ — the genuine advantage |
| Requires all features to be normalized | ❌ — exactly backwards |
| Can only classify binary classes | ❌ — handles multi-class fine |
| Always achieves higher accuracy | ❌ — "always" makes any option wrong |

Logistic regression draws one straight decision boundary; a tree stacks threshold splits into rectangles, which can approximate curves, interactions, and "if-this-then-that" logic with no feature transformation.

**Key Rule:**

> Trees: threshold splits → scale-free, naturally non-linear. Distance/gradient models (KNN, SVM, NN, K-Means): scaling required. And beware absolute words — "always", "100%", "only" mark wrong options.

</p>
</details>

---

###### 17. A data scientist runs `KMeans(n_clusters=4)` on unlabeled customer data. Which statement about the `4` is correct?

- A: It is a hyperparameter chosen by the data scientist before training — the algorithm does not learn it
- B: It is learned automatically from the data during training
- C: It is the number of features used
- D: It is the accuracy target

<details><summary><b>Answer</b></summary>
<p>

#### Answer: A

K-Means requires **you** to specify how many clusters to look for. Given `n_clusters=4`, it will find exactly 4 clusters — whether or not 4 is the natural number of groups in the data.

**What K-Means learns vs what you choose:**

| | Set by you (hyperparameter) | Learned by the algorithm (parameters) |
|---|---|---|
| K-Means | `n_clusters` (K) | The cluster **centroid positions** |
| Random Forest | `n_estimators`, `max_depth` | The split thresholds in each tree |
| Neural Network | learning rate, layers | The weights |

**How do you pick K sensibly?** The **elbow method**: run K-Means for K = 1…10, plot the **inertia** against K, and pick the K where the curve bends (the "elbow") — beyond it, extra clusters add little. Tutorial 9's exact framing: *inertia is the loss function K-Means minimises* (sum of squared distances to each point's cluster centre), and it *always* drops as K rises — which is why the elbow can never pick K alone; K = number-of-points gives inertia 0. That's also why Tutorial 9 pairs it with the **silhouette score** (−1 to +1, peaks at a good K) as the tie-breaker.

**K-Means in one row:**

| Question signal | Answer |
|-----------------|--------|
| "group customers **without knowing categories beforehand**" | K-Means — the unsupervised choice; every supervised option needs labels that don't exist here |
| Logistic/Linear Regression, Decision Tree | All supervised — they need labels |

**Key Rule:**

> No labels + want groups → **K-Means (unsupervised)**. K is a **hyperparameter** — a choice you make before training, not something learned from data.

</p>
</details>

---

###### 18. How does a Random Forest **classifier** produce its final prediction from its many trees?

- A: Each tree votes for a class, and the majority vote wins
- B: Only the deepest tree's prediction is used
- C: The trees' predictions are multiplied together
- D: The first tree to finish predicts for the whole forest

<details><summary><b>Answer</b></summary>
<p>

#### Answer: A

A Random Forest is **many decision trees** — that phrase is the definition to hold onto — each trained slightly differently, whose predictions are combined:

**How the trees are made different (and why that helps):**

| Mechanism | What it does |
|-----------|--------------|
| **Bootstrap sampling** | Each tree trains on a random sample (with replacement) of the rows |
| **Feature randomness** | Each split considers only a random subset of features |
| Result | Diverse trees whose individual errors partly cancel out |

**How predictions combine:**

| Task | Combination |
|------|-------------|
| Classification | **Majority vote** across trees |
| Regression | **Average** of the trees' predictions |

**Why a forest beats a single tree:** one deep tree memorises its training data (high variance). Averaging many diverse trees keeps the flexibility but cancels much of the memorisation — that's why `RandomForest` overfits less than a lone `DecisionTree`.

**A favourite follow-up:** which of a forest's numbers is a **hyperparameter**? `n_estimators` (the number of trees) — set by you before training. Learned feature weights, predicted labels, and data means are *outputs or statistics*, not hyperparameters.

**Key Rule:**

> Forest = many trees + randomness (rows and features) + vote/average. `n_estimators` and `max_depth` are its main hyperparameters.

</p>
</details>

---

###### 19. A model achieves **Training Accuracy = 99%** and **Testing Accuracy = 62%**. What is the most likely problem, and which is a sensible fix?

- A: Underfitting — make the model more complex
- B: Overfitting — reduce model complexity (e.g. lower `max_depth`) or get more training data
- C: The model is fine — 99% is excellent
- D: Data leakage — the test set must have been lost

<details><summary><b>Answer</b></summary>
<p>

#### Answer: B

A **large gap** between excellent training performance and much worse test performance is the signature of **overfitting** (high variance): the model has memorised training-set noise that doesn't generalise.

**The diagnosis table — learn to read the two numbers:**

| Train | Test | Gap | Diagnosis |
|-------|------|-----|-----------|
| 99% | 62% | Huge | **Overfitting** (high variance) — this question |
| 61% | 59% | Tiny, both low | **Underfitting** (high bias) |
| 90% | 88% | Small, both high | Healthy model 🎉 |
| 100% | 100% | None | Suspicious — check for leakage |

**Fixes for overfitting:**

| Fix | Why it works |
|-----|--------------|
| Reduce complexity (lower `max_depth`, fewer features) | Less capacity to memorise noise |
| More training data | Noise patterns stop looking like signal |
| Regularization (L1/L2) | Penalises extreme weights |
| Cross-validation for tuning | Detects overfit hyperparameters early |

**Key Rule:**

> Both low → underfit (add complexity). Train high but test far below → overfit (reduce complexity / regularise / more data). Diagnose from the **gap**, not from either number alone.

**Why this matters:** students who pattern-match "training higher than test = overfitting" get the mirror-image question wrong — a 2-point gap is nothing; when both numbers are poor, the diagnosis is underfitting (drilled in Q23).

</p>
</details>

---

###### 20. A cancer-screening test is evaluated on 100 patients who truly have cancer and 900 who don't. The model catches 80 of the cancer cases but misses 20. It also wrongly flags 45 healthy patients.

What is the model's **recall**, and which number represents the "missed cancer cases" the hospital most wants to reduce?

- A: Recall = 80/(80+20) = 0.80; the missed cases are the 20 False Negatives
- B: Recall = 80/(80+45) = 0.64; the missed cases are the 45 False Positives
- C: Recall = 900/1000 = 0.90; the missed cases are the True Negatives
- D: Recall cannot be computed without accuracy

<details><summary><b>Answer</b></summary>
<p>

#### Answer: A

**Put the numbers in a confusion matrix first:**

| | Predicted Cancer | Predicted Healthy |
|---|---|---|
| **Actually Cancer (100)** | TP = 80 | **FN = 20** ← missed cancers |
| **Actually Healthy (900)** | FP = 45 | TN = 855 |

**Recall** answers: *of everyone who truly has cancer, what fraction did we catch?*

```
Recall = TP / (TP + FN) = 80 / (80 + 20) = 0.80
```

**Precision** (option B's formula) answers a different question: *of everyone we flagged, how many really had cancer?* = 80/(80+45) ≈ 0.64.

**Which metric to prioritise — the decision table:**

| Scenario | Costly mistake | Prioritise |
|----------|----------------|------------|
| **Cancer screening** | Missing a real case (FN) | **Recall** |
| Spam filter | Deleting a real email (FP) | Precision |
| Balanced concern | Both | F1-score |

MSE, RMSE and R² are **regression** metrics — they don't apply to classification at all, which is exactly why they show up as distractors on classification-metric questions.

**Key Rule:**

> Recall = TP/(TP+FN) — the "don't miss the positives" metric. When a missed positive is dangerous or expensive, recall is the metric to maximise, even at the cost of some false alarms.

</p>
</details>

---

## Core-Pattern Drills

These six drill the module's most important recurring patterns — the ones worth over-learning.

---

###### 21. Which visualisations require **TWO variables** (i.e. are bivariate, not univariate)? (Select ALL that apply)

- A: Scatter Plot
- B: Line Chart
- C: Histogram
- D: Boxplot

<details><summary><b>Answer</b></summary>
<p>

#### Answer: A, B

The split that decides this question — and its mirror image ("which charts show the univariate distribution of one numerical variable?") — is how many variables each chart needs:

| Chart | Variables needed | What it shows |
|-------|------------------|---------------|
| **Scatter plot** | **2** | ✅ bivariate — the *relationship between two* variables |
| **Line chart** | **2** (x usually = time) | ✅ bivariate — *trend over a sequence* |
| Histogram | 1 | ❌ univariate — value-range frequencies, the shape of one distribution |
| Boxplot | 1 | ❌ univariate — median, quartiles, whiskers, outliers of one column |

**What each is FOR (the fast lookup):**

| Goal | Chart |
|------|-------|
| Shape of one variable's distribution | Histogram |
| Outliers + quartiles of one variable | Boxplot |
| Relationship between two variables | Scatter |
| Trend over time | Line |
| Composition / share of whole | Pie |
| Correlation between many variables | Heatmap |

**Key Rule:**

> Histogram and boxplot = the two **univariate** charts (one column each). Scatter and line = **bivariate** (x and y). Asked from either side, the table above answers it — which is the point of learning the split rather than answer letters.

</p>
</details>

---

###### 22. A Decision Tree overfits its training data. Which change is most likely to reduce the overfitting?

- A: Increase `max_depth` from 5 to `None`
- B: Increase `min_samples_leaf` from 1 to 20
- C: Add more features to the model
- D: Evaluate on the training set instead of the test set

<details><summary><b>Answer</b></summary>
<p>

#### Answer: B

`min_samples_leaf` forces every leaf to hold at least that many training rows. At 1, the tree may carve the data down to one row per leaf — pure **memorisation**. At 20, every rule the tree keeps must describe at least 20 real customers — only broad, general patterns survive.

**Direction of each option:**

| Option | Effect on overfitting |
|--------|-----------------------|
| `max_depth` 5 → `None` | ❌ removes the depth ceiling → MORE capacity to memorise → worse |
| **`min_samples_leaf` 1 → 20** | ✅ every leaf must generalise over ≥20 rows |
| Add features | ❌ more dimensions = more ways to memorise |
| Evaluate on training data | ❌ hides the overfitting instead of fixing it |

**All the tree-regularisation knobs (one logic, different levers):**

| Parameter | Overfitting ↓ when you... |
|-----------|---------------------------|
| `max_depth` | **decrease** (shallower tree) |
| `min_samples_leaf` | increase (each leaf must hold more rows) |
| `min_samples_split` | increase |

Whichever knob a question offers, the same principle picks the answer: the fix is always the direction that *reduces the tree's freedom to memorise*.

**Key Rule:**

> Overfitting is *too much flexibility*. Every fix reduces flexibility: shallower trees, bigger leaves, regularisation, fewer features, or more data to fill the flexibility with signal. Lab 8's phrase is worth memorising: **`max_depth` is a ceiling, not a target** — the tree may stop earlier; the parameter only caps how far it *can* go.

**Why this matters:** Lab 8's own depth sweep is this question in data: `max_depth=None` gave train 1.000 / test 0.722, and the guide's comment — "that gap *is* overfitting" — is the exact mental model to carry in.

</p>
</details>

---

###### 23. A model achieves **Training Accuracy = 61%** and **Testing Accuracy = 59%**. What is the most likely problem?

- A: Overfitting
- B: Data Leakage
- C: Underfitting
- D: High Variance

<details><summary><b>Answer</b></summary>
<p>

#### Answer: C

Read the two numbers as a pair:

| Observation | Interpretation |
|-------------|----------------|
| Both accuracies are **low** | The model hasn't captured the pattern at all |
| The gap is **tiny** (2 points) | It generalises fine — it just has nothing worth generalising |

Low + low + small gap = **Underfitting** (high **bias**): the model is too simple for the problem. Any similar pair of low, close scores earns the identical diagnosis, because the diagnosis comes from the *shape* (both low, no gap), not the specific values.

**Eliminate the others:**

| Option | Why wrong |
|--------|-----------|
| High Variance / Overfitting | Requires a **large train–test gap** (e.g. 99% vs 62%) — no gap here |
| Data Leakage | Makes scores suspiciously **high**, not low |

**Fixes for underfitting (opposite direction from overfitting fixes!):**

| Fix | Why |
|-----|-----|
| More complex model (deeper tree, more layers) | More capacity to capture the pattern |
| Better features / feature engineering | Give the model something with signal |
| Train longer / reduce regularisation | Stop restraining the model |

**Key Rule:**

> **Underfitting = high bias = both scores low.** **Overfitting = high variance = big gap.** The words "bias" and "variance" in the options are synonyms for these two diagnoses — see B5 for the bull's-eye picture of the same idea.

</p>
</details>

---

###### 24. Which Gradient Descent variant updates the model parameters only **after processing the entire training dataset**?

- A: Stochastic Gradient Descent
- B: Batch Gradient Descent
- C: Mini-batch Gradient Descent
- D: Complete Gradient Descent

<details><summary><b>Answer</b></summary>
<p>

#### Answer: B

**The three real variants** (D is invented — there is no "Complete Gradient Descent", and no "Random Gradient Descent" either; every version of this question plants one made-up name):

| Variant | Updates parameters after... | Character |
|---------|----------------------------|-----------|
| **Batch** GD | seeing **ALL** training samples | Most stable per step, slowest updates on big data |
| **Stochastic** GD (SGD) | **EVERY single sample** | Fastest, noisiest updates |
| **Mini-batch** GD | a **small batch** (e.g. 32–512 samples) | The practical compromise |

**Why mini-batch wins in practice** — a Select-ALL favourite where **all four** advantages are true:

- ✅ More frequent parameter updates than Batch GD on large datasets
- ✅ More stable than SGD (averaging over a batch smooths the noise)
- ✅ Efficient for GPU training (batches map perfectly onto parallel hardware)
- ✅ Commonly used in deep learning (it's the default everywhere)

**Mnemonic:**

> **Batch = all. Stochastic = one. Mini-batch = some.**

**Heads-up — treat this taxonomy as new material.** Tutorial 10 walks through one manual gradient-descent loop (which is batch GD, though it never uses the name) and mentions `SGDRegressor` in passing — the three-way comparison itself is new. Learn the three-row table above from scratch rather than leaning on lab memory.

**And what is gradient descent minimising?** The **loss function** — its purpose (measuring prediction error so it can be minimised) is a question of its own; see B1. Gradient descent repeatedly nudges the parameters in the direction that reduces that loss.

</p>
</details>

---

###### 25. Which operations belong to **data cleaning**? (Select ALL that apply)

- A: Dropping rows that appear twice in the dataset
- B: Filling in `NaN` values in the Age column
- C: Unifying `"S'pore"`, `"SG"` and `"Singapore"` into one label
- D: Tuning `n_estimators` to improve the Random Forest's score

<details><summary><b>Answer</b></summary>
<p>

#### Answer: A, B, C

Data cleaning fixes problems **in the data itself** — before any model exists.

| Operation | Cleaning? | Why |
|-----------|-----------|-----|
| Dropping duplicate rows | ✅ | `df.drop_duplicates()` — the same record twice distorts counts and can leak across a split |
| Filling `NaN` values | ✅ | Handle missing data — drop rows or impute (e.g. median) |
| Unifying inconsistent labels | ✅ | Three spellings of one country would be treated as three categories |
| Tuning `n_estimators` | ❌ | That's **hyperparameter tuning** — a modelling stage, touches no data |

**Where cleaning sits in the ML workflow:**

```
Collect → CLEAN → Transform (scale/encode) → Split → Train → Evaluate → Deploy
```

Option D is a stage-confusion trap; the same trap arrives in other clothes ("changing algorithms", "improving accuracy") — same reason every time: if the action doesn't modify the dataset, it isn't cleaning.

**Key Rule:**

> Cleaning = fixing **duplicates, missing values, inconsistencies, and errors in the data**. If the action doesn't modify the dataset, it isn't cleaning.

**Why this matters:** In the mini-project, one group's own duplicate-removal step was their leakage-prevention argument — duplicates that straddle a train/test split let the model "see" test rows during training.

</p>
</details>

---

###### 26. Which of the following are valid Python libraries commonly used in Machine Learning? (Select ALL that apply)

- A: Matplotlib
- B: Modbus
- C: Scikit-learn
- D: NumPy

<details><summary><b>Answer</b></summary>
<p>

#### Answer: A, C, D

| Name | What it is | ML library? |
|------|------------|-------------|
| **Matplotlib** | The plotting library — every chart in this module | ✅ |
| **Scikit-learn** | Models, scalers, encoders, `train_test_split`, metrics | ✅ The ML toolkit itself |
| **NumPy** | Fast numerical arrays, vectorised math | ✅ The numeric foundation |
| Modbus | An industrial **communications protocol** for PLCs and equipment | ❌ Networking, not ML — planted because DCPE students know the name from other modules |

**MQTT (Message Queue Telemetry Transport)** is the same trick in IoT clothing — a messaging protocol, not a library. The pattern to spot: one option is a *communications protocol you recognise from a different module*, not a Python library. Familiarity ≠ relevance.

**Who does what in a typical project:**

| Task | Library |
|------|---------|
| `pd.read_csv`, `df.isnull().sum()`, `fillna` | Pandas |
| Array math, `np.array`, slicing | NumPy |
| `StandardScaler`, `LogisticRegression`, `train_test_split` | Scikit-learn |
| Plotting (`plt.xlabel`…) | Matplotlib |
| Saving/loading models | joblib |

**Key Rule:**

> The ML stack in this module: **NumPy + Pandas + Scikit-learn + Matplotlib (+ joblib)**. MQTT is an IoT *communication protocol* — planted precisely because DCPE students have seen the acronym elsewhere.

</p>
</details>

---

## Bonus Section — Trickier Corners

Loss functions, `finally`, NumPy slicing, RMSE, the bull's-eye diagram, and model persistence.

---

###### B1. What role does the **loss function** play while a model is being trained?

- A: It shuffles the training data between epochs
- B: It quantifies how wrong the current predictions are, giving the optimizer a number to minimise
- C: It encodes categorical variables into numbers
- D: It writes the trained model to disk

<details><summary><b>Answer</b></summary>
<p>

#### Answer: B

The loss function converts "how wrong is the model right now?" into a **single number**. Training *is* the process of minimising that number.

**The training loop in plain words:**

```
1. Model makes predictions with current parameters
2. LOSS FUNCTION measures the total error          ← this question
3. Gradient descent computes which direction reduces the loss
4. Parameters take a small step in that direction
5. Repeat until the loss stops improving
```

**Which loss goes with which task (as named in this course):**

| Task | Typical loss |
|------|--------------|
| Regression | **MSE** — Tutorial 10 writes it out: `loss = mean((y_true - y_pred)^2)` |
| Classification | **Cross-entropy** (the course calls it "log-loss") |
| K-Means clustering | **Inertia** — Tutorial 9: "the loss function K-Means minimises" |

**Loss ≠ evaluation metric** (a subtle but exam-relevant distinction):

| | Loss function | Evaluation metric |
|---|---|---|
| Used | *during* training, by the optimizer | *after* training, by you |
| Must be | smoothly differentiable (gradients!) | anything meaningful |
| Example | cross-entropy | accuracy, F1, recall |

You can't train "on F1" directly — F1 isn't differentiable; the model trains on cross-entropy and you *evaluate* with F1.

**Key Rule:**

> Loss = the error signal being **minimised by gradient descent**. However the right answer is worded — measuring error, guiding optimization — the wrong options are other pipeline stages in disguise (scaling, saving, splitting). Any option that isn't about *measuring error to minimise it* is a stage-confusion trap.

</p>
</details>

---

###### B2. What is the output of this code?

```python
try:
    result = 10 / 0
    print("Computed")
except ZeroDivisionError:
    print("Cannot divide")
finally:
    print("Done")
```

- A: `Cannot divide` then `Done`
- B: `Computed` then `Done`
- C: `Done` only
- D: `Cannot divide` only

<details><summary><b>Answer</b></summary>
<p>

#### Answer: A

**Trace:**

| Step | Line | What happens |
|------|------|--------------|
| 1 | `10 / 0` | raises `ZeroDivisionError` immediately |
| 2 | `print("Computed")` | **never runs** — the exception jumped out |
| 3 | `except ZeroDivisionError` | matches → prints `Cannot divide` |
| 4 | `finally` | **always runs** → prints `Done` |

**The `finally` guarantee** — the answer to any "which block always executes?" phrasing:

| Scenario | Does `finally` run? |
|----------|---------------------|
| No exception at all | ✅ |
| Exception raised and caught | ✅ (this question) |
| Exception raised and NOT caught | ✅ (runs before the crash propagates) |
| `return` inside the `try` | ✅ (runs before the function returns!) |

**The four blocks in one table:**

| Block | Runs when |
|-------|-----------|
| `try` | Always attempted — holds the risky code |
| `except` | Only if a matching exception occurs |
| `else` | Only if NO exception occurred |
| **`finally`** | **Always, no matter what** |

**Key Rule:**

> `finally` = guaranteed cleanup (close files, release connections). If the question says "always executes regardless of whether an exception occurs," the answer is `finally`.

</p>
</details>

---

###### B3. `A` is a 6×6 NumPy matrix. Which statements are correct? (Select ALL that apply)

- A: `A[0, 0]` is the top-left element
- B: `A[-1]` returns the last row
- C: `A[:2, :2]` returns the top-left 2×2 sub-matrix
- D: In a slice like `A[1:4]`, the start index is included and the stop index is excluded

<details><summary><b>Answer</b></summary>
<p>

#### Answer: A, B, C, D — all four are correct

This is an "all true" question — they're common, because NumPy-basics statements (0-indexing, negative indices, slicing subsets, column extraction) are usually all verifiable facts. Verify each rather than hunting for a wrong one that isn't there:

| Statement | Check |
|-----------|-------|
| `A[0, 0]` top-left | ✅ 0-indexed on both axes; in a 6×6 the valid indices are 0–5 |
| `A[-1]` last row | ✅ negative indices count from the end; a bare index selects a **row** |
| `A[:2, :2]` top-left 2×2 | ✅ rows 0–1 × cols 0–1 — slicing returns a rectangular subset |
| Start included, stop excluded | ✅ `A[1:4]` = rows 1, 2, 3 — same rule as Python lists |

**The slicing cheat sheet:**

| Expression | Meaning |
|------------|---------|
| `A[0]` or `A[0, :]` | first **row** |
| `A[:, 0]` | first **column** |
| `A[-1]` | last row |
| `A[1:4]` | rows 1, 2, 3 (start included, **stop excluded**) |
| `A[:2, :2]` | top-left 2×2 sub-matrix |
| `A[6, 6]` | ❌ `IndexError` on a 6×6 (valid indices 0–5) |

**Key Rule:**

> Rows before the comma, columns after: `A[row, col]`. `:` = "everything along this axis". Start included, stop excluded — same rules as Python lists, extended to 2D.

**Why this matters:** Don't force one option to be wrong on a Select-ALL — genuine all-true questions exist (this one, RMSE in B4, and the bull's-eye in B5).

</p>
</details>

---

###### B4. Which statements about **RMSE** are true? (Select ALL that apply)

- A: RMSE is the square root of MSE
- B: A model with perfect predictions has RMSE = 0
- C: On the same data, RMSE is always ≥ MAE
- D: If house prices are in dollars, RMSE is also in dollars

<details><summary><b>Answer</b></summary>
<p>

#### Answer: A, B, C, D — all four are true

**Why each holds:**

| Statement | Reason |
|-----------|--------|
| RMSE = √MSE | By definition — Tutorial 10 computes it as `mean_squared_error(...) ** 0.5` |
| Perfect model → RMSE 0 | Every error is 0, so the mean of squares is 0. And since squares can't be negative, RMSE ≥ 0 always |
| RMSE ≥ MAE | Squaring weights big errors more; equality only when all errors are identical. A large RMSE-vs-MAE gap ⇒ a few big misses dominate (Lab 9 drills this) |
| Same units as target | Squaring puts MSE in units², the square **root** brings it back — prices in $ give RMSE in $ |

Adjacent facts — RMSE ≥ 0, lower is better, used in regression — are equally true for the same reasons; don't force a wrong option onto an all-true set.

**MSE vs RMSE — the practical difference:**

| Metric | Formula | Units (target in $) | Readability |
|--------|---------|---------------------|-------------|
| MSE | mean of (error)² | $² | Hard to interpret (what's 3.3 billion $²?) |
| RMSE | √MSE | **$** | "typically off by about $57,000" — directly meaningful |

**Which metric for which task (a staple):**

| Task | Metrics |
|------|---------|
| Regression | **MSE, RMSE**, MAE, R² |
| Classification | Accuracy, Precision, Recall, F1, confusion matrix |

"Which metric evaluates Linear Regression?" → **MSE** — accuracy, precision, and F1 are classification-only and can never be the answer for a regression model.

**Two more Lab 9 facts that make great trap questions:** **RMSE ≥ MAE, always** (a large gap between them means a few big errors are dominating), and **R² is NOT "the % of predictions that are correct"** — it measures how much better you do than just predicting the mean (0 = no better than the mean, 1 = perfect, and it *can go negative*). Lab 9 calls the R²-as-accuracy reading "the single most common misconception."

**Key Rule:**

> RMSE = √MSE: non-negative, lower-is-better, regression-only, target-units. All four properties can appear together as a Select-ALL where everything is true.

</p>
</details>

---

###### B5. A lecturer shows four bull's-eye diagrams of model predictions (the centre = the true value):

- Diagram W: widely scattered **around** the centre
- Diagram X: tight cluster **away from** the centre
- Diagram Y: widely scattered **away from** the centre
- Diagram Z: tight cluster **at the centre**

Which statements are correct? (Select ALL that apply)

- 1: Diagram W represents low bias and high variance
- 2: Diagram X represents high bias and low variance
- 3: Diagram Y represents high bias and high variance
- 4: Diagram Z represents low bias and low variance

<details><summary><b>Answer</b></summary>
<p>

#### Answer: 1, 2, 3, 4 — all correct

**Decode the two words, then every diagram reads itself** (whatever letters a question assigns, the *decoder* is what matters):

| Visual cue | Concept | Meaning |
|------------|---------|---------|
| **Where** the cluster sits (centre vs off-centre) | **Bias** | Systematic error — consistently aiming at the wrong spot |
| **How spread out** the shots are (tight vs scattered) | **Variance** | Inconsistency — predictions all over the place |

**Apply to each diagram:**

| Diagram | Position → bias | Spread → variance | Verdict |
|---------|-----------------|-------------------|---------|
| W: scattered, around centre | Low | **High** | Right on average, unreliable per-shot = **overfitting** |
| X: tight, off-centre | **High** | Low | Consistently wrong = **underfitting** |
| Y: scattered, off-centre | High | High | Worst of both |
| Z: tight, at centre | Low | Low | 🎯 The ideal model |

**Link to the accuracy questions (Q19 / Q23):**

| Bull's-eye | Train/test signature |
|------------|----------------------|
| X (high bias) | 61% / 59% — both low |
| W (high variance) | 99% / 62% — big gap |

**And the "good model" variant:** a good model shows **low bias + low variance + predictions near the centre + tightly grouped** — all four descriptors at once, because the last two *are* the first two in visual form.

**The trade-off statements (another all-true set):** increasing complexity may increase variance ✅; high bias ↔ underfitting ✅; high variance ↔ overfitting ✅; the goal is balancing both for good generalisation ✅.

**Key Rule:**

> **Position = bias. Spread = variance.** Two words, four diagrams, zero memorisation needed.

**Heads-up — treat this as new material:** the labs and tutorials taught these ideas as *underfitting* (Tutorial 10: "too simple… both training and test performance are poor") and *overfitting* ("learns noise… training high but test drops") without ever using the words "bias" or "variance". The translation table above — high bias ↔ underfitting, high variance ↔ overfitting — is the bridge between the vocabulary you know and the vocabulary questions may use. Cross it fluently in both directions.

</p>
</details>

---

###### B6. A developer writes:

```python
from sklearn.tree import DecisionTreeClassifier
import joblib

model = DecisionTreeClassifier(max_depth=4)
joblib.dump(model, "churn_model.pkl")

loaded_model = joblib.load("churn_model.pkl")
prediction = loaded_model.predict(X_new)
```

The last line raises `NotFittedError`. What is the cause?

- A: The tree's `max_depth` is too small
- B: joblib cannot save Decision Trees
- C: The model was saved before `fit()` was ever called
- D: `X_new` contains too many rows

<details><summary><b>Answer</b></summary>
<p>

#### Answer: C

Trace the lifecycle — the model was **created** and **saved**, but never **trained**:

| Step | Code | Model state |
|------|------|-------------|
| 1 | `model = DecisionTreeClassifier(max_depth=4)` | Created — hyperparameters set, but no learned splits yet |
| 2 | *(missing!)* `model.fit(X_train, y_train)` | **This never happened** |
| 3 | `joblib.dump(model, "churn_model.pkl")` | Saved an **untrained** model — dump saves whatever state exists |
| 4 | `joblib.load(...)` | Loads it back, still untrained |
| 5 | `.predict(X_new)` | ❌ `NotFittedError` — there are no learned splits to predict with |

**The fix:** call `model.fit(X_train, y_train)` **before** `joblib.dump`. The model class is irrelevant — the *gap in the lifecycle* is the whole question.

**The model-persistence error family (know all three):**

| Error | Cause | Fix |
|-------|-------|-----|
| `NotFittedError` | Saved/used before `fit()` | Train first, then save |
| `FileNotFoundError` on `joblib.load` | **The file doesn't exist at that path** | Check filename/folder — nothing to do with training length, missing values, or tree count |
| Overwritten model, can't roll back | Same filename every month | **Version the filenames:** `model_v1.pkl`, `model_v2.pkl`, … |

**Why the versioning practice wins (the monthly-update scenario):** version numbers let you roll back a bad model, compare versions, and know exactly what's deployed. Same-filename saves destroy history; deleting old models immediately removes your rollback; retraining on every prediction request is absurdly wasteful.

**Key Rule:**

> The lifecycle is **create → fit → dump → load → predict**. Skip `fit` and you get `NotFittedError`; botch the path and you get `FileNotFoundError`; skip versioning and you get a career lesson.

</p>
</details>

---

# Part 2 — Python, NumPy/Pandas, Workflow & Evaluation

## Study Guide — Part 2 Concepts

### Python Fundamentals
- [ ] **Default parameters** — `def f(a, b=2)`: `b` is optional, `a` is NOT; calling `f()` is a `TypeError`
- [ ] **Early return** — `if cond: return X` then `return Y` needs no `else`; first `return` reached wins
- [ ] **Classes** — `__init__` runs at creation; `self.attr` is per-object state; a method without `return` gives `None`
- [ ] **Operator precedence** — `and` binds tighter than `or`: `P and Q or R` = `(P and Q) or R`
- [ ] **`continue`** — skips the rest of the current iteration; the loop still runs all its iterations
- [ ] **File modes** — `"w"` overwrites, `"a"` appends, `"r"` reads; disappearing log lines = `"w"` bug

### NumPy & Pandas
- [ ] **2D slicing** — `A[2:5, 0:3]` = rows 2–4, cols 0–2 (stop excluded); `A[r][c]` chaining ≠ `A[r, c]`
- [ ] **1D vs 2D results** — `A[:, 2]` → 1D values; `A[:, 2:3]` → 2D one-column matrix; `A[..., 2]` ≡ `A[:, 2]`
- [ ] **X/y slicing** — features `X = data[:, :2]`, target `y = data[:, 2]`
- [ ] **Column selection** — `df["Salary"]` one column; `df[["Age","Salary"]]` (double brackets) several
- [ ] **Loading & inspecting** — `pd.read_csv()`; `df.info()` = dtypes + non-null counts; `df.shape` = (rows, cols)
- [ ] **Text standardization** — `df["City"].str.lower()` / `.str.upper()` unifies inconsistent category spellings

### Visualization
- [ ] **Matplotlib** = the fundamental library; **Seaborn** = polished statistical charts with minimal effort
- [ ] **Chart choice** — `scatter` = relationship between two variables; `plot` = trend; `hist` = distribution; `bar` = category comparison
- [ ] **Chart clarity** — real axis labels with units (`"Month"`, `"Visitors"`, `"$"`) and a specific title beat `"X"`/`"Y"` every time
- [ ] **`plt.show()`** — no call, no window; **heatmap** = the correlation-matrix chart

### Workflow, Algorithms & Evaluation
- [ ] **ML workflow order** — Import → Clean → **Split** → Train → Evaluate (split BEFORE train; evaluate LAST)
- [ ] **Supervised vs unsupervised** — labels/prediction vs no-labels/pattern discovery; spam = classification
- [ ] **Decision tree** — explainable, non-linear, produces rules; `max_depth=3` limits tree depth
- [ ] **SVM & scaling** — distance-based → scale features
- [ ] **Regularization** — penalises large coefficients; **Ridge = L2**, Lasso = L1
- [ ] **Overfitting = high variance** — memorises training data, fails on unseen data
- [ ] **Accuracy** = (TP+TN)/total — know it apart from precision and recall on the same matrix
- [ ] **Model comparison** — higher accuracy wins (classification); lower MSE/RMSE + higher R² wins (regression)
- [ ] **Test set** — final evaluation ONLY; never for feature selection, model comparison, or tuning
- [ ] **Data quality** — impossible values (age −5), extreme outliers ($1M salary); **binning** = numeric → ranges
- [ ] **Regression equation** — in `y = b₀ + b₁x`: `b₀` = intercept (y when x = 0), `b₁` = slope (change in y per unit x)

---

## Python Fundamentals

---

###### 27. Given the Python function below, which statements are correct? (Select ALL that apply)

```python
def power(base, exp=2):
    return base ** exp
```

- A: `power(3)` returns 9
- B: `power(2, 3)` returns 8
- C: Parameter `exp` has a default value
- D: Both parameters are optional

<details><summary><b>Answer</b></summary>
<p>

#### Answer: A, B, C

**Trace each call:**

| Call | `base` | `exp` | Result |
|------|--------|-------|--------|
| `power(3)` | 3 | 2 (default used) | 3² = **9** ✅ |
| `power(2, 3)` | 2 | 3 (default overridden) | 2³ = **8** ✅ |
| `power()` | ❌ missing | — | `TypeError: missing 1 required positional argument: 'base'` |

**Why D is the trap:** only parameters **with** a default are optional. `base` has no default → it is **required**. "Both parameters are optional" would need `def power(base=1, exp=2)`.

**Key Rule:**

> Default value → optional. No default → required. Whatever the function is called, the planted false statement is always some form of "both parameters are optional" — only the defaulted one is.

**Bonus rule:** parameters with defaults must come **after** ones without — `def f(a=1, b)` is a `SyntaxError`.

</p>
</details>

---

###### 28. Consider the Python code. Which statements are correct? (Select ALL that apply)

```python
def sign(n):
    if n >= 0:
        return "Positive"
    return "Negative"
```

- A: `sign(7)` returns `"Positive"`
- B: An `else` statement is required for this function to work
- C: The function always returns a string (for numeric input)
- D: `sign(-3)` returns `"Negative"`

<details><summary><b>Answer</b></summary>
<p>

#### Answer: A, C, D

**The early-return pattern:** `return` **exits the function immediately**. If the `if` branch fires, the second `return` is never reached; if it doesn't fire, execution falls through to the second `return`. The two paths are mutually exclusive **without any `else`**.

**Trace:**

| Call | `n >= 0`? | Path | Returns |
|------|-----------|------|---------|
| `sign(7)` | ✅ | first `return` | `"Positive"` |
| `sign(-3)` | ❌ | falls through | `"Negative"` |
| `sign(0)` | ✅ (0 ≥ 0) | first `return` | `"Positive"` |

**Why B is false:** these two are exactly equivalent —

```python
if n >= 0:                    if n >= 0:
    return "Positive"             return "Positive"
return "Negative"             else:
                                  return "Negative"
```

The `else` is legal but **redundant** — experienced Python style actually prefers the left version.

**Why C is true:** every numeric input reaches one of the two `return "..."` lines, so the output is always a string. (Pedantic footnote: a non-numeric input like `sign("hi")` raises `TypeError` at the comparison and returns nothing — but within the intended numeric domain, C holds. Any two-branch return function has this property: one of the two `return` statements always fires.)

**Key Rule:**

> `return` ends the function on the spot. An `if` + `return` followed by a bare `return` is a complete either/or — "the `else` is required" is the planted false statement in every version of this question.

</p>
</details>

---

###### 29. Consider the Python class. Which statements are correct? (Select ALL that apply)

```python
class BankAccount:

    def __init__(self):
        self.balance = 0

    def deposit(self):
        self.balance += 100
```

- A: `balance` is initialized to 0
- B: Calling `deposit()` increases `balance` by 100
- C: `deposit()` returns the new balance
- D: Different `BankAccount` objects maintain their own balances

<details><summary><b>Answer</b></summary>
<p>

#### Answer: A, B, D

**Trace the lifecycle:**

```python
acc1 = BankAccount()     # __init__ runs → acc1.balance = 0
acc2 = BankAccount()     # a SECOND, independent object → acc2.balance = 0
acc1.deposit()           # acc1.balance becomes 100
print(acc1.balance)      # 100
print(acc2.balance)      # 0  ← untouched!
x = acc1.deposit()       # balance becomes 200, but...
print(x)                 # None ← deposit() has NO return statement
```

**Statement by statement:**

| Statement | Verdict | Why |
|-----------|---------|-----|
| A | ✅ | `__init__` runs automatically at creation and sets `self.balance = 0` |
| B | ✅ | `self.balance += 100` mutates the object's attribute |
| **C** | ❌ | There is **no `return`** in `deposit()` — it returns `None`. It *changes* the value but doesn't *hand it back* |
| D | ✅ | `self.balance` is an **instance attribute** — each object carries its own copy |

**Key Rule:**

> `__init__` = runs once per object at creation. `self.attr` = per-object state (that's what `self` means). A method without `return` **modifies but returns `None`** — and a "the method returns the new value" statement is the planted trap whenever the method body has no `return`.

**Why this matters:** "It changed the value, therefore it returned the value" is the classic confusion. Mutation and return are independent — a method can do either, both, or neither.

</p>
</details>

---

###### 30. Given the code below, which statements are TRUE? (Select ALL that apply)

```python
x = 10
y = 8

if x > 7 and y < 5 or x == 10:
    print("YES")
else:
    print("NO")
```

- A: The condition is evaluated as `(x>7 and y<5) or (x==10)`
- B: The output is YES
- C: Python evaluates `and` before `or`
- D: Adding parentheses — `x>7 and (y<5 or x==10)` — produces the same output for all values

<details><summary><b>Answer</b></summary>
<p>

#### Answer: A, B, C, D — all four are true (D is the subtle one)

**A and C — precedence:** Python's operator precedence puts `and` above `or`, so the bare expression groups as `(x>7 and y<5) or (x==10)`. Both statements say the same thing.

**B — trace with x=10, y=8:**

| Piece | Value |
|-------|-------|
| `x > 7` | True (10 > 7) |
| `y < 5` | False (8 < 5 ✗) |
| `x > 7 and y < 5` | False |
| `x == 10` | True |
| `False or True` | **True → prints YES** ✅ |

**D — the higher-order-thinking catch.** In *general*, moving parentheses like this changes the logic: `(P and Q) or R` differs from `P and (Q or R)` whenever `R` is True but `P` is False. **But look at what P and R are here:**

- `R` is `x == 10`, and `P` is `x > 7`
- If `x == 10` is True, then `x > 7` is **automatically also True** — 10 is greater than 7
- So the only case where the two forms could disagree (`R` True, `P` False) is **impossible** for these particular conditions

Formally: `P and (Q or R)` expands to `(P and Q) or (P and R)`, and since `R` implies `P`, the term `P and R` is just `R`. The two expressions are equivalent **for every value of x and y** — statement D is true *for this specific pair of conditions*, even though the rearrangement would be unsafe in general.

**Prove the general danger to yourself:** if the equality were `x == 5` instead of `x == 10`, then `x = 5` gives: original `(False and ...) or True` → **YES**, rearranged `False and (...)` → **NO**. Different! The safety here comes entirely from `x == 10 ⟹ x > 7`. Whenever a question claims two boolean forms agree "for all values", check whether the moved condition *implies* its new partner before judging.

**Key Rule:**

> `not` > `and` > `or` in precedence. And when a question claims two boolean forms are "the same for all values," don't guess — check whether the moved term can ever be True while its new partner is False.

</p>
</details>

---

###### 31. Given the code below, which statements are TRUE? (Select ALL that apply)

```python
total = 0

for i in range(1, 8):
    if i % 3 == 0:
        continue
    total += i
```

- A: Removing `continue` changes the final value to 28
- B: `continue` skips the numbers that are NOT divisible by 3
- C: The loop body starts seven times
- D: The final value of `total` is 19

<details><summary><b>Answer</b></summary>
<p>

#### Answer: A, C, D

**Trace:**

| `i` | `i % 3 == 0`? | Action | `total` |
|-----|---------------|--------|---------|
| 1 | No | `total += 1` | 1 |
| 2 | No | `total += 2` | 3 |
| 3 | **Yes** | `continue` → skip the `+=` | 3 |
| 4 | No | `total += 4` | 7 |
| 5 | No | `total += 5` | 12 |
| 6 | **Yes** | `continue` | 12 |
| 7 | No | `total += 7` | **19** |

**Statement by statement:**

| Statement | Verdict | Why |
|-----------|---------|-----|
| A | ✅ | Without `continue`, every `i` is added: 1+2+3+4+5+6+7 = **28**, not 19 |
| **B** | ❌ | `i % 3 == 0` is true for **multiples of 3** — those are exactly what `continue` skips. Everything else gets added. Read the condition, not the vibe |
| C | ✅ | `i` takes all seven values 1–7. `continue` skips the *rest of one iteration* — it doesn't reduce how many iterations happen (that would be `break`) |
| D | ✅ | 1 + 2 + 4 + 5 + 7 = 19 |

**Key Rule:**

> `continue` = "skip the rest of THIS iteration, keep looping." The loop body still *starts* for every element. `break` = "stop looping entirely." Whatever the modulus and range, trace it the same way — and expect one statement to claim `continue` skips the numbers it actually *keeps*.

</p>
</details>

---

###### 32. A script records one sensor reading each time it runs, but the history file only ever contains the **most recent** reading — all earlier readings vanish. What is the most likely reason?

```python
with open("readings.csv", "w") as f:
    f.write(f"{sensor_id},{value}\n")
```

- A: The `with` statement erases the file when it closes
- B: `f.write()` always clears the file before writing
- C: Opening the file in `"w"` mode truncates (empties) the existing file
- D: CSV files can only hold one line

<details><summary><b>Answer</b></summary>
<p>

#### Answer: C

**File modes are the whole story:**

| Mode | Name | Behaviour |
|------|------|-----------|
| `"r"` | read | Read only; error if the file doesn't exist |
| **`"w"`** | write | **Truncates (empties) the file the moment it's opened**, then writes fresh |
| `"a"` | append | Keeps existing content, adds new writes at the **end** — the correct mode for logs |

Every run opens the file in `"w"`, which wipes it *before* a single byte is written — so only the newest reading survives.

**The fix:**

```python
with open("readings.csv", "a") as f:      # append mode
    f.write(f"{sensor_id},{value}\n")
```

**Why the other options are wrong:**

| Option | Why wrong |
|--------|-----------|
| A | `with` guarantees the file is *closed* properly (even on exceptions) — it never deletes anything |
| B | `write()` just writes at the current position — the deletion happened at `open(..., "w")`, not at `write()` |
| D | A CSV is just a text file — it holds as many lines as you write |

**Key Rule:**

> `"w"` wipes, `"a"` appends. Logs, histories, anything accumulating → `"a"`. The `with` block is good practice (auto-close) and is innocent here. A log file losing old messages is the same bug in different clothes — and "Python automatically clears files" style distractors are always invented behaviour.

</p>
</details>

---

## NumPy & Pandas

---

###### 33. What does this code print?

```python
import numpy as np

A = np.arange(1, 37).reshape(6, 6)
print(A[2:5, 0:3])
```

- A: `[[ 7 8 9] [13 14 15] [19 20 21]]`
- B: `[[13 14 15] [19 20 21] [25 26 27]]`
- C: `[[ 3 4 5] [ 9 10 11] [15 16 17]]`
- D: `[[14 15 16] [20 21 22] [26 27 28]]`

<details><summary><b>Answer</b></summary>
<p>

#### Answer: B

**Lay out the matrix with its indices first — always:**

```
            col:  0   1   2   3   4   5
row 0          [  1   2   3   4   5   6 ]
row 1          [  7   8   9  10  11  12 ]
row 2          [ 13  14  15  16  17  18 ]
row 3          [ 19  20  21  22  23  24 ]
row 4          [ 25  26  27  28  29  30 ]
row 5          [ 31  32  33  34  35  36 ]
```

**Decode the slice `A[2:5, 0:3]`:**

| Part | Meaning | Selected |
|------|---------|----------|
| `2:5` (rows) | start 2 included, stop 5 **excluded** | rows 2, 3, 4 |
| `0:3` (cols) | start 0 included, stop 3 excluded | cols 0, 1, 2 |

**Intersect:** rows 2–4 × cols 0–2 →

```
[[13 14 15]
 [19 20 21]
 [25 26 27]]
```

**How the wrong options are generated (learn the traps):**

| Option | The mistake it represents |
|--------|---------------------------|
| A | Starting rows one too early (`1:4` instead of `2:5`) |
| C | Swapping rows and columns (`A[0:3, 2:5]`) |
| D | Treating the starts as 1-indexed positions (off-by-one on both axes) |

**Key Rule:**

> `A[rows, cols]` — rows before the comma. Start **included**, stop **excluded**, everything 0-indexed. Sketch the grid with indices before answering; it takes 15 seconds and eliminates all three traps. Matrix-slice questions are a fixture (often more than one per paper), so the 15-second habit pays every time.

</p>
</details>

---

###### 34. `A = np.arange(1, 37).reshape(6, 6)` (the same 6×6 as Q33). Which statements return the following? (Select ALL that apply)

```
[[15 16]
 [21 22]]
```

- A: `A[[2,3], 2:4]`
- B: `A[2:4, 2:4]`
- C: `A[2:4][2:4]`
- D: `A[2:4, :][:, 2:4]`

<details><summary><b>Answer</b></summary>
<p>

#### Answer: A, B, D

The target is rows 2–3 × cols 2–3 (values 15, 16 / 21, 22).

**Evaluate each:**

| Expression | Step by step | Result |
|------------|--------------|--------|
| **A** `A[[2,3], 2:4]` | Fancy-index rows [2, 3], then slice cols 2:4 | ✅ rows 2–3, cols 2–3 |
| **B** `A[2:4, 2:4]` | The canonical form: rows 2–3, cols 2–3 | ✅ |
| **C** `A[2:4][2:4]` | **Two ROW operations, not row-then-column!** See below | ❌ |
| **D** `A[2:4, :][:, 2:4]` | First take rows 2–3 (all cols) → 2×6; then all rows, cols 2–3 → 2×2 | ✅ |

**Why C fails — the chained-bracket trap:**

```python
step1 = A[2:4]        # rows 2–3 → a 2-row array:
                      # [[13 14 15 16 17 18]
                      #  [19 20 21 22 23 24]]
step2 = step1[2:4]    # rows 2–3 OF THAT — but it only has rows 0 and 1!
                      # → an EMPTY array, shape (0, 6)
```

Each `[...]` applied to a 2D array indexes **rows** (axis 0) again. `A[2:4][2:4]` never touches columns — and because out-of-range *slices* return empty rather than erroring, it fails silently. Compare with D, which works because the second bracket explicitly says `[:, 2:4]` — all rows, columns 2–3.

**Key Rule:**

> Row-and-column selection needs the **comma inside one bracket** (`A[r, c]`) or an explicit column slice in the second bracket (`[:, c]`). Chained plain brackets `A[r1][r2]` slice rows twice — the classic wrong option on every NumPy question.

</p>
</details>

---

###### 35. Given `A = np.arange(1, 21).reshape(4, 5)`, which statements print exactly `[ 3 8 13 18]`? (Select ALL that apply)

- A: `A[2]`
- B: `A[:, 2]`
- C: `A[:, 2:3]`
- D: `A[..., 2]`

<details><summary><b>Answer</b></summary>
<p>

#### Answer: B, D

**The matrix:**

```
            col:  0   1   2   3   4
row 0          [  1   2   3   4   5 ]
row 1          [  6   7   8   9  10 ]
row 2          [ 11  12  13  14  15 ]
row 3          [ 16  17  18  19  20 ]
```

Target: column 2 as a **1D array** — printed `[ 3 8 13 18]`.

**Evaluate each:**

| Expression | Shape | Printed as | Match? |
|------------|-------|-----------|--------|
| **A** `A[2]` | (5,) | `[11 12 13 14 15]` | ❌ that's **row** 2, not column 2 |
| **B** `A[:, 2]` | (4,) — 1D | `[ 3  8 13 18]` | ✅ |
| **C** `A[:, 2:3]` | (4, 1) — **2D column** | `[[ 3]`<br>` [ 8]`<br>` [13]`<br>` [18]]` | ❌ same numbers, different shape and printout |
| **D** `A[..., 2]` | (4,) — 1D | `[ 3  8 13 18]` | ✅ `...` (Ellipsis) means "all the other axes" — identical to `A[:, 2]` here |

**The integer-vs-slice rule (this is the whole question):**

| Index style | Effect on that axis |
|-------------|---------------------|
| Integer `1` | Selects and **collapses** the axis → dimension disappears → 1D result |
| Slice `1:2` | Selects but **keeps** the axis → still 2D, just one column wide |

Same data, different shape — and the printout gives it away instantly (one row of numbers vs a stack of bracketed singles).

**Key Rule:**

> `A[:, c]` = 1D column values. `A[:, c:c+1]` = 2D one-column matrix. `A[..., c]` = same as `A[:, c]`. Bare `A[r]` = a **row**. On "which prints exactly…" questions, shape is the answer — check whether the target shows one pair of brackets (1D) or nested brackets (2D). The integer-vs-slice logic transfers unchanged to any matrix size.

</p>
</details>

---

###### 36. A developer has this dataset and wants to train a model where `Churned` is the target. Which slicing strategy is most appropriate?

```python
data = np.array([
    [34, 5200, 3, 1],
    [45, 6100, 8, 0],
    [29, 4800, 2, 1],
    [52, 7300, 12, 0]
])
# Col 0 = Age, Col 1 = Income, Col 2 = YearsCustomer, Col 3 = Churned
```

- A: `X = data[:, 3]` and `y = data[:, :3]`
- B: `X = data` and `y = data[:, 3]`
- C: `X = data[:, :3]` and `y = data[:, 3]`
- D: `X = data[:, 0]` and `y = data[:, 0]`

<details><summary><b>Answer</b></summary>
<p>

#### Answer: C

**What the model needs:**

| Piece | Contents | Slice |
|-------|----------|-------|
| `X` (features) | Age, Income, YearsCustomer — everything the model may look at | `data[:, :3]` → all rows, columns 0–2 |
| `y` (target) | Churned — the answer column | `data[:, 3]` → all rows, column 3 |

**Why each wrong option is wrong:**

| Option | Problem |
|--------|---------|
| A | Reversed — trains on the answer to predict the features |
| B | X = the whole array — **the target column is inside X**. The model can read the answer directly: perfect training scores, zero real learning. Target leakage in its purest form |
| D | X = y = the Age column — the model "predicts" a feature from itself and has no target |

**Key Rule:**

> Features = every column **except** the target (`[:, :3]` here, or `np.delete`/`df.drop` in general). Target = exactly one column. If the target column is reachable inside X, your model is cheating — and option B is what that mistake looks like in code. However many columns the array has, the pattern is identical: features = every column before the target, target = its own column.

**Why this matters:** This is the exam-sized version of the leakage errors that decided real marks in the mini-project — one group's EDA created a column equal to the target and only survived because a single `drop` line removed it.

</p>
</details>

---

###### 37. Given the DataFrame below, which statements are correct? (Select ALL that apply)

```python
df = pd.DataFrame({
    "Age": [25, 30, 35],
    "Salary": [3000, 4500, 6000],
    "Purchased": ["Yes", "No", "Yes"]
})
```

- A: `df["Salary"]` selects the Salary column
- B: `df[["Age", "Salary"]]` returns a DataFrame with both columns
- C: `df[Salary]` raises a `NameError`
- D: `df["Age", "Salary"]` also returns the two columns

<details><summary><b>Answer</b></summary>
<p>

#### Answer: A, B, C

**The bracket rules:**

| Code | What happens |
|------|--------------|
| **A** `df["Salary"]` | ✅ One string key → the Salary column (a Series) |
| **B** `df[["Age", "Salary"]]` | ✅ A **list** of column names → a DataFrame with those columns. Outer brackets = indexing, inner brackets = the list — hence "double brackets" |
| **C** `df[Salary]` | ✅ the statement is correct — without quotes, `Salary` is treated as a Python **variable**, which doesn't exist → `NameError: name 'Salary' is not defined` |
| **D** `df["Age", "Salary"]` | ❌ Two strings without list brackets form a **tuple** key `("Age", "Salary")` — pandas looks for a single column with that weird name → `KeyError` |

**The selection cheat sheet:**

| Want | Code |
|------|------|
| One column | `df["Salary"]` |
| Several columns | `df[["Age", "Salary"]]` — double brackets |
| One column by position | `df.iloc[:, 1]` |
| Rows by condition | `df[df["Age"] > 28]` |

**Key Rule:**

> Quotes make it a column name; no quotes make it a variable. One name → single brackets; multiple names → a **list inside** the brackets. And watch for invented methods like `df.select("Salary")` — pandas has no such method; bracket selection is the way.

</p>
</details>

---

###### 38. A developer receives `sales_records.csv` and wants to load it into a DataFrame. (pandas imported as `pd`) Which code should be used?

- A: `df = pd.open_csv("sales_records.csv")`
- B: `df = pd.read_csv("sales_records.csv")`
- C: `df = pd.csv_read("sales_records.csv")`
- D: `df = pd.get_csv("sales_records.csv")`

<details><summary><b>Answer</b></summary>
<p>

#### Answer: B

`pd.read_csv()` is the real function — the other three are invented, and any spelling that isn't `read_<format>` (`load_csv`, `import_csv`, bare `read`) is invented too. Pandas readers all follow the same naming pattern:

| Format | Real function |
|--------|---------------|
| CSV | `pd.read_csv("file.csv")` |
| Excel | `pd.read_excel("file.xlsx")` |
| JSON | `pd.read_json("file.json")` |

**Pattern:** `pd.read_<format>()`. There is no `load_csv`, no bare `read`, no `import_csv`.

**What can still go wrong with the correct code:**

| Symptom | Cause |
|---------|-------|
| `FileNotFoundError` | The file isn't in the working directory / path is wrong — same error family as `joblib.load` in B6 |
| Everything in one column | Wrong separator — e.g. the bank dataset needed `sep=";"` |

**Key Rule:**

> `pd.read_csv()` to load, then immediately inspect: `df.head()` (first rows), `df.shape` (size), `df.info()` (structure — next question). Read → inspect → clean, in that order.

</p>
</details>

---

###### 39. A developer wants a single command that shows a dataset's structure — every column's data type AND how many non-null values it holds. Which is correct? (pandas imported, `df` loaded)

- A: `df.head()`
- B: `df.shape()`
- C: `df.info()`
- D: `df.sum()`

<details><summary><b>Answer</b></summary>
<p>

#### Answer: C

`df.info()` prints, per column: the **dtype**, the **non-null count** (which reveals missing values by subtraction), plus row count and memory usage — exactly "structure including data types and missing values."

**Why the others fail:**

| Option | Problem |
|--------|---------|
| A `df.head()` | Shows the first 5 rows of *data* — you can eyeball types, but no dtype list, no missing counts |
| B `df.shape()` | **Trap:** `df.shape` is an *attribute*, not a method — with `()` it raises `TypeError`. Even without, it's just `(rows, cols)` |
| D `df.sum()` | Column totals — a statistic, not structure |

(`df.columns()` is another instance of the same attribute-called-as-method trap — `columns`, like `shape`, is an attribute.)

**The inspection toolkit (know all four):**

| Command | Tells you |
|---------|-----------|
| `df.info()` | dtypes + non-null counts + memory — the structure overview |
| `df.shape` | `(rows, columns)` tuple — **`(900, 8)` means 900 rows and 8 columns**, in that order — worth stating from memory |
| `df.head()` | First 5 rows — eyeball the actual values |
| `df.describe()` | Count/mean/std/min/quartiles/max for numeric columns |

**Key Rule:**

> `shape` = how big, `info` = what types and what's missing, `head` = what it looks like, `describe` = how it's distributed. Rows always come first in `shape` — `(900, 8)` is 900 rows, never 900 columns.

</p>
</details>

---

###### 40. What is the purpose of this line? (pandas imported, `df` loaded)

```python
df["City"] = df["City"].str.lower()
```

- A: Remove duplicate rows
- B: Standardize values
- C: Sort the City column alphabetically
- D: Fill missing city names

<details><summary><b>Answer</b></summary>
<p>

#### Answer: B

**The problem it solves:** free-text categorical columns arrive messy —

| Raw `City` values | After `.str.lower()` |
|-------------------|----------------------|
| `"Singapore"`, `"SINGAPORE"`, `"singapore"` | all become `"singapore"` |
| `"Jurong"`, `"JURONG"` | all become `"jurong"` |

Three spellings of the same city would otherwise be treated as **three different categories** — a groupby shows 3 groups, one-hot encoding creates 3 columns, the model sees 3 distinct values. Unifying the case **standardizes** them into one consistent label. This is the "correct inconsistent data" step of data cleaning.

**Method map for the option types:**

| Goal | Method |
|------|--------|
| **Standardize text case** | `.str.lower()` or `.str.upper()` — both work; pick one and apply it everywhere (upper or lower, on any text column — same purpose, same reasoning) |
| Fill missing | `.fillna(...)` |
| Remove duplicates | `.drop_duplicates()` |
| Sort | `.sort_values(...)` |

**Key Rule:**

> `.str.upper()` / `.str.lower()` = make inconsistent category spellings identical = **standardizing values**. Watch for the trap pairing: `.mean()` on a text column (errors), `.duplicated()` (returns True/False flags — it doesn't standardize anything).

</p>
</details>

---

## Visualization

---

###### 41. Two requests come in: (1) a developer wants to build a simple line chart using the most **fundamental** Python visualization library; (2) a manager wants a **professional-looking statistical chart with minimal customization effort**. Which library pairing is correct?

- A: (1) Matplotlib, (2) Seaborn
- B: (1) Seaborn, (2) Matplotlib
- C: (1) NumPy, (2) TensorFlow
- D: (1) Scikit-learn, (2) Pandas

<details><summary><b>Answer</b></summary>
<p>

#### Answer: A

| Library | Role | The signal words in exam questions |
|---------|------|--------------------------------------|
| **Matplotlib** | The foundational plotting library — everything else builds on it | "fundamental", "basic", "simple line chart" |
| **Seaborn** | Built ON TOP of Matplotlib; attractive statistical charts with one-liners and good default styling | "professional-looking", "minimal effort", "statistical" |
| NumPy | Arrays and math — no charts | — |
| TensorFlow | Deep learning — not in this module's toolkit | — |
| Scikit-learn | Models and preprocessing — no charts | — |
| Pandas | Data handling (it has `.plot()`, but it calls Matplotlib underneath) | — |

**The relationship in one line:** Seaborn is a beautification layer over Matplotlib — `import seaborn as sns; sns.boxplot(data=df)` gives you in one call what raw Matplotlib needs a dozen styling lines for. Matplotlib gives full control; Seaborn gives fast polish.

**Key Rule:**

> "Fundamental" → **Matplotlib**. "Professional with minimal effort" → **Seaborn**. These usually arrive as two separate questions — one keyword decides each.

</p>
</details>

---

###### 42. A developer wants to visualize the **relationship between StudyHours and ExamScore**. What goes in the blank? (pandas imported, `df` loaded)

```python
import matplotlib.pyplot as plt

plt.________(df["StudyHours"], df["ExamScore"])
plt.show()
```

- A: `bar`
- B: `scatter`
- C: `hist`
- D: `plot`

<details><summary><b>Answer</b></summary>
<p>

#### Answer: B

"**Relationship between two** numeric variables" is the scatter plot's exact job: one dot per row at (StudyHours, ExamScore), and the cloud's shape shows whether they move together. (The trigger phrase "relationship between" is what you're matching — the column names never matter.)

**Chart-type decision table (this decides a whole family of questions):**

| You want to show | Chart | Call |
|------------------|-------|------|
| **Relationship between two numerics** | Scatter | `plt.scatter(x, y)` |
| Trend over an ordered sequence (time) | Line | `plt.plot(x, y)` |
| Distribution of ONE numeric | Histogram | `plt.hist(x)` |
| Comparison across categories | Bar | `plt.bar(labels, values)` |
| Outliers / quartiles of one numeric | Boxplot | `plt.boxplot(x)` |
| Correlation matrix of many features | Heatmap | `sns.heatmap(df.corr())` |

**Why not `plot`?** `plt.plot` draws a **connected line** in the order the rows happen to be in — for unordered Age/Salary data, that's spaghetti. A line implies sequence; a relationship question wants unconnected points.

**Key Rule:**

> Two variables, "relationship/correlated?" → `scatter`. One variable, "distribution?" → `hist` or boxplot. Ordered x (months, years), "trend?" → `plot`. Match the chart to the *question the viewer is asking*.

</p>
</details>

---

###### 43. A developer charts website traffic with the code below. The manager comments: *"Visitors to which site? Over what period? What do the axes show?"* Which modifications would MOST improve the chart? (Select ALL that apply)

```python
plt.plot(months, visitors)
plt.title("Traffic")
plt.show()
```

- A: `plt.grid(True)`
- B: `plt.title("Monthly Visitor Traffic — beco.com, Jan–Jun 2026")`
- C: `plt.xlabel("X-axis")` and `plt.ylabel("Y-axis")`
- D: `plt.xlabel("Month")` and `plt.ylabel("Visitors")`

<details><summary><b>Answer</b></summary>
<p>

#### Answer: B, D

**Map the manager's complaints to fixes — every complaint names its own fix:**

| Complaint | Fix |
|-----------|-----|
| "Visitors to **which site**? Over **what period**?" | **B** — a specific title: *what* (Visitor Traffic), *whose* (beco.com), *period* (Jan–Jun 2026) |
| "What do the **axes** show?" | **D** — real axis labels: `"Month"`, `"Visitors"` |

**Why A and C don't make the cut:**

| Option | Problem |
|--------|---------|
| A | Gridlines are cosmetic polish; they address none of the three complaints. Not *wrong* — just not what "MOST improves" this chart |
| C | Labelling the x-axis `"X-axis"` adds literally zero information — it answers the manager's question with the question |

**The professional-chart checklist (sales, revenue, traffic — the scenario changes, the logic doesn't):**

- Specific title: what, where, when
- Axis labels **with units** (`$`, `°C`, `%`)
- Legend when there are multiple series
- Then, optionally: grid, styling, annotations

**Key Rule:**

> Labels answer the viewer's questions; decoration doesn't. On "which modifications MOST improve" questions, pick the options that resolve the stated complaints — placeholder labels (`"X"`, `"Data"`, `"Value"`) are always wrong.

</p>
</details>

---

###### 44. A developer runs the following script from the terminal and **no chart appears** (and no error either). What is the most likely issue?

```python
import matplotlib.pyplot as plt

plt.bar(["A", "B", "C"], [3, 7, 5])
```

- A: Missing `plt.title()`
- B: Missing seaborn
- C: Bar charts require NumPy arrays, not lists
- D: Missing `plt.show()`

<details><summary><b>Answer</b></summary>
<p>

#### Answer: D

`plt.bar()` — like every other `plt.*` chart call — only **builds the figure in memory**. Nothing is rendered to the screen until `plt.show()` is called.

**The two-step model:**

| Step | Call | What happens |
|------|------|--------------|
| 1. Build | `plt.bar(...)`, `plt.xlabel(...)`, `plt.title(...)` | Figure assembled invisibly in memory |
| 2. Render | `plt.show()` | Window/graph actually appears |

**Why the others are wrong:**

| Option | Why |
|--------|-----|
| A | A missing title makes a *less informative* chart, not an *invisible* one |
| B | Matplotlib needs no seaborn; and a missing import would raise a visible `ImportError`, not silent nothingness |
| C | Plain lists are fine — matplotlib converts them internally |

**Jupyter footnote:** notebooks often display plots without `show()` (the cell auto-renders the figure) — which is exactly why students forget it exists. In a `.py` script run from the terminal, no `plt.show()` = no window, ever.

**Key Rule:**

> Symptom "no graph appears, no error" → missing `plt.show()`. Build first, render second.

</p>
</details>

---

###### 45. A developer wants one picture showing the **pairwise correlations between all numeric features at once**. Which visualisation is the standard choice?

- A: Histogram
- B: Area Chart
- C: Heatmap
- D: Boxplot

<details><summary><b>Answer</b></summary>
<p>

#### Answer: C

A correlation matrix is a grid of numbers — every feature against every feature, each cell holding a correlation from −1 to +1. A **heatmap** paints each cell by its value, so strong relationships jump out as hot/cold spots instead of hiding in a wall of decimals.

**The standard one-liner:**

```python
import seaborn as sns
sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
```

**Reading it:**

| Cell value | Meaning |
|------------|---------|
| Close to +1 | Features rise together (e.g. floor area vs price) |
| Close to −1 | One rises as the other falls |
| Close to 0 | No linear relationship |
| The diagonal | Always exactly 1 (each feature with itself) — ignore it |

**Why the others fail:** a histogram shows one variable's distribution, a boxplot shows one variable's spread, an area chart shows a trend — none can display an N×N grid of pairwise values. (Whatever the distractors — pie, line, boxplot — the elimination logic is identical: matrix-shaped data needs a matrix-shaped chart.)

**Key Rule:**

> Matrix-shaped data → heatmap. "Which features are correlated?" → `df.corr()` + heatmap. (You used these in the mini-projects — a correlation heatmap is often what first exposes two features carrying duplicated information.)

</p>
</details>

---

## ML Workflow, Algorithms & Evaluation

---

###### 46. A telco wants to predict which customers will churn (Yes/No). Which workflow is most appropriate?

- A: Train Classifier → Evaluate → Split Data
- B: Import Data → Evaluate → Split Data → Train
- C: Import Data → Clean Data → Train-Test Split → Train Classifier → Evaluate using Accuracy and F1
- D: Split Data → Import Data → Train Classifier → Evaluate

<details><summary><b>Answer</b></summary>
<p>

#### Answer: C

**The canonical order, and why each step must precede the next:**

| Step | Why it's here |
|------|---------------|
| 1. Import | Nothing happens without data |
| 2. Clean | Fix missing/duplicate/invalid values *before* they poison anything downstream |
| 3. **Split** | Set the test data aside **before** training so evaluation is honest |
| 4. Train | Model learns from the **training** portion only |
| 5. Evaluate | Judge on the held-out test portion — with **Accuracy and F1** because churn Yes/No is *classification* |

**Sanity-check the wrong options by asking "evaluate WHAT? train on WHAT? split WHAT?":**

| Option | Absurdity |
|--------|-----------|
| A | Splits the data *after* training and evaluating are already done |
| B | Evaluates a model that doesn't exist yet |
| D | Splits data that hasn't been imported |

**The regression twin:** for a price-prediction task the skeleton is identical — only the model and metrics change. The deciding features of the correct option never change: **Split before Train, Evaluate last**, and metrics that match the task type (RMSE/R² for regression, Accuracy/F1 for classification).

**Key Rule:**

> Import → Clean → **Split** → Train → Evaluate. Two instant elimination tests: does Split come before Train? Is Evaluate last? Any option failing either is wrong — and match the metrics to the task (RMSE/R² = regression; accuracy/F1 = classification).

</p>
</details>

---

###### 47. Which statements about supervised and unsupervised learning are correct? (Select ALL that apply)

- A: Supervised learning needs each training example to come paired with the correct answer
- B: Predicting a flat's resale price from past labelled sales is supervised learning
- C: Unsupervised learning finds structure in data that has no target column
- D: Grouping shoppers into segments with no predefined labels is unsupervised learning

<details><summary><b>Answer</b></summary>
<p>

#### Answer: A, B, C, D — all four are correct

Another all-true Select-ALL. Supervised-vs-unsupervised statement sets are frequently all-true, because two facts (labels/prediction vs no-labels/pattern-discovery) generate many equivalent phrasings. Verify each statement rather than hunting for a fake:

**The complete picture:**

| | Supervised | Unsupervised |
|---|---|---|
| Labels/target? | ✅ Required — that's the "supervision" | ❌ Not required |
| Learns | Input → output relationships | Structure hidden in the inputs |
| Used for | **Prediction** (of a target for unseen inputs) | **Pattern discovery** (groups, structure) |
| This module's examples | Linear/Logistic Regression, Decision Tree, Random Forest, SVM | K-Means clustering, PCA |

**The one-question test that sorts any scenario:** *"Does each training row come with a correct answer attached?"*

| Scenario | Answer attached? | Type |
|----------|------------------|------|
| Predict house price (past sale prices known) | ✅ | Supervised — regression |
| Spam or not (emails labelled) | ✅ | Supervised — classification |
| Group customers, no categories known | ❌ | Unsupervised — clustering |

**Key Rule:**

> Supervised = has labels = predicts. Unsupervised = no labels = discovers patterns. Four phrasings of two facts — that's why all the statements can be simultaneously true.

</p>
</details>

---

###### 48. A maintenance team wants to predict whether a machine will **Fail or Not Fail** tomorrow. Which type of ML problem is this?

- A: Clustering
- B: Regression
- C: Dimensionality Reduction
- D: Classification

<details><summary><b>Answer</b></summary>
<p>

#### Answer: D

The target is a **category from a fixed set** (Fail / Not Fail) — that is classification by definition, and with exactly two options it's *binary* classification. Spam or not, churn or not, pass or fail — the "whether X is A or B" phrasing always points the same way.

**The task-identification table (decides a whole family of questions):**

| The target is... | Task | Module example |
|------------------|------|----------------|
| A category (Yes/No, Spam/Ham, Pass/Fail) | **Classification** | Logistic Regression, Decision Tree |
| A continuous number ($, °C, count) | **Regression** | Linear Regression |
| Nonexistent — find natural groups | **Clustering** | K-Means |
| Nonexistent — compress many features | **Dimensionality Reduction** | PCA |

**Spot-the-task drill:**

| Scenario | Task |
|----------|------|
| Will this customer churn? | Classification |
| What will this flat sell for? | Regression |
| Segment shoppers with no predefined groups | Clustering |
| 500 correlated features → fewer | Dimensionality reduction |

**Key Rule:**

> Ask "what does one prediction look like?" A label → classification. A number → regression. No labels exist at all → clustering/PCA. The phrase "whether X is A or B" is always classification.

</p>
</details>

---

###### 49. Which statements about K-Means clustering are correct? (Select ALL that apply)

- A: K-Means finds the best number of clusters automatically during training
- B: It is unsupervised — it needs no target column
- C: Each data point is assigned to the cluster with the nearest centre
- D: The cluster centres summarise a typical member of each group

<details><summary><b>Answer</b></summary>
<p>

#### Answer: B, C, D

**Statement by statement:**

| Statement | Verdict | Why |
|-----------|---------|-----|
| **A** | ❌ | K is a **hyperparameter you choose before training** — `KMeans(n_clusters=3)`. The algorithm cannot learn it (elbow method + silhouette help *you* choose; see Q17) |
| B | ✅ | No target column, no labels — K-Means finds structure on its own |
| C | ✅ | Its whole objective: assign each point to the nearest centroid, i.e. group similar points |
| D | ✅ | Tutorial 9's phrasing: the centres are "the representative profile for each group" |

**The other classic false statement is "it requires labelled training data" planted next to an "it is unsupervised" statement.** Those two can never both be true, which hands you a free elimination: *unsupervised means no labels*. Whether the fake is a labels claim or a k-is-learned claim, the K-Means facts to hold onto are the same four.

**K-Means in 30 seconds:** pick K → place K centroids → assign each point to its nearest centroid → move each centroid to its cluster's mean → repeat until stable. Distance-based → **scale your features first**.

**Key Rule:**

> K-Means: unsupervised, K chosen in advance, groups by similarity, needs **no labels**. The false statement in any K-Means question is almost always a labels/supervised claim.

</p>
</details>

---

###### 50. A company needs a model that is easy to explain to managers, can handle non-linear relationships, and produces decision rules. Also: in `DecisionTreeClassifier(max_depth=3)`, what does `max_depth=3` do?

- A: Decision Tree; `max_depth` limits the tree depth
- B: SVM; `max_depth` limits the number of classes
- C: K-Means; `max_depth` limits the dataset size
- D: PCA; `max_depth` limits the test size

<details><summary><b>Answer</b></summary>
<p>

#### Answer: A

**Match the three requirements — only one candidate scores on all three:**

| Requirement | Decision Tree | SVM | K-Means | PCA |
|-------------|---------------|-----|---------|-----|
| Easy to explain to managers | ✅ literally a flowchart | ❌ abstract margins | (not a classifier) | (not a classifier) |
| Non-linear relationships | ✅ threshold splits stack into curves | ✅ with kernels, but opaque | — | — |
| Produces decision rules | ✅ "IF income > 5000 AND age < 30 THEN..." | ❌ | ❌ | ❌ |

**And `max_depth=3`:** it caps how many **levels of questions** the tree may ask — at most 3 splits from root to any leaf. Small depth = few, broad rules (explainable, may underfit); large/unlimited depth = many micro-rules (memorises, overfits). It is the tree's main overfitting control — the same knob as Q22, seen from the constructor side.

```
depth 1:        income > 5000?
               /              \
depth 2:  age < 30?        owns_home?
           /    \            /     \
depth 3:  ...   ...        ...     ...   ← stops here with max_depth=3
```

**Key Rule:**

> "Explainable + non-linear + rules" → **Decision Tree**, every time. `max_depth` limits **tree depth** — the distractors (classes, dataset size, test size) are controlled by entirely different things (your data and `train_test_split`).

</p>
</details>

---

###### 51. A K-Nearest-Neighbours classifier often improves after feature scaling because it:

- A: automatically removes outliers
- B: relies on distances between data points
- C: converts categorical features internally
- D: only accepts values between 0 and 1

<details><summary><b>Answer</b></summary>
<p>

#### Answer: B

KNN classifies a point by looking at its **nearest neighbours** — and "nearest" is a *distance*. If Salary spans 2000–20000 and Age spans 18–65, the distance is utterly dominated by Salary, and Age barely participates. Scaling puts both on comparable footing so "nearest" reflects *all* features.

**The SVM version of this question runs on the same mechanism:** an SVM maximises the **margin**, which is the distance between the boundary and the nearest points of each class. Any algorithm whose core computation is a distance needs scaled features — that phrase, "depends on distances between data points", is the reason whichever algorithm is named.

**The scaling-sensitivity table, completed (same as Q5):**

| Model | Scaling needed? | Mechanism that cares |
|-------|-----------------|----------------------|
| KNN | ✅ | Neighbour distances |
| **SVM** | ✅ | **Margin distances** |
| K-Means | ✅ | Centroid distances |
| Neural Network / MLP | ✅ | Gradient descent stability |
| Decision Tree / Random Forest | ❌ | Threshold splits — scale-free |

**The wrong options are different tools entirely:** outlier removal is data cleaning (IQR method), encoding categoricals is a separate preprocessing step KNN does not do for you, and KNN accepts any numeric range — [0, 1] is a MinMaxScaler *output*, not a KNN *requirement*. (Distractors like "removes duplicate records" or "automatically performs PCA" are the same category of stage-confusion.)

**Key Rule:**

> If the algorithm's core computation is a **distance**, scale first. KNN's "nearest" and SVM's margin are both distances — that's the entire answer, whichever algorithm the question names.

</p>
</details>

---

###### 52. Which regularization method is commonly known as **Ridge Regression** — and what does regularization generally do?

- A: L2; it penalizes large model coefficients
- B: L1; it creates new features
- C: Elastic Net; it increases dataset size
- D: SGD; it scales the data

<details><summary><b>Answer</b></summary>
<p>

#### Answer: A

**The name map (memorise this two-liner):**

| Penalty | Name | What the penalty does to coefficients |
|---------|------|---------------------------------------|
| **L2** (sum of squared coefficients) | **Ridge** | Shrinks all of them smoothly toward 0 |
| L1 (sum of absolute coefficients) | Lasso | Shrinks AND zeroes some out entirely — built-in feature selection |
| L1 + L2 combined | Elastic Net | Both behaviours blended |

(SGD is an *optimizer*, not a regularizer — it's the odd one out planted in the options.)

**What regularization is, mechanically:** a penalty term added to the loss —

```
new loss = prediction error + α × (size of coefficients)
```

Now the optimizer must balance fitting the data against keeping coefficients small. Huge coefficients — the signature of a model contorting itself around training noise — become expensive. Smaller coefficients = smoother, simpler model = **less overfitting**. That's why the general-purpose answer is "**penalizing large model coefficients**" — not creating features, not more data, not scaling (all real techniques, none of them regularization).

**Memory hook:** **L1 = Lasso** (both start with L... and Lasso *lassoes* coefficients to zero). Ridge gets the other one: **L2**.

**As Tutorial 10 wrote it** (worth recognising on sight):

```
MSE loss:                loss = mean((y_true - y_pred)^2)
Ridge regularization (L2):  + alpha * sum(w_i^2)
Lasso regularization (L1):  + alpha * sum(abs(w_i))
```

with `alpha` controlling penalty strength — "too small may not control overfitting much; too large may make the model too rigid and underfit." Tutorial 10 says Lasso "may even push some coefficients close to zero"; the sharper (and true) version is that Lasso can push coefficients **exactly** to zero, which is why it doubles as automatic feature selection.

**Key Rule:**

> Ridge = L2, Lasso = L1, Elastic Net = both; all of them work by penalizing large coefficients. Bigger α, stronger shrinkage — and the taught definition to quote: "a penalty added to the loss function to discourage overly large weights."

</p>
</details>

---

###### 53. A model **memorizes the training data but performs poorly on unseen data**. Separately: a bull's-eye chart shows predictions tightly clustered around the centre target. What do these two indicate?

- A: High Variance (overfitting); Low Bias + Low Variance
- B: High Bias (underfitting); High Bias + High Variance
- C: Underfitting; Low Bias + High Variance
- D: Scaling Error; High Bias + Low Variance

<details><summary><b>Answer</b></summary>
<p>

#### Answer: A

**Scenario 1 — "memorizes training, fails unseen":** that is the *definition* of **overfitting**, and its statistical name is **high variance**. Watch for the twist: an option list can offer "High Variance" but NOT "Overfitting" — you must know they're the same diagnosis, or you'll wrongly grab "Underfitting" as the nearest familiar word.

| Everyday name | Statistical name | Signature |
|---------------|------------------|-----------|
| Overfitting | **High variance** | Memorises training data, poor on unseen (big train–test gap) |
| Underfitting | High bias | Too simple — poor on both sets |

**Scenario 2 — tight cluster AT the centre:** apply the B5 decoder — position = bias, spread = variance:

| Cue | Reading |
|-----|---------|
| At the centre | **Low bias** — aiming at the right target |
| Tightly clustered | **Low variance** — consistent |

Low bias + low variance = the ideal model. (A "which characteristics describe a good model?" variant keys all four of *low bias, low variance, near the centre, tightly grouped* at once — because the last two are the first two in picture form.)

**Key Rule:**

> Overfitting **is** high variance; underfitting **is** high bias — one concept, two vocabularies, and a question may deliberately offer only one of them. Bull's-eye: **position = bias, spread = variance.**

</p>
</details>

---

###### 54. Using the confusion matrix below, calculate **Accuracy**.

| Actual \ Predicted | Fraud | Legitimate |
|---|---|---|
| **Fraud** | 50 | 25 |
| **Legitimate** | 10 | 115 |

- A: 66.7%
- B: 82.5%
- C: 83.3%
- D: 90%

<details><summary><b>Answer</b></summary>
<p>

#### Answer: B

**Label the four cells first (Fraud = positive class):**

| Cell | Meaning | Value |
|------|---------|-------|
| TP | Fraud predicted Fraud | 50 |
| FN | Fraud predicted Legitimate (missed) | 25 |
| FP | Legitimate predicted Fraud (false alarm) | 10 |
| TN | Legitimate predicted Legitimate | 115 |

**Accuracy = everything correct over everything:**

```
Accuracy = (TP + TN) / total = (50 + 115) / (50 + 25 + 10 + 115) = 165 / 200 = 82.5%
```

**Now decode the distractors — each is a REAL metric on the SAME matrix:**

| Option | What it actually is | Calculation |
|--------|--------------------|-------------|
| A 66.7% | **Recall** (of fraud) | 50 / (50+25) = 50/75 ≈ 66.7% |
| **B 82.5%** | **Accuracy** ✅ | (50+115)/200 |
| C 83.3% | **Precision** (of fraud) | 50 / (50+10) = 50/60 ≈ 83.3% |
| D 90% | plausible-looking filler | — |

The wrong options aren't random — they're the *other* metrics computed correctly. Every version of this question is built the same way: the wrong options are the recall and precision of the same matrix. So **compute, don't recognise**: four cells first, then (TP+TN)/total.

**The three formulas side by side:**

| Metric | Formula | Question it answers |
|--------|---------|--------------------|
| Accuracy | (TP+TN) / all | How often is the model right overall? |
| Precision | TP / (TP+FP) | Of the flagged, how many were real? |
| Recall | TP / (TP+FN) | Of the real, how many did we catch? |

**Key Rule:**

> Accuracy uses **all four cells**; precision and recall use only the positive-class row/column. On calculation questions, write the four-cell table first — the distractors are engineered to catch formula mix-ups.

**Layout convention:** these matrices put **Actual on rows, Predicted on columns** — the same convention as sklearn's `confusion_matrix` and Lab 9's plots. Week 9's warning applies: "half the class will read it transposed." Check the row/column headers before you compute anything.

</p>
</details>

---

###### 55. Two selection scenarios:

**(1)** Validation accuracies: KNN 79%, Decision Tree 86%, Random Forest 90%. If accuracy is the **only** criterion, which model is selected?
**(2)** Regression models: Model X — MSE 25, RMSE 5, R² 0.91; Model Y — MSE 81, RMSE 9, R² 0.64. Which deploys?

- A: (1) Decision Tree, (2) Both equal
- B: (1) Random Forest, (2) Model Y
- C: (1) KNN, (2) Need more data
- D: (1) Random Forest, (2) Model X

<details><summary><b>Answer</b></summary>
<p>

#### Answer: D

**Scenario 1:** the question *stipulates* accuracy is the only criterion — so it's a reading test: pick the biggest number. Random Forest, 90%. Don't overthink a question that has already fixed the rule ("all models equally suitable" is the overthinking trap).

**Scenario 2:** check the direction of each metric, then check they agree:

| Metric | Better is... | Model X | Model Y | Winner |
|--------|--------------|---------|---------|--------|
| MSE | Lower | 25 | 81 | X |
| RMSE | Lower | 5 | 9 | X |
| R² | **Higher** (closer to 1) | 0.91 | 0.64 | X |

All three point the same way → **Model X**, no ambiguity, no "need more data." (Sanity check the table is internally consistent: √25 = 5 and √81 = 9 — RMSE really is √MSE. Well-set tables always are; use it as a cross-check.)

**The direction table — worth over-learning:**

| Metric | Direction | Type |
|--------|-----------|------|
| Accuracy, Precision, Recall, F1 | Higher = better | Classification |
| R² | Higher = better (max 1.0) | Regression |
| MSE, RMSE, MAE | **Lower** = better | Regression |

**The trap this protects you from:** R² runs the *opposite* direction from the error metrics. A student who blurs "R² is like an error" picks Model Y off the 0.64 < 0.91 comparison — smaller number, wrong direction. Direction first, comparison second.

**Key Rule:**

> Errors go down, scores go up. When a comparison table gives multiple metrics, verify they agree — when they all point one way, that's your answer; if they conflict, the question is really asking which metric matters for the business.

</p>
</details>

---

###### 56. Which uses of the **test set** are acceptable? (Select ALL that apply)

- A: Deciding which features to keep in the model
- B: One final measurement of the chosen model's performance
- C: Comparing three candidate models to pick the winner
- D: Choosing the best `max_depth` for a Decision Tree

<details><summary><b>Answer</b></summary>
<p>

#### Answer: B — and only B

The test set exists to answer exactly one question, exactly once: *"how will the finished model do on data it has never influenced?"* Any activity that **makes a decision** based on test scores contaminates that answer. (Asked from the other side — "which activities should NOT use the test set?" — the same single fact answers it, mirrored: everything that *decides* is out.)

| Activity | Test set? | Where it belongs |
|----------|-----------|------------------|
| Feature selection (A) | ❌ | Training set (or train + validation) |
| **Final evaluation (B)** | ✅ | The test set's one and only job |
| Model comparison (C) | ❌ | **Validation** set |
| Hyperparameter tuning (D) | ❌ | Validation set / cross-validation on training data |

**Why decisions on the test set are poisonous:** if you pick features, models, or hyperparameters because they score best on the test set, the test set has *shaped* the model — its score is now an optimistic self-fulfilling number, not an honest estimate of unseen-data performance. You've silently converted your test set into a second validation set and have nothing left to measure with.

**The companion pattern — leakage-prevention Select-ALLs:** the correct actions are always the Q13 workflow (split first; fit the scaler on train only; transform both sets with it), and the planted wrong action is that workflow reversed — scaling before the split, which is the *definition* of preprocessing leakage.

**Key Rule:**

> Train = fit. Validation = decide (compare, tune, select). Test = **one final honest measurement**. If an activity involves *choosing between options*, it must not touch the test set.

**Why this matters:** This was one of the most common mistakes across the mini-projects — choosing hyperparameters or features by test-set scores while believing the test set was "held out." An exam question on this is the same principle with the difficulty turned down.

</p>
</details>

---

## Data Quality & Preparation

---

###### 57. A developer reviews the delivery-driver dataset below. Which records should be investigated as potential outliers or data-quality issues? (Select ALL that apply)

| Driver | Age | Weekly deliveries |
|--------|-----|-------------------|
| Raj | 24 | 310 |
| Mei | 28 | 295 |
| Sam | 24 | 310 |
| Kai | **−2** | 300 |
| Tan | 27 | **25,000** |

- A: Sam's record
- B: Kai's record
- C: Raj's record
- D: Tan's record

<details><summary><b>Answer</b></summary>
<p>

#### Answer: B, D

**Scan each record with the data-quality checklist:**

| Record | Issue | Type |
|--------|-------|------|
| **Kai, Age = −2** | A negative age is **impossible** — not merely unusual | **Invalid entry** (data error, certainly wrong) |
| **Tan, 25,000 deliveries/week** | ~80× his colleagues — one parcel every 24 seconds, around the clock | **Extreme outlier** (suspicious — investigate whether it's a typo, a unit error, or a logging glitch) |
| Raj / Sam | Identical Age and deliveries — but **different drivers** | Not an issue. Two 24-year-olds delivering 310 parcels is entirely plausible. A *duplicate* means the **same record** appears twice (same driver, all fields identical) — matching values across different people is coincidence, not duplication |
| Mei | Nothing unusual | Clean |

**The Raj/Sam subtlety is the real test:** if identical values made a record suspect, Raj would be exactly as suspect as Sam — the question offering them as *separate options* is the hint that neither is intended. `df.duplicated()` checks whole rows; with the Driver name included, Raj's and Sam's rows differ. Any version of this table is built the same way: find the impossible value, find the extreme outlier, and don't take the bait of matching values across different people.

**Invalid vs outlier — related but different:**

| | Invalid entry | Outlier |
|---|---|---|
| Example | Age −2, Gender "Yes" | 25,000 deliveries among ~300s; a $1M salary among $4k salaries |
| Could it be real? | **No** — violates the definition of the field | Possibly — that's why you investigate before deleting (remember the temperature sensor in Q3) |
| Typical fix | Correct at the source or treat as missing | Investigate → keep, cap, or remove with justification |

**Key Rule:**

> Impossible values = errors, always flagged. Extreme values = outliers, flagged for investigation. Matching values across *different* entities = usually nothing. Read the rows, not just the numbers.

</p>
</details>

---

###### 58. A developer transforms an `ExamScore` column into the categories `0-49`, `50-69`, `70-84`, `85-100`. What technique is this — and which variables are good candidates for it? (Select ALL candidates that apply)

The technique: **(i)** One-Hot Encoding / **(ii)** Normalization / **(iii)** Binning / **(iv)** Scaling

Candidates: — A: Monthly Income — B: Payment Method — C: Humidity — D: Height

<details><summary><b>Answer</b></summary>
<p>

#### Answer: The technique is (iii) Binning; good candidates are A, C, D

**What binning is:** converting a **continuous numeric** variable into a small set of **ranges (bins)** — `ExamScore 76` becomes category `70-84`. Direction matters: numeric → categorical.

**Why it's not the others:**

| Technique | What it does | Direction |
|-----------|--------------|-----------|
| **Binning** | Numeric → range categories | numeric → categorical ✅ this case |
| Scaling / Normalization | Numeric → numeric on a new range (StandardScaler, MinMaxScaler) | stays numeric |
| One-Hot Encoding | Categories → 0/1 columns | categorical → numeric (the *opposite* direction!) |

(In practice binning is often *followed by* one-hot encoding — but the range-creation step itself is binning. In pandas: `pd.cut(df["ExamScore"], bins=[0, 49, 69, 84, 100])` — Lab 6's AgeGroup feature and Tutorial 6's age bands are exactly this, and age bands are the most common exam dressing for it.)

**Candidate check — binnable means continuous numeric:**

| Variable | Continuous numeric? | Binnable? |
|----------|--------------------|-----------|
| Monthly Income | ✅ | ✅ → income brackets |
| Humidity | ✅ | ✅ → dry/comfortable/humid ranges |
| Height | ✅ | ✅ → height bands |
| **Payment Method** | ❌ already categorical | ❌ there are no numeric ranges to cut — nothing to bin |

**Key Rule:**

> Binning = numeric → ranges. Only continuous numeric variables qualify; anything already categorical (a payment method, a customer category) is automatically the wrong option. Why bin at all? Interpretability ("the 26–35 group churns most"), robustness to outliers, and letting simple models capture non-linear effects.

</p>
</details>

---

###### 59. A developer trains a linear regression model on HDB resale data and obtains:

```
Price = 50000 + 3000 × Floor_Area_sqm
```

What does the value **3000** represent?

- A: The number of flats in the training data
- B: The model's intercept
- C: The increase in price for every additional square metre of floor area
- D: The predicted price of a flat with zero floor area

<details><summary><b>Answer</b></summary>
<p>

#### Answer: C

**Anatomy of the fitted line `y = b₀ + b₁x`:**

| Piece | Name | Meaning here |
|-------|------|--------------|
| 50,000 | **Intercept** (b₀) | Predicted price at `Floor_Area = 0` — the starting point (options B and D describe *this* number, not 3000) |
| **3000** | **Slope / coefficient** (b₁) | **Price rises by $3,000 for each additional square metre** ✅ |

**Verify with two predictions:**

| Floor area (sqm) | Price = 50000 + 3000 × sqm |
|------------------|-----------------------------|
| 0 | 50,000 ← the intercept, in the flesh |
| 1 | 53,000 |
| 2 | 56,000 ← each extra sqm adds exactly 3,000 |

**Why the wrong options fail:** B and D are both descriptions of **50,000** (the intercept — they're the same distractor twice), and A is nonsense — the sample count is nowhere in the equation; coefficients describe the *relationship*, not the dataset size. (Salary-vs-experience, price-vs-area, anything-vs-anything — the anatomy never changes: the added constant is the intercept, the multiplier is the per-unit change.)

**Sign and size read-out (how to interpret any coefficient):**

| Coefficient | Interpretation |
|-------------|----------------|
| +3000 | Target **rises** 3,000 per unit of the feature |
| −300 | Target **falls** 300 per unit |
| ≈ 0 | Feature has little linear effect |

**In sklearn's vocabulary (as Tutorial 7 taught it):** after fitting, `model.coef_` holds the slope ("how price increases with size") and `model.intercept_` holds the base value ("the base price"). Same two numbers, code names instead of equation names — questions come in either dress. Tutorial 5's version: the whole model is `y = mx + b`, m = slope, b = intercept.

**Key Rule:**

> Intercept = prediction at zero. Coefficient = **change in target per one-unit change in the feature**. When two options describe the same other number (here: B and D both = intercept), that's a strong hint neither is the answer.

</p>
</details>

---

## Final-Check List

Night-before revision — one fact per line, grouped by topic.

**Pandas & data handling**
- `pd.read_csv()` loads a CSV; `df.info()` = dtypes + non-null counts; `df.shape` = (rows, cols) — rows FIRST
- `df.isnull().sum()` counts missing per column; handle with `dropna()` or `fillna(df[col].median())`
- `df["Salary"]` = one column; `df[["Age","Salary"]]` = two (list inside brackets); `df[Salary]` without quotes = NameError
- `.str.upper()` / `.str.lower()` = standardize inconsistent text values

**NumPy**
- `A[rows, cols]` — rows before the comma; start **included**, stop **excluded** (`A[2:5, 0:3]` = rows 2–4 × cols 0–2)
- `A[r][c]` chains row-slices twice — use the comma instead
- `A[:,2]` is 1D · `A[:,2:3]` is 2D · `A[...,2]` ≡ `A[:,2]` · bare `A[2]` is a ROW
- Features/target split: `X` = every column except the target, `y` = the target column — the target is never inside X

**Python**
- `def f(a, b=2)` — `b` is optional, `a` is required
- Early `return` needs no `else`; a method without `return` gives `None`; `self.attr` = per-object state
- `and` binds before `or`: `P and Q or R` = `(P and Q) or R`
- `continue` skips the rest of ONE iteration — the loop still runs every iteration; check which values the condition *keeps*
- `finally` always runs, exception or not
- `"w"` wipes the file, `"a"` appends — vanishing history = a `"w"` bug

**Visualization**
- `plt.xlabel` / `plt.ylabel` / `plt.title` — everything else is an invented name
- Boxplot = outliers (fences at Q1 − 1.5×IQR and Q3 + 1.5×IQR) · scatter = two-variable relationship · heatmap = correlation matrix
- Histogram and boxplot are univariate; scatter and line need two variables
- No graph + no error = missing `plt.show()`
- Matplotlib = the fundamental library; Seaborn = polished statistical charts with minimal effort
- Real axis labels with units beat `"X"` / `"Y"` every time

**Preprocessing**
- `StandardScaler` → mean 0, std 1 · `MinMaxScaler` → [0, 1] · fit on **train only**, transform both
- Ordered category → Label Encoding · unordered → One-Hot
- Hundreds of correlated numeric features → PCA · numeric → ranges = binning
- A negative age = invalid entry; a value ~100× its neighbours = outlier — investigate before deleting
- Trees and forests don't need scaling; distance/gradient models (KNN, SVM, K-Means, NN, LR) do

**Splitting & workflow**
- Import → Clean → **Split** → Train → Evaluate: Split before Train, Evaluate last
- `train_test_split()`, `test_size=0.2` = 20% test; `random_state` = reproducible split
- Test set = **final evaluation only** — never feature selection, model comparison, or tuning

**Algorithms**
- Continuous target → Linear Regression · Yes/No → Logistic Regression · no labels → K-Means
- Random Forest = many trees + majority vote; `n_estimators` (and K in K-Means) are hyperparameters **you** choose
- In `y = b₀ + b₁x`: b₀ = intercept (prediction at zero), b₁ = change in y per unit of x

**Training & regularization**
- Loss function = the error signal training minimises
- Batch = update after ALL samples · SGD = after every ONE · mini-batch = after SOME (the deep-learning default)
- Ridge = L2, Lasso = L1 — both penalize large coefficients
- `fit()` before `joblib.dump()`, or `NotFittedError`; version your model files

**Diagnosis & metrics**
- Both scores low → **underfitting** (high bias) · big train–test gap → **overfitting** (high variance) → reduce complexity
- Bull's-eye: position = bias, spread = variance
- Costly to miss a positive (cancer screening) → **Recall** = TP/(TP+FN)
- Accuracy = (TP+TN)/all — write the four cells first; wrong options are usually the precision and recall of the same matrix
- Regression → MSE/RMSE/MAE (lower = better, RMSE in target units) and R² (higher = better, and NOT "% correct")
