window.onload = function (e) {
    for(var i=0;i<=9;i++){
        document.getElementById("num_"+i).addEventListener("click", function(i){
            // aa=$("#num_"+i).text()
            num = event.target.id
            // $("#foo2").text();
            old_bus_title = $("#bus_title").text()
            document.getElementById('bus_title').innerHTML = old_bus_title+num.substr(4);
            $('#myTable').empty()
        });
    }
	GetBusAllNum()
}

function GetBusAllNum(){
	$.ajax({
		type: 'GET',
		url: 'http://127.0.0.1:5000/bus_all_num',
		dataType: 'json',
		success: function(dict) {
            console.log(dict)
			document.getElementById("abc").addEventListener("click", function(){
                itclear(dict)
            });
		}
	});
}



function itclear(dict) {
    document.getElementById('sss').value='2'
    console.log('ss');
    $('#myTable').empty()
    console.log('dd')
    var count = 0;
    var table = document.getElementById("myTable");
    for (var i=dict.length-1; i>=0; i--){
        num_zero=dict[i].RouteName.Zh_tw.split("")[0]
        console.log(num_zero)
        console.log(i)
        if (num_zero=='5'){   
            var row = table.insertRow(count);
            // var cell1 = row.insertCell(count);
            // var cell2 = row.insertCell(1);
            // cell1.innerHTML = dict[i].RouteName.Zh_tw;
            row.innerHTML = dict[i].RouteName.Zh_tw;
            // cell2.innerHTML = "NEW CELL2";
            count = count + 1;
            }
        }
}

