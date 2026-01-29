const API_URL = 'http://localhost:8000';

function addMessage(text, isUser = false, sources = []) {
    const chatArea = document.getElementById('chatArea');
    const messageDiv = document.createElement('div');
    messageDiv.className = `message ${isUser ? 'user-message' : 'agent-message'}`;
    messageDiv.innerHTML = text;

    if (sources && sources.length > 0) {
        const sourcesDiv = document.createElement('div');
        sourcesDiv.style.marginTop = '10px';
        sources.forEach(source => {
            const link = document.createElement('a');
            link.href = source.url;
            link.target = '_blank';
            link.className = 'source-link';
            link.textContent = source.title || 'Source';
            sourcesDiv.appendChild(link);
        });
        messageDiv.appendChild(sourcesDiv);
    }

    chatArea.appendChild(messageDiv);
    chatArea.scrollTop = chatArea.scrollHeight;
}

function showThinking() {
    const chatArea = document.getElementById('chatArea');
    const thinkingDiv = document.createElement('div');
    thinkingDiv.className = 'thinking';
    thinkingDiv.id = 'thinking';
    thinkingDiv.textContent = '🔍 Researching your question...';
    chatArea.appendChild(thinkingDiv);
    chatArea.scrollTop = chatArea.scrollHeight;
}

function removeThinking() {
    const thinking = document.getElementById('thinking');
    if (thinking) thinking.remove();
}

async function askQuestion() {
    const input = document.getElementById('questionInput');
    const button = document.getElementById('askButton');
    const question = input.value.trim();

    if (!question) return;

    addMessage(question, true);
    input.value = '';
    button.disabled = true;

    showThinking();

    try {
        const response = await fetch(`${API_URL}/research`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ question })
        });

        const data = await response.json();

        removeThinking();
        addMessage(data.answer, false, data.sources);

    } catch (error) {
        removeThinking();
        addMessage('❌ Sorry, something went wrong. Please try again.', false);
        console.error('Error:', error);
    } finally {
        button.disabled = false;
    }
}