#!/bin/bash
# Repo Reader - Quick repository analysis tool
# Analyzes the current repository structure and content

set -e

# Colors
GREEN='\033[0;32m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
NC='\033[0m'

REPO_ROOT=$(git rev-parse --show-toplevel 2>/dev/null || pwd)

echo -e "${CYAN}============================================${NC}"
echo -e "${CYAN}        Repository Reader${NC}"
echo -e "${CYAN}============================================${NC}"
echo ""

# Repository info
echo -e "${BLUE}Repository Information:${NC}"
echo "  Path: $REPO_ROOT"
echo "  Name: $(basename "$REPO_ROOT")"

# Git info
if [ -d "$REPO_ROOT/.git" ]; then
    BRANCH=$(git branch --show-current 2>/dev/null || echo "unknown")
    REMOTE=$(git remote get-url origin 2>/dev/null || echo "no remote")
    COMMITS=$(git rev-list --count HEAD 2>/dev/null || echo "0")
    echo "  Branch: $BRANCH"
    echo "  Remote: $REMOTE"
    echo "  Commits: $COMMITS"
fi
echo ""

# File statistics
echo -e "${BLUE}File Statistics:${NC}"
TOTAL_FILES=$(find "$REPO_ROOT" -type f -not -path '*/.git/*' | wc -l)
MD_FILES=$(find "$REPO_ROOT" -name "*.md" -not -path '*/.git/*' | wc -l)
JS_FILES=$(find "$REPO_ROOT" -name "*.js" -not -path '*/.git/*' -not -path '*/node_modules/*' | wc -l)
TS_FILES=$(find "$REPO_ROOT" -name "*.ts" -not -path '*/.git/*' -not -path '*/node_modules/*' | wc -l)
PY_FILES=$(find "$REPO_ROOT" -name "*.py" -not -path '*/.git/*' | wc -l)
JSON_FILES=$(find "$REPO_ROOT" -name "*.json" -not -path '*/.git/*' -not -path '*/node_modules/*' | wc -l)

echo "  Total files: $TOTAL_FILES"
echo "  Markdown (.md): $MD_FILES"
echo "  JavaScript (.js): $JS_FILES"
echo "  TypeScript (.ts): $TS_FILES"
echo "  Python (.py): $PY_FILES"
echo "  JSON (.json): $JSON_FILES"
echo ""

# Directory structure
echo -e "${BLUE}Top-Level Structure:${NC}"
ls -1 "$REPO_ROOT" | head -20 | while read -r item; do
    if [ -d "$REPO_ROOT/$item" ]; then
        COUNT=$(find "$REPO_ROOT/$item" -type f -not -path '*/.git/*' 2>/dev/null | wc -l)
        echo "  [dir]  $item/ ($COUNT files)"
    else
        SIZE=$(ls -lh "$REPO_ROOT/$item" 2>/dev/null | awk '{print $5}')
        echo "  [file] $item ($SIZE)"
    fi
done
echo ""

# Claude configuration
if [ -d "$REPO_ROOT/.claude" ]; then
    echo -e "${BLUE}Claude Configuration:${NC}"
    AGENTS=$(find "$REPO_ROOT/.claude/agents" -name "*.md" 2>/dev/null | wc -l)
    COMMANDS=$(find "$REPO_ROOT/.claude/commands" -name "*.md" 2>/dev/null | wc -l)
    HELPERS=$(find "$REPO_ROOT/.claude/helpers" -type f 2>/dev/null | wc -l)
    echo "  Agents: $AGENTS"
    echo "  Commands: $COMMANDS"
    echo "  Helpers: $HELPERS"

    if [ -f "$REPO_ROOT/.claude/settings.json" ]; then
        echo "  Settings: configured"
    fi
    echo ""
fi

# Recent activity
echo -e "${BLUE}Recent Activity (last 5 commits):${NC}"
git log --oneline -5 2>/dev/null | while read -r line; do
    echo "  $line"
done
echo ""

echo -e "${GREEN}Analysis complete.${NC}"
echo ""
echo "For deeper analysis, use:"
echo "  npx claude-flow github repo-analyze --repository <owner/repo> --deep"
