// PART 4 ARRAY EXERCISE
// This is  a .js file with commented hints, its optional to use this.

// Create Empty Student Roster Array
// This has been done for you!
var roster = []

// Create the functions for the tasks

// ADD A NEW STUDENT

function addStudent() {
  var student = prompt('Type a name');
  roster.push(student)
}

// Create a function called addNew that takes in a name
// and uses .push to add a new student to the array


// REMOVE STUDENT

function removeStudent() {
  var student = prompt('What Student?');
  for (var i = 0; i < roster.length; i++) {
    if(roster[i] == student) {
      roster.splice(i ,1)
    }
  }
}

// Create a function called remove that takes in a name
// Finds its index location, then removes that name from the roster

// HINT: http://stackoverflow.com/questions/5767325/how-to-remove-a-particular-element-from-an-array-in-javascript
//

// DISPLAY ROSTER

function display() {
  console.log(roster);
}

// Create a function called display that prints out the orster to the console.

// Start by asking if they want to use the web app

var start = prompt('Do you want to use the web app?');

if(start == 'y') {
  while(true) {
    var func = prompt('Select an action');
    if (func == 'add') addStudent();
    else if (func == 'remove') removeStudent();
    else if (func == 'display') display();
    else if (func == 'quit') break;
  }
} else if(start == 'n') {
  alert('Hope to see you soon!');
}
// Now create a while loop that keeps asking for an action (add,remove, display or quit)
// Use if and else if statements to execute the correct function for each command.
