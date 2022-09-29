$(document).ready( function () {

    // console.log(context);
    $('#table_id').dataTable({
        "processing": true,
        "data": context,
        "deferRender": true
    });



});
    