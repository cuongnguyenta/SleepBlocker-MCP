# Sleep Blocker MCP Server

Model Context Protocol (MCP) server for controlling macOS sleep prevention using the `caffeinate` command.

## Overview

This MCP server provides tools to prevent system sleep, manage sleep prevention modes, and monitor active sleep prevention sessions. It integrates with your Sleep Blocker app to provide AI assistants access to sleep management functionality.

## Installation

1. Ensure Python 3.7+ is installed
2. Make the server executable:
   ```bash
   chmod +x mcp_server.py
   ```

## MCP Tools

### `start_sleep_prevention`
Start preventing system sleep with specified mode and duration.

**Parameters:**
- `mode` (string, optional): Sleep prevention mode
  - `"display"` - Keep screen on while allowing system to sleep  
  - `"idle"` - Keep system awake but allow display to sleep (default)
  - `"disk"` - Keep hard drives spinning
  - `"ac"` - Only when connected to power adapter
  - `"all"` - Keep everything awake (display, system, disk)
- `duration_minutes` (integer, optional): Duration in minutes. Omit for indefinite.

**Example:**
```json
{
  "name": "start_sleep_prevention",
  "arguments": {
    "mode": "idle",
    "duration_minutes": 60
  }
}
```

### `stop_sleep_prevention`
Stop active sleep prevention.

**Parameters:** None

### `get_sleep_status`
Get current sleep prevention status and remaining time.

**Parameters:** None

**Returns:**
- Active status
- Process ID (if running)
- Elapsed time
- Remaining time (if duration was set)
- Start time

### `list_sleep_modes`
List all available sleep prevention modes with descriptions.

**Parameters:** None

**Returns:**
- Array of available modes with IDs, names, and descriptions
- Default mode

### `set_duration_preset`
Set duration using preset values.

**Parameters:**
- `preset` (string, required): Duration preset
  - `"30min"` - 30 minutes
  - `"1hr"` - 1 hour  
  - `"2hr"` - 2 hours
  - `"4hr"` - 4 hours
  - `"indefinite"` - No time limit

## Configuration

### Claude Code Integration

Add to your Claude Code MCP settings:

```json
{
  "mcpServers": {
    "sleep-blocker": {
      "command": "python3",
      "args": ["/path/to/CaffeinateManager/mcp_server.py"]
    }
  }
}
```

### Other MCP Clients

For other MCP clients, use the stdio transport with:
- **Command:** `python3`
- **Args:** `["mcp_server.py"]`
- **Working Directory:** Path to your CaffeinateManager directory

## Usage Examples

### Start sleep prevention for 2 hours
```json
{
  "method": "tools/call",
  "params": {
    "name": "start_sleep_prevention", 
    "arguments": {
      "mode": "idle",
      "duration_minutes": 120
    }
  }
}
```

### Check current status
```json
{
  "method": "tools/call",
  "params": {
    "name": "get_sleep_status",
    "arguments": {}
  }
}
```

### Stop sleep prevention
```json
{
  "method": "tools/call", 
  "params": {
    "name": "stop_sleep_prevention",
    "arguments": {}
  }
}
```

## Safety Features

- Automatic cleanup of processes on server shutdown
- Signal handling for graceful termination
- Process validation to prevent zombie processes
- Error handling for invalid commands

## Requirements

- macOS (uses `/usr/bin/caffeinate`)
- Python 3.7+
- No additional Python dependencies required

## Troubleshooting

### Permission Issues
If you get permission errors, ensure the server has access to execute `/usr/bin/caffeinate`:

```bash
which caffeinate
# Should return: /usr/bin/caffeinate
```

### Process Not Starting
Check that Python 3 is available:

```bash
python3 --version
```

### Debug Mode
Run the server directly to see debug output:

```bash
python3 mcp_server.py
```

Then send MCP messages via stdin to test functionality.