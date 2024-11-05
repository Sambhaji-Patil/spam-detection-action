# Spam Detection GitHub Action
This action detects spam comments using an ML model. Add it to `.github/workflows/spam-detection.yml` in your repository.

Example:
```yaml
name: Spam Detection

on:
  issue_comment:
    types: [created]

jobs:
  moderate_comment:
    runs-on: ubuntu-latest
    steps:
    - name: Run Spam Detection
      uses: your-username/spam-detection-action@v1
      with:
        github_token: ${{ secrets.GITHUB_TOKEN }}
        comment_body: ${{ github.event.comment.body }}
