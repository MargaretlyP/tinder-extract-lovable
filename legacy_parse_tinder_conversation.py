#!/usr/bin/env python3
import re
import sys
from bs4 import BeautifulSoup
from datetime import datetime
import html
import textwrap

def extract_conversation(html_file):
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Parse HTML
    soup = BeautifulSoup(content, 'html.parser')
    
    # Find all message elements
    messages = []
    
    # Process all message containers
    msg_containers = soup.find_all(['div'], class_=lambda c: c and ('Pos(r) Ta(e)' in c or 'Pos(r) Ta(start)' in c))
    
    for container in msg_containers:
        # Determine sender based on container class
        is_sent = 'Ta(e)' in container.get('class', [])
        sender = 'You' if is_sent else 'Margaret'
        
        # Find the message text
        msg_div = container.find('div', class_=lambda c: c and ('msg BreakWord' in c))
        if not msg_div:
            continue
            
        text_span = msg_div.find('span', class_='text')
        if not text_span:
            continue
            
        text = text_span.get_text()
        
        # Find timestamp
        time_elem = container.find('time')
        if not time_elem:
            continue
            
        timestamp = time_elem.get('datetime')
        
        messages.append({
            'sender': sender,
            'text': text,
            'timestamp': timestamp
        })
    
    # Sort messages by timestamp
    messages.sort(key=lambda x: x['timestamp'])
    
    return messages

def format_timestamp(timestamp):
    dt = datetime.fromisoformat(timestamp.replace('Z', '+00:00'))
    return dt.strftime('%Y-%m-%d %H:%M')

def format_message_text(text, width=80):
    # Replace multiple newlines with a single one
    text = re.sub(r'\n{3,}', '\n\n', text)
    
    # Wrap long lines
    paragraphs = text.split('\n\n')
    wrapped_paragraphs = []
    
    for paragraph in paragraphs:
        lines = paragraph.split('\n')
        wrapped_lines = []
        
        for line in lines:
            if line.strip():
                wrapped = textwrap.fill(line, width=width)
                wrapped_lines.append(wrapped)
            else:
                wrapped_lines.append('')
        
        wrapped_paragraphs.append('\n'.join(wrapped_lines))
    
    return '\n\n'.join(wrapped_paragraphs)

def print_conversation(messages, width=80):
    print("=" * width)
    print(f"{'TINDER CONVERSATION':^{width}}")
    print("=" * width)
    print()
    
    current_date = None
    for msg in messages:
        timestamp = format_timestamp(msg['timestamp'])
        date, time = timestamp.split(' ')
        
        # Print date separator if it's a new day
        if date != current_date:
            print()
            print("-" * width)
            print(f"{date:^{width}}")
            print("-" * width)
            print()
            current_date = date
        
        # Format and print the message
        sender = msg['sender']
        text = format_message_text(msg['text'], width=width-10)  # Leave some margin
        
        # Print sender and timestamp
        print(f"[{time}] {sender}:")
        
        # Print message with indentation
        for line in text.split('\n'):
            print(f"    {line}")
        
        print()

def save_conversation_to_file(messages, output_file, width=80):
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("=" * width + "\n")
        f.write(f"{'TINDER CONVERSATION':^{width}}" + "\n")
        f.write("=" * width + "\n\n")
        
        current_date = None
        for msg in messages:
            timestamp = format_timestamp(msg['timestamp'])
            date, time = timestamp.split(' ')
            
            # Print date separator if it's a new day
            if date != current_date:
                f.write("\n" + "-" * width + "\n")
                f.write(f"{date:^{width}}" + "\n")
                f.write("-" * width + "\n\n")
                current_date = date
            
            # Format and write the message
            sender = msg['sender']
            text = format_message_text(msg['text'], width=width-10)  # Leave some margin
            
            # Write sender and timestamp
            f.write(f"[{time}] {sender}:\n")
            
            # Write message with indentation
            for line in text.split('\n'):
                f.write(f"    {line}\n")
            
            f.write("\n")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <tinder_html_file> [output_file]")
        sys.exit(1)
    
    html_file = sys.argv[1]
    messages = extract_conversation(html_file)
    
    # Print to console
    print_conversation(messages)
    
    # Save to file if output file is specified
    if len(sys.argv) > 2:
        output_file = sys.argv[2]
        save_conversation_to_file(messages, output_file)
        print(f"\nConversation saved to {output_file}")
    else:
        # Default output file
        output_file = "tinder_conversation.txt"
        save_conversation_to_file(messages, output_file)
        print(f"\nConversation saved to {output_file}") 