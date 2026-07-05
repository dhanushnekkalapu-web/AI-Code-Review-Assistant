async function reviewCode() {
    const code = document.getElementById("codeInput").value;
    const language = document.getElementById("language").value;
    const output = document.getElementById("output");

    if (!code) {
        output.innerText = "⚠️ Please paste some code.";
        return;
    }

    output.innerText = "⏳ Analyzing code...";
    try {
        const res = await fetch("http://localhost:5000/review", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ code, language })
        });
        const data = await res.json();
        output.innerText = data.review;
    } catch (err) {
        output.innerText = "❌ Error connecting to server.";
    }
}