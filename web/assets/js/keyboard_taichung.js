window.onload = function (e) {
    liff.init(
		data => {
		  // Now you can call LIFF API
            document.getElementById("clear").addEventListener("click", function(i){
                document.getElementById('bus_title').innerHTML = "";
                $('#myTable').empty()
            });
            GetBusAllNum()
		},
		err => {
          // LIFF initialization failed
          console.log('you must use line')
		}
      );
    //   document.getElementById("clear").addEventListener("click", function(i){
    //     document.getElementById('bus_title').innerHTML = "";
    //     $('#myTable').empty()
    // });
    // GetBusAllNum()
}

function GetBusAllNum(){
	$.ajax({
		type: 'GET',
		url: 'https://worldcrater.com/Ahfargo_bus_bot_staging_free_api/bus_all_num',
		dataType: 'json',
		success: function(dict) {
            console.log(dict)
            //1~9的按鍵
			for(var i=0;i<=9;i++){
                document.getElementById("num_"+i).addEventListener("click", function(i){
                    var num = event.target.id
                    var old_bus_title = $("#bus_title").text()
                    var new_bus_title = old_bus_title+num.substring(4);
                    //檢查是否有這輛公車
                    (function(){
                        var count = 0;
                        for (var i=0; i<=dict.length-1; i++){
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
                        for (var i=0; i<=dict.length-1; i++){
                            num_zero=dict[i].RouteName.Zh_tw.substring(0,new_bus_title.length)
                            if (num_zero==new_bus_title){   
                                var row = table.insertRow(count);
                                var cell1 = row.insertCell(0);
                                var cell2 = row.insertCell(1);
                                cell1.innerHTML = dict[i].RouteName.Zh_tw;
                                cell2.innerHTML = dict[i].SubRoutes[0].Headsign;
                                row.className = 'bus_card'
                                cell1.className = 'bus_num'
                                cell2.className = 'bus_name'
                                count = count + 1;
                                }
                        };
                        //將table新增點擊功能
                        var table = document.getElementById("myTable");
                        if (table != null) {
                            for (var i = 0; i < table.rows.length; i++) {
                                table.rows[i].onclick = function () {
                                    var word = $(this).children('td').eq(0).html()
                                    liff.sendMessages([
                                        {
                                          type:'text',
                                          text: word
                                        }
                                      ])
                                      .then(() => {
                                        console.log('message sent');
                                        liff.closeWindow();
                                      })
                                      .catch((err) => {
                                        console.log('error', err);
                                      });
                                };
                            }
                        }
                    })(new_bus_title);
                });
            }
            //公車專用道按鍵
            document.getElementById("bus_lane").addEventListener("click", function(i){
                var bus_title = 300;
                //添加公車列表至table
                (function(bus_title){
                    var count = 0;
                    var table = document.getElementById("myTable");
                    for (var i=0; i<=dict.length-1; i++){
                        var num=parseInt(dict[i].RouteName.Zh_tw.substring(0,3))
                        if (bus_title<=num && num<=bus_title+10){   
                            var row = table.insertRow(count);
                            var cell1 = row.insertCell(0);
                            var cell2 = row.insertCell(1);
                            cell1.innerHTML = dict[i].RouteName.Zh_tw;
                            cell2.innerHTML = dict[i].SubRoutes[0].Headsign;
                            row.className = 'bus_card'
                            cell1.className = 'bus_num'
                            cell2.className = 'bus_name'
                            count = count + 1;
                            }
                        document.getElementById('bus_title').innerHTML = '公車專用道';
                    };
                    //將table新增點擊功能
                    var table = document.getElementById("myTable");
                    if (table != null) {
                        for (var i = 0; i < table.rows.length; i++) {
                            table.rows[i].onclick = function () {
                                var word = $(this).children('td').eq(0).html()
                                liff.sendMessages([
                                    {
                                      type:'text',
                                      text: word
                                    }
                                  ])
                                  .then(() => {
                                    console.log('message sent');
                                    liff.closeWindow();
                                  })
                                  .catch((err) => {
                                    console.log('error', err);
                                  });
                            };
                        }
                    }
                })(bus_title);
            });
		}
	});
}