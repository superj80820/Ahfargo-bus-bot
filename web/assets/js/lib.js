function getQueryVariable_bike(variable,callback)
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

function getQueryVariable_bus(variable)
{
    var query = window.location.search.substring(1);
    var vars = query.split("&");
    for (var i=0;i<vars.length;i++) {
            var pair = vars[i].split("=");
            if(pair[0] == variable){
            // return pair[1];
            // alert(pair[1]);
            // callback(,)
            return pair[1]
        }
    }
}

function getLocationCenter(loc1, loc2)
{
    var lat_long = Math.abs(loc2.PositionLat-loc1.PositionLat)/2
    console.log(loc2.PositionLat)
    console.log(loc1.PositionLat)
    var lon_long = Math.abs(loc2.PositionLon-loc1.PositionLon)/2
    var lat = Math.min(loc1.PositionLat,loc2.PositionLat)
    var lon = Math.min(loc1.PositionLon,loc2.PositionLon)
    var lat = lat+lat_long
    var lon = lon+lon_long
    return {lat,lon}
}