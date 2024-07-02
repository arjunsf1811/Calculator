// script.js

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
