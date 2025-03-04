function fetchData() {
    fetch("/api/data")
        .then(response => response.json())
        .then(data => {
            document.getElementById("output").textContent = data.message;
        })
        .catch(error => console.error("Error fetching data:", error));
}

