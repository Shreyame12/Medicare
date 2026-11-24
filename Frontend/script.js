
const API_URL = "http://127.0.0.1:5000/api/medicines/";

const addButton = document.getElementById("addMedicine");
const medicineList = document.getElementById("medicineList");

addButton.addEventListener("click", async function () {
    const medicineName = prompt("Enter medicine name:");

    if (!medicineName || medicineName.trim() === "") {
        alert("Please enter a medicine name.");
        return;
    }

    try {
        const response = await fetch(API_URL, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                name: medicineName.trim(),
                instructions: ""
            })
        });

        const result = await response.json();

        if (!response.ok) {
            alert(result.message || "Could not add medicine.");
            return;
        }

        const medicine = document.createElement("div");
        medicine.textContent = "💊 " + result.medicine.name;
        medicineList.appendChild(medicine);

        alert("Medicine details accepted by backend!");

    } catch (error) {
        console.error("Backend connection error:", error);
        alert("Could not connect to the backend. Check whether Flask is running.");
    }
});
