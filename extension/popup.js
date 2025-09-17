document.getElementById("send").addEventListener("click", async () => {
  let [tab] = await chrome.tabs.query({ active: true, currentWindow: true });
  let instruction = document.getElementById("instruction").value;

  // Inject content.js to grab DOM
  chrome.scripting.executeScript({
    target: { tabId: tab.id },
    files: ["content.js"]
  }, async (results) => {
    let html = results[0].result;

    let payload = {
      url: tab.url,
      html: html,
      instruction: instruction
    };

    try {
      let response = await fetch("http://127.0.0.1:8000/ingest", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload)
      });

      let data = await response.json();
      document.getElementById("result").innerText = JSON.stringify(data, null, 2);
    } catch (err) {
      document.getElementById("result").innerText = "Error: " + err.message;
    }
  });
});
