// fetch('secrets.txt')
//   .then(response => response.text())
//   .then(data => {
//   	// Do something with your data
//   	console.log(data);
//   });

const TODOIST_TOKEN = '';
const PROJECT_ID = '2242454039';

function onDragStart(event) {
  event
    .dataTransfer
    .setData('text/plain', event.target.id);

    event
    .currentTarget
    .style
    .backgroundColor = 'yellow';
}

function onDragOver(event) {
  event.preventDefault();
}

function onDrop(event) {
  const id = event
    .dataTransfer
    .getData('text');

    const draggableElement = document.getElementById(id);
    const dropzone = event.target;
    dropzone.appendChild(draggableElement);

    const priority = parseInt(dropzone.id);

    const postData = {
      "priority": priority
  };

    var apiUrl = "https://api.todoist.com/rest/v1/tasks/"+draggableElement.id.toString();
fetch(apiUrl, { 
method: 'post', 
 body:JSON.stringify(postData),
headers: new Headers({
  "Content-Type": "application/json",
'Authorization': 'Bearer '+TODOIST_TOKEN, 
})})
    
    event
    .dataTransfer
    .clearData();
}

const tasks = [];
const parentElement = document.getElementById('tasks');

var apiUrl = "https://api.todoist.com/rest/v1/tasks?project_id="+PROJECT_ID;
fetch(apiUrl, { 
method: 'get', 

headers: new Headers({
'Authorization': 'Bearer '+TODOIST_TOKEN, 
})}).then(response => {
  return response.json();
}).then(data => {
  // Work with JSON data here
  for (item in data) {
      tasks.push({id: data[item]['id'], content: data[item]['content'], priority: data[item]['priority']});

      // Add child elements  
  }

  for (let bookmark of tasks) {
    const childElement = document.createElement('div');
    childElement.id = bookmark.id.toString()
    childElement.className = "example-draggable"
    childElement.draggable = "true"

    childElement.setAttribute('ondragstart', 'onDragStart(event);')

    const appendChildElement = parentElement.appendChild(childElement)
    appendChildElement.innerHTML = bookmark.content.substring(0,10);

  } 

}).catch(err => {
  // Do something for an error here
});


