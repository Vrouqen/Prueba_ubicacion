document.addEventListener("DOMContentLoaded", async () => {
    // Obtiene la ip de donde carga el front
    const backendURL = `http://${window.location.hostname}:8081/users/load_users`;
    const users = await fetch(backendURL);
    
    const usersjson = await users.json();
    const usersdiv = document.getElementById('users');

    for (const user of usersjson.result){
        const user_info = document.createElement("div");
        user_info.innerHTML = `
            <label>id_user: ${user.id_user}</label>
            <br><label>username: ${user.username}</label>
            <br><label>password: ${user.password}</label>
            <br><label>name: ${user.name}</label>
            <br><label>description: ${user.description}</label>
            <br><label>email: ${user.email}</label><br><br>
        `;
        usersdiv.appendChild(user_info);
    }
});