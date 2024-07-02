/*

let currentInput = '';

function appendNumber(num) {
    currentInput += num;
    document.getElementById('result').value = currentInput;
}

function appendOperator(op) {
    if (currentInput !== '' && !isNaN(currentInput[currentInput.length - 1])) {
        currentInput += op;
        document.getElementById('result').value = currentInput;
    }
}

function clearResult() {
    currentInput = '';
    document.getElementById('result').value = currentInput;
}

function calculateResult() {
    try {
        currentInput = eval(currentInput).toString();
        document.getElementById('result').value = currentInput;
    } catch (error) {
        document.getElementById('result').value = 'Error';
    }
}
*/
function addToDisplay(value) {
    document.getElementById('display').innerText += value;
}

function clearDisplay() {
    document.getElementById('display').innerText = '';
}

function backspace() {
    let display = document.getElementById('display');
    display.innerText = display.innerText.slice(0, -1);
}

function calculate() {
    let display = document.getElementById('display');
    try {
        display.innerText = eval(display.innerText);
    } catch (e) {
        display.innerText = 'Error';
    }
}
