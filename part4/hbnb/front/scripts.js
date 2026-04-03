document.addEventListener('DOMContentLoaded', () => {
    const loginForm = document.getElementById('login-form');

    if (loginForm) {
        loginForm.addEventListener('submit', async (event) => {
            event.preventDefault();

            const email = document.getElementById('email').value;
            const password = document.getElementById('password').value;

            console.log('Tentative login:', email);

            try {
                const response = await fetch('http://172.18.21.91:5000/api/v1/auth/login', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({ email, password })
                });

                console.log('Status:', response.status);

                if (response.ok) {
                    const data = await response.json();
                    console.log('Token reçu:', data);

                    const token = data.access_token || data.token;
                    document.cookie = `token=${token}; path=/`;
                    window.location.href = 'index.html';
                } else {
                    const errorData = await response.json();
                    console.error('Erreur API:', errorData);
                    alert('Login failed: ' + (errorData.message || response.statusText));
                }
            } catch (error) {
                console.error('Fetch error:', error);
                alert('Erreur: ' + error.message);
            }
        });
    }
});