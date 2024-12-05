// function drawPattern(character, lines) {
//     for (let i = 1; i <= lines; i++) {
//     console.log(character.repeat(i));
//     }
// }

// drawPattern('%', 6);




function drawPattern(character, lines) {
    let output = '';
    for (let i = 1; i < lines+1; i++) {
        output += character.repeat(i) + '<br>';
    }
    document.getElementById('pattern').innerHTML = output;
}

window.onload = function() {
    drawPattern('*', 6);
};


// function drawPattern(character, lines) {
//     for (let i = 1; i <= lines; i++) {
//     console.log(character.repeat(i));
//     }
//     }
    
//     drawPattern('%', 5);