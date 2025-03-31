In **Trunk-Based Development (TBD)**, developers **always work on `main`** and only create `release-*` branches when they are preparing for a release. Let me break down the workflow clearly.  

---

# **🔹 Trunk-Based Development Workflow**  

## **📌 1. Daily Development (Work Happens on `main`)**
- Developers **create short-lived feature branches** from `main` (e.g., `feature/new-login`).
- They **merge back into `main` quickly** (sometimes daily or even multiple times per day).
- `main` **is always deployable** (CI/CD ensures tests pass before merging).

✅ **Example (Developer Workflow)**
```sh
git checkout main  # Always start from main
git pull origin main  # Get the latest changes
git checkout -b feature/new-login  # Create a short-lived feature branch

# Work on the feature...

git commit -m "Added new login functionality"
git push origin feature/new-login  # Push to GitHub

# Open a Pull Request (PR) → Review → Merge into main

git checkout main
git pull origin main  # Ensure latest changes
```
🚀 Now `main` has the feature, and the **next deployment can include it immediately**.

---

## **📌 2. Preparing a Release (Create `release-*` Branch)**
Once `main` is **stable enough for a release**, create a **temporary** `release-0.1` branch.

✅ **Example (Release Manager Workflow)**
```sh
git checkout main
git pull origin main
git checkout -b release-0.1  # Create a new release branch
git push origin release-0.1  # Push to GitHub
```
Now, the `release-0.1` branch is used **only for bug fixes and final testing**.

- **Developers continue working in `main` on future features.**
- **The `release-0.1` branch gets only bug fixes related to the release.**
- Developers **create short-lived bugfix branches** from `release-*` (e.g., `bugfix/1234`).
- They **merge back into `release-*` as soon as the bug is fixed**

---

## **📌 3. Tagging Pre-Release Versions (`alpha`, `beta`, `rc`)**
As fixes are made in `release-0.1`, tag **alpha, beta, or RC versions**.

✅ **Example**
```sh
git checkout release-0.1
git tag v0.1.0-alpha.1
git push origin v0.1.0-alpha.1
```

- If more bugs are fixed, create `v0.1.0-alpha.2`, `v0.1.0-beta.1`, etc.
- Continue until the release is stable.

---

## **📌 4. Final Release (Merge `release-0.1` into `main`)**
Once testing is complete:
1. Tag the **final stable version**.
2. Merge `release-0.1` back into `main`.
3. Delete the `release-0.1` branch.

✅ **Example**
```sh
git checkout release-0.1
git tag v0.1.0  # Final stable version
git push origin v0.1.0

git checkout main
git merge release-0.1  # Merge the stable release into main
git push origin main

git branch -d release-0.1  # Delete locally
git push origin --delete release-0.1  # Delete remotely
```

🚀 Now, `main` contains `v0.1.0`, and developers continue working on **future versions** in `main`.

---

## **📌 5. Bug Fixes (PATCH Releases in `release-*`)**
- If you need to fix a bug **in a released version**, work on the `release-*` branch.
- Create a **PATCH version** (`v0.1.1`).
- Merge the fix **back into `main`**.

✅ **Example**
```sh
git checkout release-0.1
git commit -m "Fixed login bug"
git push origin release-0.1

git tag v0.1.1
git push origin v0.1.1

git checkout main
git merge release-0.1  # Bring the fix into main
git push origin main
```

---

# **🔹 Summary of Workflow**
| Step | Action |
|------|--------|
| **1. Daily Work** | Developers work in `main`, merging small feature branches frequently. |
| **2. Preparing Release** | Create a `release-*` branch when ready to stabilize a version. |
| **3. Pre-Release Testing** | Fix bugs in `release-*` and tag `alpha`, `beta`, `rc` versions. |
| **4. Final Release** | Merge `release-*` into `main`, tag final version, delete `release-*`. |
| **5. Bug Fixes** | If needed, fix in `release-*`, tag PATCH (`v0.1.1`), and merge into `main`. |

✅ **Developers always work in `main`, not `release-*`.**
🚀 **Releases happen in `release-*`, but developers do not merge features there.**
🔥 **No `develop` branch needed!**