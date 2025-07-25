# Sleep Blocker MCP Server - Troubleshooting Guide

This guide helps you diagnose and fix common issues with the Sleep Blocker MCP Server.

## 🚨 Quick Diagnostics

### Step 1: System Requirements Check
Run these commands to verify your system:

```bash
# Check macOS version
sw_vers

# Check Python version (should be 3.7+)
python3 --version

# Check if caffeinate exists
which caffeinate

# Test caffeinate command
caffeinate -d -t 1 &
sleep 2
killall caffeinate
```

### Step 2: Server Test
```bash
# Navigate to your server directory
cd /path/to/your/CaffeinateManager

# Test server initialization
echo '{"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {}}' | python3 mcp_server.py

# Test tools listing
echo '{"jsonrpc": "2.0", "id": 2, "method": "tools/list", "params": {}}' | python3 mcp_server.py
```

## 🔧 Common Issues & Solutions

### Issue 1: "Command not found: python3"

**Symptoms:**
- Installation script fails
- Cannot run server manually
- Error: `python3: command not found`

**Solutions:**

1. **Install Python 3:**
   ```bash
   # Using Homebrew
   brew install python
   
   # Using macOS installer
   # Download from https://python.org
   ```

2. **Check Python path:**
   ```bash
   which python3
   # Should return: /usr/bin/python3 or /usr/local/bin/python3
   ```

3. **Update PATH if needed:**
   ```bash
   export PATH="/usr/local/bin:$PATH"
   ```

---

### Issue 2: "Permission denied" when running server

**Symptoms:**
- Server file exists but won't execute
- Error: `Permission denied: ./mcp_server.py`

**Solutions:**

1. **Make server executable:**
   ```bash
   chmod +x mcp_server.py
   ```

2. **Check file permissions:**
   ```bash
   ls -la mcp_server.py
   # Should show: -rwxr-xr-x
   ```

3. **Run with python explicitly:**
   ```bash
   python3 mcp_server.py
   ```

---

### Issue 3: "caffeinate: command not found"

**Symptoms:**
- Server starts but tools fail
- Error about caffeinate not being available

**Solutions:**

1. **Verify you're on macOS:**
   ```bash
   uname -s
   # Should return: Darwin
   ```

2. **Check caffeinate location:**
   ```bash
   ls -la /usr/bin/caffeinate
   ```

3. **This issue typically means you're not on macOS** - the server only works on Mac systems.

---

### Issue 4: MCP Client Can't Connect to Server

**Symptoms:**
- Client shows "Server not found" or similar error
- Tools don't appear in client interface
- Connection timeouts

**Solutions:**

1. **Verify server path in client config:**
   ```json
   {
     "mcpServers": {
       "sleep-blocker": {
         "command": "python3",
         "args": ["/FULL/PATH/TO/mcp_server.py"]
       }
     }
   }
   ```

2. **Use absolute paths:**
   ```bash
   # Find absolute path
   realpath mcp_server.py
   ```

3. **Test server manually:**
   ```bash
   python3 mcp_server.py
   # Type: {"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {}}
   # Should get JSON response
   ```

4. **Restart your MCP client** after configuration changes.

---

### Issue 5: Sleep Prevention Not Working

**Symptoms:**
- Server responds but Mac still sleeps
- No error messages but sleep prevention ineffective

**Solutions:**

1. **Check macOS Energy Saver settings:**
   - System Preferences → Energy Saver
   - Verify sleep settings allow prevention

2. **Test caffeinate directly:**
   ```bash
   # Test 10-second prevention
   caffeinate -d -t 10
   ```

3. **Check for conflicting apps:**
   - Other sleep prevention software
   - System security software
   - Parental controls

4. **Verify server process:**
   ```bash
   # Check if caffeinate is running
   ps aux | grep caffeinate
   ```

---

### Issue 6: Server Starts But Tools Don't Work

**Symptoms:**
- Server initializes successfully
- Tool calls return errors or timeouts

**Solutions:**

1. **Check tool call format:**
   ```json
   {
     "jsonrpc": "2.0",
     "id": 3,
     "method": "tools/call",
     "params": {
       "name": "get_sleep_status",
       "arguments": {}
     }
   }
   ```

2. **Test each tool individually:**
   ```bash
   # Test status tool
   echo '{"jsonrpc": "2.0", "id": 3, "method": "tools/call", "params": {"name": "get_sleep_status", "arguments": {}}}' | python3 mcp_server.py
   ```

3. **Enable debug mode:**
   ```bash
   DEBUG=1 python3 mcp_server.py
   ```

---

### Issue 7: Installation Script Fails

**Symptoms:**
- `./install.sh` doesn't work
- Script reports errors during setup

**Solutions:**

1. **Make installer executable:**
   ```bash
   chmod +x install.sh
   ```

2. **Run with bash explicitly:**
   ```bash
   bash install.sh
   ```

3. **Check script output for specific errors:**
   - Look for red ✗ markers
   - Follow suggested solutions in output

4. **Manual installation:**
   - Skip automated installer
   - Follow manual steps in USER_GUIDE.md

---

### Issue 8: Server Process Doesn't Clean Up

**Symptoms:**
- Multiple caffeinate processes running
- Server doesn't stop properly
- System resources consumed

**Solutions:**

1. **Kill zombie processes:**
   ```bash
   # Find caffeinate processes
   ps aux | grep caffeinate
   
   # Kill specific process
   kill [PID]
   
   # Kill all caffeinate processes
   killall caffeinate
   ```

2. **Restart the server:**
   ```bash
   # Stop server with Ctrl+C
   # Restart server
   python3 mcp_server.py
   ```

3. **Check for signal handling:**
   - Server should handle SIGTERM and SIGINT
   - Use proper shutdown methods

## 🔍 Debug Mode

Enable detailed logging:

```bash
DEBUG=1 python3 mcp_server.py
```

This will show:
- Incoming JSON-RPC messages
- Tool execution details
- Process management information
- Error stack traces

## 📊 Log Analysis

### Normal Operation Logs
```
✓ MCP server initialized
✓ Tool call: start_sleep_prevention
✓ Process started: PID 12345
✓ Sleep prevention active
```

### Error Logs to Watch For
```
✗ Failed to start caffeinate process
✗ Permission denied accessing /usr/bin/caffeinate
✗ Invalid JSON-RPC message format
✗ Tool call timeout
```

## 🔧 Advanced Diagnostics

### Process Monitoring
```bash
# Monitor active processes
watch "ps aux | grep -E '(python|caffeinate)'"

# Check system resources
top -pid `pgrep python3`
```

### Network Diagnostics (for HTTP transport)
```bash
# Check if server binds to port (if using HTTP)
netstat -an | grep :8080

# Test HTTP endpoint (if configured)
curl -X POST http://localhost:8080/mcp \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {}}'
```

### File System Permissions
```bash
# Check server file permissions
ls -la mcp_server.py

# Check directory permissions
ls -la .

# Verify Python can read the file
python3 -c "import os; print(os.access('mcp_server.py', os.R_OK))"
```

## 🆘 When All Else Fails

### Complete Reset
1. **Kill all related processes:**
   ```bash
   killall python3
   killall caffeinate
   ```

2. **Remove and reinstall:**
   ```bash
   rm mcp_server.py
   # Re-download or copy fresh version
   chmod +x mcp_server.py
   ```

3. **Reset MCP client configuration:**
   - Remove server from client settings
   - Restart client
   - Re-add server configuration

### System Reboot
Sometimes a system reboot resolves mysterious issues with:
- Process management
- File permissions
- System sleep settings

### Contact Support Checklist
If you need help, gather this information:

1. **System Information:**
   ```bash
   sw_vers
   python3 --version
   which python3
   which caffeinate
   ```

2. **Error Messages:**
   - Exact error text
   - When error occurs
   - Steps to reproduce

3. **Configuration:**
   - MCP client type and version
   - Server file location
   - Client configuration JSON

4. **Debug Output:**
   ```bash
   DEBUG=1 python3 mcp_server.py 2>&1 | tee debug.log
   ```

## 🎯 Prevention Tips

### Best Practices
1. **Use absolute paths** in all configurations
2. **Test server manually** before client integration
3. **Keep Python updated** to latest stable version
4. **Restart clients** after configuration changes
5. **Monitor system resources** during extended use

### Regular Maintenance
1. **Check for zombie processes** weekly
2. **Verify server functionality** monthly
3. **Update documentation** as needed
4. **Backup working configurations**

### Safe Operation
1. **Set reasonable durations** to prevent battery drain
2. **Monitor system temperature** during extended use
3. **Use appropriate sleep modes** for your workflow
4. **Have fallback sleep settings** in System Preferences

Remember: The Sleep Blocker MCP Server is designed to be simple and reliable. Most issues stem from basic configuration or system requirement problems that can be quickly resolved with these troubleshooting steps.