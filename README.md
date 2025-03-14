# Tinder Conversation Exporter

A utility script to export your Tinder conversations into text format for archival or analysis.

## Prerequisites

- Desktop web browser (Chrome recommended)
- Access to Tinder web interface (tinder.com)

## Usage

1. Log into [Tinder Web](https://tinder.com) in your browser
2. Open the conversation you want to export
3. **Important:** Scroll to the very beginning of the conversation to load all messages
4. Open browser's Developer Tools (F12 or Right Click -> Inspect)
5. Navigate to Console tab
6. Copy and paste the contents of `extract_conversation.js` into the console
7. Press Enter to execute

The script will automatically:
- Extract all messages from the current conversation
- Save them in chronological order
- Generate a .txt file with the conversation

## Output Format

The script generates a text file containing:
- Timestamp for each message
- Sender name
- Message content
- See `tinder_conversation.txt` for an example output

## Project Structure

```
├── extract_conversation.js     # Main script for conversation export
├── tinder_conversation.txt     # Example output file
├── legacy_*.js/py             # Deprecated versions (for reference)
└── flirtation-exporter/       # Related project shared with Margaret
```

## Known Limitations

- All conversation history must be loaded (scroll to start)
- Works only on desktop Tinder web interface
- Must be run from browser console tools

## Tips

- Run the script only after the entire conversation is scrolled to the beginning

## Legacy Code

Files prefixed with `legacy_` contain previous versions of the exporter. These are kept for reference but should not be used.

## Contributing

Feel free to submit issues and enhancement requests. Enjoy 😇

## License

MIT 