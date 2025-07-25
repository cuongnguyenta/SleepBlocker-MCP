# Sleep Blocker MCP Server - Usage Examples

This document provides practical examples of how to use the Sleep Blocker MCP Server with AI assistants.

## 🎯 Real-World Scenarios

### 📊 Work & Productivity

#### Presentation Mode
**User**: *"I'm giving a presentation in 5 minutes. Keep my screen on for the next 2 hours."*

**AI Response**: Using the `start_sleep_prevention` tool with:
- Mode: `display` (keeps screen on)
- Duration: 120 minutes

**Result**: Screen stays on, system can still sleep to save battery.

---

#### Long Download/Process
**User**: *"I'm downloading a 50GB file overnight. Make sure my Mac doesn't sleep for 8 hours."*

**AI Response**: Using the `start_sleep_prevention` tool with:
- Mode: `idle` (keeps system awake)
- Duration: 480 minutes

**Result**: System stays awake, display can sleep to save power.

---

#### Video Call Marathon
**User**: *"I have back-to-back video calls all afternoon. Prevent display sleep indefinitely."*

**AI Response**: Using the `start_sleep_prevention` tool with:
- Mode: `display`
- Duration: indefinite

**Result**: Screen never sleeps until manually stopped.

### 🎵 Media & Entertainment

#### Movie Night
**User**: *"I'm watching a 3-hour movie. Keep everything awake."*

**AI Response**: Using the `start_sleep_prevention` tool with:
- Mode: `all` (prevents all sleep)
- Duration: 180 minutes

**Result**: Screen, system, and drives stay active.

---

#### Music Production
**User**: *"I'm recording music and need my external drives to stay spinning for the next 4 hours."*

**AI Response**: Using the `start_sleep_prevention` tool with:
- Mode: `disk` (prevents drive sleep)
- Duration: 240 minutes

**Result**: Hard drives stay active, system and display can sleep.

### 🔋 Battery Management

#### AC Power Only
**User**: *"Only prevent sleep when I'm plugged in to power."*

**AI Response**: Using the `start_sleep_prevention` tool with:
- Mode: `ac` (only when on AC power)
- Duration: indefinite

**Result**: Sleep prevention only active when plugged in.

## 📱 Common Commands & Responses

### Starting Sleep Prevention

#### Quick 30-Minute Block
**User**: *"Don't let my Mac sleep for 30 minutes"*
```json
Tool: start_sleep_prevention
Args: {"mode": "idle", "duration_minutes": 30}
```

#### Using Presets
**User**: *"Set sleep prevention to 2 hour preset"*
```json
Tool: set_duration_preset
Args: {"preset": "2hr"}
```

#### Indefinite Prevention
**User**: *"Keep my Mac awake indefinitely"*
```json
Tool: start_sleep_prevention  
Args: {"mode": "idle"}
```

### Checking Status

#### Basic Status Check
**User**: *"Is sleep prevention currently active?"*
```json
Tool: get_sleep_status
Response: {
  "active": true,
  "elapsed_seconds": 1847,
  "remaining_seconds": 1453,
  "remaining_time": "0:24:13"
}
```

#### Detailed Status
**User**: *"How much time is left on my sleep prevention?"*

**AI Response**: "Sleep prevention is active with 24 minutes and 13 seconds remaining. It's been running for about 31 minutes."

### Stopping Sleep Prevention

#### Simple Stop
**User**: *"Stop preventing sleep"*
```json
Tool: stop_sleep_prevention
```

#### Conditional Stop
**User**: *"I'm done with my presentation, allow normal sleep again"*
```json
Tool: stop_sleep_prevention
```

### Exploring Options

#### Available Modes
**User**: *"What sleep prevention modes are available?"*
```json
Tool: list_sleep_modes
Response: Shows all 5 modes with descriptions
```

#### Understanding Modes
**User**: *"What's the difference between display and idle modes?"*

**AI Response**: 
- **Display mode**: Keeps your screen on but allows the system to sleep
- **Idle mode**: Keeps the system awake but allows the display to sleep

## 🔄 Workflow Examples

### Morning Routine Setup
```
User: "I'm starting my workday"
AI: Checks current status, sets up 4-hour idle prevention
User: "What's my current sleep status?"
AI: Reports active prevention with remaining time
```

### End of Day Cleanup
```
User: "I'm done working for the day"
AI: Stops any active sleep prevention
AI: Confirms Mac can now sleep normally
```

### Gaming Session
```
User: "I'm starting a 3-hour gaming session"
AI: Sets display + system prevention for 3 hours
User: "Extend it by another hour"
AI: Stops current, starts new 4-hour session
```

### Content Creation
```
User: "I'm editing a video and need drives to stay active"
AI: Sets disk prevention mode
User: "How long has this been running?"
AI: Reports elapsed time and remaining duration
```

## 🎨 Creative Use Cases

### Time-Based Automation
**User**: *"Every weekday at 9 AM, prevent sleep for 8 hours"*

While the MCP server doesn't have scheduling built-in, it can be combined with system scheduling tools or AI assistant workflows.

### Conditional Prevention
**User**: *"Only prevent sleep if I'm on AC power and it's during work hours"*

The AC power mode can be combined with time-based logic in your AI assistant.

### Multi-Stage Workflows
**User**: *"Start with 1 hour of display prevention, then switch to idle prevention"*

This requires multiple tool calls orchestrated by the AI assistant.

## 🔍 Monitoring & Debugging

### Health Checks
**User**: *"Is the sleep prevention system working correctly?"*
```json
Tool: get_sleep_status
Expected: Active status with valid remaining time
```

### Performance Monitoring
**User**: *"How long have I been preventing sleep today?"*

The AI can track cumulative usage through multiple status checks.

### Troubleshooting
**User**: *"Sleep prevention isn't working, what's wrong?"*

AI can:
1. Check current status
2. Try stopping and restarting
3. Verify mode settings
4. Report any errors

## 📊 Pro Tips

### Battery Optimization
- Use `idle` mode instead of `all` for better battery life
- Use `ac` mode for laptop users who move between power sources
- Set reasonable durations rather than indefinite prevention

### Performance Optimization
- Use `disk` mode only when necessary for drive-intensive tasks
- Combine with macOS Energy Saver settings for best results
- Monitor system temperature during extended prevention

### Workflow Integration
- Chain commands: "Stop current prevention and start 2-hour display mode"
- Use status checks before starting new prevention
- Set reminders to check on long-duration prevention

## 🎪 Fun Examples

### Movie Marathon
**User**: *"I'm having a Lord of the Rings marathon - about 9 hours total"*
```json
Tool: start_sleep_prevention
Args: {"mode": "display", "duration_minutes": 540}
```

### All-Nighter
**User**: *"I'm pulling an all-nighter for this project"*
```json
Tool: start_sleep_prevention
Args: {"mode": "idle"}
```

### Power User
**User**: *"Show me the current status, then extend prevention by 2 hours"*
1. Check status
2. Stop current prevention  
3. Start new prevention with extended time

These examples show the flexibility and power of the Sleep Blocker MCP Server. The natural language interface makes it easy to control your Mac's sleep behavior through conversational commands with your AI assistant.