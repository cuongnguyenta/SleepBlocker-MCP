# 🚫💤 Sleep Blocker MCP Server

> **Control your Mac's sleep settings through AI assistants using the Model Context Protocol (MCP)**

[![macOS](https://img.shields.io/badge/macOS-Required-blue.svg)]()
[![Python](https://img.shields.io/badge/Python-3.7+-green.svg)]()
[![MCP](https://img.shields.io/badge/MCP-Compatible-orange.svg)]()
[![License](https://img.shields.io/badge/License-MIT-lightgrey.svg)]()

Sleep Blocker MCP Server enables AI assistants like Claude Code to prevent your Mac from sleeping using natural language commands. Built on the Model Context Protocol, it provides seamless integration with various AI development tools.

## ✨ Features

- 🎯 **Natural Language Control** - *"Keep my Mac awake for 2 hours"*
- 🔧 **Multiple Sleep Modes** - Display, idle, disk, AC power, and all
- ⏰ **Flexible Duration** - Preset durations or custom times
- 📊 **Status Monitoring** - Check active prevention and remaining time
- 🛡️ **Safe Operation** - Automatic cleanup and error handling
- 🔌 **Universal MCP Compatibility** - Works with Claude Code, Cursor, and more

## 🚀 Quick Start

### 1-Minute Setup

```bash
# Clone this repository
git clone https://github.com/yourusername/SleepBlocker-MCP.git
cd SleepBlocker-MCP

# Run the installer
./install.sh

# Follow the setup instructions
```

### Manual Setup

```bash
# Make server executable
chmod +x mcp_server.py

# Test the server
echo '{"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {}}' | python3 mcp_server.py
```

### Configure Your AI Assistant

**For Claude Code**, add to your MCP settings:
```json
{
  "mcpServers": {
    "sleep-blocker": {
      "command": "python3",
      "args": ["/path/to/SleepBlocker-MCP/mcp_server.py"]
    }
  }
}
```

## 💬 Usage Examples

Once configured, you can use natural language with your AI assistant:

- *"Prevent my Mac from sleeping for the next hour"*
- *"Keep my screen on during this presentation"*
- *"Stop sleep prevention"*
- *"What's my current sleep status?"*
- *"Show me all available sleep modes"*

## 🛠️ Available Tools

| Tool | Description | Example |
|------|-------------|---------|
| `start_sleep_prevention` | Start preventing sleep with mode and duration | *"Keep system awake for 2 hours"* |
| `stop_sleep_prevention` | Stop active sleep prevention | *"Allow my Mac to sleep again"* |
| `get_sleep_status` | Check current status and remaining time | *"How much time is left?"* |
| `list_sleep_modes` | Show all available prevention modes | *"What sleep modes are available?"* |
| `set_duration_preset` | Use preset durations (30min, 1hr, 2hr, 4hr) | *"Set to 1 hour preset"* |

## 🎯 Sleep Prevention Modes

- **🖥️ Display** - Keep screen on, allow system sleep
- **💤 Idle** - Keep system awake, allow display sleep (default)
- **💾 Disk** - Keep hard drives spinning
- **🔌 AC Power** - Only prevent sleep when plugged in
- **🚫 All** - Prevent all sleep (display + system + disk)

## 📋 Requirements

- **macOS** (any version with `caffeinate` command)
- **Python 3.7+**
- **MCP-compatible client** (Claude Code, Cursor, etc.)

## 📚 Documentation

- **[📖 User Guide](USER_GUIDE.md)** - Complete setup and usage guide
- **[💡 Examples](EXAMPLES.md)** - Real-world usage scenarios
- **[🔧 Troubleshooting](TROUBLESHOOTING.md)** - Common issues and solutions
- **[⚙️ Technical Details](README_MCP.md)** - MCP implementation details
- **[📦 Distribution Guide](DISTRIBUTION.md)** - Packaging and distribution

## 🎪 Real-World Use Cases

### 👨‍💼 Professional
- **Presentations** - Keep screen on during demos
- **Long Downloads** - Prevent sleep during file transfers
- **Video Calls** - Maintain display during meetings
- **Development** - Keep system active during builds

### 🎵 Creative
- **Music Production** - Keep drives spinning for sample libraries
- **Video Editing** - Prevent interruptions during renders
- **Live Streaming** - Maintain system during broadcasts

### 🎮 Personal
- **Gaming** - Extended gaming sessions
- **Movie Nights** - Keep display on for movies
- **File Organization** - System stays awake during large operations

## 🔒 Security & Privacy

- ✅ **100% Local** - No network connections or data sharing
- ✅ **Standard Tools** - Uses only macOS built-in `caffeinate` command
- ✅ **Process Safety** - Automatic cleanup and proper termination
- ✅ **No Permissions** - No special system permissions required

## 🎯 Quick Test

After installation, test with your AI assistant:

1. *"What sleep prevention modes are available?"*
2. *"Start sleep prevention for 5 minutes"*
3. *"Check my sleep status"*
4. *"Stop sleep prevention"*

## 🆘 Need Help?

1. **Installation Issues**: Run `./install.sh` and follow the colored output
2. **Connection Problems**: Check [Troubleshooting Guide](TROUBLESHOOTING.md)
3. **Usage Questions**: See [Examples](EXAMPLES.md) for inspiration
4. **Technical Details**: Review [MCP Documentation](README_MCP.md)

## 🎉 Compatible AI Assistants

- **Claude Code** ✅
- **Cursor** ✅
- **Claude Desktop** ✅
- **Windsurf** ✅
- **Any MCP-compatible client** ✅

## 📦 What's Included

```
SleepBlocker-MCP/
├── mcp_server.py          # Main MCP server
├── install.sh             # Automated installer
├── package.json           # MCP configuration
├── README.md              # This file
├── USER_GUIDE.md          # Complete user guide
├── EXAMPLES.md            # Usage examples
├── TROUBLESHOOTING.md     # Problem solving
├── README_MCP.md          # Technical documentation
├── DISTRIBUTION.md        # Distribution guide
└── LICENSE                # MIT License
```

## 🚀 Getting Started in 30 Seconds

```bash
# 1. Clone and setup
git clone https://github.com/yourusername/SleepBlocker-MCP.git
cd SleepBlocker-MCP
./install.sh

# 2. Add to your AI assistant's MCP config
# (Path shown by installer)

# 3. Restart your AI assistant

# 4. Try it out!
# Say: "Keep my Mac awake for 30 minutes"
```

## 🎊 Why Sleep Blocker MCP?

- **🗣️ Natural Language** - No complex commands to remember
- **🔧 Flexible Control** - Multiple modes for different needs  
- **⚡ Instant Setup** - Working in minutes, not hours
- **🛡️ Rock Solid** - Proper error handling and cleanup
- **📖 Great Docs** - Clear guides for every skill level
- **🔄 Universal** - Works with any MCP-compatible AI assistant

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built with the [Model Context Protocol](https://modelcontextprotocol.io/)
- Uses macOS built-in `caffeinate` command
- Inspired by the need for AI-controlled system management

---

**Ready to take control of your Mac's sleep settings with AI?** 

⭐ **[Start with the installation script →](./install.sh)**

Made with ❤️ for the MCP community. Questions? Check the [User Guide](USER_GUIDE.md) or [Troubleshooting](TROUBLESHOOTING.md) docs!
