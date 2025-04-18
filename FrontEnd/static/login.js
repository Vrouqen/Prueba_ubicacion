document.getElementById("formuser").addEventListener("submit", async(e)=>{
    e.preventDefault();

    const formdata = new FormData();

    formdata.append('username',document.getElementById('username').value);
    formdata.append('password',document.getElementById('password').value);

    const backendURL = `http://${window.location.hostname}:8081/users/login`;
    response = await fetch(backendURL,{
        'body': formdata,
        'method': "POST"
    });

    const responsejson = await response.json();

    if (responsejson.id_user!=0){    
        localStorage.setItem("id_user", responsejson.id_user);
        window.location.href = "/dashboard";
    }else{
        alert(responsejson.message);
    }

});