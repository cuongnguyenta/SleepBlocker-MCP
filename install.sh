#!/bin/bash

# Sleep Blocker MCP Server Installation Script
# This script sets up the MCP server for use with Claude Code and other MCP clients

set -e

echo "🚀 Sleep Blocker MCP Server Installation"
echo "========================================"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Function to print colored output
print_status() {
    echo -e "${GREEN}✓${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}⚠${NC} $1"
}

print_error() {
    echo -e "${RED}✗${NC} $1"
}

print_info() {
    echo -e "${BLUE}ℹ${NC} $1"
}

# Check if running on macOS
if [[ "$OSTYPE" != "darwin"* ]]; then
    print_error "This MCP server is designed for macOS only (uses caffeinate command)"
    exit 1
fi

print_status "Detected macOS system"

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null; then
    print_error "Python 3 is required but not installed"
    echo "Please install Python 3 from https://python.org or using Homebrew:"
    echo "  brew install python"
    exit 1
fi

PYTHON_VERSION=$(python3 --version 2>&1 | cut -d' ' -f2)
print_status "Found Python $PYTHON_VERSION"

# Check if caffeinate is available
if ! command -v caffeinate &> /dev/null; then
    print_error "caffeinate command not found"
    print_info "This should be available on all macOS systems. Please check your system."
    exit 1
fi

print_status "Found caffeinate command"

# Get installation directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
MCP_SERVER_PATH="$SCRIPT_DIR/mcp_server.py"

if [[ ! -f "$MCP_SERVER_PATH" ]]; then
    print_error "MCP server file not found at $MCP_SERVER_PATH"
    exit 1
fi

# Make server executable
chmod +x "$MCP_SERVER_PATH"
print_status "Made MCP server executable"

# Test the server
print_info "Testing MCP server..."
if echo '{"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {}}' | python3 "$MCP_SERVER_PATH" > /dev/null 2>&1; then
    print_status "MCP server test successful"
else
    print_error "MCP server test failed"
    exit 1
fi

echo ""
echo "🎉 Installation Complete!"
echo ""

# Provide setup instructions
echo "📋 Next Steps:"
echo "=============="
echo ""

# Claude Code setup
echo "1. ${BLUE}For Claude Code:${NC}"
echo "   Add this to your Claude Code MCP settings:"
echo ""
echo "   {"
echo "     \"mcpServers\": {"
echo "       \"sleep-blocker\": {"
echo "         \"command\": \"python3\","
echo "         \"args\": [\"$MCP_SERVER_PATH\"]"
echo "       }"
echo "     }"
echo "   }"
echo ""

# Generic MCP client setup
echo "2. ${BLUE}For other MCP clients:${NC}"
echo "   Use these connection details:"
echo "   - Command: python3"
echo "   - Args: [\"$MCP_SERVER_PATH\"]"
echo "   - Transport: stdio"
echo ""

# Usage examples
echo "3. ${BLUE}Available Tools:${NC}"
echo "   • start_sleep_prevention - Start preventing system sleep"
echo "   • stop_sleep_prevention - Stop active sleep prevention"
echo "   • get_sleep_status - Check current status"
echo "   • list_sleep_modes - Show available modes"
echo "   • set_duration_preset - Use preset durations"
echo ""

# Configuration file locations
echo "4. ${BLUE}Configuration Files:${NC}"
echo "   • Claude Code: ~/.config/claude-code/settings.json"
echo "   • Server Location: $MCP_SERVER_PATH"
echo ""

print_info "For detailed usage examples, see USER_GUIDE.md and EXAMPLES.md"
print_warning "Remember to restart your MCP client after adding the server configuration"

echo ""
echo "🔧 Quick Test:"
echo "You can test the server manually by running:"
echo "  echo '{\"jsonrpc\": \"2.0\", \"id\": 1, \"method\": \"tools/list\", \"params\": {}}' | python3 $MCP_SERVER_PATH"
echo ""

print_status "Setup complete! Enjoy using Sleep Blocker MCP Server!"