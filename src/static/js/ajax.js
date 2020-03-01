document.addEventListener('DOMContentLoaded', function () {
    var elems = document.querySelectorAll('.dropdown-trigger');
    var instances = M.Dropdown.init(elems, options);

});

// Or with jQuery

$(document).ready(function () {
    $(".dropdown-trigger").dropdown({ constrainWidth: false, coverTrigger: false});
});

