---
name: markdown-to-gcal
description: Create Google Calendar events from structured markdown files using MCP.
metadata:
  author: "hadenlabs"
  version: "0.0.0"
  opencode:
    emoji: 📅
    tags:
      - google-calendar
      - mcp
      - event
      - workflow
    mcp:
      preferredServer: google-calendar
---

# Markdown to Google Calendar

Use this skill when you have a markdown file with event details and want to create a Google Calendar event using MCP.

## Objective

Convert a structured markdown file into a Google Calendar event using the `@cocal/google-calendar-mcp` MCP.

## Expected Markdown Format

The markdown file should follow the `event.md.tpl` structure:

```md
# Event: <title>

## Metadata

- start: <datetime>
- end: <datetime>
- timezone: <timezone>
- duration: <duration_optional>
- attendees:
  - <email1>
  - <email2>
- recurrence: <RRULE string>

## Description

<event description>

## Location

<location>
```

### Date Format Options

| Format     | Example                     | Description                            |
| ---------- | --------------------------- | -------------------------------------- |
| Simplified | `2026-04-20 09:00`          | Recommended - no T, no timezone suffix |
| ISO 8601   | `2026-04-20T09:00:00-03:00` | Full format                            |
| Natural    | `next monday 9am`           | Human readable                         |
| Relative   | `+1d`                       | Days from now                          |
| Duration   | `1h30m`                     | Use instead of end time                |

## Required Metadata

- `title` - Event title (from `# Event:` heading)
- `start` - Start datetime (simplified: `2026-04-20 09:00`, ISO 8601: `2026-04-20T09:00:00-03:00`, or natural: `next monday 9am`)
- `timezone` - Timezone identifier (e.g., `America/Argentina/Buenos_Aires`)

## Optional Metadata

- `id` - Google Calendar event ID (if present, update existing event; if absent, create new)
- `end` - End datetime (or use `duration` instead)
- `duration` - Event duration (e.g., `1h`, `30m`, `1h30m`) as alternative to `end`
- `attendees` - List of email addresses
- `recurrence` - RRULE string for recurring events (e.g., `FREQ=WEEKLY;BYDAY=MO`)
- `description` - Event description
- `location` - Physical or virtual location

## Operational Flow

1. Read the markdown file indicated by the user.
2. Parse the content to extract:
   - `title` from `# Event:` heading
   - `id` from Metadata section (optional - determines create vs update)
   - `start`, `end`, `duration`, `timezone` from Metadata section
   - `attendees` list from Metadata section
   - `recurrence` from Metadata section
   - `description` from Description section
   - `location` from Location section
3. Convert date formats to ISO 8601:
   - **Simplified** (`2026-04-18 22:00`): `start.replace(' ', 'T') + ':00' + getTimezoneOffset(timezone)`
   - **ISO 8601** (`2026-04-18T22:00:00-05:00`): use as-is
   - **Duration** (`1h`): calculate end time by adding duration to start
4. Validate required fields are present.
5. **Create vs Update**:
   - If `id` is empty or not present → Use `google-calendar_create-event` to create new event
   - If `id` has a value → Use `google-calendar_update-event` to update existing event
6. After create: Add the returned `id` to the markdown file so future runs update instead of create
7. Return the result to the user.

### Date Conversion Helper

```javascript
// Timezone offsets (add more as needed)
const TIMEZONE_OFFSETS = {
  "America/Lima": "-05:00",
  "America/Argentina/Buenos_Aires": "-03:00",
  "America/New_York": "-04:00",
  UTC: "+00:00",
};

function toISO8601(dateStr, timezone) {
  // Simplified: "2026-04-18 22:00" → "2026-04-18T22:00:00-05:00"
  if (/^\d{4}-\d{2}-\d{2} \d{2}:\d{2}$/.test(dateStr)) {
    const offset = TIMEZONE_OFFSETS[timezone] || "+00:00";
    return dateStr.replace(" ", "T") + ":00" + offset;
  }
  // Already ISO 8601
  return dateStr;
}

function parseDuration(durationStr) {
  const match = durationStr.match(/^(?:(\d+)h)?(?:(\d+)m)?$/);
  if (!match) return 0;
  return (
    ((parseInt(match[1]) || 0) * 60 + (parseInt(match[2]) || 0)) * 60 * 1000
  );
}
```

## MCP Tool Usage

```javascript
// Create new event (when no id in markdown)
{
  tool: "google-calendar_create-event",
  arguments: {
    summary: "<title>",
    start: "<ISO 8601 datetime>",
    end: "<ISO 8601 datetime>",
    timeZone: "<timezone>",
    description: "<description>",
    location: "<location>",
    attendees: [{ email: "<email1>" }, { email: "<email2>" }],
    recurrence: ["RRULE:<rrule>"]
  }
}

// Update existing event (when id is present in markdown)
{
  tool: "google-calendar_update-event",
  arguments: {
    eventId: "<id from markdown>",
    summary: "<title>",
    start: "<ISO 8601 datetime>",
    end: "<ISO 8601 datetime>",
    timeZone: "<timezone>",
    description: "<description>",
    location: "<location>"
  }
}
```

## Validation Rules

- Required fields: title, start, timezone
- datetime can be: simplified (`2026-04-20 09:00`), ISO 8601 (`2026-04-20T09:00:00-03:00`), natural (`next monday 9am`), or relative (`+1d`)
- Use either `end` OR `duration`, not both
- attendees must be valid email addresses
- end time must be after start time (or duration must be positive)
- timezone must be a valid IANA timezone identifier

## Error Handling

- If markdown is invalid or missing required fields, explain what is missing.
- If MCP tool fails, report the error from the MCP.
- Do not invent any field values.

## Your human can ask you

- "Use the `markdown-to-gcal` skill with this file"
- "Create a Google Calendar event from this markdown"
- "Schedule this event from the markdown file"