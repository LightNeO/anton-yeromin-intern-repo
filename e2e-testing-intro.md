# 1. What is the difference between E2E, Unit, and Integration testing?

* **Unit Testing:**
  * *What it tests:* Individual components in isolation (functions, classes).
  * *Example:* Checking if the `calculate_tax()` function returns the correct number.
* **Integration Testing:**
  * *What it tests:* How two or more components work together.
  * *Example:* Checking if the "Save" button successfully writes data to the Database.
* **E2E Testing:**
  * *What it tests:* The entire flow from start to finish, exactly as a user would do it.
  * *Example:* Purchase flow on some webside: registration, item search, adding to the cart, payment.

# 2. What are the key benefits of E2E tests in a real-world application?

* **User-Centric Confidence:** Unit tests can pass even if the app is broken (e.g., the database works, but the "Login" button is unclickable). E2E tests confirm the *user* can achieve their goal.
* **Cross-System Verification:** Modern apps rely on APIs, databases, and OS permissions. E2E tests verify that all these external parts communicate correctly.
* **Safety Net for Refactoring:** Developers can rewrite the entire backend code; if the E2E tests still pass, we know the user experience hasn't changed.

# 3. How does automated testing help Focus Bear reduce regression bugs?

* **Regression** means "something that used to work has stopped working."
* **Manual vs. Auto:** Focus Bear has many features (Blocking, Pomodoro, Habits). Manually clicking through every feature on Windows, Mac, and Mobile before every release would take days.
* **The "Nightly Watchman":** Automated Pywinauto tests(usually) run every night. If a developer accidentally breaks the "Block YouTube" feature while fixing a typo, the E2E test will fail immediately. This prevents the bug from ever reaching the users.

# 4. What are some challenges of writing and maintaining E2E tests?

* **Flakiness:** E2E tests are "fragile." A test might fail just because the PC lagged for 1 second or a Windows update popup appeared. We have to write robust "Waiting" logic to handle this.
* **Execution Speed:** Unit tests take milliseconds. E2E tests (launching an app, clicking buttons) take seconds or minutes. A full suite can take hours to run.
* **Maintenance Cost:** If the design team changes the "Save" button to "Submit," the automated test might fail because it can't find the button. We use patterns like **Page Object Model (POM)** to fix this quickly in one place.
* **Environment Dependency:** Windows tests require a real Windows Desktop environment (Headful), which is harder to set up in CI/CD than simple Linux scripts.
