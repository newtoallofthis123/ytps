var modal_popup = document.getElementById("credits")
var modal_btn = document.getElementById("modal_btn")
var modal_close = document.getElementsByClassName("close_modal")[0]

modal_btn.onclick = function(){
  modal_popup.style.display = "block";
}

modal_close.onclick = function(){
  modal_popup.style.display = "none";
}

window.onclick = function(event){
  if (event.target == modal_popup){
    modal_popup.style.display = "none"
  };
}