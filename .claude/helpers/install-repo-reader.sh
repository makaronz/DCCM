#!/bin/bash
# Install Repo Reader - Deep repository analysis with AI insights
# Part of DCCM Claude Flow integration

set -e

echo "============================================"
echo "      Repo Reader Installation"
echo "============================================"
echo ""

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

print_status() {
    echo -e "${GREEN}[OK]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARN]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

print_info() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

# Check prerequisites
echo "Checking prerequisites..."
echo ""

# Check Node.js
if command -v node &> /dev/null; then
    NODE_VERSION=$(node -v)
    print_status "Node.js installed: $NODE_VERSION"
else
    print_error "Node.js not found. Please install Node.js 18+"
    exit 1
fi

# Check npm
if command -v npm &> /dev/null; then
    NPM_VERSION=$(npm -v)
    print_status "npm installed: v$NPM_VERSION"
else
    print_error "npm not found"
    exit 1
fi

# Check Claude CLI
if command -v claude &> /dev/null; then
    print_status "Claude Code CLI found"
else
    print_warning "Claude Code CLI not found - some features may be limited"
fi

# Check gh CLI (optional but recommended)
if command -v gh &> /dev/null; then
    print_status "GitHub CLI (gh) found"
else
    print_warning "GitHub CLI (gh) not found - GitHub integration will be limited"
    print_info "Install with: brew install gh (macOS) or sudo apt install gh (Linux)"
fi

echo ""
echo "Installing dependencies..."
echo ""

# Install/update claude-flow
print_info "Installing claude-flow@alpha..."
npm install -g claude-flow@alpha 2>/dev/null || npx claude-flow@alpha --version

echo ""
echo "Setting up MCP servers..."
echo ""

# Setup MCP server if claude CLI is available
if command -v claude &> /dev/null; then
    print_info "Adding claude-flow MCP server..."
    claude mcp add claude-flow npx claude-flow@alpha mcp start 2>/dev/null || print_warning "MCP server may already be configured"

    print_info "Adding ruv-swarm MCP server (optional)..."
    claude mcp add ruv-swarm npx ruv-swarm mcp start 2>/dev/null || print_warning "ruv-swarm MCP may already be configured"
fi

echo ""
echo "Verifying installation..."
echo ""

# Test claude-flow
if npx claude-flow@alpha --version &> /dev/null; then
    VERSION=$(npx claude-flow@alpha --version 2>/dev/null || echo "installed")
    print_status "claude-flow is working: $VERSION"
else
    print_warning "claude-flow verification skipped"
fi

echo ""
echo "============================================"
echo "      Installation Complete!"
echo "============================================"
echo ""
echo "Repo Reader Commands:"
echo ""
echo "  Basic Analysis:"
echo "    npx claude-flow github repo-analyze --repository owner/repo"
echo ""
echo "  Deep Analysis:"
echo "    npx claude-flow github repo-analyze --repository owner/repo --deep"
echo ""
echo "  Specific Areas:"
echo "    npx claude-flow github repo-analyze --repository owner/repo --include issues,prs,code"
echo ""
echo "  Current Repository:"
echo "    ./.claude/helpers/repo-reader.sh"
echo ""
echo "For more information, see:"
echo "  .claude/commands/github/repo-analyze.md"
echo "  .claude/agents/github/repo-architect.md"
echo ""
