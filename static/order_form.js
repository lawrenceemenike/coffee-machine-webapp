orderForm.addEventListener('submit', (event) => {
    event.preventDefault();

    const formData = new FormData(orderForm);
    fetch('/order', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.status === 'success') {
            messageDiv.textContent = data.message;
            messageDiv.classList.add('success');
            setTimeout(() => {
                messageDiv.textContent = '';
                messageDiv.classList.remove('success');
                location.reload();
            }, 3000);
        } else {
            messageDiv.textContent = data.message;
            messageDiv.classList.add('error');
        }
    })
    .catch(error => {
        console.error('Error:', error);
        messageDiv.textContent = 'An error occurred. Please try again later.';
        messageDiv.classList.add('error');
    });
});