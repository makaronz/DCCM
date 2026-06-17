```markdown
# DCCM Development Patterns

> Auto-generated skill from repository analysis

## Overview
This skill teaches the core development patterns and workflows used in the DCCM repository, a TypeScript project focused on structured documentation management. You'll learn the project's coding conventions, how to update or add documentation chapters, and the typical testing patterns found in the codebase.

## Coding Conventions

### File Naming
- **PascalCase** is used for file names.
  - Example: `ChapterManager.ts`, `2.1_ARRI_Cameras.md`

### Import Style
- **Relative imports** are used for referencing other files or modules.
  ```typescript
  import { ChapterManager } from './ChapterManager';
  ```

### Export Style
- **Named exports** are preferred.
  ```typescript
  // In ChapterManager.ts
  export function updateChapter() { ... }
  export const CHAPTER_LIMIT = 100;
  ```

### Commit Messages
- **Freeform** style, often mentioning the chapter and nature of the update.
  - Example: `Update 2.1 ARRI Cameras with new workflow section`

## Workflows

### Update Existing Chapter Markdown
**Trigger:** When you need to revise, expand, or modernize the content of an existing DCCM chapter.  
**Command:** `/update-chapter`

1. Identify the chapter to update.
2. Edit the corresponding `.md` file (e.g., `2.1_ARRI_Cameras.md`) with new or revised content.
3. Commit the changes with a message indicating the chapter and nature of the update.
   - Example commit: `Expand 2.1 ARRI Cameras with new color settings`

#### Example
```bash
# Edit the file
nano 2.1_ARRI_Cameras.md

# Commit your changes
git add 2.1_ARRI_Cameras.md
git commit -m "Update 2.1 ARRI Cameras: add new workflow section"
```

---

### Add New Chapter Markdown
**Trigger:** When you want to introduce a new topic or section to the DCCM documentation.  
**Command:** `/add-chapter`

1. Determine the new chapter or topic to add.
2. Create a new `.md` file following the naming convention (e.g., `13.0_AI_ML_Color_Management.md`).
3. Write the initial content for the new chapter.
4. Commit the new file with a message indicating the addition.
   - Example commit: `Add 13.0 AI ML Color Management chapter`

#### Example
```bash
# Create the new file
nano 13.0_AI_ML_Color_Management.md

# Add initial content and save

# Commit your new chapter
git add 13.0_AI_ML_Color_Management.md
git commit -m "Add 13.0 AI ML Color Management chapter"
```

## Testing Patterns

- Test files follow the pattern: `*.test.*`
  - Example: `ChapterManager.test.ts`
- The specific testing framework is **unknown**, but tests are likely colocated with the code they verify.

#### Example
```typescript
// ChapterManager.test.ts
import { updateChapter } from './ChapterManager';

test('updateChapter updates chapter content', () => {
  // ...test implementation
});
```

## Commands

| Command         | Purpose                                               |
|-----------------|-------------------------------------------------------|
| /update-chapter | Update the content of an existing chapter markdown    |
| /add-chapter    | Add a new chapter markdown to the documentation       |
```
