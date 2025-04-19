document.addEventListener("DOMContentLoaded", async()=>{
    const id_user = localStorage.getItem("id_user");
    if (!id_user || id_user==0) {
        window.location.href = "/";
    }
    
    const backendURL = `http://${window.location.hostname}:8081/users/search_user/${id_user}`;
    const response = await fetch(backendURL);
    const userdata = await response.json();

    const nameLabel = document.getElementById("name").innerText = userdata.result.name;
    const usernameLabel = document.getElementById("username").innerText = userdata.result.username;
    const emailLabel = document.getElementById("email").innerText = userdata.result.email;
    const descriptionLabel = document.getElementById("description").innerText = userdata.result.description;
});


document.getElementById("logout_button").addEventListener("click", async()=>{
    localStorage.setItem("id_user", 0);
    window.location.href = "/";
});