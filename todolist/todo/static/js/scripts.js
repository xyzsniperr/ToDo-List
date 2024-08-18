document.querySelectorAll('input[type="checkbox"]').forEach(function(checkbox) {
    checkbox.addEventListener('change', function() {
        const taskId = this.getAttribute('data-task-id')
        const isChecked = this.checked

        fetch(`/update_task_status/${taskId}/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCsrfToken()
            },
            body: JSON.stringify({
                'completed': isChecked
            })
        }).then(response => response.json())
          .then(data => {
              if (data.success) {
                  const badge = document.querySelector(`#taskBadge${taskId}`)
                  if (isChecked) {
                      badge.classList.remove('badge-warning')
                      badge.classList.add('badge-success')
                      badge.textContent = 'Erledigt'
                  } else {
                      badge.classList.remove('badge-success')
                      badge.classList.add('badge-warning')
                      badge.textContent = 'Offen'
                  }
              } else {
                Swal.fire({
                    title: 'Es gab ein Problem beim Aktualisieren der Aufgabe.',
                    text: 'Es gab ein Problem beim Aktualisieren der Aufgabe.',
                    icon: 'error',
                    confirmButtonText: 'OK'
                });
              }
          });
    });
});


function getCsrfToken() {
    return document.querySelector('[name=csrfmiddlewaretoken]').value;
}