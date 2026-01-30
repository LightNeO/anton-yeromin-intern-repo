# What caused the conflict?
 Just for testing I created simple function that adds a + b, in another branch I changed it to a - b
# How did you resolve it?
 After merge comand I received merge conflict(separate conflict file was opened because i use VS code), I manualy saved new version a - b, added the to staging area and commited changes
# What did you learn?
 Nothing new, I already know about it, just a small practice

# What is the difference between staging and committing?
 Staging makes a snapshot of the file, Commiting - saves it to the history
# Why does Git separate these two steps?
 To separate functionality that I send to repo. I cover make several test cases during the day that covers different functionality. And after that I can split files (by git add files names) into different commits to make clear history, and also to be able to revert to specific commit if there will be some issues
# When would you want to stage changes without committing?
 For partial commit - I can add only part of the file to staging area
 And for some sanity checks before commiting

# Why is pushing directly to main problematic?
 Possibility of broken builds, bypassing autotests CI/CD pipelines, many people + many commits = history mess
# How do branches help with reviewing code?
 Cannt do merge without pull request, specific context for each branch helps to understand code, easier to resolve conflicts
# What happens if two people edit the same file on different branches?
 IF they edited different lines/functions in different places - nothing specific
 IF they edited same lines - will be a merge conflict

# What does each command do? When would you use it in a real project (hint: these are all really important in long running projects with multiple developers)? What surprised you while testing these commands?

1. git checkout main -- <file>

What does it do?
    It forcibly restores a specific file in my current working directory to match the version found on the `main` branch. It ignores all other files; it only resets the one I specified.

When would you use it in a real project?
    If for example I changed alot in the file, and need to revert it to the "start" stage, instead of clicking Ctrl+Z 999 times, I can use this command

What surprised you while testing?
    I was surprised that it does not ask for confirmation.

2. git cherry-pick <commit>

What does it do?
    It takes a specific commit from a different branch and "copies" it onto my current branch. It is like a precise "Copy-Paste" for a commit, rather than merging the entire history of a branch.

When would you use it in a real project?
    If I accidentally committed my changes to the wrong branch. I can switch to the correct branch, cherry-pick the commit, and then delete it from the wrong branch.

What surprised you while testing?
    Nothing really

---

3. `git log`

What does it do?
    It displays the chronological history of the repository, showing commit Hashes, Authors, Dates, and Messages.

When would you use it in a real project?
    As a QA, I use this to verify "What is in the build?"

What surprised you while testing?
    I learned that the default view is a bit hard to read. Using `git log --oneline --graph`

4. `git blame <file>`

What does it do?
    It shows the file line-by-line, listing exactly who modified that line last and when

When would you use it in a real project?
    To check whom to blame when there is a bug


## 1. What does `git bisect` do?
`git bisect` is a debugging tool that uses a **Binary Search algorithm** to find the specific commit that introduced a bug.

Instead of checking commits one by one (Linear Search), `git bisect` cuts the history in half.
1.  I tell Git a "Bad" commit (where the bug exists).
2.  I tell Git a "Good" commit (where the feature worked).
3.  Git checks out the commit exactly in the middle.
4.  I test that commit.
    * If it works, the bug is in the *second* half.
    * If it fails, the bug is in the *first* half.
5.  Git repeats this "halving" process until only one commit remains—the culprit.



## 2. When would you use it in a real-world debugging situation?
I would use this for **Regression Testing**.
**Scenario:** A critical test passed in the release 5 days ago (v1.0), but it is failing in the current build (v1.1). There have been 100 commits since then by 5 different developers.
Instead of reading 100 diffs or guessing, I start `git bisect`.
* **Good:** v1.0 tag.
* **Bad:** HEAD (Current).
Within a few minutes (and about 6-7 steps), I can pinpoint exactly which developer broke the build and assign the ticket to them with proof.

## 3. How does it compare to manually reviewing commits?
* **Manual Review:** This is slow and prone to error. If I have to check 100 commits, I might have to do 100 checks (Linear Time). I also might miss a subtle code change that caused the issue.
* **Git Bisect:** This is exponentially faster (Logarithmic Time). For 100 commits, `bisect` only needs about **7 steps**. For 1,000 commits, it only needs about **10 steps**. It is the most efficient way to debug large history gaps.