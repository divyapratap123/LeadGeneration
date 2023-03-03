$(document).ready(function(){
   $.getJSON('/api/displaymanager',function(data){
    var htm=`<table class="table">
  <thead>
    <tr>
      <th scope="col">#</th>
      <th scope="col">managerid</th>
      <th scope="col">Name</th>
      <th scope="col">birth details</th>
      <th scope="col">Gender</th>
      <th scope="col">Address</th>
      <th scope="col">MobileNo</th>
      <th scope="col">Email Id</th>
      <th scope="col">Picture</th>
      <th scope="col">Update</th>





    </tr>
  </thead>
  <tbody>`
  data.map((item)=>{
  htm+=`<tr>
   <th scope="row">${item.id}</th>
   <td> ${item.managerid}</td>
   <td> ${item.managername}</td>
   <td> ${item.dob}</td>
   <td> ${item.gender}</td>
  <td> ${item.address}<br>${item.cityname},${item.statename}</td>
  <td>${item.mobileno}</td>
   <td>${item.emailid}</td>
  <td><a href='/api/display_manager_picture?mid=${item.id}&managername=${item.managername}&picture=${item.photograph}'> <img src="/${item.photograph}" width="30"></a></td>
   <td><a href='/api/managerbyid?managerid=${item.id}'>Update/Delete</a></td>`

  })

    htm+=`
   </tbody>
</table>`
  $('#ManagerData').html(htm)
  })

})