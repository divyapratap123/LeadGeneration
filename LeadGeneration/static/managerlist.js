$(document).ready(function(){
$.getJSON("http://localhost:8000/api/displaymanager",function(data){
    data.map((item)=>{
     $('#managerid').append($('<option>').text(item.managername).val(item.id))

    })
    })
 })