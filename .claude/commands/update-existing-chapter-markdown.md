---
name: update-existing-chapter-markdown
description: Workflow command scaffold for update-existing-chapter-markdown in DCCM.
allowed_tools: ["Bash", "Read", "Write", "Grep", "Glob"]
---

# /update-existing-chapter-markdown

Use this workflow when working on **update-existing-chapter-markdown** in `DCCM`.

## Goal

Updates the content of an existing chapter or section in the DCCM documentation by modifying its corresponding markdown file.

## Common Files

- `*.md`

## Suggested Sequence

1. Understand the current state and failure mode before editing.
2. Make the smallest coherent change that satisfies the workflow goal.
3. Run the most relevant verification for touched files.
4. Summarize what changed and what still needs review.

## Typical Commit Signals

- Identify the chapter to update.
- Edit the corresponding .md file (e.g., 2.1_ARRI_Cameras.md) with new or revised content.
- Commit the changes with a message indicating the chapter and nature of the update.

## Notes

- Treat this as a scaffold, not a hard-coded script.
- Update the command if the workflow evolves materially.