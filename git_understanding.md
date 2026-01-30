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