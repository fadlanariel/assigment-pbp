$.ajax({
    url: './json/',
    dataType: 'json',
    success: function (data) { // jika request berhasil
      for (var i = 0; i < data.length; i++) {
        var row = $('<div class="row"><div class="card m-4 mx-auto"><h5 class="card-header text-center">' + data[i].fields.title +
          '</h5><div class="card-body"><p class="card-text">' + data[i].fields.description +
          '</p></div><p class="card-footer text-muted">Created: ' + data[i].fields.date +
          '</p></div></div>');
        $('#cardTable').append(row);
      }
    },
    error: function (jqXHR, textStatus, errorThrown) { // jika request gagal tampilkan error message
      alert('Error: ' + textStatus + ' - ' + errorThrown);
    }
  });

  $(document).on('submit', '#add-task', function (e) { // dapatkan trigger melalui id dari button
    $.ajax({
      type: 'POST',
      url: "{% url 'todolist:add_task' %}", //url untuk ke views tambahkan data
      data: { // dapatkan data sesuai id dari input yang ada di form
        title: $('#title').val(),
        description: $('#Description').val(),
        csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
        action: 'post'
      },
      success: function (json) {
        //document.getElementById("add-wishlist").reset();
      },
      error: function (xhr, errmsg, err) { // tampilkan error message jika gagal
        console.log(xhr.status + ": " + xhr.responseText);
      }
    });
  });