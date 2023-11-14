function addQuantity(element, displayID) {
    const display = document.getElementById(displayID);
    display.classList.add('keep-display');

    if (element.value === '.') {
        // Check if the clicked button value is a dot
        if (!display.value.includes('.')) {
            display.value = display.value + element.value;
        }
    } else {
        display.value = display.value + element.value;
    }

    // display.value = display.value + element.value;
}

// M.AutoInit();

document.addEventListener('DOMContentLoaded', function () {
    const elems = document.querySelectorAll('.sidenav');
    const instances = M.Sidenav.init(elems, {
        // specify options here
        edge: 'right',
    });

    const modal_elems = document.querySelectorAll('.modal');
    const modal_instances = M.Modal.init(modal_elems, {
        // specify options here
        opacity: .8,
        inDuration: 100,
    });

    const fixed_action_btn_elems = document.querySelectorAll('.fixed-action-btn');
    const fixed_action_btn_instances = M.FloatingActionButton.init(fixed_action_btn_elems, {
        // specify options here
        hoverEnabled: false
    });

    const select_instances = M.FormSelect.init(document.querySelectorAll('select'), {
        // specify options here
    });

    const collapsible_elems = document.querySelectorAll('.collapsible');
    const collapsible_instances = M.Collapsible.init(collapsible_elems, {
        // specify options here
    });


});

M.Tabs.init(document.querySelectorAll('.tabs'), {
    // TODO: Fix the height when the swipeable is enable to full screen.
    // swipeable: true,
});