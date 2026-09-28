# START HERE – Omni Digital work vault

You prompt, Claude writes: clock-in, check-in, EOD and weekly summary.

## Setup (one time, about 15 minutes)

1. **Copy this folder into your Obsidian vault** (for example `MyVault/Omni Digital/`).
2. **Install Node.js** (LTS) from nodejs.org.
3. **Claude Desktop → Settings → Developer → Edit Config**, paste this (use your real folder path):
   ```json
   {
     "mcpServers": {
       "obsidian": {
         "command": "npx",
         "args": ["-y", "@modelcontextprotocol/server-filesystem", "C:\\Users\\YOU\\Documents\\MyVault\\Omni Digital"]
       }
     }
   }
   ```
   Mac path example: `/Users/you/Documents/MyVault/Omni Digital`
4. **Fully quit and reopen Claude Desktop.**
5. **Create a Claude Project** called `Omni Digital – Breaker`. In its instructions paste:
   > Before every reply, read "AI Instructions.md" in my Obsidian vault and follow it. Use the vault files as my work log.
6. In claude.ai **Settings → Connectors**, connect **Make** so Claude can run your "Omni Digital – Send EOD" scenario. It emails the EOD, and the email includes a **Send on WhatsApp** button.
7. Fill in [[Task Board]] with your current tasks.

## Option: Claude inside Obsidian (terminal)
Use this instead of Claude Desktop if you want Claude in a panel inside Obsidian.
1. Install **Git for Windows** (git-scm.com), then open **PowerShell** and run:
   `irm https://claude.ai/install.ps1 | iex`
2. In Obsidian: **Settings → Community plugins → Browse**, search **"Terminal"** (by polyipseity), then **Install → Enable**.
3. Press **Ctrl+P**, type **"Terminal: Open terminal"**, and choose the **root directory** of this vault.
4. In the terminal, type `claude` and press Enter. Log in with your Claude account (first time only).
5. Type your prompts there, e.g. `Clock me in`. Claude reads `CLAUDE.md` in this folder automatically and edits your notes directly.

## Every shift
- 9:00 PM: `Clock me in 9:00pm` → copy the check-in to **WhatsApp** (Ronin)
- During the shift: `Done: ...`, `Blocked: ...`
- 4:30 AM: `Clock me out 5:00am and write my EOD` → paste the short version in **WhatsApp**, send the **email** (or the Gmail draft)

More prompts: [[Prompts Cheat Sheet]]. Rules Claude follows: [[AI Instructions]]. Handbook summary: [[Handbook/Omni Digital Handbook]].

## Want WhatsApp sent automatically later?
Claude writes the message but cannot press send on WhatsApp by itself. That needs a Make (or n8n) scenario with WhatsApp Business. Add it once Ronin approves the channel.
