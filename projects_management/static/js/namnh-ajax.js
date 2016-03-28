$(document).ready(function() {
    $('#prg-btn-save').click(function () {
        var employee_ids = new Array();
        var project_id = $('#project_id').val();
        $('#prg-tbl-other-emps').find('input[type="checkbox"]:checked').each(function(){
            id = $(this).attr("record-id");
            employee_ids.push(id);
        });
        console.log(employee_ids);
        $.ajax({
            url: '/projects/add_emps_to_project/' + project_id + '/',
            data: {employee_ids: employee_ids},
            success: function(data) {
                $('#prg-tbl-project-emps').html(data);
            },
            error: function(data) {
                console.log(data);
            }
        });
    });
});