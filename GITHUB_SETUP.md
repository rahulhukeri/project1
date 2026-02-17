# Connect to GitHub and push this project

## 1. Connect to GitHub (one-time)

### Option A: HTTPS (simplest)
1. Create a new repository on GitHub: https://github.com/new  
   - Name it (e.g. `cursor-projects` or `hello-script`)
   - Leave "Initialize with README" **unchecked** (you already have a repo)
2. Copy the repo URL (e.g. `https://github.com/YOUR_USERNAME/REPO_NAME.git`)

### Option B: SSH
1. If you use SSH keys, create the repo on GitHub and use the SSH URL:  
   `git@github.com:YOUR_USERNAME/REPO_NAME.git`

---

## 2. Add the remote and push

In PowerShell, from this folder:

```powershell
# Add your GitHub repo as "origin" (replace with YOUR repo URL)
git remote add origin https://github.com/YOUR_USERNAME/REPO_NAME.git

# Push your code (first time)
git push -u origin master
```

If your default branch is `main` on GitHub, use:

```powershell
git push -u origin master:main
```

---

## 3. Run the script locally

```powershell
python hello.py
```

Or with the full path:

```powershell
python "c:\Users\RahulHukeri\OneDrive - White Wolf Capital\CursorProjects\hello.py"
```

---

## 4. After changing code: push again

```powershell
git add .
git commit -m "Your message"
git push
```

---

## Troubleshooting

- **Authentication**: GitHub no longer accepts account passwords for git. Use:
  - **Personal Access Token (HTTPS)**: GitHub → Settings → Developer settings → Personal access tokens. Use the token as the password when `git push` asks.
  - **SSH key**: Add your public key in GitHub → Settings → SSH and GPG keys, then use the SSH repo URL.
- **Branch name**: If GitHub shows `main` and you have `master`, either rename locally (`git branch -M main`) or push as `git push -u origin master:main`.
