document.addEventListener("DOMContentLoaded", fetchUsers);

function fetchUsers() {
    fetch("/api/users")
        .then(response => response.json())
        .then(users => {
            let userList = document.getElementById("userList");
            userList.innerHTML = "";
            users.forEach(user => {
                let li = document.createElement("li");
                li.textContent = user.name;
                userList.appendChild(li);
            });
        })
        .catch(error => console.error("Error fetching users:", error));
}
function fetchData() {
    fetch("/api/data")
        .then(response => response.json())
        .then(data => {
            document.getElementById("output").textContent = data.message;
        })
        .catch(error => console.error("Error fetching data:", error));
}
function addUser() {
    let name = document.getElementById("username").value;
    fetch("/api/users", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ name })
    })
    .then(response => response.json())
    .then(() => {
        fetchUsers();
        document.getElementById("username").value = "";
    })
    .catch(error => console.error("Error adding user:", error));
}

