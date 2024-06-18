document.addEventListener("DOMContentLoaded", function() {
    const deleteForms = document.querySelectorAll(".delete-form");

    deleteForms.forEach(form => {
        form.addEventListener("submit", function(event) {
            if (!confirm("Czy na pewno chcesz usunąć tę książkę?")) {
                event.preventDefault();
            }
        });
    });
});
