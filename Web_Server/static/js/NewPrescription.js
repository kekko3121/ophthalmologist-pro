// Funzione per generare opzioni da -10.00 a +10.00 con incrementi di 0.25
function generateOptions(selector) {
    const selectElement = document.querySelector(selector);

    for (let i = -10.00; i <= 10.00; i += 0.25) {
        const option = document.createElement('option');
        option.value = i.toFixed(2); // Limita il numero di decimali a due
        option.textContent = i.toFixed(2);
        selectElement.appendChild(option);
    }
}

function generateOptionsAsse(selector) {
    const selectElementAsse = document.querySelector(selector);

    for (let i = 0; i <= 180; i += 5) {
        const option = document.createElement('option');
        option.value = i.toFixed(0); // Limita il numero di decimali a due
        option.textContent = i.toFixed(0);
        selectElementAsse.appendChild(option);
    }
}