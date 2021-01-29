var restart = document.getElementById('rs');

var tds = document.body.getElementsByTagName('td');

function clearTable() {
  for (tag of tds) {
    tag.textContent = '';
  }
}
restart.addEventListener('click', clearTable)

for (tag of tds) {
  tag.addEventListener('click', function() {
    if (this.textContent == '') {
      this.textContent = 'X';
    } else if (this.textContent == 'X') {
      this.textContent = 'O';
    } else {
      this.textContent = '';
    }
  })
}
