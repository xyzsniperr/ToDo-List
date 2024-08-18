function getCsrfToken() {
    return document.querySelector('[name=csrfmiddlewaretoken]').value;
}

function confirmDelete(listId) {
    Swal.fire({
        title: 'Bist du sicher?',
        text: "Diese Aktion kann nicht rückgängig gemacht werden!",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Ja, löschen!',
        cancelButtonText: 'Abbrechen'
    }).then((result) => {
        if (result.isConfirmed) {
            const form = document.createElement('form');
            form.method = 'POST';
            form.action = '/delete/' + listId + '/';
            
            const csrfToken = document.createElement('input');
            csrfToken.type = 'hidden';
            csrfToken.name = 'csrfmiddlewaretoken';
            csrfToken.value = getCsrfToken();

            form.appendChild(csrfToken);
            document.body.appendChild(form);
            form.submit();
        }
    })
}
