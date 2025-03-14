// Function to extract conversation data
function extractConversationData() {
	// Select all message elements
	const messageElements = document.querySelectorAll('.msg')

	// Array to hold the conversation data
	const conversationData = []

	// Iterate over each message element
	messageElements.forEach((messageElement) => {
		// Extract the message text
		const messageText = messageElement.querySelector('.text').innerText

		// Extract the timestamp
		const timestampElement = messageElement
			.closest('.msgHelper')
			.querySelector('time')
		const timestamp = timestampElement
			? timestampElement.getAttribute('datetime')
			: 'Unknown'

		// Determine if the message is sent by the user or received
		const isSentByUser = messageElement.closest('[class*="Ta(e)"]') !== null

		// Add the message data to the conversation array
		conversationData.push({
			text: messageText,
			timestamp: timestamp,
			isSentByUser: isSentByUser,
		})
	})

	return conversationData
}

// Function to export conversation data to text file
function exportToText(conversationData) {
	// Format the conversation data
	const formattedText = conversationData
		.map((msg) => {
			const sender = msg.isSentByUser ? 'You' : 'Other'
			return `[${msg.timestamp}] ${sender}: ${msg.text}`
		})
		.join('\n')

	// Create a blob with the formatted text
	const blob = new Blob([formattedText], { type: 'text/plain' })

	// Create a download link
	const url = window.URL.createObjectURL(blob)
	const a = document.createElement('a')
	a.href = url
	a.download = `conversation_${new Date().toISOString().split('T')[0]}.txt`

	// Trigger the download
	document.body.appendChild(a)
	a.click()

	// Cleanup
	window.URL.revokeObjectURL(url)
	document.body.removeChild(a)
}

// Execute the function and export the conversation data
const conversationData = extractConversationData()
exportToText(conversationData)
