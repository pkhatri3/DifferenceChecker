document.getElementById('compareBtn').addEventListener('click', async () => {
    const text1 = document.getElementById('text1').value;
    const text2 = document.getElementById('text2').value;
    
    try {
        const response = await fetch('/compare', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ text1, text2 }),
        });
        
        const data = await response.json();
        document.getElementById('result').innerHTML = data.diff;
    } catch (error) {
        console.error('Error:', error);
        document.getElementById('result').innerHTML = 'An error occurred while comparing the texts.';
    }
}); 
