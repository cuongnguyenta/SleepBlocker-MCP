# Changelog

All notable changes to the Sleep Blocker MCP Server will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Initial planning for automated testing framework
- Consideration for additional MCP client integrations

### Changed
- Nothing yet

### Deprecated
- Nothing yet

### Removed
- Nothing yet

### Fixed
- Nothing yet

### Security
- Nothing yet

## [1.0.0] - 2025-01-25

### 🎉 Initial Release

This is the first public release of Sleep Blocker MCP Server!

### Added
- **Core MCP Server Implementation**
  - Full Model Context Protocol v2024-11-05 compatibility
  - JSON-RPC communication over stdio transport
  - Proper server initialization and capability reporting

- **Sleep Prevention Tools**
  - `start_sleep_prevention` - Start preventing system sleep with mode and duration
  - `stop_sleep_prevention` - Stop active sleep prevention
  - `get_sleep_status` - Check current status and remaining time
  - `list_sleep_modes` - Show all available prevention modes
  - `set_duration_preset` - Use preset durations (30min, 1hr, 2hr, 4hr, indefinite)

- **Sleep Prevention Modes**
  - 🖥️ Display mode - Keep screen on, allow system sleep
  - 💤 Idle mode - Keep system awake, allow display sleep (default)
  - 💾 Disk mode - Keep hard drives spinning
  - 🔌 AC Power mode - Only prevent sleep when plugged in
  - 🚫 All mode - Prevent all sleep (display + system + disk)

- **Duration Management**
  - Custom duration support (in minutes)
  - Preset duration options (30min, 1hr, 2hr, 4hr)
  - Indefinite prevention support
  - Real-time remaining time calculation

- **Process Management**
  - Automatic process cleanup on server shutdown
  - Signal handling for graceful termination (SIGTERM, SIGINT)
  - Process validation and zombie prevention
  - Safe process group management

- **Error Handling**
  - Comprehensive error catching and reporting
  - Graceful degradation on failures
  - User-friendly error messages with recovery suggestions
  - Input validation on all parameters

- **Installation & Setup**
  - Automated installation script (`install.sh`)
  - System requirements validation
  - Python and macOS compatibility checking
  - MCP client configuration guidance

### Documentation
- **Complete Documentation Suite**
  - `README.md` - Main project documentation with quick start
  - `USER_GUIDE.md` - Comprehensive setup and usage guide
  - `EXAMPLES.md` - Real-world usage scenarios and examples
  - `TROUBLESHOOTING.md` - Detailed problem-solving guide
  - `README_MCP.md` - Technical MCP implementation details
  - `DISTRIBUTION.md` - Packaging and distribution guidance
  - `CONTRIBUTING.md` - Contribution guidelines and development setup

### AI Assistant Compatibility
- **Claude Code** - Full integration with configuration examples
- **Cursor** - Compatible with MCP stdio transport
- **Continue** - Supports standard MCP protocol
- **Windsurf** - Works with MCP server configuration
- **Universal MCP Support** - Compatible with any MCP-compatible client

### Security & Privacy
- **100% Local Operation** - No network connections or data sharing
- **Standard System Tools** - Uses only macOS built-in `caffeinate` command
- **Process Safety** - Proper cleanup and termination handling
- **No Special Permissions** - Runs with standard user privileges

### Platform Support
- **macOS** - Primary platform with full `caffeinate` support
- **Python 3.7+** - Broad Python version compatibility
- **No External Dependencies** - Uses only Python standard library

### Performance
- **Lightweight** - Minimal memory footprint and CPU usage
- **Fast Startup** - Quick server initialization (< 1 second)
- **Efficient Communication** - Optimized JSON-RPC message handling
- **Resource Cleanup** - Automatic process and memory management

### Developer Experience
- **Natural Language Interface** - AI assistants understand conversational commands
- **Rich Tool Schemas** - Detailed parameter validation and documentation
- **Debug Support** - Optional debug mode with detailed logging
- **Easy Testing** - Simple command-line testing interface

### Quality Assurance
- **Manual Testing** - Comprehensive testing across different scenarios
- **Error Recovery** - Robust handling of edge cases and failures
- **Documentation Quality** - Professional-grade documentation with examples
- **Code Quality** - Clean, well-commented Python code following PEP 8

---

## Version History

- **v1.0.0** (2025-01-25) - Initial public release with full MCP compatibility
- **v0.1.0** (Development) - Internal development and testing phase

## Upgrade Notes

### From Development to v1.0.0
This is the first public release. No upgrade path needed.

## Breaking Changes

### v1.0.0
- No breaking changes (initial release)

## Migration Guide

### New Installation
Follow the [Quick Start guide](README.md#quick-start) in the README.

## Contributors

Thank you to all contributors who made this release possible:

- **Core Development** - Initial MCP server implementation and documentation
- **Testing** - Cross-platform compatibility and integration testing
- **Documentation** - Comprehensive user guides and examples

## Roadmap

Looking ahead to future releases:

### v1.1.0 (Planned)
- Enhanced error reporting with detailed diagnostics
- Additional sleep mode options
- Performance optimizations
- Automated testing framework

### v1.2.0 (Planned)
- Configuration file support
- Custom preset management
- Extended logging capabilities
- Additional MCP client examples

### v2.0.0 (Future)
- Possible HTTP transport support
- Advanced scheduling features
- Plugin architecture
- Cross-platform compatibility (Linux, Windows WSL)

---

For more information about any release, please check the [GitHub Releases](https://github.com/yourusername/SleepBlocker-MCP/releases) page.