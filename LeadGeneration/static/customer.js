$(document).ready(function(){
 $.getJSON('/api/displaycustomer',function(data){
 var htm=`<table class="table">
 <thead>
 <tr>
 <th scope="col">#</th>
      <th scope="col">Name</th>
      <th scope="col">Birth</th>
      <th scope="col">contact</br>details</th>
      <th scope="col">Address</th>
      <th scope="col">Organization</br>Name</th>
      <th scope="col">Picture</th>
      <th scope="col">Make Call</th>
      <th scope="col">Follow Up </th>
      <th scope="col">Modification</th>
  </tr>
  </thead>
  <tbody>
 `
 data.map((item)=>{
 htm+=`<tr>
 <th scope="row">${item.id}</th>
  <td> ${item.firstname} ${item.lastname}</td>
  <td> ${item.dob}</td>
  <td>${item.emailid}<br>${item.mobileno}</td>
  <td> ${item.address}<br>${item.cityname},${item.statename}</td>
  <td> ${item.orgname}</td>
  <td><img src="/${item.photograph}" width="30"></a></td>
  <td><a href="tel:{{item.mobileno}}"><img src="/static/phonecall.png" width="30"> </a> </td>
  <td><a href="/api/callcustomerbyid?customerid=${item.id}">Fill Detail</a> </td>
   <td><a href='/api/customerbyid?customerid=${item.id}'>Update/Delete</a></td>`

 })
  htm+=`
   </tbody>
</table>`
  $('#CustomerData').html(htm)
 })
})