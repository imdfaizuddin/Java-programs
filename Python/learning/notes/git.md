To delete a branch in Git, you can use the following commands, depending on whether you want to delete a local branch or a remote branch.

### Deleting a Local Branch

1. Open your terminal or command prompt.
2. Navigate to your repository.
3. Use the following command to delete the branch:

   ```bash
   git branch -d branch_name
   ```

   Replace `branch_name` with the name of the branch you want to delete. This will only work if the branch has been fully merged.

   If you want to forcefully delete a branch that hasn’t been merged, use:

   ```bash
   git branch -D branch_name
   ```

### Deleting a Remote Branch

To delete a branch on a remote repository (like GitHub or GitLab), use the following command:

```bash
git push origin --delete branch_name
```

Replace `branch_name` with the name of the remote branch you want to delete.

### Important Note

Make sure you really want to delete the branch, as this action can’t be easily undone, especially for remote branches!

To rename a branch in Git, you can follow these steps depending on whether you want to rename a local branch or a remote branch.

### Renaming a Local Branch

1. **Switch to the branch you want to rename** (if you're not already on it):

   ```bash
   git checkout old_branch_name
   ```

2. **Rename the branch**:

   ```bash
   git branch -m new_branch_name
   ```

   Replace `old_branch_name` with the current name of the branch and `new_branch_name` with the desired new name.

### Renaming a Remote Branch

1. **Rename the local branch** as described above.

2. **Delete the old branch on the remote**:

   ```bash
   git push origin --delete old_branch_name
   ```

3. **Push the renamed branch to the remote**:

   ```bash
   git push origin new_branch_name
   ```

4. **Reset the upstream branch for the new local branch** (if needed):

   ```bash
   git push --set-upstream origin new_branch_name
   ```

### Important Note

Make sure to notify your team if you're renaming branches that others might be using!