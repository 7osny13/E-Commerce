
   function saveName() {
    let email = document.getElementsByTagName("input")[1].value;
    let password = document.getElementsByTagName("input")[2].value;
document.cookie = "email=" + email ;
document.cookie = "password=" + password;
}
