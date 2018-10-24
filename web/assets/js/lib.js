function getQueryVariable(variable,callback)
{
       var query = window.location.search.substring(1);
       var vars = query.split("&");
       for (var i=0;i<vars.length;i++) {
               var pair = vars[i].split("=");
               if(pair[0] == variable){
                var local_pos = pair[1].split("and")
                // return pair[1];
                // alert(pair[1]);
                callback(pair[1],local_pos,initbike)
            }
       }
    // alert('false');
    //return(false);
}