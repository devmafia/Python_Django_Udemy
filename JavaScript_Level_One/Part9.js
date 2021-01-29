var first_n = prompt("What' s your first name?");
var last_n = prompt("What' s your last name?");
var age = +prompt("how old are you?");
var height = +prompt('how toll are you?');
var pet = prompt("What's your pet's name?");

if ((first_n[0] == last_n[0]) && (age > 20 && age < 30) && (height >= 170) && (pet[pet.length-1] == 'y')) {
  alert('The code is "alpha"');
} else {
  alert("Welcome!")
}
