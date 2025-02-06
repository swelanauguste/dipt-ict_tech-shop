$(document).ready(function () {
    $('.btn').addClass('btn btn-sm btn-outline-dark');
    $('.del-btn').addClass('btn btn-sm btn-outline-danger');
    $('.link').addClass('text-decoration-none text-dark');
    $('.del-link').addClass('text-decoration-none text-danger');
    $('#id_quantity').addClass('p-1 rounded-2');
    $('#id_quantity').attr('onchange', 'this.form.submit()');
});