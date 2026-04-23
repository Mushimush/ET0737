# Lab 1 – Mastering AI for EEE & Programming

**Module:** ET0737 ML & AI with Python
**Student:** Stanley
**Date:** 2026-04-21

Each prompt follows the **Persona → Constraint → Task** structure (the "Three Layers of a Great Prompt").

---

## Exercise 1: The Conceptual Bridge (EEE)

**Step 1 — Formula Selected:**
V = IR (Ohm's Law)

**Step 2 — Your Prompt:**

> Act as a physics tutor who teaches through analogies, not math. I am studying Ohm's Law (V = IR). **Do not solve a circuit for me** and do not plug in any numbers. Instead, explain the physical intuition of voltage, current, and resistance using a **water-pressure / pipe analogy** — what does each variable correspond to in the real world, and why does increasing resistance reduce current for a fixed voltage? End your response with **one conceptual question** that tests whether I understand how energy is dissipated as heat inside a resistor.

**Your Output (answer to AI's conceptual question):**
_(fill in after running the prompt)_

---

## Exercise 2: The Code Logic Architect (Programming)

**Step 1 — Programming Goal:**
Write a C++ function that sorts a list of temperature sensor readings in ascending order and returns the median value.

**Step 2 — Your Prompt:**

> Act as a senior C++ mentor guiding a junior student. I am writing a function that sorts a list of temperature sensor readings and returns the **median**. **Do not write any C++ code or code blocks.** Instead, give me a **pseudocode outline** (plain English, numbered steps) covering the sort logic and how to correctly pick the median for both odd- and even-length lists. After the pseudocode, give me **one "buggy hint"** — a common mistake students make with **loop counters or off-by-one errors** when indexing the middle of a sorted list — so I can watch out for it.

**AI Response Summary (the buggy hint / logic step warned about):**
_(fill in after running the prompt)_

---

## Exercise 3: The Circuit Troubleshooter (EEE)

**Step 1 — Broken State:**
In a series circuit with a 9V battery, R1 (1kΩ), and R2 (2kΩ), the measured voltage across R2 is 0V (expected ~6V).

**Step 2 — Your Prompt:**

> Act as an experienced electronics lab technician. I have a series circuit: 9V battery → R1 (1kΩ) → R2 (2kΩ) → back to battery. I measured **0V across R2**, but I expected about 6V. **Do not recalculate the theoretical voltages for me.** Instead, give me **three distinct physical failure hypotheses** (e.g., short circuit across R2, open circuit elsewhere, faulty battery/loose wire). For **each hypothesis**, tell me: (a) the exact **multimeter setting** I should use (DC voltage, resistance, continuity), (b) **where to place the probes**, and (c) **what reading would confirm** that specific failure.

**Diagnostic Plan (one verification method suggested by AI):**
_(fill in after running the prompt)_

---

## Exercise 4: The Edge-Case Stress Test (Programming)

**Step 1 — Function Description:**
A C++ function `int divide(int a, int b)` that returns `a / b`.

**Step 2 — Your Prompt:**

> Act as a **Quality Assurance (QA) Engineer** with a paranoid mindset. I have a C++ function `int divide(int a, int b)` that returns `a / b`. **Do not rewrite the function for me.** Instead, list **5 edge cases or malicious inputs** that could crash the program, cause undefined behavior, or produce a silently wrong result. For each case, give: (1) the **specific input values**, (2) **why it's dangerous** (e.g., division by zero, integer overflow, INT_MIN / -1), and (3) what **category of defect** it represents (crash, logic error, security risk).

**Risk Analysis (two edge cases I hadn't previously considered):**
1. _(fill in after running the prompt)_
2. _(fill in after running the prompt)_

---

## Exercise 5: The Reverse Instructor (Comprehensive)

**Step 1 — Topic Chosen:** C++ Pointers

**My explanation in my own words:**
> A pointer in C++ is a variable that stores a memory address instead of a regular value. You declare it with a `*`, like `int* p`. You use `&x` to get the address of a variable `x`, and you use `*p` to access the value stored at that address. Pointers let you share data between functions without copying it.

**Step 2 — Your Prompt:**

> Act as a **confused first-year student** who has never programmed before. I am going to explain **C++ pointers** to you as if I am the teacher. Read my explanation below and **critically analyze it for technical inaccuracies, missing links in logic, or concepts I glossed over** (e.g., null pointers, dereferencing uninitialized pointers, the difference between the pointer and what it points to, stack vs. heap). **Do not rewrite my explanation for me.** Instead, ask me **specific follow-up questions** about the parts that would confuse a beginner, and point out exactly **where my logic has gaps**.
>
> *My explanation:* "A pointer in C++ is a variable that stores a memory address instead of a regular value. You declare it with a `*`, like `int* p`. You use `&x` to get the address of a variable `x`, and you use `*p` to access the value stored at that address. Pointers let you share data between functions without copying it."

**Critique & Refinement (weakness AI found + how I corrected it):**
_(fill in after running the prompt)_

---

## Reflection Question

> *How did your understanding of the topic change when you were forbidden from asking the AI for the direct answer?*

_(fill in after completing all exercises)_
