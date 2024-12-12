// static/employees/js/employee_admin.js

(function($) {
    $(document).ready(function() {
        // Get the company select field and department select field
        var companyField = $('#id_company');
        console.log('company', companyField)
        var departmentField = $('#id_department');

        // Listen for changes on the company field
        companyField.change(function() {
            var companyId = $(this).val();  // Get the selected company ID
            console.log('companyId', companyId)

            if (companyId) {
                // Make an AJAX request to fetch departments based on the selected company
                $.ajax({
                    url: '/employees/department_choices/',  // Custom URL to fetch departments
                    data: { 'company_id': companyId },  // Send the selected company ID
                    success: function(response) {
                        // Empty the department field and populate with new options
                        departmentField.empty();  // Clear current departments
                        departmentField.append('<option value="">---------</option>');  // Add a default "Select" option
                        $.each(response.departments, function(index, department) {
                            departmentField.append('<option value="' + department.id + '">' + department.name + '</option>');
                        });
                    },
                    error: function() {
                        alert("Error fetching departments.");
                    }
                });
            } else {
                // If no company selected, clear the department field
                departmentField.empty();
            }
        });

        // Trigger the change event on page load if a company is already selected
        companyField.trigger('change');
    });
})(django.jQuery);
