document.getElementById("userform").addEventListener("submit", async(e) => {
    e.preventDefault(); 

    const form = new FormData();
    form.append("id_user", document.getElementById("id_user").value);

    const backendURL = `http://${window.location.hostname}:8081/users/delete_user`;
    const response = await fetch(backendURL, {
        method: "POST",
        body: form
    });

    const result = await response.json();

    document.getElementById("responseMessage").innerText = result.message+" - id_user: "+result.user;
});