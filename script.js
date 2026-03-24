const button = document.querySelector('.search-button');

button.addEventListener('click', async function () {
    var url = document.querySelector('.search-input').value;
    const dynamicVariable = url;
    const response = await fetch('http://127.0.0.1:5000/run-script', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ dynamic_variable: dynamicVariable })
    });

    const data = await response.json();
    console.log(data.output);
    document.getElementById('output').innerText = data.output;
});
