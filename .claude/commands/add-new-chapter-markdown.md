---
name: add-new-chapter-markdown
description: Workflow command scaffold for add-new-chapter-markdown in DCCM.
allowed_tools: ["Bash", "Read", "Write", "Grep", "Glob"]
---

# /add-new-chapter-markdown

Use this workflow when working on **add-new-chapter-markdown** in `DCCM`.

## Goal

Adds a new chapter or section to the DCCM documentation by creating a new markdown file.

## Common Files

- `*.md`

## Suggested Sequence

1. Understand the current state and failure mode before editing.
2. Make the smallest coherent change that satisfies the workflow goal.
3. Run the most relevant verification for touched files.
4. Summarize what changed and what still needs review.

## Typical Commit Signals

- Determine the new chapter or topic to add.
- Create a new .md file following the naming convention (e.g., 13.0_AI_ML_Color_Management.md).
- Write the initial content for the new chapter.
- Commit the new file with a message indicating the addition.

## Notes

- Treat this as a scaffold, not a hard-coded script.
- Update the command if the workflow evolves materially.