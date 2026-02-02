# 38
## 1. Core Principles

### Simplicity (KISS - Keep It Simple, Stupid)
* **Definition:** Code should solve the problem with the fewest moving parts possible.
* **Why it matters:** Complex code is a breeding ground for bugs. If a function does three different things, it is three times harder to test.

### Readability
* **Definition:** Code is read 10x more often than it is written. Variable and function names should reveal *intent*.
* **Why it matters:** You shouldn't need a decoder ring to understand what `x` or `temp_var_2` does.
* **QA Context:** `click_button()` is vague. `click_submit_login_form()` is readable.

### Maintainability
* **Definition:** The ability for a future dev or QA Auto to modify the code without breaking everything.
* **Why it matters:** Rigid code requires a rewrite for every small feature change. Modular code just needs a tweak.
* **QA Context:** If the "Login" URL changes, you should only have to update it in *one* file (config), not in 50 different test scripts.

### Consistency
* **Definition:** Following a uniform style guide (like PEP 8 for Python) throughout the project.
* **Why it matters:** It reduces cognitive load. You don't have to guess if variables are `camelCase` or `snake_case`; you just know.
* **QA Context:** If one test file uses `setup_method()` and another uses `before_test()`, it creates confusion.

### Efficiency
* **Definition:** Writing code that performs well without wasting resources, but avoiding "Premature Optimization."
* **Why it matters:** Efficiency is good, but readability comes first. Don't write cryptic, "clever" one-liners just to save 0.001 seconds unless performance is critical.

---

## 2. Practical Example: Messy vs. Clean

### ❌ The Messy Code (Bad)
*Why is this difficult to read?*
1.  **Meaningless Names:** `d`, `l`, `c` tell us nothing.
2.  **Magic Numbers:** What is `0.2`? Tax? Discount? Tip?
3.  **No Type Hinting:** We don't know if `l` is a list of numbers or objects.
4.  **Poor Formatting:** No spacing makes it visually dense.

```python
def calc(l):
    t = 0
    for i in l:
        if i > 100:
            d = i * 0.2
            c = i - d
            t += c
        else:
            t += i
    return t
```

### ✅ The Clean Code (Good)
*Why is this much better?*
1. **Descriptive Names:** `total`, `price`, `discount` clearly explain what each variable does.
2. **Named Constants:** `DISCOUNT_RATE` shows intent instead of magic `0.2`.
3. **Type Hints:** We know we're working with a list of floats.
4. **Docstring:** Future devs understand the function's purpose at a glance.
5. **Readable Logic:** The calculation is easy to follow.

```python
DISCOUNT_RATE = 0.2
DISCOUNT_THRESHOLD = 100

def calculate_total_price(prices: list[float]) -> float:
    """
    Calculate total price with a discount applied to items above threshold.
    
    Args:
        prices: List of item prices (floats)
    
    Returns:
        Total price after applying discounts
    """
    total = 0
    for price in prices:
        if price > DISCOUNT_THRESHOLD:
            discount = price * DISCOUNT_RATE
            discounted_price = price - discount
            total += discounted_price
        else:
            total += price
    return total
```

# 39

## 1. Why is code formatting important?
Code formatting is not about aesthetics; it is about cognitive load
* **Brain Power:** When code looks consistent, my brain stops processing *how* it looks (brackets, spaces) and focuses entirely on *what* it does (logic).
* **Diff Readability:** If everyone formats code differently, a Code Review diff will show 100 changes just because someone added spaces. With a formatter, the diff shows only logic changes.
* **Ending Arguments:** It stops "Bikeshedding" (pointless arguments about where to put braces). We just delegate those decisions to the tool.

### 1.1. The Airbnb Style Guide (Research Summary)
I reviewed the Airbnb JavaScript Style Guide, which is considered the "Gold Standard" in the industry. But as I understand from future tasks we'll be using Python for E2E testing, so I desided to dive diper into PEP8

## 2. What issues did the linter detect?
I'm using Flake8 and Black formater for VS Code, so it detects regular issue in writing a code: wrong imports, wrong variable namings, whitespaces etc. And also Alt+Shift+T for marmating make thing easier

## 4. Did formatting the code make it easier to read?
**Yes, immediately.**
I used **Black** (the Python formatter). It automatically:
* Fixed all my indentation.
* Standardized string quotes (changed `'` to `"`).
* Broke long lines into readable chunks.