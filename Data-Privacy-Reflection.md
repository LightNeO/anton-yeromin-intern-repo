# Reflections

1. What steps can you take to ensure you handle data securely in your daily tasks?

Use Synthetic Data: I script fake data for automated tests instead of using real customer database dumps.

Sanitize Evidence: I remove PII or tokens from screenshots and logs before attaching them to Jira tickets.

Git Safety: I strictly check that configuration files with secrets are listed in .gitignore before committing.

2. How should you store, share, and dispose of sensitive information safely?

Store: In local environment variables (.env) or a password manager, never hardcoded in the Python script.

Share: Via one-time, self-destructing links (e.g., 1Password Share), never as plain text in Discord/Slack.

Dispose: Delete local test logs and temporary data files immediately after the task is finished.

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