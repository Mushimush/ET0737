# MLAI Mid-Semester Test — Practice Questions

A collection of 30 Python / ML practice questions covering every concept tested in the actual MST. The questions are **deliberately different** from the real ones — same concepts, new angles — so you learn the *why* instead of memorising answers.

Structure: **Q1–Q20** are concept-different-angle questions, **Q21–Q25** are direct MST mirrors, and **B1–B5** are bonus questions on less-common topics.

Click any **Answer** block to reveal the explanation, the trace, and the key rule.

---

## Study Guide — Concepts Covered

Tick each one as you can confidently explain *why* the answer is what it is.

### Python Fundamentals
- [ ] **Comments** — `#` starts a comment outside strings; inside `"..."` it's just a character
- [ ] **Imports & aliases** — `import x as y` must run *before* any code uses `y`
- [ ] **Indentation** — defines code blocks (not just style); same indent = same block
- [ ] **Functions** — defined with `def`, must be *called* with `()`; missing `return` gives `None`

### Control Flow
- [ ] **Loops** — `continue` skips current iteration; `break` exits the innermost loop only
- [ ] **`if / elif / else`** — only ONE branch runs; `elif` short-circuits after first match
- [ ] **Independent `if`s** — each checks separately; multiple can run
- [ ] **Logical operators** — `and` / `or` short-circuit; `not` negates

### Collections
- [ ] **Lists** `[...]` — ordered, mutable, allow duplicates, mixed types
- [ ] **Tuples** `(...)` — ordered, **immutable**, allow duplicates
- [ ] **Sets** `{...}` — unordered, **no duplicates**, mutable
- [ ] **Dictionaries** `{key: value}` — **unique keys** (duplicates overwrite)
- [ ] **Indexing** — `data[0]` first, `data[-1]` last, `data[len(data)]` is OUT OF RANGE
- [ ] **Reference vs copy** — `b = a` shares the list; `b = a.copy()` makes a new one

### Error Handling
- [ ] **`try / except`** — `try` for risky code, `except` catches specific exceptions
- [ ] **Specific exception types** — `ValueError`, `ZeroDivisionError`, `TypeError`, `KeyError`
- [ ] **Multiple `except` blocks** — order matters; broad `Exception` last

### AI / ML
- [ ] **AI ⊃ ML ⊃ DL** — Deep Learning is a subset of Machine Learning, which is a subset of AI
- [ ] **Supervised learning** — learns from **labeled** data (inputs + correct answers)
- [ ] **Unsupervised learning** — finds patterns in **unlabeled** data (no answers given)

### Libraries
- [ ] **NumPy** — fast vectorised ops, broadcasting, efficient memory for numeric arrays
- [ ] **Pandas** — `pd.concat([df1, df2])` to stack; `df['col'] = [...]` to add a column
- [ ] **Code reuse via functions** — DRY: a bug in repeated code must be fixed everywhere

### Bonus Topics (B1–B5)
- [ ] **Type casting** — `int()` only accepts pure-integer strings; `int(float(...))` for decimals; `bool()` quirks (`bool("False")` is `True`)
- [ ] **String comparison** — lexicographic by ASCII: digits (48–57) < uppercase (65–90) < lowercase (97–122)
- [ ] **NumPy 2D indexing** — `arr[row, col]` (comma syntax) is faster than `arr[row][col]`; `arr[:, j]` extracts a column
- [ ] **Classes** — `def __init__(self, ...)` is the constructor; `s.method` is a reference, `s.method()` is a call
- [ ] **Matplotlib** — `plt.plot()` builds the figure in memory; `plt.show()` actually renders it

---

###### 1. What is the output?

```python
message = "# Welcome to Python #"
print(message)
# print("This is hidden")
print("Done")
```

- A: `# Welcome to Python #` then `Done`
- B: `# Welcome to Python #` then `This is hidden` then `Done`
- C: `Done` only (the first line is a comment)
- D: SyntaxError — `#` cannot appear inside a string

<details><summary><b>Answer</b></summary>
<p>

#### Answer: A

Let's trace each line:

| Line | What Python sees | Result |
|------|------------------|--------|
| `message = "# Welcome to Python #"` | A string assignment — the `#`s are characters | `message` is set |
| `print(message)` | Prints the variable | Outputs `# Welcome to Python #` |
| `# print("This is hidden")` | This whole line is a comment | **Skipped** |
| `print("Done")` | Normal print | Outputs `Done` |

**Key Rule:**

`#` starts a comment **only outside of strings**.

| Where `#` appears | Treated as |
|-------------------|------------|
| Outside any quotes | Start of comment (rest of line ignored) |
| Inside `"..."` or `'...'` | Just a regular character |

**Why this matters:** Hashtags, URL fragments, and markdown headers can all live happily inside strings — Python only stops at the `#` when it's outside string boundaries.

**Edge case to remember:**
```python
url = "https://example.com#section"  # the # is part of the string
# but this line is a comment
```

</p>
</details>

---

###### 2. A developer runs this script. What happens?

```python
df = pd.read_csv("students.csv")
import pandas as pd
print(df.head())
```

- A: It runs successfully — Python finds the `import` automatically
- B: `NameError: name 'pd' is not defined`
- C: `ImportError: pandas must be imported at the top of the file`
- D: It prints a warning but still works

<details><summary><b>Answer</b></summary>
<p>

#### Answer: B

Python executes code **top to bottom, one line at a time.** When line 1 runs, the `import pandas as pd` statement on line 2 has not been executed yet — so the name `pd` does not exist in the namespace.

**Trace:**

| Step | Line | State of `pd` | Outcome |
|------|------|---------------|---------|
| 1 | `df = pd.read_csv(...)` | undefined | ❌ `NameError: name 'pd' is not defined` |
| 2 | `import pandas as pd` | (never reached) | — |
| 3 | `print(df.head())` | (never reached) | — |

**Key Rule:**

> Imports must execute **before** any code that uses them.

Python does NOT "hoist" imports the way some languages hoist function declarations. The `import` is a real statement that runs in order.

**Correct version:**
```python
import pandas as pd                      # ← run FIRST
df = pd.read_csv("students.csv")
print(df.head())
```

**Why this matters:** In a notebook, you may have run the import cell earlier and forgotten — the import lives in memory across cells. But in a single `.py` file, order is everything.

**Related pitfall:** Even with the import in the right place, `pd.read_csv("students.csv")` will still fail with `FileNotFoundError` if the file isn't in the working directory.

</p>
</details>

---

###### 3. What is the output?

```python
x = 10
if x > 5:
    print("A")
    if x > 8:
        print("B")
print("C")
```

- A: `A`
- B: `A` `B` `C`
- C: `A` `C`
- D: `B` `C`

<details><summary><b>Answer</b></summary>
<p>

#### Answer: B

Indentation is what tells Python which block a statement belongs to.

**Trace by indentation level:**

| Line | Indent | Belongs to | Runs? |
|------|--------|------------|-------|
| `x = 10` | 0 spaces | top level | ✓ |
| `if x > 5:` | 0 spaces | top level | ✓ (10 > 5 is True) |
| &nbsp;&nbsp;&nbsp;&nbsp;`print("A")` | 4 spaces | inside outer `if` | ✓ prints `A` |
| &nbsp;&nbsp;&nbsp;&nbsp;`if x > 8:` | 4 spaces | inside outer `if` | ✓ (10 > 8 is True) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`print("B")` | 8 spaces | inside inner `if` | ✓ prints `B` |
| `print("C")` | 0 spaces | **top level** (not inside any `if`) | ✓ prints `C` always |

**Key Rule:**

> Indentation is **syntax**, not style. Statements at the same indentation level belong to the same block.

| Indent of `print` | When it runs |
|-------------------|--------------|
| 0 spaces (top level) | Always |
| Same indent as `if` body | Only when `if` condition is true |
| Deeper than `if` body | Only when nested `if` is also true |

**Why this matters:** Moving a single line in or out by 4 spaces changes which block it belongs to — and therefore *when* it runs. This is one of the most common bugs for Python beginners coming from `{...}`-based languages.

**Try this variation in your head:** What would output if `print("C")` were indented 4 spaces instead?

<details><summary>Click for answer</summary>

It would still output `A B C` here, because the outer `if` is True. But if `x = 3`, only that version would skip `C` (because `C` would be inside the outer `if`). With the original (no indent on `C`), `C` *always* prints regardless of `x`.

</details>

</p>
</details>

---

###### 4. What is the output?

```python
for i in range(3):
    for j in range(3):
        if j == 1:
            break
        print(i, j)
```

- A: `0 0`, `0 1`, `1 0`, `1 1`, `2 0`, `2 1`
- B: `0 0`, `1 0`, `2 0`
- C: `0 0` only
- D: `0 0`, `0 1`, `0 2`

<details><summary><b>Answer</b></summary>
<p>

#### Answer: B

`break` exits **only the innermost loop** containing it — the outer loop continues normally.

**Trace:**

| Outer `i` | Inner `j` | `j == 1`? | Action |
|-----------|-----------|-----------|--------|
| 0 | 0 | No | prints `0 0` |
| 0 | 1 | Yes | `break` → exit inner loop |
| 1 | 0 | No | prints `1 0` |
| 1 | 1 | Yes | `break` → exit inner loop |
| 2 | 0 | No | prints `2 0` |
| 2 | 1 | Yes | `break` → exit inner loop |

Output: `0 0`, `1 0`, `2 0`

**Key Rule:**

| Statement | Effect |
|-----------|--------|
| `break` | Exits the **innermost** loop only |
| `continue` | Skips to the next iteration of the **innermost** loop |
| `return` (inside function) | Exits **all** loops and the function itself |

**Why this matters:** A common bug is assuming `break` exits *all* nested loops. If you need to break out of multiple loops, you need a flag variable or refactor into a function and use `return`.

**Compare with `continue`:** If `break` were `continue`, the output would be `0 0`, `0 2`, `1 0`, `1 2`, `2 0`, `2 2` (skips only the `j == 1` iteration, then carries on with `j = 2`).

</p>
</details>

---

###### 5. What is the output?

```python
data = [10, 20, 30, 40, 50]
print(data[-1])
print(data[-3:])
print(data[:-2])
```

- A: `50` / `[30, 40, 50]` / `[10, 20, 30]`
- B: `50` / `[40, 50]` / `[10, 20]`
- C: `10` / `[10, 20, 30]` / `[30, 40, 50]`
- D: Error — negative indexes are not allowed

<details><summary><b>Answer</b></summary>
<p>

#### Answer: A

Python supports **negative indexing**, where `-1` is the last element, `-2` the second-to-last, and so on.

**Visualising the list:**

| Element | `10` | `20` | `30` | `40` | `50` |
|---------|------|------|------|------|------|
| Positive index | 0 | 1 | 2 | 3 | 4 |
| Negative index | -5 | -4 | -3 | -2 | -1 |

**Trace each line:**

| Expression | Meaning | Result |
|------------|---------|--------|
| `data[-1]` | last element | `50` |
| `data[-3:]` | from index `-3` to end (the last 3 items) | `[30, 40, 50]` |
| `data[:-2]` | from start, stop **before** index `-2` (drop last 2) | `[10, 20, 30]` |

**Key Rule:**

Slicing syntax: `data[start : stop]` — `start` is **included**, `stop` is **excluded**.

| Slice | Meaning |
|-------|---------|
| `data[-1]` | Single last item |
| `data[len(data) - 1]` | Same as `data[-1]` (the equivalent positive index) |
| `data[len(data)]` | ❌ **IndexError** — there is no element at `len(data)` |
| `data[-n:]` | Last n items |
| `data[:-n]` | Everything except the last n items |

**Why this matters:** Negative indexing makes "get the last item" a one-character expression (`data[-1]`) instead of `data[len(data) - 1]`. But beware: `data[len(data)]` is always out of range — many beginners try this and get an `IndexError`.

</p>
</details>

---

###### 6. What is the output?

```python
a = [1, 2, 3]
b = a.copy()
b.append(4)
print(a)
print(b)
```

- A: `[1, 2, 3, 4]` and `[1, 2, 3, 4]`
- B: `[1, 2, 3]` and `[1, 2, 3, 4]`
- C: `[1, 2, 3]` and `[1, 2, 3]`
- D: Error — cannot copy a list

<details><summary><b>Answer</b></summary>
<p>

#### Answer: B

`a.copy()` creates a **new independent list** that contains the same elements. Mutating `b` does NOT affect `a`.

**Compare to the MST question (`b = a`):**

| Code | Memory model | After `b.append(4)`, `a` is... |
|------|--------------|--------------------------------|
| `b = a` | Both names point to the **same** list | `[1, 2, 3, 4]` (mutated!) |
| `b = a.copy()` | `b` is a **new** list with same contents | `[1, 2, 3]` (unchanged) |
| `b = a[:]` | Same as `.copy()` — slice produces a new list | `[1, 2, 3]` (unchanged) |
| `b = list(a)` | Same — `list()` builds a new list | `[1, 2, 3]` (unchanged) |

**Mental model:**

```
b = a              b = a.copy()
                   
a ──┐              a ──→ [1,2,3]
    ├─→ [1,2,3]    
b ──┘              b ──→ [1,2,3]   (separate list)
```

**Key Rule:**

> Assignment (`=`) in Python does NOT copy objects — it binds a name to the **same** object. To get an independent copy, use `.copy()`, `[:]`, or `list(...)`.

**Why this matters:** A huge category of bugs comes from "I changed `b` but `a` mutated too?!" The fix is almost always to make a copy.

**Edge case — shallow vs deep copy:**
```python
a = [[1, 2], [3, 4]]
b = a.copy()
b[0].append(99)
print(a)  # [[1, 2, 99], [3, 4]] — the INNER list is still shared!
```
For nested structures, use `copy.deepcopy(a)`.

</p>
</details>

---

###### 7. What is the output?

```python
fruits = {"apple", "banana", "apple", "cherry", "banana", "apple"}
print(len(fruits))
```

- A: `6`
- B: `3`
- C: `2`
- D: Error — sets do not allow duplicates

<details><summary><b>Answer</b></summary>
<p>

#### Answer: B

A set **silently discards duplicates** when it is created. No error — Python just keeps each unique element once.

**What's stored:**

| Attempted | After deduplication |
|-----------|---------------------|
| `apple`, `banana`, `apple`, `cherry`, `banana`, `apple` | `apple`, `banana`, `cherry` |

So `len(fruits)` is `3`.

**Key Rule — Sets in Python:**

| Property | Set |
|----------|-----|
| Duplicates? | ❌ Automatically removed |
| Ordered? | ❌ No guaranteed order |
| Mutable? | ✅ Yes (can `.add()` and `.remove()`) |
| Indexable? | ❌ `s[0]` raises `TypeError` |
| Syntax | `{1, 2, 3}` or `set([1, 2, 3])` |

**Why this matters:** Sets are the right tool when you want to **deduplicate** a collection or check membership fast (`x in s` is O(1) on a set vs O(n) on a list).

**Useful idiom:**
```python
unique_values = list(set([1, 1, 2, 3, 3]))   # → [1, 2, 3]
```

**Gotcha:** `{}` is an **empty dict**, not an empty set. For an empty set you must write `set()`.

</p>
</details>

---

###### 8. What happens when this code runs?

```python
point = (10, 20, 30)
point[1] = 50
print(point)
```

- A: Prints `(10, 50, 30)`
- B: Prints `(10, 20, 30)` (the assignment is ignored)
- C: `TypeError: 'tuple' object does not support item assignment`
- D: Prints `(50, 20, 30)`

<details><summary><b>Answer</b></summary>
<p>

#### Answer: C

Tuples are **immutable** — once created, you cannot change their contents. Trying to assign to an index raises a `TypeError` at runtime.

**What you CAN do vs CANNOT do with a tuple:**

| Operation | Allowed? | Example |
|-----------|----------|---------|
| Read by index | ✅ | `point[1]` → `20` |
| Iterate | ✅ | `for x in point: ...` |
| Slice | ✅ | `point[1:]` → `(20, 30)` |
| Concatenate (creates NEW tuple) | ✅ | `point + (40,)` → `(10, 20, 30, 40)` |
| Assign to index | ❌ | `point[1] = 50` → `TypeError` |
| `.append()` | ❌ | Tuples have no `.append()` method |
| Reassign the whole variable | ✅ | `point = (1, 2, 3)` (this creates a new tuple) |

**Key Rule:**

| Collection | Immutable? |
|------------|-----------|
| `tuple` | ✅ Yes |
| `list` | ❌ No |
| `set` | ❌ No |
| `dict` | ❌ No (but keys must be immutable types) |
| `str` | ✅ Yes |

**Why this matters:** Immutability makes tuples safe to use as **dictionary keys** and **set elements**. A list can't be a dict key (`d = {[1, 2]: "x"}` errors) but a tuple can (`d = {(1, 2): "x"}` works).

**Single-element tuple gotcha:**
```python
not_a_tuple = (5)      # this is just the int 5 in parentheses
yes_a_tuple = (5,)     # the trailing comma makes it a tuple
```

</p>
</details>

---

###### 9. Which of the following create a **dictionary**? (Select ALL that apply)

```python
a = {}
b = {1, 2, 3}
c = {"name": "Alice"}
d = {1: "one", 2: "two"}
e = dict(name="Bob")
```

- A: `a` (empty curly braces)
- B: `b` (`{1, 2, 3}`)
- C: `c` (`{"name": "Alice"}`)
- D: `d` (`{1: "one", 2: "two"}`)
- E: `e` (`dict(name="Bob")`)

<details><summary><b>Answer</b></summary>
<p>

#### Answer: A, C, D, E

The curly-brace syntax `{...}` is **ambiguous** — Python decides whether you mean a dict or a set based on **whether you used `key: value` pairs**.

**Analysis:**

| Variable | Code | Type | Why |
|----------|------|------|-----|
| `a` | `{}` | **`dict`** ✓ | Empty `{}` is always a dict (historical reason — dicts were in Python before sets) |
| `b` | `{1, 2, 3}` | `set` ✗ | No `key: value` pairs — just values |
| `c` | `{"name": "Alice"}` | **`dict`** ✓ | Has `key: value` |
| `d` | `{1: "one", 2: "two"}` | **`dict`** ✓ | Has `key: value` |
| `e` | `dict(name="Bob")` | **`dict`** ✓ | Built using the `dict()` constructor |

**Key Rule:**

| Literal | Type |
|---------|------|
| `{}` | `dict` (empty) |
| `set()` | `set` (empty — `{}` won't work for empty sets!) |
| `{x, y, z}` | `set` |
| `{k: v, k2: v2}` | `dict` |
| `[x, y, z]` | `list` |
| `(x, y, z)` | `tuple` |

**Why this matters:** When you see `{...}` in code, look for **colons**. Colons → dict. No colons → set.

**Confusion check:**
```python
type({})        # → <class 'dict'>     ← empty curly braces
type(set())     # → <class 'set'>      ← empty set requires set()
type({1})       # → <class 'set'>      ← set with one element
type({1: 2})    # → <class 'dict'>     ← dict with one key:value pair
```

</p>
</details>

---

###### 10. What is the output?

```python
score = 85
if score >= 60:
    print("Pass")
elif score >= 80:
    print("Distinction")
elif score >= 90:
    print("High Distinction")
else:
    print("Fail")
```

- A: `Pass`
- B: `Distinction`
- C: `Pass` and `Distinction`
- D: `High Distinction`

<details><summary><b>Answer</b></summary>
<p>

#### Answer: A

In an `if / elif / elif / else` chain, **only the first matching branch runs.** After the first match, all remaining `elif` and `else` blocks are skipped.

**Trace:**

| Check | Result | Action |
|-------|--------|--------|
| `score >= 60` (85 ≥ 60) | ✅ True | Run `print("Pass")`, then **skip the rest** |
| `score >= 80` | (never checked) | — |
| `score >= 90` | (never checked) | — |
| `else` | (never reached) | — |

**This is a logic bug, even though no error is raised.** The author probably wanted Distinction to print for scores 80–89 — but because `score >= 60` is checked first and is *also* true for 85, the Distinction branch never gets a chance.

**The fix:** Order the conditions from **most specific (highest threshold) to least specific.**

```python
if score >= 90:
    print("High Distinction")
elif score >= 80:
    print("Distinction")
elif score >= 60:
    print("Pass")
else:
    print("Fail")
```

**Key Rule:**

> `elif` chains short-circuit at the **first true** condition. Order matters — put the **strictest** condition first.

**Why this matters:** This was a real MST question pattern. The conditions look "correct" individually, but the *order* makes the logic wrong. Always trace your `if/elif` chains top-to-bottom.

</p>
</details>

---

###### 11. What is the output?

```python
x = 5
if x > 0:
    print("positive")
if x > 3:
    print("big")
if x > 10:
    print("huge")
```

- A: `positive`
- B: `positive` and `big`
- C: `positive`, `big`, and `huge`
- D: `big`

<details><summary><b>Answer</b></summary>
<p>

#### Answer: B

These are **three independent `if` statements**, not an `if / elif` chain. Each one is checked separately, so **multiple can run**.

**Trace:**

| Statement | Check | Result |
|-----------|-------|--------|
| `if x > 0` | 5 > 0 ✅ | prints `positive` |
| `if x > 3` | 5 > 3 ✅ | prints `big` |
| `if x > 10` | 5 > 10 ❌ | skipped |

**Independent `if`s vs `if/elif`:**

| Pattern | Behaviour |
|---------|-----------|
| 3 separate `if`s | Each runs independently — 0, 1, 2, or 3 prints possible |
| `if / elif / elif` | Only ONE branch runs total — short-circuits at first match |

**Same `x = 5`, same conditions, written as `if/elif`:**
```python
if x > 0:
    print("positive")
elif x > 3:
    print("big")        # never runs — first branch already matched
elif x > 10:
    print("huge")
```
Output: just `positive`.

**Key Rule:**

> Look for `elif` to know whether the branches are exclusive. No `elif` = independent checks.

**Why this matters:** Beginners sometimes write three `if`s when they meant one `if/elif/elif`, causing duplicate prints. Or vice versa — they want all matching to print but use `elif` and only get one.

</p>
</details>

---

###### 12. How many times does `checking` print?

```python
def check(value):
    print(f"checking {value}")
    return value > 0

if check(5) or check(-3):
    print("yes")
```

- A: Once
- B: Twice
- C: Zero times
- D: Three times

<details><summary><b>Answer</b></summary>
<p>

#### Answer: A

Python's `or` operator **short-circuits**: if the left side is already `True`, the right side is never evaluated.

**Trace:**

| Step | What runs | Output |
|------|-----------|--------|
| 1 | `check(5)` is called | prints `checking 5`, returns `True` |
| 2 | `or` sees `True` on the left → **skips the right side entirely** | — |
| 3 | `check(-3)` is **never called** | — |
| 4 | `if True:` runs the body | prints `yes` |

Total output:
```
checking 5
yes
```

**Key Rule — Short-circuit evaluation:**

| Operator | Left value | Right side evaluated? |
|----------|------------|------------------------|
| `or` | `True` | ❌ No (already true) |
| `or` | `False` | ✅ Yes (need to check) |
| `and` | `True` | ✅ Yes (need to check) |
| `and` | `False` | ❌ No (already false) |

**Why this matters:** Short-circuit is not just a performance trick — it's used **defensively**:
```python
if x is not None and x.value > 0:   # safe: x.value only accessed if x is not None
    ...
```
If the order were reversed (`x.value > 0 and x is not None`), Python would crash with `AttributeError` on `None.value` before it ever got to the `None` check.

**Try predicting:** If the operator were `and` instead of `or`, how many times would `checking` print?

<details><summary>Click for answer</summary>

Twice. `check(5)` returns `True`, so `and` *does* evaluate the right side `check(-3)` (which returns `False`). The `if` then fails and `yes` is not printed.

</details>

</p>
</details>

---

###### 13. What is the output?

```python
def calculate():
    return 5 + 3

result = calculate
print(result)
```

- A: `8`
- B: `<function calculate at 0x...>` (something like this)
- C: `Error — function not called`
- D: `5 + 3`

<details><summary><b>Answer</b></summary>
<p>

#### Answer: B

`calculate` (without `()`) is a **reference to the function itself**, not the value it returns. Assigning `result = calculate` makes `result` another name for the same function — it does NOT run the function.

**To actually run the function**, you must add the parentheses:

| Code | What it does | `result` is... |
|------|--------------|----------------|
| `result = calculate` | Bind `result` to the function object | the function itself |
| `result = calculate()` | **Call** the function, store the return value | `8` |

**Printing each:**
```python
print(calculate)    # <function calculate at 0x10a1b2c30>
print(calculate())  # 8
```

**Key Rule:**

> A function name without `()` is a **reference** (you can pass it around, assign it, store it in a list). A function name with `()` is a **call** (it executes and gives you the return value).

**Why this matters:** This is the bug from the actual MST question (`greet` vs `greet()`). It's also the foundation for:

```python
# Pass a function as an argument (callback)
sorted_list = sorted([3, 1, 2], key=abs)   # `abs`, not `abs()`

# Store functions in a list
operations = [sum, max, min]
for op in operations:
    print(op([1, 2, 3]))
```

**A function that doesn't return anything returns `None`:**
```python
def greet(name):
    print(f"Hello, {name}")   # prints but doesn't return

x = greet("Alice")
print(x)   # → None
```

</p>
</details>

---

###### 14. Which exception type is raised by `int("abc")`?

```python
try:
    num = int("abc")
    print(num)
except ____:
    print("Cannot convert")
```

- A: `TypeError`
- B: `ValueError`
- C: `SyntaxError`
- D: `ConvertError`

<details><summary><b>Answer</b></summary>
<p>

#### Answer: B

`int("abc")` raises a **`ValueError`** — the argument is the right *type* (a string, which `int()` accepts), but its *value* doesn't represent a valid integer.

**`TypeError` vs `ValueError`:**

| Situation | Exception |
|-----------|-----------|
| `int("abc")` — string, but not a number | `ValueError` |
| `int("12")` — string of digits | ✅ Works (`12`) |
| `int([1, 2])` — wrong TYPE entirely (list) | `TypeError` |
| `int(None)` — wrong type | `TypeError` |
| `"hello" + 5` — string + int, types incompatible | `TypeError` |

**Mental model:**

| Exception | "The problem is..." |
|-----------|---------------------|
| `TypeError` | The **kind of thing** is wrong (wrong category) |
| `ValueError` | The **specific value** is wrong (right kind, bad content) |

**Common exception types you should recognise:**

| Exception | Triggered by |
|-----------|--------------|
| `ValueError` | `int("abc")`, `float("hello")` |
| `TypeError` | `"a" + 1`, `len(5)`, calling a non-function |
| `ZeroDivisionError` | `1 / 0`, `5 % 0` |
| `IndexError` | `[1, 2, 3][10]` |
| `KeyError` | `{"a": 1}["b"]` |
| `FileNotFoundError` | `open("missing.csv")` |
| `AttributeError` | `"hello".does_not_exist()` |
| `NameError` | Using a variable before it's defined |

**Why this matters:** Catching `Exception` is a lazy habit — it hides bugs. Catching the *specific* exception means your error message is meaningful, and unexpected bugs still surface.

</p>
</details>

---

###### 15. What is wrong with this code? (Select ALL that apply)

```python
try:
    result = 10 / int(input("Enter: "))
    print(result)
except Exception:
    print("Generic error")
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Invalid number")
```

- A: `Exception` is too broad and matches everything — `ZeroDivisionError` and `ValueError` will never run
- B: The order should be reversed — specific exceptions first, then `Exception` last
- C: It will work correctly as written
- D: Python will automatically reorder the `except` blocks so the most specific one runs first

<details><summary><b>Answer</b></summary>
<p>

#### Answer: A, B

`except` blocks are checked **top to bottom**, and Python uses the **first one that matches.** Since `Exception` is the parent class of nearly every error, putting it first means it swallows everything before the more specific blocks get a chance.

**What actually happens with this code:**

| User enters | Exception raised | Caught by | Output |
|-------------|------------------|-----------|--------|
| `0` | `ZeroDivisionError` | First `except Exception` | `Generic error` |
| `abc` | `ValueError` | First `except Exception` | `Generic error` |
| `5` | (no exception) | — | `2.0` |

The `ZeroDivisionError` and `ValueError` blocks are **dead code** — they never run.

**The fix — specific first, general last:**

```python
try:
    result = 10 / int(input("Enter: "))
    print(result)
except ZeroDivisionError:           # specific
    print("Cannot divide by zero")
except ValueError:                  # specific
    print("Invalid number")
except Exception:                   # catch-all, last
    print("Generic error")
```

**Key Rule:**

> `except` blocks are matched in order, like a `switch / case`. List the **most specific** exception classes first, the **most general** (`Exception`) last.

**Class hierarchy intuition:**
```
Exception
├── ArithmeticError
│   ├── ZeroDivisionError
│   └── ...
├── ValueError
├── TypeError
├── LookupError
│   ├── IndexError
│   └── KeyError
└── ...
```
Any specific exception is *also* an `Exception` — so a broad `except Exception` will catch it.

**Why this matters:** Linters (`pyflakes`, `pylint`, `ruff`) flag this pattern as unreachable code — CPython itself does **not** warn. Option D is the trap: Python executes `except` blocks in the order you write them and never reorders them. If you want specific handling, you have to write the blocks in the right order yourself.

</p>
</details>

---

###### 16. Which statement correctly describes the relationship between AI, ML, and DL?

- A: AI is a subset of ML, which is a subset of DL
- B: DL is a subset of ML, which is a subset of AI
- C: AI, ML, and DL are three independent fields with no overlap
- D: ML and DL are both subsets of AI, but DL is not a subset of ML

<details><summary><b>Answer</b></summary>
<p>

#### Answer: B

The standard hierarchy is **DL ⊂ ML ⊂ AI** — Deep Learning is a specialised subset of Machine Learning, which is itself a subset of the broader field of Artificial Intelligence.

**Visual model (nested circles):**

```
┌─────────────────────────────────────────┐
│  AI  — any system that exhibits         │
│       intelligent behaviour             │
│   (rule-based expert systems, search,   │
│    chess engines, ML, ...)              │
│                                         │
│   ┌─────────────────────────────────┐   │
│   │  ML  — systems that LEARN from  │   │
│   │       data instead of being     │   │
│   │       hand-coded                │   │
│   │   (decision trees, SVM, k-NN,   │   │
│   │    linear regression, DL, ...)  │   │
│   │                                 │   │
│   │   ┌─────────────────────────┐   │   │
│   │   │  DL  — ML using deep    │   │   │
│   │   │       neural networks   │   │   │
│   │   │   (CNNs, RNNs, Trans-   │   │   │
│   │   │    formers, LLMs, ...)  │   │   │
│   │   └─────────────────────────┘   │   │
│   └─────────────────────────────────┘   │
└─────────────────────────────────────────┘
```

**Quick distinctions:**

| Term | What it is | Example |
|------|------------|---------|
| **AI** | Any system that mimics intelligent behaviour | A chess engine, a chatbot, a spam filter |
| **ML** | Subset of AI — learns patterns from data | Predicting house prices from past sales |
| **DL** | Subset of ML — uses multi-layer neural networks | Image classification, ChatGPT, AlphaGo |

**Why this matters:** Not all AI is ML (rule-based expert systems are AI but not ML). Not all ML is DL (a decision tree is ML but not DL). Knowing the hierarchy helps you describe a solution accurately — "we used ML to predict churn" is more honest than "we used AI" if no neural networks are involved.

</p>
</details>

---

###### 17. A retailer has 5 years of customer purchase history but **no labels** on which customers are "valuable" or "low-value". They want to discover natural groups of customers with similar buying patterns. Which approach should they use?

- A: Supervised learning — they have plenty of historical data
- B: Unsupervised learning — clustering customers by patterns, no labels needed
- C: Reinforcement learning — customers learn from rewards
- D: This problem cannot be solved with machine learning

<details><summary><b>Answer</b></summary>
<p>

#### Answer: B

**Unsupervised learning** is the right approach here. The key signal in the problem is "**no labels**" — there is no pre-assigned "correct answer" for each customer.

**Decision tree for picking the learning type:**

| Question | If YES → | If NO → |
|----------|----------|---------|
| Do you have labeled examples (input + correct output)? | **Supervised** | Continue ↓ |
| Are you looking for structure or groups in the data? | **Unsupervised** | Continue ↓ |
| Is an agent learning by trial and error with rewards? | **Reinforcement** | — |

**Three learning paradigms — quick reference:**

| Type | Has labels? | Goal | Example |
|------|-------------|------|---------|
| **Supervised** | ✅ Yes | Predict the label for new inputs | Spam detection, house price prediction |
| **Unsupervised** | ❌ No | Find structure / groups / patterns | Customer segmentation, anomaly detection |
| **Reinforcement** | ❌ No (uses rewards) | Learn a policy by trial and error | Game-playing AI, robotics |

**Why option A is wrong:** Having data ≠ having labeled data. Supervised learning requires `(input, correct_answer)` pairs — the customer history alone is just input.

**Why this matters:** Mislabelling a problem as "supervised" when it's really "unsupervised" wastes time — you'd waste hours trying to train a classifier you have no labels for. The first question in any ML project is: *do I have labels?*

</p>
</details>

---

###### 18. Which of the following is **NOT** a valid reason to choose NumPy over a regular Python list for numerical computation?

- A: Faster vectorised operations on numerical data
- B: NumPy arrays can store mixed data types (e.g. `int + str + bool`) more efficiently
- C: Supports broadcasting for elementwise operations on arrays of different shapes
- D: More memory-efficient for large numerical arrays

<details><summary><b>Answer</b></summary>
<p>

#### Answer: B

This statement is **false** — and that makes it the correct answer to the "NOT a benefit" question.

**Reality check:**

| Container | Stores mixed types? |
|-----------|---------------------|
| Python `list` | ✅ Yes — `[1, "hi", True, 3.14]` is fine |
| NumPy `ndarray` | ❌ **No** — must be **homogeneous** (all same dtype) |

If you try to create a NumPy array with mixed types, NumPy will **silently coerce** everything to a common type (usually `object` or `str`), which is **slower** than a Python list, not faster.

**The other three are real NumPy advantages:**

| Reason | Why it's true |
|--------|---------------|
| **A — vectorised ops** | `arr * 2` runs in C-level loops, no Python overhead per element |
| **C — broadcasting** | `arr_2d + arr_1d` automatically aligns shapes without explicit loops |
| **D — memory efficiency** | A `np.array([1, 2, 3])` of int32 uses 12 bytes of contiguous data. The equivalent Python list costs ~88 bytes of list overhead **plus** ~28 bytes per int object (≈172 bytes total) |

**Key Rule:**

> NumPy gets its speed and efficiency by enforcing **homogeneous, fixed-type arrays**. That's a feature, not a bug — but it means you trade flexibility for performance.

**When to use what:**

| Use case | Choose |
|----------|--------|
| Heterogeneous data (records with name, age, gender) | Python list, or Pandas DataFrame |
| Large numerical arrays, math operations | NumPy array |
| Tabular data with labelled columns | Pandas DataFrame (built on NumPy) |

</p>
</details>

---

###### 19. What is printed?

```python
config = {
    "timeout": 30,
    "retries": 3,
    "timeout": 60
}
print(len(config))
print(config["timeout"])
```

- A: `3` and `30`
- B: `3` and `60`
- C: `2` and `30`
- D: `2` and `60`

<details><summary><b>Answer</b></summary>
<p>

#### Answer: D

Dictionary keys are **unique**. When the same key appears twice in a literal, the **later assignment overwrites the earlier one** — silently, no error.

**Trace:**

| Step | Action | Dict state |
|------|--------|------------|
| 1 | `"timeout": 30` | `{"timeout": 30}` |
| 2 | `"retries": 3` | `{"timeout": 30, "retries": 3}` |
| 3 | `"timeout": 60` ← **overwrites** | `{"timeout": 60, "retries": 3}` |

Final dict has **2 unique keys**, and `"timeout"` holds the **later** value: `60`.

**Key Rule:**

| Operation | Behaviour |
|-----------|-----------|
| Duplicate key in literal | Later value silently overwrites earlier |
| `d[key] = value` on existing key | Overwrites |
| `d[key] = value` on new key | Adds |
| `len(d)` | Number of **unique** keys |

**Why this matters:** No warning is raised. If you build a dict from a loop and accidentally use a non-unique key, you'll **lose data silently** — your final dict will be shorter than you expected with values from the *last* duplicate.

**Defensive pattern — detect duplicates as you build:**
```python
result = {}
for key, value in pairs:
    if key in result:
        print(f"Warning: duplicate key {key}")
    result[key] = value
```

**Common gotcha — dict from a list of tuples:**
```python
dict([("a", 1), ("b", 2), ("a", 3)])   # → {"a": 3, "b": 2}   ← "a": 1 is lost
```

</p>
</details>

---

###### 20. What happens when this code runs?

```python
import pandas as pd

df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [15, 18, 30]
})

df['City'] = ['NY', 'LA']
```

- A: The third row gets `NaN` for `City`
- B: `ValueError: Length of values (2) does not match length of index (3)`
- C: Pandas silently truncates the DataFrame to 2 rows to match the list length
- D: Pandas auto-pads the missing value with the last given value (`LA`)

<details><summary><b>Answer</b></summary>
<p>

#### Answer: B

When you assign a **list** as a new column, Pandas requires the list length to **exactly match the number of rows**. If the lengths don't match, Pandas raises a `ValueError` — it does NOT silently pad, truncate, or fill with `NaN`.

**The DataFrame has 3 rows, the list has 2 values → mismatch → error.**

**Ways to add a column correctly:**

| Approach | Code | Result |
|----------|------|--------|
| List of the right length | `df['City'] = ['NY', 'LA', 'SF']` | ✅ Works |
| A single scalar (broadcasts) | `df['City'] = 'Unknown'` | ✅ All 3 rows get `'Unknown'` |
| A `Series` aligned by index | `df['City'] = pd.Series(['NY', 'LA'])` | Last row gets `NaN` (Series alignment, NOT list assignment) |
| Computed from existing columns | `df['IsAdult'] = df['Age'] >= 18` | ✅ Works elementwise |

**Why option A is wrong:** Pandas only silently inserts `NaN` when you align by **index** (using a `Series` with a partial index). With a plain Python list, the lengths must match exactly.

**Key Rule:**

> `df['col'] = a_list` → length must match `len(df)` **exactly.**
> `df['col'] = a_scalar` → broadcast to every row.
> `df['col'] = a_series` → align by index, fill gaps with `NaN`.

**Why this matters:** This was a real MST question pattern. The wrong-answer options in the actual test (`df.add(...)`, `df.insert_column(...)`, `df.append(...)`) are all made-up method names. The **only** correct way to add a column from a list is `df['ColName'] = [...]` — and the length must match.

</p>
</details>

---

###### 21. What is the output?

```python
total = 0
for i in range(1, 6):
    if i % 2 == 0:
        continue
    total += i
print(total)
```

- A: `15`
- B: `9`
- C: `6`
- D: `0`

<details><summary><b>Answer</b></summary>
<p>

#### Answer: B

`continue` skips the rest of the current iteration and jumps to the next one. Here, every even `i` triggers `continue` *before* `total += i` runs — so only odd numbers are added.

**Trace:**

| `i` | `i % 2 == 0`? | Action | `total` after |
|-----|---------------|--------|---------------|
| 1 | No (1 ≠ 0) | `total += 1` | `1` |
| 2 | Yes | `continue` → skip rest | `1` |
| 3 | No | `total += 3` | `4` |
| 4 | Yes | `continue` → skip rest | `4` |
| 5 | No | `total += 5` | `9` |

Final: `total = 9`.

**Key Rule — `continue` vs `break`:**

| Statement | Effect |
|-----------|--------|
| `continue` | Skip the rest of the current iteration; **loop continues** |
| `break` | Exit the loop entirely |
| `pass` | Do nothing (placeholder, loop continues normally) |

**Visual difference:**
```python
for i in range(5):
    if i == 2:
        continue        # skips just i=2 → prints 0,1,3,4
    print(i)

for i in range(5):
    if i == 2:
        break           # exits at i=2 → prints 0,1
    print(i)
```

**Why this matters:** A common bug is using `break` when you meant `continue` (or vice versa). `break` exits and never comes back; `continue` skips one iteration and resumes.

</p>
</details>

---

###### 22. Which expression produces a single DataFrame with all 4 students stacked as rows?

```python
import pandas as pd

df1 = pd.DataFrame({'Name': ['Alice', 'Bob'], 'Age': [20, 25]})
df2 = pd.DataFrame({'Name': ['Charlie', 'Diana'], 'Age': [30, 35]})
```

- A: `pd.concat([df1, df2])`
- B: `pd.merge(df1, df2)`
- C: `df1 + df2`
- D: `pd.append(df1, df2)`

<details><summary><b>Answer</b></summary>
<p>

#### Answer: A

`pd.concat([df1, df2])` stacks DataFrames along an axis — by default, vertically (axis=0). This is the standard way to "append rows" in modern Pandas.

**Why each other option is wrong:**

| Option | What it actually does |
|--------|-----------------------|
| **B** `pd.merge(df1, df2)` | Joins on common columns (like SQL JOIN). Returns rows where keys match — NOT a stack |
| **C** `df1 + df2` | Element-wise operation. For string columns, concatenates values pairwise (`'Alice' + 'Charlie'`); for numeric, adds. NOT a stack |
| **D** `pd.append(df1, df2)` | `pd.append` doesn't exist at the module level. (`DataFrame.append()` was a method, but it was **removed in Pandas 2.0**) |

**concat vs merge — when to use each:**

| Goal | Tool | Example |
|------|------|---------|
| Stack rows (same columns) | `pd.concat([df1, df2])` | Combine monthly sales files |
| Stack columns (same rows) | `pd.concat([df1, df2], axis=1)` | Add features side-by-side |
| Join on a key (different columns) | `pd.merge(df1, df2, on='id')` | Combine customer + order tables |

**Key Rule:**

> Use `concat` when DataFrames have the **same shape** of one axis (you're extending the other). Use `merge` when you have a **shared key** and want to align rows on that key.

**Why this matters:** Merging when you meant to stack can silently lose rows (inner join drops non-matching ones). Stacking when you meant to merge creates duplicated rows. The right tool depends on what your data represents.

</p>
</details>

---

###### 23. Which of the following is a **tuple** that contains **duplicate** values?

- A: `[1, 1, 2]`
- B: `{1, 1, 2}`
- C: `(1, 1, 2)`
- D: `"1, 1, 2"`

<details><summary><b>Answer</b></summary>
<p>

#### Answer: C

The brackets / braces determine the type. Only `(...)` creates a tuple.

**Analysis:**

| Option | Syntax | Type | Contains duplicates? |
|--------|--------|------|----------------------|
| A | `[1, 1, 2]` | `list` | ✅ Yes (`[1, 1, 2]`, length 3) |
| B | `{1, 1, 2}` | `set` | ❌ No — set deduplicates to `{1, 2}`, length 2 |
| **C** | `(1, 1, 2)` | **`tuple`** | ✅ Yes (`(1, 1, 2)`, length 3) |
| D | `"1, 1, 2"` | `str` | (it's a string of characters, not a collection of numbers) |

**Key Rule — Bracket Cheat Sheet:**

| Brackets | Type | Mutable? | Duplicates? |
|----------|------|----------|-------------|
| `[...]` | list | ✅ Yes | ✅ Yes |
| `(...)` | tuple | ❌ No | ✅ Yes |
| `{...}` (with `key: value`) | dict | ✅ Yes | ❌ Keys must be unique |
| `{...}` (just values) | set | ✅ Yes | ❌ Auto-deduplicated |
| `"..."` | str | ❌ No | ✅ (characters) |

**Why this matters:** Tuples and lists are often confused because both preserve order and allow duplicates. The key differences:

| Property | List `[1, 2, 3]` | Tuple `(1, 2, 3)` |
|----------|------------------|-------------------|
| Mutable | ✅ | ❌ |
| Use as dict key | ❌ | ✅ |
| Methods like `.append()` | ✅ | ❌ |

**Single-element tuple gotcha:**
```python
not_a_tuple = (5)      # → int 5 (parentheses are just grouping)
yes_a_tuple = (5,)     # → tuple (5,) — the trailing comma matters
```

</p>
</details>

---

###### 24. A developer copies the same 15-line validation routine into 8 different places in their codebase instead of using a function. A bug is later found in the validation logic. Which are disadvantages of this approach? (Select ALL that apply)

- A: The bug must be fixed in all 8 locations
- B: It is easy to miss a copy, leading to inconsistent behaviour across the program
- C: It makes the code harder to read and longer than necessary
- D: Python automatically synchronises duplicate code, so the bug spreads to all copies safely

<details><summary><b>Answer</b></summary>
<p>

#### Answer: A, B, C

This is the **DRY principle** (Don't Repeat Yourself). Duplicate code is one of the most common sources of bugs and maintenance pain.

**Why each option:**

| Option | Status | Reason |
|--------|--------|--------|
| **A** ✅ | Correct | A bug fix at one location is useless if the same bug lives in 7 others — every copy must be updated |
| **B** ✅ | Correct | Humans miss things. One forgotten copy = a place where the old buggy behaviour still runs |
| **C** ✅ | Correct | 15 × 8 = 120 lines of repeated logic vs 15 lines of function + 8 one-line calls = much harder to read |
| **D** ❌ | Wrong | Python does NOT "sync" copies. Each copy is independent. There's no magic — duplicated code stays duplicated until a human fixes it |

**Key Rule — Why use functions:**

| Without function (8 copies) | With function (1 copy) |
|-----------------------------|------------------------|
| Bug fix: edit 8 places, hope you find them all | Bug fix: edit 1 place |
| Improvement: rewrite 8 times | Improvement: rewrite once |
| Reading: scroll past 120 lines of repetition | Reading: 1 named function call shows intent |
| Testing: have to test all 8 sites | Testing: test the function once |

**The DRY principle in one sentence:**

> Every piece of knowledge should have a **single, authoritative representation** in your code.

**Refactor example:**
```python
# DRY violation — same 3 lines repeated
if user_age is None or user_age < 0 or user_age > 150:
    print("Invalid age")
    return
# ... later in another file ...
if user_age is None or user_age < 0 or user_age > 150:
    print("Invalid age")
    return

# Refactored
def is_valid_age(age):
    return age is not None and 0 <= age <= 150

if not is_valid_age(user_age):
    print("Invalid age")
    return
```

**Why this matters:** Most legacy-code bugs trace back to inconsistency between copies of "the same" logic. Every time you copy-paste code, you're creating a future maintenance problem.

</p>
</details>

---

###### 25. A developer wants to safely handle the situation where `int(user_input)` might fail. Which keyword marks the block of code where the risky operation goes?

- A: `catch`
- B: `try`
- C: `except`
- D: `handle`

<details><summary><b>Answer</b></summary>
<p>

#### Answer: B

In Python, the `try` keyword starts the protected block. The `except` keyword catches errors raised inside that block.

**The full pattern:**

```python
try:
    num = int(user_input)   # ← risky code goes inside `try`
    print(num)
except ValueError:
    print("Not a number")   # ← error handler goes inside `except`
```

**Where each keyword goes:**

| Keyword | Purpose |
|---------|---------|
| `try` | Marks a block of code that might raise an exception |
| `except` | Catches exceptions of a specified type |
| `else` (optional) | Runs only if NO exception occurred in `try` |
| `finally` (optional) | Runs **always**, even if an exception was raised or caught |

**Why each other option is wrong:**

| Option | Why it's wrong |
|--------|----------------|
| **A** `catch` | Not a Python keyword. (Java and JavaScript use `catch` — common confusion) |
| **C** `except` | Real Python keyword, but it catches errors — it does NOT mark the protected block |
| **D** `handle` | Not a Python keyword in any sense |

**Full structure example:**

```python
try:
    file = open("data.csv")           # might raise FileNotFoundError
    data = file.read()
    number = int(data)                # might raise ValueError
except FileNotFoundError:
    print("File missing")
except ValueError:
    print("File contains non-numeric data")
else:
    print(f"Got {number}")            # runs only if no exception
finally:
    print("Cleanup")                  # always runs
```

**Key Rule:**

> Python uses `try` / `except` (not `try` / `catch` like Java). Confusing the two is one of the most common syntax errors for students with prior Java experience.

**Why this matters:** Without exception handling, any error inside your code crashes the entire program. `try`/`except` lets you fail gracefully — log the error, ask the user again, fall back to a default, etc.

</p>
</details>

---

## Bonus Section — Additional MST Topics

These cover concepts that appear in the MST's *metadata list* but didn't show up as worked examples — type casting, string comparison, NumPy 2D arrays, Python classes, and Matplotlib. Worth knowing just in case.

---

###### B1. What is the output?

```python
value = "3.14"
result = int(value)
print(result)
```

- A: `3` (the integer part)
- B: `3.14`
- C: `ValueError: invalid literal for int() with base 10: '3.14'`
- D: `3` — silently truncates the decimal part

<details><summary><b>Answer</b></summary>
<p>

#### Answer: C

`int()` will only parse a string that looks like a **pure integer**. The string `"3.14"` contains a decimal point, so `int()` refuses to parse it and raises a `ValueError`.

**Type casting rules:**

| Conversion | Works? | Result |
|------------|--------|--------|
| `int("5")` | ✅ | `5` |
| `int("5.0")` | ❌ | `ValueError` |
| `int(5.9)` | ✅ | `5` (truncates, doesn't round!) |
| `int(float("3.14"))` | ✅ | `3` (two-step conversion) |
| `float("3.14")` | ✅ | `3.14` |
| `float("abc")` | ❌ | `ValueError` |
| `str(42)` | ✅ | `"42"` |
| `bool(0)` / `bool("")` / `bool([])` | ✅ | `False` (falsy values) |
| `bool(1)` / `bool("False")` | ✅ | `True` (any non-empty value) |

**Key Rule:**

> `int(string)` only accepts strings of pure digits (optionally with a `+` / `-` sign). To convert `"3.14"` to an integer, do **two steps**: `int(float("3.14"))` → `3`.

**Counter-intuitive `bool` cases:**
```python
bool("False")    # → True  (any non-empty string is truthy!)
bool("0")        # → True  (still a non-empty string)
bool(0)          # → False (the number zero)
bool([])         # → False (empty list)
```

**Why this matters:** Reading user input (`input()`) always gives a string. Converting it to a number with the *wrong* function — or without handling the `ValueError` — is a top source of beginner bugs.

</p>
</details>

---

###### B2. What is the output?

```python
print("apple" < "banana")
print("Apple" < "apple")
print("10" < "9")
```

- A: `True`, `True`, `False`
- B: `True`, `True`, `True`
- C: `True`, `False`, `False`
- D: `False`, `True`, `True`

<details><summary><b>Answer</b></summary>
<p>

#### Answer: B

Strings are compared **lexicographically** — character by character, using the **ASCII / Unicode code point** of each character.

**Trace each comparison:**

| Comparison | First differing char | Code points | Result |
|------------|---------------------|-------------|--------|
| `"apple" < "banana"` | `a` vs `b` | 97 < 98 | ✅ `True` |
| `"Apple" < "apple"` | `A` vs `a` | 65 < 97 | ✅ `True` (uppercase < lowercase) |
| `"10" < "9"` | `1` vs `9` | 49 < 57 | ✅ `True` (compares as strings, NOT numbers!) |

**Key Rule:**

> String comparison is **NOT** numeric — it's character-by-character ASCII comparison. `"10" < "9"` is `True` because `'1'` (49) comes before `'9'` (57) in ASCII.

**ASCII cheat sheet for comparison:**

| Range | Code points |
|-------|-------------|
| Digits `0`–`9` | 48–57 |
| Uppercase `A`–`Z` | 65–90 |
| Lowercase `a`–`z` | 97–122 |

So: **digits < uppercase < lowercase**.

**Why this matters:** Sorting filenames like `["file1", "file10", "file2"]` will give `["file1", "file10", "file2"]` — because `"1" < "2"` is true at the second character. To sort numerically, you need a custom key:
```python
sorted(files, key=lambda f: int(f.replace("file", "")))
```

**Case-insensitive equality the right way:**
```python
"Hello".lower() == "HELLO".lower()   # → True
"Hello".casefold() == "hello"        # → True (more robust for Unicode)
```

</p>
</details>

---

###### B3. What is the output?

```python
import numpy as np

arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

print(arr[1, 2])
print(arr[:, 1])
print(arr[0:2, 1:3])
```

- A: `6` / `[2, 5, 8]` / `[[2, 3], [5, 6]]`
- B: `5` / `[4, 5, 6]` / `[[1, 2], [4, 5]]`
- C: `6` / `[4, 5, 6]` / `[[2, 3], [5, 6]]`
- D: Error — cannot index 2D arrays with commas

<details><summary><b>Answer</b></summary>
<p>

#### Answer: A

NumPy uses the comma syntax `arr[row, col]` to index multi-dimensional arrays — this is **more efficient** than chained `arr[row][col]` (which works too).

**Visualising the array:**

```
         col 0  col 1  col 2
row 0    [ 1,    2,    3 ]
row 1    [ 4,    5,    6 ]
row 2    [ 7,    8,    9 ]
```

**Trace each line:**

| Expression | Meaning | Result |
|------------|---------|--------|
| `arr[1, 2]` | row 1, col 2 → single value | `6` |
| `arr[:, 1]` | all rows, col 1 → entire column | `[2, 5, 8]` |
| `arr[0:2, 1:3]` | rows 0–1, cols 1–2 → 2×2 sub-array | `[[2, 3], [5, 6]]` |

**Key Rule:**

| Syntax | What it returns |
|--------|-----------------|
| `arr[i, j]` | Single element at `(i, j)` |
| `arr[i]` | Entire row `i` (1D array) |
| `arr[:, j]` | Entire column `j` (1D array) |
| `arr[i, :]` | Same as `arr[i]` |
| `arr[i1:i2, j1:j2]` | Sub-array (2D) — `i2` and `j2` are excluded |

**`arr[1, 2]` vs `arr[1][2]`:**

Both return `6`. But:
- `arr[1, 2]` — one indexing operation, fast
- `arr[1][2]` — first creates row 1 (a temp array), then indexes — slower

**Why this matters:** Comma indexing is a NumPy-only feature; Python lists don't support it (`my_list[1, 2]` raises `TypeError`). It's also the foundation for advanced indexing — boolean masks, fancy indexing — that makes NumPy fast for data science.

**Common shape gotcha:**
```python
arr.shape       # → (3, 3)  — (rows, cols)
arr[:, 1].shape # → (3,)    — 1D after column extraction, NOT (3, 1)
```

</p>
</details>

---

###### B4. What is the output of the last line?

```python
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def display(self):
        print(f"{self.name}: {self.grade}")

s = Student("Alice", 85)
s.display
```

- A: Prints `Alice: 85`
- B: Nothing visible is printed — the method is referenced but not called
- C: `SyntaxError: missing parentheses`
- D: Prints the literal text `s.display`

<details><summary><b>Answer</b></summary>
<p>

#### Answer: B

`s.display` (without `()`) is a **bound method reference**, not a call. Python evaluates it to a method object and then discards it — no exception, no output.

**This is the same lesson as Q13, applied to methods:**

| Code | What it does |
|------|--------------|
| `s.display` | Evaluates to a bound method object — does nothing visible |
| `s.display()` | **Calls** the method — prints `Alice: 85` |

**Bonus understanding — what `self` actually is:**

When you call `s.display()`, Python automatically passes `s` as the first argument (which the method receives as `self`). It's equivalent to:

```python
Student.display(s)   # same as s.display()
```

This is why every instance method has `self` as the first parameter — Python fills it in for you.

**Key Rule:**

> A method reference without `()` is just an object. Add `()` to actually invoke it. This rule applies to **functions**, **methods**, and **classes** (instantiating a class is also a call: `Student(...)`).

**Class anatomy refresher:**

| Part | Purpose |
|------|---------|
| `class Student:` | Defines a new type |
| `def __init__(self, ...)` | Constructor — runs when you create an instance |
| `self.name = name` | Attaches data to the instance |
| `s = Student("Alice", 85)` | Creates an instance (calls `__init__`) |
| `s.display()` | Calls the method on that instance |
| `s.display` | Method reference — does nothing on its own |

**Why this matters:** Forgetting `()` on a method call is silent — no error, no output, your program just doesn't do what you expected. The bug from the MST (`greet` instead of `greet()`) applies equally to methods.

</p>
</details>

---

###### B5. A developer writes the following code but no chart appears on screen. What's missing?

```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [10, 20, 25, 30]

plt.plot(x, y)
plt.xlabel("Time")
plt.ylabel("Value")
plt.title("Trend Over Time")
```

- A: `plt.show()` at the end
- B: `plt.draw()` at the end
- C: `plt.display()` at the end
- D: `plt.render()` at the end

<details><summary><b>Answer</b></summary>
<p>

#### Answer: A

Matplotlib **builds the figure in memory** as you call `plot()`, `xlabel()`, etc. The figure isn't actually rendered to the screen until you call `plt.show()`.

**The standard Matplotlib workflow:**

| Step | Code | Purpose |
|------|------|---------|
| 1. Import | `import matplotlib.pyplot as plt` | Load the library |
| 2. Plot | `plt.plot(x, y)` | Add data to the current figure |
| 3. Label | `plt.xlabel(...)` / `plt.ylabel(...)` / `plt.title(...)` | Annotate the axes |
| 4. **Display** | `plt.show()` | **Render the figure on screen** |
| 5. Save (optional) | `plt.savefig("chart.png")` | Save to file (must come BEFORE `show()`) |

**Why options B, C, D are wrong:**

| Method | Real? | What it does |
|--------|-------|--------------|
| `plt.show()` | ✅ Yes | Displays the figure (this is the answer) |
| `plt.draw()` | ✅ Yes | Redraws the current figure (used inside event loops; doesn't open a window) |
| `plt.display()` | ❌ No | Not a Matplotlib function |
| `plt.render()` | ❌ No | Not a Matplotlib function |

**Key Rule:**

> Matplotlib commands accumulate state into the current figure. Nothing appears until you call `plt.show()` — except in **Jupyter notebooks**, where `%matplotlib inline` (the default) auto-displays at the end of each cell.

**Common chart types — one-liners:**

| Chart | Code |
|-------|------|
| Line | `plt.plot(x, y)` |
| Scatter | `plt.scatter(x, y)` |
| Bar | `plt.bar(categories, values)` |
| Histogram | `plt.hist(data, bins=10)` |
| Pie | `plt.pie(values, labels=labels)` |

**Why this matters:** In a `.py` script, forgetting `plt.show()` is the #1 reason "my chart isn't showing up." In a Jupyter notebook, it usually works without it — which lulls people into a bad habit that breaks when they move code to a script.

</p>
</details>

---

## Quick Reference Tables

### Python Collections at a Glance

| Type | Syntax | Ordered? | Mutable? | Duplicates? | Indexable? | Use when... |
|------|--------|----------|----------|-------------|------------|-------------|
| `list` | `[1, 2, 3]` | ✅ Yes | ✅ Yes | ✅ Yes | ✅ Yes | You need an ordered, changeable sequence |
| `tuple` | `(1, 2, 3)` | ✅ Yes | ❌ No | ✅ Yes | ✅ Yes | The data shouldn't change (coordinates, dict keys) |
| `set` | `{1, 2, 3}` | ❌ No | ✅ Yes | ❌ No | ❌ No | You need fast membership checks or deduplication |
| `dict` | `{"k": "v"}` | ✅ (3.7+) | ✅ Yes | ❌ keys | by key | You need key → value lookup |

### Indexing & Slicing

```
data = [10, 20, 30, 40, 50]
        0   1   2   3   4       ← positive indexes
       -5  -4  -3  -2  -1       ← negative indexes
```

| Expression | Result | Notes |
|------------|--------|-------|
| `data[0]` | `10` | First |
| `data[-1]` | `50` | Last |
| `data[len(data)]` | `IndexError` | One past the end — invalid |
| `data[1:4]` | `[20, 30, 40]` | start included, stop excluded |
| `data[:3]` | `[10, 20, 30]` | first three |
| `data[-2:]` | `[40, 50]` | last two |
| `data[::-1]` | `[50, 40, 30, 20, 10]` | reverse |

### Common Exception Types

| Exception | Triggered when... |
|-----------|-------------------|
| `ValueError` | Right type, bad value: `int("abc")` |
| `TypeError` | Wrong type entirely: `"a" + 1` |
| `ZeroDivisionError` | Dividing by zero: `1 / 0` |
| `IndexError` | List index out of range: `[1, 2][5]` |
| `KeyError` | Dict key not found: `{}["x"]` |
| `NameError` | Variable not defined: `print(undefined_var)` |
| `AttributeError` | Method/attribute doesn't exist: `"hi".foo()` |
| `FileNotFoundError` | `open("missing.txt")` |

### AI / ML / DL Cheat Sheet

| Concept | One-line definition | Example |
|---------|---------------------|---------|
| **AI** | Systems that mimic intelligent behaviour | Chess engine, spam filter, chatbot |
| **ML** | AI that learns patterns from data instead of hard-coded rules | Predicting prices from past sales |
| **DL** | ML using multi-layer neural networks | Image recognition, LLMs |
| **Supervised** | Learn from labeled examples (input + correct output) | Spam vs not-spam classifier |
| **Unsupervised** | Find patterns in unlabeled data | Customer segmentation |
| **Reinforcement** | Learn a policy via trial-and-error with rewards | Game-playing agents |

### NumPy vs Python List

| | Python `list` | NumPy `array` |
|---|---|---|
| Types | Mixed allowed | **Homogeneous** (one dtype) |
| Math (`arr * 2`) | Doesn't work elementwise — repeats list | Elementwise |
| Speed (large data) | Slow (Python loops) | Fast (C loops, vectorised) |
| Memory | High overhead per element | Compact, contiguous |
| Broadcasting | ❌ | ✅ |
| Best for | Heterogeneous data | Numerical computation |

### Pandas — Common One-Liners

| Task | Code |
|------|------|
| Create DataFrame | `pd.DataFrame({'A': [1, 2], 'B': [3, 4]})` |
| Read a CSV | `pd.read_csv("file.csv")` |
| First 5 rows | `df.head()` |
| Add a column from a list | `df['NewCol'] = [v1, v2, v3]` *(length must match)* |
| Add a constant column | `df['NewCol'] = 'value'` |
| Stack two DataFrames | `pd.concat([df1, df2])` |
| Merge on a key | `pd.merge(df1, df2, on='id')` |

---

## How to Use This Guide

1. **Work through each question without revealing the answer first** — write down your guess.
2. **Click the Answer block** to check your reasoning, not just the letter.
3. **Read the "Why this matters" section** — that's where deep understanding lives.
4. **Tick off the Study Guide checklist** only once you can explain the concept *out loud* without looking at the table.

Good luck on the MST.
