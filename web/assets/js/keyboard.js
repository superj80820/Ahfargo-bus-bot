window.onload = function (e) {
    
    GetBusAllNum()
}

function GetBusAllNum(){
	$.ajax({
		type: 'GET',
		url: 'https://messfar.com/Ahfargo_bus_bot_staging_free_api/bus_all_num',
		dataType: 'json',
		success: function(dict) {
            console.log(dict)
			for(var i=0;i<=9;i++){
                document.getElementById("num_"+i).addEventListener("click", function(i){
                    num = event.target.id
                    old_bus_title = $("#bus_title").text()
                    new_bus_title = old_bus_title+num.substring(4);
                    //檢查是否有這輛公車
                    (function(){
                        var count = 0;
                        for (var i=dict.length-1; i>=0; i--){
                            num_zero=dict[i].RouteName.Zh_tw.substring(0,new_bus_title.length)
                            if (num_zero==new_bus_title){   
                                count = count + 1;
                                }
                        }
                        if (count==0){
                            //None
                        }else{
                            document.getElementById('bus_title').innerHTML = new_bus_title;
                            $('#myTable').empty()
                        }
                    })();
                    //添加公車列表至table
                    (function(new_bus_title){
                        var count = 0;
                        var table = document.getElementById("myTable");
                        for (var i=dict.length-1; i>=0; i--){
                            num_zero=dict[i].RouteName.Zh_tw.substring(0,new_bus_title.length)
                            if (num_zero==new_bus_title){   
                                var row = table.insertRow(count);
                                row.innerHTML = dict[i].RouteName.Zh_tw;
                                count = count + 1;
                                }
                        }
                    })(new_bus_title);
                });
            }
		}
	});
}