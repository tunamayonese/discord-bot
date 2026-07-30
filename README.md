# Simple Discord Bot

A simple discord bot built with discord.py that allows the authorized users to post announcement embeds to any channel using `/announce` 

**Features**
- Slash command support
- Discord embeds
- Choose destination channel
- Custom title
- Custom message
- Optional logo
- Optional banner image
- Confirmation message
- Easy to modify

**Requirements**
- Python
- Discord Bot App
- Admin permissions


# STEPS
Installation
1. Clone the repository
```bash
git clone https://github.com/USERNAME/REPOSITORY.git
cd REPOSITORY
```

2. Install dependencies
```bash
pip install discord.py python-dotenv
```

3. Create a Discord Bot

  1. Visit the Discord Developer Portal:
     https://discord.com/developers/applications

  2. Click **New Application**

  3. Navigate to **Bot**

  4. Click **Add Bot**

  5. Under **Privileged Gateway Intents**, enable:
      - Server Members Intent

  6. Copy your Bot Token.

4. Invite the Bot
Go to:
```
OAuth2
→ URL Generator
```

Select:

  Scopes
  - bot
  - applications.commands

  Permissions
  - Send Messages
  - Embed Links
  - Manage Roles (optional)
  - Read Message History
  - View Channels

Invite the bot to your server.

5. Create the .env file

Inside the project folder create:
```
.env
```
Add:
```env
TOKEN=YOUR_BOT_TOKEN
```
Example:
```env
TOKEN=MTExMjIyMzMz...
```


Running the Bot

```bash
python bot.py
```

or

```bash
python3 bot.py
```

You should see:

```
Logged in as YourBot
Synced 1 slash commands.
```


Commands

### /announce

Posts a custom embed.

Arguments

| Argument | Description |
|----------|-------------|
| channel | Destination channel |
| title | Embed title |
| message | Embed body |
| logo | Thumbnail image URL (optional) |
| image | Banner image URL (optional) |

---


Example

Title

```
Security Forces Headquarters
```

Message

```
Welcome to the Air Force Security Forces Command.
```

Logo

```
https://example.com/logo.png
```

Image

```
https://example.com/banner.png


## Project Structure

```
.
├── bot.py
├── .env
├── requirements.txt
└── README.md
```

---

## Notes

- Discord slash command text inputs are **single-line**.
- Multi-line announcements require Discord **Modals**, which are not included in this basic version.
- Only users with the required permissions or roles should have access to the `/announce` command.

---


