fetch("data.json")
    .then(res => res.json())
    .then(data => {
        document.getElementById("status").innerText = data.status;
        document.getElementById("lastRun").innerText = data.last_run;

        const tbody = document.getElementById("data");
        data.cryptos.forEach(c => {
            const row = `<tr>
                <td>${c.name}</td>
                <td>${c.price_usd}</td>
                <td>${c.price_inr}</td>
            </tr>`;
            tbody.innerHTML += row;
        });
    });
