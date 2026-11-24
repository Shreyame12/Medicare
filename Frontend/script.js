// Find the Add Medicine button
const addButton = document.getElementById("addMedicine");

// Find the medicine list
const medicineList = document.getElementById("medicineList");

// When the button is clicked
addButton.addEventListener("click", function () {

    // Ask the user for medicine name
    let medicineName = prompt("Enter medicine name:");

    // Check whether a name was entered
    if (medicineName && medicineName.trim() !== "") {

        // Create a new medicine item
        let medicine = document.createElement("div");

        medicine.textContent = "💊 " + medicineName;

        // Add it to the medicine list
        medicineList.appendChild(medicine);

        alert("Medicine added successfully!");
    }

});