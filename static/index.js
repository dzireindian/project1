document.addEventListener('submit', e =>{
  let mail = document.forms["myForm"]["email"].value;
  let pwrd = document.forms["myForm"]["password"].value;
  let passw = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$@$!%*?&.])[A-Za-z\d$@$!%*?&.]{6, 20}/;
  let cmail = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/

  var m = 0;

  if (!cmail.test(mail)) {
    // console.log(mail);
    // alert(mail)
    document.getElementById('mail-log').innerHTML = "Enter a valid email";
    m = 1;
  }
  else {
    document.getElementById('mail-log').innerHTML = "";
  }



  if (!passw.test(pwrd)) {
    // alert(passw.test(pwrd));
    // alert(pwrd);
    // console.log(passw.test(pwrd));
    // console.log(pwrd);
    document.getElementById("password-log").innerHTML = "Password should contain atleast one [A-Z],[a-z],[1-0],special characters.";
    m=1;
  }
  else {
    document.getElementById('password-log').innerHTML = "";
  }

  if(m!=0)
  {
    // console.log(m);
    // alert(m)
    e.preventDefault();
  }
  else {
    return true;
  }

});

// document.addEventListener('DOMContentLoaded',function() {
//
// });

// function validateForm() {
//
// }
