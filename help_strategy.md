# Reflection: Troubleshooting & Help Strategy

## 1. When do I prefer using AI vs. searching Google?

I view AI (ChatGPT/Gemini) as a **Generator and Explainer**, while Google is a **Verifier and Finder**.

### **I use AI when:**

* **I need a template or boilerplate:** For example, "Write a standard Pytest setup for a Pywinauto test." It saves 15 minutes of typing setup code.
* **I have a complex error log:** Pasting a massive Python stack trace into AI often pinpoints the root cause (e.g., "ElementNotFoundError on line 45") faster than I can scan it visually.
* **I need to understand a concept:** Asking "How does the Page Object Model work in Python?" gives me a tailored tutorial.
* **I need to generate tedious logic:** Writing Regex patterns or complex XPath selectors is error-prone for humans but trivial for AI.

### **I use Google when:**

* **I need current documentation:** AI knowledge has a cutoff. For the latest library updates (e.g., a new feature in Selenium 4.x), official docs found via Google are essential.
* **I encounter environment-specific bugs:** Issues like "Windows 11 System Tray automation" are often discussed in specific GitHub Issues or StackOverflow threads that AI might hallucinate solutions for.
* **I need to verify AI code:** If AI suggests a method that doesn't work, I search the library's documentation to see if that method actually exists or if the AI "hallucinated" it.

---

## 2. How do I decide when to ask a colleague instead?

Escalating to a human is a strategic decision to balance independence with efficiency. I follow the **"30-Minute Rule"** and the **"Internal vs. External"** check.

### **I ask a colleague when:**

* **The problem is "Internal":** If the issue relates to proprietary business logic, internal API keys, or specific test environment configurations (e.g., "Why is the debug port blocked in the Production build?"). Google and AI cannot answer questions about our private code.
* **I am blocked for > 30 minutes:** If I have tried AI, Google, and debugging for 45 minutes without progress, I am entering the zone of "diminishing returns." Asking for help prevents wasting hours on a simple fix.
* **I need architectural advice:** Decisions that affect the whole project (e.g., "Should we use Pywinauto or Appium?") require team consensus and experience, not just a code snippet.

### **Before asking, I always:**

1. **Reproduce the issue:** Ensure I can make it happen consistently.
2. **Gather artifacts:** Collect logs, screenshots, and error messages.
3. **Summarize attempts:** Be ready to say, "I tried X and Y, but Z happened."

---

## 3. What challenges do developers face when troubleshooting alone?

* **Tunnel Vision:** When working alone, it is easy to get fixated on one specific solution path (e.g., "I MUST make this specific selector work") and miss a simpler alternative (e.g., "Just use a keyboard shortcut instead").
* **The "XY Problem":** I might spend hours trying to solve problem Y (e.g., "How to hack the registry for WebView2") without realizing that problem X (e.g., "We just need a Dev Build from the team") was the real solution.
* **Burnout and Frustration:** Staring at a failing test for hours drains cognitive energy, leading to silly mistakes like typos or missing imports.
* **Knowledge Gaps:** Sometimes, "you don't know what you don't know." A colleague might spot a missing environment variable in 5 seconds because they encountered it last week, whereas I might spend days searching for it.
