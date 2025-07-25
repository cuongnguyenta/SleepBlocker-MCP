# Contributing to Sleep Blocker MCP Server

We love your input! We want to make contributing to Sleep Blocker MCP Server as easy and transparent as possible, whether it's:

- Reporting a bug
- Discussing the current state of the code
- Submitting a fix
- Proposing new features
- Becoming a maintainer

## 🚀 Development Process

We use GitHub to host code, to track issues and feature requests, as well as accept pull requests.

## 📋 Pull Request Process

1. **Fork the repo** and create your branch from `main`
2. **Add tests** if you've added code that should be tested
3. **Update documentation** if you've changed APIs
4. **Ensure the test suite passes**
5. **Make sure your code follows** the existing style
6. **Issue the pull request**!

## 🐛 Bug Reports

We use GitHub issues to track public bugs. Report a bug by [opening a new issue](https://github.com/yourusername/SleepBlocker-MCP/issues).

**Great Bug Reports** tend to have:

- A quick summary and/or background
- Steps to reproduce
  - Be specific!
  - Give sample code if you can
- What you expected would happen
- What actually happens
- Notes (possibly including why you think this might be happening, or stuff you tried that didn't work)

## 💡 Feature Requests

We use GitHub issues to track feature requests as well. Create a feature request by [opening a new issue](https://github.com/yourusername/SleepBlocker-MCP/issues) with the "enhancement" label.

## 🎯 Development Setup

1. **Clone your fork:**
   ```bash
   git clone https://github.com/yourusername/SleepBlocker-MCP.git
   cd SleepBlocker-MCP
   ```

2. **Make the server executable:**
   ```bash
   chmod +x mcp_server.py
   ```

3. **Test the server:**
   ```bash
   echo '{"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {}}' | python3 mcp_server.py
   ```

## 🧪 Testing

### Manual Testing
```bash
# Test server initialization
echo '{"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {}}' | python3 mcp_server.py

# Test tools listing
echo '{"jsonrpc": "2.0", "id": 2, "method": "tools/list", "params": {}}' | python3 mcp_server.py

# Test tool execution
echo '{"jsonrpc": "2.0", "id": 3, "method": "tools/call", "params": {"name": "get_sleep_status", "arguments": {}}}' | python3 mcp_server.py
```

### Integration Testing
- Test with Claude Code
- Test with other MCP clients
- Test on different macOS versions
- Test with different Python versions (3.7+)

## 📝 Code Style

- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) for Python code
- Use meaningful variable and function names
- Add docstrings for all functions and classes
- Keep functions small and focused
- Handle errors gracefully with helpful error messages

### Code Examples

**Good:**
```python
async def start_sleep_prevention(mode: str = "idle", duration_minutes: Optional[int] = None) -> Dict[str, Any]:
    """Start preventing system sleep with specified mode and duration."""
    try:
        # Implementation here
        return {"success": True, "message": "Sleep prevention started"}
    except Exception as e:
        return {"success": False, "error": str(e)}
```

**Bad:**
```python
def start(m="idle", d=None):
    # No docstring, unclear parameters
    cmd = ["/usr/bin/caffeinate"] + get_args(m)
    # No error handling
```

## 🎨 Documentation Style

- Use clear, concise language
- Include practical examples
- Keep documentation up to date with code changes
- Use emoji consistently but sparingly
- Follow the existing documentation structure

## 🚦 Issue Labels

We use these labels to categorize issues:

- `bug` - Something isn't working
- `enhancement` - New feature or request
- `documentation` - Improvements or additions to documentation
- `good first issue` - Good for newcomers
- `help wanted` - Extra attention is needed
- `question` - Further information is requested
- `wontfix` - This will not be worked on

## 🎯 Areas for Contribution

### High Priority
- **Error handling improvements** - Better error messages and recovery
- **Performance optimization** - Reduce memory usage and startup time
- **Cross-platform support** - Adapt for other Unix systems (though macOS-focused)
- **Test coverage** - Add comprehensive test suite

### Medium Priority
- **Additional sleep modes** - New caffeinate options
- **Configuration options** - User-configurable defaults
- **Logging improvements** - Better debugging and monitoring
- **Documentation** - More examples and use cases

### Low Priority
- **UI improvements** - Better status displays
- **Integration examples** - More MCP client examples
- **Automation features** - Scheduled sleep prevention
- **Metrics collection** - Usage analytics (opt-in)

## 📜 Code of Conduct

### Our Pledge

We pledge to make participation in our project a harassment-free experience for everyone, regardless of age, body size, disability, ethnicity, sex characteristics, gender identity and expression, level of experience, education, socio-economic status, nationality, personal appearance, race, religion, or sexual identity and orientation.

### Our Standards

Examples of behavior that contributes to creating a positive environment include:

- Using welcoming and inclusive language
- Being respectful of differing viewpoints and experiences
- Gracefully accepting constructive criticism
- Focusing on what is best for the community
- Showing empathy towards other community members

### Enforcement

Instances of abusive, harassing, or otherwise unacceptable behavior may be reported by contacting the project team. All complaints will be reviewed and investigated promptly and fairly.

## 🏆 Recognition

Contributors will be recognized in:
- README.md contributors section
- Release notes for significant contributions
- Special thanks in documentation

## 📞 Getting Help

- **GitHub Issues** - For bugs and feature requests
- **GitHub Discussions** - For questions and community discussion
- **Documentation** - Check USER_GUIDE.md and TROUBLESHOOTING.md first

## 🚀 Release Process

1. **Version bump** - Update version in package.json
2. **Changelog** - Update CHANGELOG.md with changes
3. **Testing** - Ensure all tests pass
4. **Tag** - Create git tag with version
5. **Release** - Create GitHub release with binaries
6. **Announce** - Update relevant communities

## 🎉 First Time Contributors

Welcome! Here are some good ways to get started:

1. **Browse issues** labeled "good first issue"
2. **Improve documentation** - Always appreciated!
3. **Fix typos** - Small but helpful contributions
4. **Add examples** - More usage scenarios in EXAMPLES.md
5. **Test on different systems** - Help verify compatibility

## 📋 Commit Message Format

Use clear, descriptive commit messages:

```
feat: add support for custom duration presets
fix: resolve process cleanup issue on server shutdown
docs: update installation instructions for Python 3.9
test: add integration tests for sleep mode switching
refactor: improve error handling in caffeinate service
```

Prefixes:
- `feat:` - New features
- `fix:` - Bug fixes
- `docs:` - Documentation changes
- `test:` - Test additions or changes
- `refactor:` - Code refactoring
- `style:` - Code style changes
- `chore:` - Maintenance tasks

Thank you for contributing to Sleep Blocker MCP Server! 🎉