function checkAnswer(question, answer) {
    const result = document.getElementById("result");

    if (answer === "correct") {
        result.innerHTML = "✅ Correct Answer!";
        result.style.background = "#d4edda";
        result.style.color = "#155724";
    } else {
        result.innerHTML = "❌ Incorrect Answer. Try again!";
        result.style.background = "#f8d7da";
        result.style.color = "#721c24";
    }
}