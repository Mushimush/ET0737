# Prompt Evaluation Rubric

**Module:** ET0737 ML & AI with Python
**Companion to:** Lab 1 – Mastering AI for EEE & Programming
**Purpose:** A shared rubric for judging prompt quality — use it on your own prompts and on a classmate's.

---

## How to use this rubric

1. Write your prompt.
2. Score it across the **5 dimensions** below (1–5 each, 25 total).
3. Run the prompt **3 times** in a fresh chat each time (the "Triple-Run Test" — see below).
4. Re-score after seeing the outputs. Your pre-run and post-run scores usually disagree — that gap is the lesson.
5. Swap with a partner and score each other's prompts blind (no discussion until both are done).

A **great prompt scores 4+ on all five dimensions**. Most first-draft prompts fail on 2–3.

---

## The 5 Dimensions

### 1. Persona Fit — *Does the role actually shape the output?*

The persona must constrain **style, depth, vocabulary, or stance** — not just decorate the prompt.

| Score | Description |
|---|---|
| 5 | Persona changes what the AI *refuses* to say or *how* it says it (e.g., "confused first-year student" forces questions, not explanations) |
| 3 | Persona is specific but doesn't meaningfully alter output (e.g., "senior engineer" — AI was going to be helpful anyway) |
| 1 | Generic or missing ("act as an expert", "you are a helpful assistant") |

**Red flag:** Remove the persona line. If the output would be the same, the persona wasn't doing work.

---

### 2. Constraint Specificity — *Are forbidden outputs named explicitly?*

The hardest part of prompt engineering is telling the AI what **not** to do. Vague negatives fail.

| Score | Description |
|---|---|
| 5 | Names the forbidden output precisely ("Do not write code blocks", "Do not plug in numbers", "Do not rewrite my explanation") |
| 3 | Soft guidance ("keep it simple", "don't be too technical") |
| 1 | No constraints — the AI picks the format |

**Red flag:** "Explain simply" is not a constraint. "Do not use any equations or numerical examples" is.

---

### 3. Task Decomposition — *Is the deliverable broken into named parts?*

A well-decomposed task is one you can tick off with a checklist.

| Score | Description |
|---|---|
| 5 | Named, numbered sub-parts ("give me (a) multimeter setting, (b) probe placement, (c) confirming reading") |
| 3 | One task with implied sub-parts ("explain voltage, current, and resistance") |
| 1 | Single open-ended ask ("teach me about Ohm's Law") |

**Red flag:** If you can't write a 3-item checklist from the prompt, the AI can't either.

---

### 4. Verifiability — *Can you tell from the output whether the prompt worked?*

This is the dimension students miss most. A prompt you can't grade is a prompt you can't improve.

| Score | Description |
|---|---|
| 5 | Output has checkable structure: counts ("list 5 edge cases"), named fields, forbidden items absent |
| 3 | You can tell "roughly" if it worked but can't point to the evidence |
| 1 | You're just "vibing" on whether the output is good |

**Red flag:** If your grading criterion is "it feels right," the prompt is under-specified.

---

### 5. Reusability — *Could a classmate swap the topic and reuse the structure?*

Good prompts are **templates**. Bad prompts are welded to one topic.

| Score | Description |
|---|---|
| 5 | Topic appears in 1–2 clearly marked slots; structure is generic (persona + constraint + decomposed task) |
| 3 | Reusable with moderate rewriting |
| 1 | Topic is tangled into every sentence — rewriting for a new topic = writing from scratch |

**Red flag:** Try it. Swap "Ohm's Law" for "Kirchhoff's Voltage Law" in your own prompt. How many edits did you need?

---

## The Triple-Run Test (the single best diagnostic)

Run the same prompt **3 times in fresh conversations** and compare the outputs:

| Result | Diagnosis |
|---|---|
| Outputs vary wildly in **structure** (different formats, different sections) | **Under-constrained** — add format and decomposition |
| Outputs are near-identical in structure, content varies usefully | **Well-engineered** ✓ |
| Outputs are near-identical in content too | **Over-constrained or trivial** — the AI has no room to think |
| One output is great, two are bad | **Ambiguous** — the prompt is a coin flip; find and pin down the ambiguous clause |

Consistency of *structure* with variety of *content* is the target.

---

## Peer Review Protocol (10 minutes)

1. **Swap prompts** — do not explain yours.
2. Each partner runs the other's prompt **once**, cold.
3. Score the output, not the prompt, on whether it:
   - Obeyed the named constraints
   - Produced all decomposed sub-parts
   - Would help someone learn (not just sound smart)
4. Then score the **prompt itself** on the 5 dimensions above.
5. Discuss gaps between the two scores — a prompt can read well but perform badly, or vice versa.

---

## Worked Examples (from Lab 1)

**Strong prompt — Exercise 3 (Circuit Troubleshooter):**
- ✓ Persona ("lab technician") shapes tone toward practical steps
- ✓ Explicit forbidden action ("Do not recalculate theoretical voltages")
- ✓ Decomposed into (a) multimeter setting, (b) probe placement, (c) confirming reading, × 3 hypotheses
- ✓ Verifiable: count the hypotheses, check each has all three parts
- ✓ Reusable: swap the circuit, keep the structure

**Weaker prompt — Exercise 1 (Conceptual Bridge):**
- ✓ Clear forbidden actions ("do not solve", "do not plug in numbers")
- ✗ "Explain the physical intuition" is fuzzy — no checkable structure
- ✗ Hard to tell from the output whether "intuition" was achieved or just reworded
- **Fix:** Require named analogy mappings — "For each of V, I, and R, give (1) the water-world equivalent, (2) the unit in the water world, (3) a one-sentence failure mode in that analogy."

---

## Scoring Sheet

| Prompt | Persona | Constraint | Decomposition | Verifiability | Reusability | **Total /25** |
|---|---|---|---|---|---|---|
| Ex 1 |  |  |  |  |  |  |
| Ex 2 |  |  |  |  |  |  |
| Ex 3 |  |  |  |  |  |  |
| Ex 4 |  |  |  |  |  |  |
| Ex 5 |  |  |  |  |  |  |

**Reflection:** Which dimension is your weakest across all five prompts? That's the one to practice next lab.
