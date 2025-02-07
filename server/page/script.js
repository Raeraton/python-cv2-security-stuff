

var password = "szopjala";
function input_password(){
    password = document.getElementById("password-input").value;
    console.log(password)
}






function disp_log( input ){
    let log = input.split( "\n" );

    document.getElementById("outp-div").innerHTML = "";
    for( let a=0;  a<log.length-1;  a++ ){
        let line = log[a].split("\t");

        document.getElementById("outp-div").innerHTML +=    line[0] + "-" + line[1] + "-" + line[2] + "  " +
                                                            line[3] + ":" + line[4] + ":" + line[5] + "  " + line[6] + "sec<br>";
    }
}


function get_log(){
    let xhr = new XMLHttpRequest();
    xhr.open("POST", "/");

    xhr.onreadystatechange = function () {if (xhr.readyState === 4) {
        disp_log( xhr.responseText );
    }};

    xhr.send("LOG")

}