// Function to extract conversation data
function extractConversationData() {
	// Select all message elements
	const messageElements = document.querySelectorAll('.msg');

	// Array to hold the conversation data
	const conversationData = [];

	// Iterate over each message element
	messageElements.forEach(messageElement => {
			// Extract the message text
			const messageText = messageElement.querySelector('.text').innerText;

			// Extract the timestamp
			const timestampElement = messageElement.closest('.msgHelper').querySelector('time');
			const timestamp = timestampElement ? timestampElement.getAttribute('datetime') : 'Unknown';

			// Determine if the message is sent by the user or received
			const isSentByUser = messageElement.closest('[class*="Ta(e)"]') !== null;

			// Add the message data to the conversation array
			conversationData.push({
					text: messageText,
					timestamp: timestamp,
					isSentByUser: isSentByUser
			});
	});

	return conversationData;
}

// Execute the function and log the conversation data
const conversationData = extractConversationData();
console.log(conversationData);