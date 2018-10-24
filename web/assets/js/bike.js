window.onload = function (e) {
	getQueryVariable("pos",GetBikeInfo)
}

function GetBikeInfo(pos,local_pos,callback){
	$.ajax({
		type: 'GET',
		url: 'https://messfar.com/Ahfargo_bus_bot_staging_free_api/bike?pos='+pos,
		dataType: 'json',
		success: function(dict) {
			console.log(dict)
			callback(local_pos,dict);
		}
	});
}

function initbike(local_pos,dict){
	//init
	var mapObj = new GMaps({
		zoom:15,
		el: "#map",
		lat: parseFloat(local_pos[0]),
		lng: parseFloat(local_pos[1])
	});

	mapObj.addMarker({
		lat: parseFloat(local_pos[0]),
		lng: parseFloat(local_pos[1]),
		title: 'dict[dict_index].StationAddress.Zh_tw',
		icon:{url: './images/pikachu.png',scaledSize: new google.maps.Size(80, 80)},
		infoWindow: {
			content: '你的位置~呱'
		},
		click: function(e) {
			console.log("you click:"+'dict[dict_index].title');
		},
		animation: google.maps.Animation.DROP
	});		

	var timeout = 1;
	for (var dict_index in dict) {	
		// 立即函式(IIFE) Immediately Invoked Function Expression
		(function(index,dict_index) {
			setTimeout(function() { 
				var img = './images/bike liff.png';//dict[dict_index].image;
				var icon = {
				url: img,
				scaledSize: new google.maps.Size(80, 80) 
				};
				
				// Create marker
				mapObj.addMarker({
					lat: dict[dict_index].StationPosition.PositionLat,
					lng: dict[dict_index].StationPosition.PositionLon,
					title: dict[dict_index].StationAddress.Zh_tw,
					icon:icon,
					infoWindow: {
						content: dict[dict_index].StationAddress.Zh_tw+'<br/>'+'可租借數量：'+dict[dict_index].AvailableRentBikes+'<br/>'+'可歸還數量：'+dict[dict_index].AvailableReturnBikes
					},
					click: function(e) {
						console.log("you click:"+'dict[dict_index].title');
					},
					animation: google.maps.Animation.DROP
				});		
			
			}, timeout * 100);
		})(timeout,dict_index);
		
		timeout++;
	}
}