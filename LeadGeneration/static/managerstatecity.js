$(document).ready(function(){
  $.getJSON("http://localhost:8000/api/managerstatelist",function(data){
    data.map((item)=>{
     $('#inputstate').append($('<option>').text(item.statename).val(item.stateid))

    })
  })
$('#inputstate').change(function(){
   $.getJSON("http://localhost:8000/api/managercitylist",{"stateid":$('#inputstate').val()},function(data){

    $('#inputcity').empty()
    $('#inputcity').append($('<option>').text('Choose city....'))
    data.map((item)=>{
     $('#inputcity').append($('<option>').text(item.cityname).val(item.cityid))
    })


   })

})
})