# Sleep Blocker MCP Server - User Guide

Welcome to Sleep Blocker MCP Server! This guide will help you install, configure, and use the MCP server to control your Mac's sleep settings through AI assistants.

## 🎯 What is This?

Sleep Blocker MCP Server allows AI assistants (like Claude Code) to:
- Prevent your Mac from sleeping
- Control different sleep prevention modes
- Set timers for automatic sleep prevention
- Monitor active sleep prevention status

## 📋 Requirements

- **macOS** (any version with `caffeinate` command)
- **Python 3.7 or later**
- **MCP-compatible client** (Claude Code, Cursor, etc.)

## 🚀 Quick Installation

### Option 1: Automated Installation (Recommended)

1. **Download or clone** this repository
2. **Open Terminal** and navigate to the project folder
3. **Run the installer**:
   ```bash
   ./install.sh
   ```
4. **Follow the on-screen instructions**

### Option 2: Manual Installation

1. **Verify Python 3**:
   ```bash
   python3 --version
   ```

2. **Make the server executable**:
   ```bash
   chmod +x mcp_server.py
   ```

3. **Test the server**:
   ```bash
   echo '{"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {}}' | python3 mcp_server.py
   ```

## ⚙️ Configuration

### Claude Code Setup

1. **Find your Claude Code settings**:
   - macOS: `~/.config/claude-code/settings.json`

2. **Add the MCP server configuration**:
   ```json
   {
     "mcpServers": {
       "sleep-blocker": {
         "command": "python3",
         "args": ["/path/to/your/CaffeinateManager/mcp_server.py"]
       }
     }
   }
   ```

3. **Replace `/path/to/your/`** with your actual path

4. **Restart Claude Code**

### Other MCP Clients

For other MCP-compatible clients, use these settings:
- **Command**: `python3`
- **Arguments**: `["/path/to/mcp_server.py"]`
- **Transport**: `stdio`

## 🛠️ Available Tools

### 1. `start_sleep_prevention`
Prevent your Mac from sleeping.

**Parameters:**
- `mode` (optional): Sleep prevention mode
  - `"idle"` - Keep system awake, allow display sleep (default)
  - `"display"` - Keep screen on, allow system sleep
  - `"disk"` - Keep hard drives spinning
  - `"ac"` - Only when on AC power
  - `"all"` - Prevent all sleep
- `duration_minutes` (optional): How long to prevent sleep

**Examples:**
- "Start sleep prevention for 2 hours"
- "Prevent display sleep for 30 minutes"
- "Keep system awake indefinitely"

### 2. `stop_sleep_prevention`
Stop active sleep prevention.

**Examples:**
- "Stop sleep prevention"
- "Allow my Mac to sleep again"

### 3. `get_sleep_status`
Check current sleep prevention status.

**Examples:**
- "What's the current sleep status?"
- "How much time is left on sleep prevention?"

### 4. `list_sleep_modes`
Show all available sleep prevention modes.

**Examples:**
- "What sleep modes are available?"
- "Show me all sleep prevention options"

### 5. `set_duration_preset`
Use preset time durations.

**Available presets:**
- `"30min"` - 30 minutes
- `"1hr"` - 1 hour
- `"2hr"` - 2 hours
- `"4hr"` - 4 hours
- `"indefinite"` - No time limit

## 💬 Usage Examples

Here are natural language examples you can use with your AI assistant:

### Basic Usage
- *"Prevent my Mac from sleeping for the next hour"*
- *"Keep my screen on for 30 minutes"*
- *"Stop preventing sleep"*
- *"What's my current sleep prevention status?"*

### Advanced Usage
- *"Start display sleep prevention for 2 hours"*
- *"Keep my hard drives spinning indefinitely"*
- *"Only prevent sleep when I'm on AC power for 4 hours"*
- *"Show me all available sleep modes"*

### Workflow Examples
- *"I'm giving a presentation - keep my screen on for 1 hour"*
- *"I'm downloading a large file - prevent all sleep for 3 hours"*
- *"I'm done working - allow my Mac to sleep normally"*

## 🔧 Troubleshooting

### Server Won't Start
1. **Check Python version**:
   ```bash
   python3 --version
   ```
   Should be 3.7 or later.

2. **Verify caffeinate exists**:
   ```bash
   which caffeinate
   ```
   Should return `/usr/bin/caffeinate`.

3. **Test server manually**:
   ```bash
   python3 mcp_server.py
   ```
   Then type: `{"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {}}`

### MCP Client Not Connecting
1. **Check file path** in your MCP configuration
2. **Restart your MCP client** after configuration changes
3. **Verify Python path**:
   ```bash
   which python3
   ```

### Permission Issues
1. **Make server executable**:
   ```bash
   chmod +x mcp_server.py
   ```

2. **Check file permissions**:
   ```bash
   ls -la mcp_server.py
   ```

### Sleep Prevention Not Working
1. **Check macOS sleep settings** in System Preferences
2. **Verify caffeinate permissions** - no special permissions needed
3. **Check if other sleep prevention apps** are running

## 🔒 Security & Privacy

- **Local operation**: All processing happens locally on your Mac
- **No network access**: The server doesn't connect to the internet
- **Standard system tools**: Uses only macOS's built-in `caffeinate` command
- **Process cleanup**: Automatically cleans up processes when stopped

## 📚 Advanced Configuration

### Custom Installation Location
You can place the MCP server anywhere on your system. Just update the path in your MCP client configuration.

### Environment Variables
The server respects these environment variables:
- `PYTHON_PATH` - Custom Python interpreter path
- `DEBUG` - Set to `1` for debug output

### Multiple Clients
The same server can be used by multiple MCP clients simultaneously. Each client gets its own process management.

## 🆘 Getting Help

### Debug Information
To get debug information:
```bash
DEBUG=1 python3 mcp_server.py
```

### Common Issues
1. **"Command not found"** - Python 3 not installed or not in PATH
2. **"Permission denied"** - Run `chmod +x mcp_server.py`
3. **"caffeinate not found"** - You're not on macOS
4. **"Server not responding"** - Check MCP client configuration

### Support
- Check the `README_MCP.md` for technical details
- Review the installation script output for specific error messages
- Ensure all requirements are met

## 🎉 Tips for Best Experience

1. **Test first**: Use simple commands like "check sleep status" to verify everything works
2. **Use natural language**: The AI understands conversational requests
3. **Set reasonable durations**: Very long durations might affect battery life
4. **Remember to stop**: Sleep prevention continues until explicitly stopped
5. **Check status regularly**: Use status checks to monitor active prevention

Happy sleep blocking! 😴⚡