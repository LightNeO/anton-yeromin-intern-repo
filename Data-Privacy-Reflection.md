# Identify at least one habit or practice you can adopt to improve data security in your role.

I think it would be: never use hardcoded values for api keys, passwords, test data etc:

To do that I use .gitignore and .env files

# Document at least one key learning or security measure you will implement.

Problem: Hardcoding sensitive credentials (such as test user emails, passwords, and API tokens) directly into automation scripts poses a significant security risk. If pushed to a shared repository (GitHub), these credentials become visible to anyone with access to the code, leading to potential data breaches.

Action Taken: I can refactor the test automation framework to strictly separate configuration from code.

Implementation: Integrated the python-dotenv library to manage secrets.

Storage: Created a local .env file to store TEST_USER_EMAIL and TEST_USER_PASSWORD.

Protection: Configured .gitignore to explicitly exclude .env files from version control.

Verification: Verified that the authentication logic now pulls credentials dynamically from the environment, ensuring no sensitive data is committed to the repository history.