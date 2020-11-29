$(document).on("click", ".task-toggle", accFunction);

// var init to store function this
let accThis;
let childEle;

// accordion Function
function accFunction(e) {
  // storing function this in variable
  accThis = this;
  childEle = this.parentElement.parentElement;

  if (this.parentElement.classList.contains("task-open") === true) {
    // Close the clicked accordion
    this.parentElement.classList.remove("task-open");
    this.parentElement.querySelector(".task-body").classList.remove("task-body-active");
  } else {
    // Close the sibling accordions
    closeSiblings();

    // Open the clicked accordion
    this.parentElement.classList.add("task-open");
    this.parentElement.querySelector(".task-body").classList.add("task-body-active");
  }
}

/*
    On toggle Click Check other
    open siblings and close those
    open siblings
*/
function closeSiblings() {
  // checking all the parents with "task-open" class
  for (let i = 0; i <= childEle.childElementCount - 1; i++) {
    if (childEle.children[i].classList.contains("task-open") === true) {
      // checking all the parents children with "task-body-active" class
      for (let j = 0; j <= childEle.children[i].childElementCount - 1; j++) {
        if (childEle.children[i].children[j].classList.contains("task-body-active") === true) {
          // closing 'task-body-active' by removing 'task-body-active' class
          childEle.children[i].classList.remove("task-open");
          childEle.children[i].children[j].classList.remove("task-body-active");
        }
      }
    }
  }
}

$(document).on("click", ".add-task", function () {
  var addTask = `<div class="task-form">
  <div class="task-field">
    <input type="text" id="task-name" class="input-field" placeholder="Task name" />
    <textarea type="text" id="task-desc" class="input-field" placeholder="Task description" ></textarea>
  </div>
  <div class="button-group">
    <button class="add-task-button" disabled>Add task</button>
    <button class="cancel-task-button">Cancel</button>
  </div>
  
  </div>`;
  this.remove();
  $("main").html($("main").html() + addTask);
});

$(document).on("click", ".cancel-task-button", function () {
  var addTask = `      <div class="add-task" >
  <i class="fad fa-plus-circle" style="color: var(--text-primary)"></i>&nbsp;&nbsp; Add task
</div>`;
  this.parentElement.parentElement.remove();
  $("main").html($("main").html() + addTask);
});

$(document).on("keyup", "#task-name,#task-desc", function () {
  if ($("#task-name").val().length > 0 && $("#task-desc").val().length > 0) {
    $(".add-task-button").prop("disabled", false);
  } else {
    $(".add-task-button").prop("disabled", true);
  }
});

$(document).on("click", ".add-task-button", function () {
  var name = $("#task-name").val();
  var desc = $("#task-desc").val();
  var task = `<div class="task-container task-gradient">
    <div class="task-toggle">
      <label>${name}</label>
      <span class="task-indicator"></span>
    </div>
    <div class="task-body">
      <p>
        ${desc}
      </p>
      <div class="task-buttons">
            <button class='start' style="background: mediumseagreen"><i class="fa fa-check"></i> Start</button>
            <button class='delete' style="background: indianred"><i class="fa fa-trash"></i> Delete</button>
          </div>
    </div>
  </div>`;
  var addTask = `      <div class="add-task" >
  <i class="fad fa-plus-circle" style="color: var(--text-primary)"></i>&nbsp;&nbsp; Add task
</div>`;
  $.ajax({
        type: 'POST',
        url: 'add_task/',
        data: {
            'name': name,
            'desc': desc,
            csrfmiddlewaretoken: window.CSRF_TOKEN,
        },
        success: function (data, status, xhttp) {
            window.location.reload()
        }
    });

  this.parentElement.parentElement.remove();
  $("main").html($("main").html() + task + addTask);
});


$(document).on('click', '.task-buttons .delete', function () {
    let id = this.parentElement.parentElement.parentElement.id;
    $.ajax({
        type: 'DELETE',
        url: `/personal/delete_task/${id}`,
        data: {
            csrfmiddlewaretoken: window.CSRF_TOKEN,
        },
        success: function (data, status, xhttp) {
            window.location.reload();
        }
    });
});

$(document).on('click', '.task-buttons .start', function () {
    let id = this.parentElement.parentElement.parentElement.id;
    $.ajax({
        type: 'UPDATE',
        url: `/personal/start_task/${id}`,
        data: {
            csrfmiddlewaretoken: window.CSRF_TOKEN,
        },
        success: function (data, status, xhttp) {
            window.location.reload();
        }
    });
});

$(document).on('click', '.task-buttons .completed', function () {
    let id = this.parentElement.parentElement.parentElement.id;
    $.ajax({
        type: 'UPDATE',
        url: `/personal/complete_task/${id}`,
        data: {
            csrfmiddlewaretoken: window.CSRF_TOKEN,
        },
        success: function (data, status, xhttp) {
            window.location.reload();
        }
    });
});

$(document).on('click', '.filter span', function () {
    let id = this.parentElement.parentElement.parentElement.id;
    $.ajax({
        type: 'DELETE',
        url: `/personal/delete_board/${id}`,
        data: {
            csrfmiddlewaretoken: window.CSRF_TOKEN,
        },
        success: function (data, status, xhttp) {
            window.location = 'http://127.0.0.1:8000/personal/' ;
        }
    });
});