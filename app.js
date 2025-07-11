window.generateVideo = async () => {
  const skill = document.getElementById('skillInput').value;
  const section = document.getElementById('videoSection');
  section.innerHTML = '<p>Loading…</p>';
  const res = await fetch('/api/generate-video-prompt', {
    method: 'POST',
    headers: { 'Content-Type':'application/json' },
    body: JSON.stringify({ skill })
  });
  const data = await res.json();
  section.innerHTML = `
    <h3>Script for: ${skill}</h3>
    <pre>${data.script}</pre>`;
};