// Funzione per generare opzioni da -10.00 a +10.00 con incrementi di 0.25
function generateOptions(selector) {
    const selectElement = document.querySelector(selector);

    for (let i = -10.00; i <= 10.00; i += 0.25) {
        const option = document.createElement('option');
        option.value = i;
        option.textContent = i;
        selectElement.appendChild(option);
    }
}

function generateOptionsAsse(selector) {
    const selectElementAsse = document.querySelector(selector);

    for (let i = 0; i <= 180; i += 5) {
        const option = document.createElement('option');
        option.value = i;
        option.textContent = i;
        selectElementAsse.appendChild(option);
    }
}