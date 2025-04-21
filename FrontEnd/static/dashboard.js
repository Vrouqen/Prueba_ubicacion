document.addEventListener("DOMContentLoaded", async()=>{
    const id_user = localStorage.getItem("id_user");
    if (!id_user || id_user==0) {
        window.location.href = "/";
    }
    
    const backendUsersURL = `http://${window.location.hostname}:8081/users/search_user/${id_user}`;
    const responseUser = await fetch(backendUsersURL);
    const userdata = await responseUser.json();

    const nameLabel = document.getElementById("name").innerText = userdata.result.name;
    const usernameLabel = document.getElementById("username").innerText = userdata.result.username;
    const emailLabel = document.getElementById("email").innerText = userdata.result.email;
    const descriptionLabel = document.getElementById("description").innerText = userdata.result.description;

    // Costos
    const backendCostsURL = `http://${window.location.hostname}:8081/costs/load_user_costs/${id_user}`;
    const responseCosts = await fetch(backendCostsURL);
    const usercosts = await responseCosts.json();

    const costsTable = document.getElementById("costsTable");
    for(const c of usercosts.result){
        const row = document.createElement("tr");
        row.innerHTML = `
            <td>${c.name}</td>
            <td>${c.value}</td>
            <td>${c.date}</td>
            <td>${c.type_cost}</td>
            `;
        costsTable.appendChild(row);
    }
    const row_insert_cost = document.createElement("tr");
    row_insert_cost.innerHTML = `
        <td><input type="text" id="name_cost"></td>
        <td><input type="number" id="value_cost"></td>
        <td><input type="date" id="date_cost"></td>
        <td><input type="text" id="type_cost"></td>
        `;
    costsTable.appendChild(row_insert_cost);

    // Ingresos
    const backendIncomesURL = `http://${window.location.hostname}:8081/incomes/load_user_incomes/${id_user}`;
    const responseIncomes = await fetch(backendIncomesURL);
    const userincomes = await responseIncomes.json();
    
    const incomesTable = document.getElementById("incomesTable");
    for(const i of userincomes.result){
        const row = document.createElement("tr");
        row.innerHTML = `
            <td>${i.name}</td>
            <td>${i.value}</td>
            <td>${i.date}</td>
            <td>${i.type_income}</td>
            `;
        incomesTable.appendChild(row);
    }
    const row_insert_income = document.createElement("tr");
    row_insert_income.innerHTML = `
        <td><input type="text" id="name_income"></td>
        <td><input type="number" id="value_income"></td>
        <td><input type="date" id="date_income"></td>
        <td><input type="text" id="type_income"></td>
        `;
    incomesTable.appendChild(row_insert_income);
    
});

document.getElementById("insert_cost_button").addEventListener("click", async()=>{
    // Insert login on session table
    const costURL = `http://${window.location.hostname}:8081/costs/insert_cost`;

    const formdataCost = new FormData();
    formdataCost.append('id_user', localStorage.getItem("id_user"));
    formdataCost.append('name', document.getElementById("name_cost").value);
    formdataCost.append('value', document.getElementById("value_cost").value);
    formdataCost.append('date', document.getElementById("date_cost").value);
    formdataCost.append('type_cost', document.getElementById("type_cost").value);

    await fetch(costURL, {
        'body': formdataCost,
        'method': "POST"
    });

    window.location.href = "/dashboard";
});

document.getElementById("insert_income_button").addEventListener("click", async()=>{
    // Insert login on session table
    const costURL = `http://${window.location.hostname}:8081/incomes/insert_income`;

    const formdataIncome = new FormData();
    formdataIncome.append('id_user', localStorage.getItem("id_user"));
    formdataIncome.append('name', document.getElementById("name_income").value);
    formdataIncome.append('value', document.getElementById("value_income").value);
    formdataIncome.append('date', document.getElementById("date_income").value);
    formdataIncome.append('type_income', document.getElementById("type_income").value);

    await fetch(costURL, {
        'body': formdataIncome,
        'method': "POST"
    });

    window.location.href = "/dashboard";
});

document.getElementById("logout_button").addEventListener("click", async()=>{
    // Insert login on session table
    const sessionURL = `http://${window.location.hostname}:8081/users/insert_session`;

    const formdataSession = new FormData();
    formdataSession.append('id_user', localStorage.getItem("id_user"));
    formdataSession.append('log_in', 0);

    await fetch(sessionURL, {
        'body': formdataSession,
        'method': "POST"
    });

    localStorage.setItem("id_user", 0);
    window.location.href = "/";
});