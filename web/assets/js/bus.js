window.onload = function (e) {
	// liff.init(
	// 	data => {
	// 	  // Now you can call LIFF API
	// 	  getQueryVariable("pos",GetBikeInfo);
	// 	},
	// 	err => {
	// 	  // LIFF initialization failed
	// 	}
	//   );
	// alert('ssss')
	getQueryVariable_bus("BusNum",GetBusInfo)
	.then(function(object_bus){
		return GetBusPath(object_bus.bus_num,object_bus.dict_info);
	})
	.then(function(object_bus){
		initbus(object_bus.bus_num,object_bus.dict_info,object_bus.dict_path);
	})
	;
}

function GetBusInfo(bus_num){
	return new Promise(function(resole,reject){
		$.ajax({
			type: 'GET',
			url: 'https://messfar.com/Ahfargo_bus_bot_staging_free_api/bus?RouteName='+bus_num+'&City=Taichung',
			dataType: 'json',
			success:function(dict_info) {
				console.log(dict_info)
				// callback(bus_num,dict_info,initbus);
				resole({bus_num,dict_info})
			}
		})	
	})
}

function GetBusPath(bus_num,dict_info){
	return new Promise(function(resole,reject){
		$.ajax({
			type: 'GET',
			url: 'https://messfar.com/Ahfargo_bus_bot_staging_free_api/bus_path?bus_num='+bus_num,
			dataType: 'json',
			success: function(dict_path) {
				console.log(dict_path)
				// callback(bus_num,dict_info,dict_path);
				resole({bus_num,dict_info,dict_path})
			}
		})
	})
}

function initbus(bus_num,dict_info,dict_path){
	// alert(bus_num);
	// alert(dict_info);
	// alert(dict_path);
	//init
	var mapObj = new GMaps({
		zoom:13,
		el: "#map",
		lat: 24.1476340001091,
		lng: 120.683205999757
	});

	// //pokemons
	// var pokemons = {
	// 	pokemon1:{
	// 		lat: 22.604189, 
	// 		lng: 120.310286,  
	// 		content:'<img class="circle_img" src="pikachu.png" alt="pikachu" style="border: 3px solid #FF3333">',	  
	// 		image:'pikachu.png',
	// 		title:'pikachu'
	// 	},
	// 	pokemon2:{
	// 		lat: 22.618137, 
	// 		lng: 120.302434, 
	// 		content:'<img class="circle_img" src="snorlax.png" alt="snorlax" style="border: 3px solid #003C9D">',	  
	// 		image:'snorlax.png',
	// 		title:'snorlax'
	// 	},
	// 	pokemon3:{
	// 		lat: 22.624310, 
	// 		lng: 120.299419, 
	// 		content:'<img class="circle_img" src="charizard.png" alt="charizard" style="border: 3px solid #D28EFF">',	  
	// 		image:'charizard.png',
	// 		title:'charizard'
	// 	},
	// };


	// //circle
	// var circle_map={
	// 	circle1:{
	// 		lat: 22.615137,  
	// 		lng: 120.305386, 
	// 		radius:150,	//m
	// 		color:"#FF3333",
	// 	},
	// 	circle2:{
	// 		lat: 22.615537,
	// 		lng: 120.302434, 
	// 		radius:100,	//m   
	// 		color:"#003C9D",
	// 	},
	// 	circle3:{
	// 		lat: 22.614310, 
	// 		lng: 120.297419, 
	// 		radius:250,	//m
	// 		color:"#D28EFF",
	// 	},
		
	// };


	// //path
	// var paths={
	// 	path1:{
	// 		circle_lat:circle_map["circle1"].lat,
	// 		circle_lng:circle_map["circle1"].lng,
	// 		pokemon_lat:pokemons["pokemon1"].lat, 
	// 		pokemon_lng:pokemons["pokemon1"].lng,  
	// 		color:circle_map["circle1"].color,
	// 	},
	// 	path2:{
	// 		circle_lat:circle_map["circle2"].lat,
	// 		circle_lng:circle_map["circle2"].lng,
	// 		pokemon_lat:pokemons["pokemon2"].lat, 
	// 		pokemon_lng:pokemons["pokemon2"].lng,  
	// 		color:circle_map["circle2"].color,
	// 	},
	// 	path3:{
	// 		circle_lat:circle_map["circle3"].lat,
	// 		circle_lng:circle_map["circle3"].lng,
	// 		pokemon_lat:pokemons["pokemon3"].lat, 
	// 		pokemon_lng:pokemons["pokemon3"].lng,  
	// 		color:circle_map["circle3"].color,
	// 	},
		
	// }

		
					
	// for (var pokemon in pokemons) {	
	// 	var img = pokemons[pokemon].image;
	// 	var icon = {
	// 	url: img,
	// 	//anchor: new google.maps.Point(40, 45),
	// 	scaledSize: new google.maps.Size(80, 80) 
	// 	};

	// 	// Create marker
	// 	mapObj.addMarker({
	// 		lat: pokemons[pokemon].lat,
	// 		lng: pokemons[pokemon].lng,
	// 		title: pokemons[pokemon].title,
	// 		icon:icon,
	// 		infoWindow: {
	// 			content: pokemons[pokemon].content,
	// 		},
	// 		click: function(e) {
	// 			console.log("you click:"+pokemons[pokemon].title);
	// 		}
	// 	});	
	// }
	
	
	// //circle
	// for (var circle in circle_map) {
	// 	mapObj.drawCircle({
	// 	strokeColor: circle_map[circle].color,
	// 	strokeOpacity: 0.8, 
	// 	strokeWeight: 4,
	// 	fillColor: circle_map[circle].color, 
	// 	fillOpacity: 0.35,	  
	// 	lat: circle_map[circle].lat,
	// 	lng: circle_map[circle].lng,
	// 	radius: circle_map[circle].radius,
	// 	});
	// 	}

	var timeout = 1;
	for (var dict_index in dict_info.Direction1.data) {	
		// 立即函式(IIFE) Immediately Invoked Function Expression
		(function(index,dict_index) {
			setTimeout(function() { 
				var img = './images/bike liff.png';//dict_info.Direction1.data[dict_index].image;
				var icon = {
				url: img,
				scaledSize: new google.maps.Size(80, 80) 
				};
				
				// Create marker
				mapObj.addMarker({
					lat: dict_info.Direction1.data[dict_index].StopPosition.PositionLat,
					lng: dict_info.Direction1.data[dict_index].StopPosition.PositionLon,
					title: dict_info.Direction1.data[dict_index].sent_name1.Zh_tw,
					icon:icon,
					infoWindow: {
						content: 'test'
						// dict_info.Direction1.data[dict_index].sent_name1.Zh_tw+'<br/>'+'可租借數量：'+dict_info.Direction1.data[dict_index].AvailableRentBikes+'<br/>'+'可歸還數量：'+dict_info.Direction1.data[dict_index].AvailableReturnBikes+'<br/><button onclick="SearchByGoogleMap('+dict_info.Direction1.data[dict_index].StopPosition.PositionLat+','+dict_info.Direction1.data[dict_index].StopPosition.PositionLon+')">帶我去那裡~呱</button>'
					},
					click: function(e) {
						console.log("you click:"+'dict_info.Direction1.data[dict_index].title');
					},
					animation: google.maps.Animation.DROP
				});		
			
			}, timeout * 100);
		})(timeout,dict_index);
		timeout++;
	}
	
	// //path
	var polyline = dict_path.Geometry0;
	mapObj.drawPolyline({
	path: polyline,
	strokeColor: '#131540',
	strokeOpacity: 1.0,
	strokeWeight: 1.5,
	});
		
}