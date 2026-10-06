# Smart Stay – GitHub Upload Checklist

## Before uploading

- [ ] Remove real names, phone numbers, emails, and other private information.
- [ ] Do not upload `.env`.
- [ ] Do not upload database passwords.
- [ ] Do not upload database dumps containing private data.
- [ ] Confirm `venv/`, `.venv/`, `__pycache__/`, and `*.pyc` are ignored.
- [ ] Run the project locally and confirm it still works.

## Git commands

```bash
git init
git add .
git status
git commit -m "Initial Smart Stay profile matching demo"
git branch -M main
git remote add origin YOUR_GITHUB_REPOSITORY_URL
git push -u origin main
```

## Recommended public repository name

```text
smart-stay-profile-matching-demo
```

## Public repository reminder

A public GitHub repository means the source code can be viewed by anyone. Keep credentials and personal data outside the repository.
