

document.addEventListener('DOMContentLoaded', () => {


    const source = document.querySelector(".actions label:nth-of-type(1) select");
    const target = document.querySelector(".actions label:nth-of-type(2)");
    
    const displayWhenSelected = (source, value, target) => {
        const selectedIndex = source.selectedIndex;
        const isSelected = source[selectedIndex].value === value;
        console.log(value, isSelected)
        target.classList[isSelected
            ? "add"
            : "remove"
        ]("show");
    };

    source.addEventListener("change", (evt) =>
        displayWhenSelected(source, "enroll_student", target)
    );

    
}, false);