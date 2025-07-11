
function generateVideo() {
    const skill = document.getElementById('skillInput').value;
    const output = document.getElementById('output');
    if (!skill.trim()) {
        output.innerHTML = "<p>Please enter a skill.</p>";
        return;
    }

    output.innerHTML = "<p>Generating video content for <strong>" + skill + "</strong>...</p>";

    // Simulate API call
    setTimeout(() => {
        output.innerHTML += "<p><video controls width='100%'><source src='https://www.w3schools.com/html/mov_bbb.mp4' type='video/mp4'>Your browser does not support the video tag.</video></p>";
    }, 2000);
}
