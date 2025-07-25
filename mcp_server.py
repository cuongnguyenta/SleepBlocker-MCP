#!/usr/bin/env python3
"""
Sleep Blocker MCP Server

Provides MCP tools for controlling system sleep prevention using macOS caffeinate command.
"""

import asyncio
import json
import subprocess
import sys
from typing import Dict, List, Optional, Any
from datetime import datetime, timedelta
import signal
import os

# Global state
active_process: Optional[subprocess.Popen] = None
start_time: Optional[datetime] = None
duration_seconds: Optional[int] = None

class SleepMode:
    """Sleep prevention modes matching Swift app"""
    DISPLAY = "display"
    IDLE = "idle" 
    DISK = "disk"
    AC_POWER = "ac"
    ALL = "all"
    
    @classmethod
    def get_arguments(cls, mode: str) -> List[str]:
        """Get caffeinate arguments for sleep mode"""
        mode_args = {
            cls.DISPLAY: ["-d"],
            cls.IDLE: ["-i"],
            cls.DISK: ["-m"],
            cls.AC_POWER: ["-s"],
            cls.ALL: ["-d", "-i", "-m"]
        }
        return mode_args.get(mode, ["-i"])
    
    @classmethod
    def get_description(cls, mode: str) -> str:
        """Get human-readable description of mode"""
        descriptions = {
            cls.DISPLAY: "Keep screen on while allowing system to sleep",
            cls.IDLE: "Keep system awake but allow display to sleep", 
            cls.DISK: "Keep hard drives spinning",
            cls.AC_POWER: "Only when connected to power adapter",
            cls.ALL: "Keep everything awake (display, system, disk)"
        }
        return descriptions.get(mode, "Unknown mode")

def cleanup_process():
    """Clean up active caffeinate process"""
    global active_process
    if active_process and active_process.poll() is None:
        try:
            active_process.terminate()
            active_process.wait(timeout=2)
        except (subprocess.TimeoutExpired, ProcessLookupError):
            try:
                active_process.kill()
            except ProcessLookupError:
                pass
        active_process = None

def signal_handler(signum, frame):
    """Handle shutdown signals"""
    cleanup_process()
    sys.exit(0)

# Register signal handlers
signal.signal(signal.SIGTERM, signal_handler)
signal.signal(signal.SIGINT, signal_handler)

async def start_sleep_prevention(mode: str = "idle", duration_minutes: Optional[int] = None) -> Dict[str, Any]:
    """Start preventing system sleep"""
    global active_process, start_time, duration_seconds
    
    # Stop any existing process
    cleanup_process()
    
    # Build caffeinate command
    cmd = ["/usr/bin/caffeinate"] + SleepMode.get_arguments(mode)
    
    # Add duration if specified
    if duration_minutes is not None and duration_minutes > 0:
        duration_seconds = duration_minutes * 60
        cmd.extend(["-t", str(duration_seconds)])
    else:
        duration_seconds = None
    
    try:
        # Start caffeinate process
        active_process = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            preexec_fn=os.setsid  # Create new process group
        )
        start_time = datetime.now()
        
        return {
            "success": True,
            "message": f"Sleep prevention started with mode: {mode}",
            "mode": mode,
            "duration_minutes": duration_minutes,
            "process_id": active_process.pid,
            "start_time": start_time.isoformat()
        }
    except Exception as e:
        return {
            "success": False,
            "error": f"Failed to start sleep prevention: {str(e)}"
        }

async def stop_sleep_prevention() -> Dict[str, Any]:
    """Stop active sleep prevention"""
    global active_process, start_time, duration_seconds
    
    if not active_process:
        return {
            "success": False,
            "message": "No active sleep prevention to stop"
        }
    
    try:
        cleanup_process()
        end_time = datetime.now()
        duration = end_time - start_time if start_time else None
        
        start_time = None
        duration_seconds = None
        
        return {
            "success": True,
            "message": "Sleep prevention stopped",
            "duration_active": str(duration) if duration else None
        }
    except Exception as e:
        return {
            "success": False,
            "error": f"Failed to stop sleep prevention: {str(e)}"
        }

async def get_sleep_status() -> Dict[str, Any]:
    """Get current sleep prevention status"""
    global active_process, start_time, duration_seconds
    
    is_active = active_process and active_process.poll() is None
    
    if not is_active and active_process:
        # Process ended, clean up
        active_process = None
        start_time = None
        duration_seconds = None
    
    result = {
        "active": is_active,
        "process_id": active_process.pid if is_active else None
    }
    
    if is_active and start_time:
        current_time = datetime.now()
        elapsed = current_time - start_time
        result["elapsed_seconds"] = int(elapsed.total_seconds())
        result["start_time"] = start_time.isoformat()
        
        if duration_seconds:
            remaining_seconds = duration_seconds - elapsed.total_seconds()
            if remaining_seconds > 0:
                result["remaining_seconds"] = int(remaining_seconds)
                result["remaining_time"] = str(timedelta(seconds=int(remaining_seconds)))
            else:
                result["remaining_seconds"] = 0
                result["status"] = "Duration expired but process may still be running"
    
    return result

async def list_sleep_modes() -> Dict[str, Any]:
    """List available sleep prevention modes"""
    modes = [
        {
            "id": SleepMode.DISPLAY,
            "name": "🖥️ Prevent Display Sleep",
            "description": SleepMode.get_description(SleepMode.DISPLAY)
        },
        {
            "id": SleepMode.IDLE, 
            "name": "💤 Prevent Idle System Sleep",
            "description": SleepMode.get_description(SleepMode.IDLE)
        },
        {
            "id": SleepMode.DISK,
            "name": "💾 Prevent Disk Sleep", 
            "description": SleepMode.get_description(SleepMode.DISK)
        },
        {
            "id": SleepMode.AC_POWER,
            "name": "🔌 Prevent Sleep on AC Power",
            "description": SleepMode.get_description(SleepMode.AC_POWER)
        },
        {
            "id": SleepMode.ALL,
            "name": "🚫 Prevent All Sleep",
            "description": SleepMode.get_description(SleepMode.ALL)
        }
    ]
    
    return {
        "modes": modes,
        "default_mode": SleepMode.IDLE
    }

async def set_duration_preset(preset: str) -> Dict[str, Any]:
    """Set duration using preset values"""
    presets = {
        "30min": 30,
        "1hr": 60,
        "2hr": 120,
        "4hr": 240,
        "indefinite": None
    }
    
    if preset not in presets:
        return {
            "success": False,
            "error": f"Unknown preset: {preset}. Available: {list(presets.keys())}"
        }
    
    duration = presets[preset]
    return {
        "success": True,
        "preset": preset,
        "duration_minutes": duration,
        "message": f"Duration preset set to: {preset}"
    }

# MCP Protocol Implementation
async def handle_mcp_message(message: Dict[str, Any]) -> Dict[str, Any]:
    """Handle incoming MCP protocol messages"""
    method = message.get("method")
    params = message.get("params", {})
    msg_id = message.get("id")
    
    if method == "initialize":
        return {
            "jsonrpc": "2.0",
            "id": msg_id,
            "result": {
                "protocolVersion": "2024-11-05",
                "capabilities": {
                    "tools": {}
                },
                "serverInfo": {
                    "name": "sleep-blocker",
                    "version": "1.0.0"
                }
            }
        }
    
    elif method == "tools/list":
        tools = [
            {
                "name": "start_sleep_prevention",
                "description": "Start preventing system sleep with specified mode and duration",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "mode": {
                            "type": "string",
                            "enum": ["display", "idle", "disk", "ac", "all"],
                            "default": "idle",
                            "description": "Sleep prevention mode"
                        },
                        "duration_minutes": {
                            "type": "integer",
                            "minimum": 1,
                            "description": "Duration in minutes. Omit for indefinite."
                        }
                    }
                }
            },
            {
                "name": "stop_sleep_prevention", 
                "description": "Stop active sleep prevention",
                "inputSchema": {
                    "type": "object",
                    "properties": {}
                }
            },
            {
                "name": "get_sleep_status",
                "description": "Get current sleep prevention status and remaining time",
                "inputSchema": {
                    "type": "object", 
                    "properties": {}
                }
            },
            {
                "name": "list_sleep_modes",
                "description": "List all available sleep prevention modes with descriptions",
                "inputSchema": {
                    "type": "object",
                    "properties": {}
                }
            },
            {
                "name": "set_duration_preset",
                "description": "Set duration using preset values (30min, 1hr, 2hr, 4hr, indefinite)",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "preset": {
                            "type": "string",
                            "enum": ["30min", "1hr", "2hr", "4hr", "indefinite"],
                            "description": "Duration preset"
                        }
                    },
                    "required": ["preset"]
                }
            }
        ]
        
        return {
            "jsonrpc": "2.0",
            "id": msg_id,
            "result": {
                "tools": tools
            }
        }
    
    elif method == "tools/call":
        tool_name = params.get("name")
        arguments = params.get("arguments", {})
        
        try:
            if tool_name == "start_sleep_prevention":
                result = await start_sleep_prevention(
                    mode=arguments.get("mode", "idle"),
                    duration_minutes=arguments.get("duration_minutes")
                )
            elif tool_name == "stop_sleep_prevention":
                result = await stop_sleep_prevention()
            elif tool_name == "get_sleep_status":
                result = await get_sleep_status()
            elif tool_name == "list_sleep_modes":
                result = await list_sleep_modes()
            elif tool_name == "set_duration_preset":
                result = await set_duration_preset(arguments.get("preset"))
            else:
                result = {"error": f"Unknown tool: {tool_name}"}
            
            return {
                "jsonrpc": "2.0",
                "id": msg_id,
                "result": {
                    "content": [
                        {
                            "type": "text",
                            "text": json.dumps(result, indent=2)
                        }
                    ]
                }
            }
            
        except Exception as e:
            return {
                "jsonrpc": "2.0",
                "id": msg_id,
                "error": {
                    "code": -32603,
                    "message": f"Internal error: {str(e)}"
                }
            }
    
    else:
        return {
            "jsonrpc": "2.0",
            "id": msg_id,
            "error": {
                "code": -32601,
                "message": f"Method not found: {method}"
            }
        }

async def main():
    """Main server loop"""
    try:
        while True:
            # Read JSON-RPC message from stdin
            line = sys.stdin.readline()
            if not line:
                break
                
            try:
                message = json.loads(line.strip())
                response = await handle_mcp_message(message)
                
                # Send response to stdout
                print(json.dumps(response), flush=True)
                
            except json.JSONDecodeError as e:
                error_response = {
                    "jsonrpc": "2.0",
                    "id": None,
                    "error": {
                        "code": -32700,
                        "message": f"Parse error: {str(e)}"
                    }
                }
                print(json.dumps(error_response), flush=True)
                
    except KeyboardInterrupt:
        pass
    finally:
        cleanup_process()

if __name__ == "__main__":
    asyncio.run(main())