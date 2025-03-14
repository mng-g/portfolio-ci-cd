# Versioning, Branching, and Tagging Strategy

## **1. Branching Strategy**
We follow a **Trunk-Based Development (TBD)** approach where `main` is the central branch, and feature development happens in short-lived branches.

### **Main Branch (`main`)**
- The **single source of truth** for the project.
- Always **stable** and **ready for release**.
- Developers create feature branches from `main` and merge back frequently.

### **Feature & Bugfix Branches (`feature/*` and `bugfix/*`)**
- Created for new features or bug fixes.
- Merged into `main` once completed and reviewed.
- **Deleted after merging** to keep the repository clean.

### **Release Branches (`release-X.Y`)**
- Created when a release is ready for stabilization.
- Used for **bug fixes and final testing** before deployment.
- Example: `release-0.1`, `release-1.0`.
- **Merged into `main` when the version is ready**.
- **Deleted after merging** to avoid long-lived branches.

### **Hotfix Branches (`hotfix/*`)**
- Created when an **urgent fix** is required for a live release.
- Based on the latest stable release tag.
- Merged into both `main` and the active `release-*` branch (if applicable).

---

## **2. Tagging Strategy**
We use **Semantic Versioning (SemVer)** with additional pre-release identifiers. A SemVer version is structured as:

```
MAJOR.MINOR.PATCH-PRERELEASE+METADATA
```

Where:
- `MAJOR` → **Breaking changes** (incompatible API changes).
- `MINOR` → **New features** (backward-compatible).
- `PATCH` → **Bug fixes** (backward-compatible).
- `PRERELEASE` (optional) → **Alpha, Beta, RC** versions.
- `METADATA` (optional) → Extra build info, not relevant for version ordering.

### **Stable Releases (`X.Y.Z`)**
- Used for **production-ready releases**.
- Example: `v1.0.0`, `v1.2.3`.
- Created when `release-*` is merged into `main`.

### **Pre-Release Versions**
Used for releases that are still in testing or staging.

| Type  | Tag Format | Purpose | Stability |
|-------|-----------|---------|---------|
| **Alpha** | `vX.Y.Z-alpha.N` | Earliest unstable version, for internal testing only. | ❌ Highly unstable |
| **Beta** | `vX.Y.Z-beta.N` | More stable than alpha, used for user testing. | ⚠️ Somewhat stable |
| **Release Candidate (RC)** | `vX.Y.Z-rc.N` | Final testing before a stable release. | ✅ Mostly stable |
| **Stable** | `X.Y.Z` | Production-ready releases. | ✅ Fully stable |

✅ Example tag sequence for `v1.0.0`:
```
v1.0.0-alpha.1 → v1.0.0-alpha.2 → v1.0.0-beta.1 → v1.0.0-rc.1 → v1.0.0
```

### **Patch Releases (`X.Y.Z` Updates)**
- Used for small bug fixes or security patches.
- Created from an existing `release-*` branch.
- Example: `v1.0.1`, `v1.0.2`.

---

## **3. Workflow Summary**

1. **Feature Development**: Work in `feature/*` → Merge into `main` → Delete feature branch.
2. **Preparing a Release**: Create `release-*` branch from `main`.
3. **Testing & Pre-Release**: Tag with `alpha`, `beta`, `rc` versions.
4. **Stable Release**: Tag as `X.Y.Z` → Merge `release-*` into `main` → Delete `release-*`.
5. **Bug Fixes**: Apply fixes in `release-*`, tag new PATCH versions, merge back into `main`.

This ensures a **clean, efficient, and structured** release process. 🚀