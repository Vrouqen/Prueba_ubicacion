// Detecta cuando se envía el formulario
document.getElementById("userform").addEventListener("submit", async (e) => {
    e.preventDefault(); // Evita que se envía el formulario normalmente

    const formData = new FormData(); // Creamos un formdata para almacenar los valores que se enviarán a metodo post
    formData.append("username", document.getElementById("username").value);
    formData.append("password", document.getElementById("password").value);
    formData.append("name", document.getElementById("name").value);
    formData.append("email", document.getElementById("email").value);
    formData.append("description", document.getElementById("description").value);

    // Se obtiene la respuesta haciendo una solicitud al metodo post para insertar un usuario
    const backendURL = `http://${window.location.hostname}:8081/users/insert_user`;
    const response = await fetch(backendURL, { 
        method: "POST",
        body: formData
    });

    const result = await response.json(); // Se convierte en json

    // Se agrega la respuesta al html para que redireccione a la url de la api
    document.getElementById("responseMessage").innerText = result.message;
});