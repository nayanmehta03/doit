$(document).on("click", "#plus-card", function () {
    this.parentElement.remove();
    let card = `<div class="card add-form">
    <div class="input-field">
      <div class="svg-container start">
        <i class="fad fa-heading"></i>
      </div>
      <input type="text" placeholder="Board Title" id="board-title" />
    </div>
    <div class="input-field textarea">
      <div class="svg-container start">
        <i class="fa fa-text-size"></i>
      </div>
      <textarea id="board-desc" placeholder="Board Description"></textarea>
    </div>
    <div class="button-group">
      <button id='add-button'>Add</button>
      <button id='cancel-button'>Cancel</button>
    </div>
  </div>`;

    document.getElementsByClassName("boards")[0].innerHTML += card;
});

$(document).on("click", "#cancel-button", function () {
    let plusCard = `      <div class="card new-board">
    <div id="plus-card">
    <i class="fa fa-plus"></i>
    </div>
  </div>`;
    this.parentElement.parentElement.remove();
    document.getElementsByClassName("boards")[0].innerHTML += plusCard;
});

$(document).on("click", "#add-button", function () {
    var plusCard = `      <div class="card new-board">
    <div id="plus-card">
    <i class="fa fa-plus"></i>
    </div>
  </div>`;

    let bTitle = $("#board-title").val();
    let bDesc = $("#board-desc").val();
    let date = new Date();
    let card = `<div class="card">
    <div class="additional" style="background: linear-gradient(#ff7eee, #df49a6)">
      <div class="more-info">
        <h1>${bTitle}</h1>
        <div class="coords">
          <span>Made on ${date}</span>
          <p>${bDesc}</p>
        </div>
        <div class="stats">
          <div>
            <div class="title">Total</div>
            <div class="value">25</div>
          </div>
          <div>
            <div class="title">Completed</div>
            <div class="value">13</div>
          </div>
          <div>
            <div class="title">Ongoing</div>
            <div class="value">2</div>
          </div>
        </div>
      </div>
    </div>
    <div class="general">
      <h1>${bTitle}</h1>
    </div>
  </div>`;

    $.ajax({
        type: 'POST',
        url: 'add-board/',
        data: {
            'name': bTitle,
            'desc': bDesc,
            csrfmiddlewaretoken: window.CSRF_TOKEN,
        },
        success: function (data, status, xhttp) {
            window.location = data.url
        }
    });

    this.parentElement.parentElement.remove();
    document.getElementsByClassName("boards")[0].innerHTML += card;
    document.getElementsByClassName("boards")[0].innerHTML += plusCard;
});

