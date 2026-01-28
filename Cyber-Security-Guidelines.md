# Reflections

1. What security measures do you currently follow, and where can you improve?

Current: I use unique, complex passwords for all accounts and have 2FA enabled on GitHub and Google Workspace.

Improve: I need to stop manually typing test credentials into my local scripts during debugging. I will switch to strictly using environment variables (.env) even for quick local tests to prevent accidental hardcoding.

2. How can you make secure behaviour a habit rather than an afterthought?

Automation: I will set up pre-commit hooks (using tools like git-secrets or trufflehog) in my local repository. This way, the system automatically scans my code for keys or passwords before allowing me to commit, making security a constraint rather than a choice.

3. What steps will you take to ensure your passwords and accounts are secure?

Password Manager: I will use a password manager (e.g., 1Password or Bitwarden) to generate random, 20-character strings for all Test Users in my automation suite.

No Re-use: I will ensure my "Test Admin" passwords are completely different from my actual production access credentials.

# Document one new cyber security habit you will follow at Focus Bear.

I think it would be: use 2FA where possible. Previously I used it only if the app force me to do that