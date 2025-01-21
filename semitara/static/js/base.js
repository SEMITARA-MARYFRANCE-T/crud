function showStatusChangeForm(bookingId) {
    document.getElementById('booking_id').value = bookingId;
    document.getElementById('statusChangeModal').style.display = 'block';
}

document.getElementById("statusChangeForm").onsubmit = function (event) {
    event.preventDefault();
    const formData = new FormData(this);

    fetch("/update-booking-status/", {
        method: "POST",
        body: formData,
    })
        .then((response) => response.json())
        .then((data) => {
            if (data.success) {
                alert(data.message);
                location.reload(); // Reload to show updated status
            } else {
                alert(data.message);
            }
        })
        .catch((error) => console.error("Error:", error));
};
