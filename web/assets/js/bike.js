window.onload = function (e) {
	// liff.init(
	// 	data => {
	// 	  // Now you can call LIFF API
	// 	  getQueryVariable_bike("pos",GetBikeInfo);
	// 	},
	// 	err => {
	// 	  // LIFF initialization failed
	// 	}
	//   );
	getQueryVariable_bike("pos",GetBikeInfo);
}

function cityBike(evt, bikeStatus) {
	var i, x, tablinks;
	x = document.getElementsByClassName("tabcontent");
	for (i = 0; i < x.length; i++) {
		x[i].style.display = "none";
	}
	tablinks = document.getElementsByClassName("tablink");
	for (i = 0; i < x.length; i++) {
		tablinks[i].className = tablinks[i].className.replace(" tab-blue", "");
	}
	document.getElementById(bikeStatus).style.display = "block";
	evt.currentTarget.className += " tab-blue";
}

function GetBikeInfo(pos,local_pos,callback){
	$.ajax({
		type: 'GET',
		url: 'APP_URL/bike?pos='+pos,
		dataType: 'json',
		success: function(dict) {
			console.log(dict)
			callback(local_pos,dict);
		}
	});
}

function SearchByGoogleMap(lat,lon,...local_pos){
	console.log("line://app/1586634703-krVJolxJ?api=1&origin="+local_pos[0]+','+local_pos[1]+"&destination="+lat+','+lon)
	liff.openWindow({
		url:"line://app/1586634703-krVJolxJ?api=1&origin="+local_pos[0]+','+local_pos[1]+"&destination="+lat+','+lon,
		external:false
	});
}

function initbike(local_pos,dict){
	//init
	var mapObj = new GMaps({
		zoom:14,
		disableDefaultUI: true,
		el: "#map",
		lat: parseFloat(local_pos[0]),
		lng: parseFloat(local_pos[1])
	});

	mapObj.addMarker({
		lat: parseFloat(local_pos[0]),
		lng: parseFloat(local_pos[1]),
		title: 'dict[dict_index].StationAddress.Zh_tw',
		icon:{url: './images/duck_walk.gif',scaledSize: new google.maps.Size(60, 60)},
		infoWindow: {
			content: '你的位置~呱'
		},
		click: function(e) {
			console.log("you click:"+'dict[dict_index].title');
		},
		// animation: google.maps.Animation.DROP
	});	
	for (var dict_index in dict) {	
		// 立即函式(IIFE) Immediately Invoked Function Expression
		(function(dict_index) {
				var img = './images/stop/bus_egg_'+dict[dict_index].AvailableRentBikes+'.png';//dict[dict_index].image;
				var icon = {
				url: img,
				scaledSize: new google.maps.Size(35, 35) 
				};
				// Create marker
				mapObj.addMarker({
					lat: dict[dict_index].StationPosition.PositionLat,
					lng: dict[dict_index].StationPosition.PositionLon,
					title: "自行車",
					icon:icon,
					infoWindow: {
						content: '可租借數量：'+dict[dict_index].AvailableRentBikes+'<br/>'+'可歸還數量：'+dict[dict_index].AvailableReturnBikes+'<br/><button onclick="SearchByGoogleMap('+dict[dict_index].StationPosition.PositionLat+','+dict[dict_index].StationPosition.PositionLon+','+local_pos+')">帶我去那裡~呱</button>'
					},
					click: function(e) {
						console.log("you click:"+'dict[dict_index].title');
					},
					// animation: google.maps.Animation.DROP
				});		
		})(dict_index);
	}
}