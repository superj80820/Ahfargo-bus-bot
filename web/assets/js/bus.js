realMarkers = [];
realMarkers_temp = [];

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
	var getAllQuery = function(){
		return new Promise(function(resole,reject){
			const BusNum = getQueryVariable_bus("BusNum")
			const City = getQueryVariable_bus("City")
			var Direction = getQueryVariable_bus("Direction")
			resole({BusNum,City,Direction})
		});
	};
	getAllQuery()
	.then(function(all_query){
		console.log(all_query)
		return GetBusInfo(all_query);
	})
	.then(function(object_bus){
		console.log(object_bus)
		return GetBusPath(object_bus.all_query,object_bus.dict_info);
	})
	.then(function(object_bus){
		return initbus(object_bus.all_query,object_bus.dict_info,object_bus.dict_path);
	})
}

function openPage(pageName,elmnt,color) {
	var i, tabcontent, tablinks;
	tabcontent = document.getElementsByClassName("tabcontent");
		for (i = 0; i < tabcontent.length; i++) {
			tabcontent[i].style.display = "none";
		}
	tablinks = document.getElementsByClassName("tablink");
		for (i = 0; i < tablinks.length; i++) {
			tablinks[i].style.backgroundColor = "";
		}
	document.getElementById(pageName).style.display = "block";
	elmnt.style.backgroundColor = color;
}

function refleshMap(all_query,dict_info,origin_length,mapObj,change_action){
	// alert(origin_length)
	// alert(realMarkers.length)
	if(change_action==Math.abs(origin_length-realMarkers.length)){//偵測是否有切換路線
		for (var dict_index in realMarkers) {
			realMarkers[dict_index].setMap(null);//刪除全部的marker
		};
		realMarkers = []
		var timeout = 1;
		for (var dict_index in dict_info[all_query.Direction]) {	
			// 立即函式(IIFE) Immediately Invoked Function Expression
			(function(index,dict_index) {
				setTimeout(function() { 
					var img = './images/bike liff.png';//dict_info[all_query.Direction][dict_index].image;
					var icon = {
					url: img,
					scaledSize: new google.maps.Size(80, 80) 
					};
					// Create marker
					var marker = mapObj.addMarker({
						lat: dict_info[all_query.Direction][dict_index].StopPosition.PositionLat,
						lng: dict_info[all_query.Direction][dict_index].StopPosition.PositionLon,
						title: dict_info[all_query.Direction][dict_index].StopName.Zh_tw,
						icon:icon,
						infoWindow: {
							content: dict_info[all_query.Direction][dict_index].StopName.Zh_tw
						},
						click: function(e) {
							//None
						},
						animation: google.maps.Animation.DROP
					});
					realMarkers.push(marker);
				}, timeout * 15);
			})(timeout,dict_index);
			timeout++;
		}
	}
}

function GetBusInfo(all_query){
	// alert(all_query)
	return new Promise(function(resole,reject){
		$.ajax({
			type: 'GET',
			url: 'https://messfar.com/Ahfargo_bus_bot_staging_free_api/bus?RouteName='+all_query.BusNum+'&City='+all_query.City+'&Direction='+'0',
			dataType: 'json',
			success:function(dict_info) {
				console.log(dict_info)
				resole({all_query,dict_info})
			}
		})	
	})
}
function GetBusPath(all_query,dict_info){
	return new Promise(function(resole,reject){
		$.ajax({
			type: 'GET',
			url: 'https://messfar.com/Ahfargo_bus_bot_staging_free_api/bus_path?bus_num='+all_query.BusNum,
			dataType: 'json',
			success: function(dict_path) {
				// console.log(dict_path)
				resole({all_query,dict_info,dict_path})
			}
		})
	})
}
function initbus(all_query,dict_info,dict_path){
	// alert(bus_num);
	// alert(all_query);
	// alert(dict_path);
	//init
	var mapObj = new GMaps({
		zoom:12,
		el: "#map",
		lat: dict_info[all_query.Direction][Math.floor(dict_info[all_query.Direction].length/4)*3].StopPosition.PositionLat,
		lng: dict_info[all_query.Direction][Math.floor(dict_info[all_query.Direction].length/4)*3].StopPosition.PositionLon,
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
	for (var dict_index in dict_info[all_query.Direction]) {	
		// 立即函式(IIFE) Immediately Invoked Function Expression
		(function(index,dict_index) {
			setTimeout(function() { 
				var img = './images/bike liff.png';//dict_info[all_query.Direction][dict_index].image;
				var icon = {
				url: img,
				scaledSize: new google.maps.Size(80, 80) 
				};
				// Create marker
				var marker = mapObj.addMarker({
					lat: dict_info[all_query.Direction][dict_index].StopPosition.PositionLat,
					lng: dict_info[all_query.Direction][dict_index].StopPosition.PositionLon,
					title: dict_info[all_query.Direction][dict_index].StopName.Zh_tw,
					icon:icon,
					infoWindow: {
						content: dict_info[all_query.Direction][dict_index].StopName.Zh_tw
					},
					click: function(e) {
						//None
					},
					animation: google.maps.Animation.DROP
				});
				realMarkers.push(marker);
			}, timeout * 15);
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
	var change_action = dict_info[0].length - dict_info[1].length
	document.getElementById("tab_1").addEventListener("click", function(i){
		all_query.Direction = 0;
		refleshMap(all_query,dict_info,dict_info[0].length,mapObj,change_action);
	});
	document.getElementById("tab_2").addEventListener("click", function(i){
		all_query.Direction = 1;
		refleshMap(all_query,dict_info,dict_info[1].length,mapObj,change_action);
	});
		
}