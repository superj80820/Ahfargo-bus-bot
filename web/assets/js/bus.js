realMarkers = [];
carMarkers = [];
carMarkers_pos = [];

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
	// var _width =0;
	// setInterval(function(){
	// 	_width +=0.014
	// 	if(_width>=100){_width=0;}
	// 		document.getElementsByClassName("time")[0].style.width=_width+"%";
	// })

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
		initbus(object_bus.all_query,object_bus.dict_info,object_bus.dict_path);
		document.getElementsByClassName("update_time")[0].style.width=0+"%";
		update_bar(object_bus)
	})
}

function update_bar(object_bus){
	var bar_len = parseFloat(document.getElementsByClassName("update_time")[0].style.width)
	bar_len += 1/5
	document.getElementsByClassName("update_time")[0].style.width=bar_len+"%";
	// console.log(bar_len)
	if(bar_len>=100){
		document.getElementsByClassName("update_time")[0].style.width=0+"%";
		GetBusInfo(object_bus.all_query)
		.then(() => {
			update_bar(object_bus)
		})
		return
	}
	setTimeout(() => {update_bar(object_bus)}, 60);
}


function openCity(evt, cityName) {
	var i, x, tablinks;
	x = document.getElementsByClassName("tabcontent");
	for (i = 0; i < x.length; i++) {
		x[i].style.display = "none";
	}
	tablinks = document.getElementsByClassName("tablink");
	for (i = 0; i < x.length; i++) {
		tablinks[i].className = tablinks[i].className.replace(" tab-blue", "");
	}
	document.getElementById(cityName).style.display = "block";
	evt.currentTarget.className += " tab-blue";
}

function refleshMap(all_query,dict_info,origin_length,mapObj,change_action){
	// alert(origin_length)
	// alert(realMarkers.length)
	carMarkers_pos = []
	for (var index in carMarkers) {
		// alert(index)
		carMarkers[index].setMap(null);
	}
	carMarkers = []
	if(change_action==Math.abs(origin_length-realMarkers.length)){//偵測是否有切換路線
		for (var dict_index in realMarkers) {
			realMarkers[dict_index].setMap(null);//刪除全部的marker
		};
		realMarkers = []
		var timeout = 1;
		// alert(dict_info[all_query.Direction].length)
		// alert(all_query.Direction)
		for (var dict_index in dict_info[all_query.Direction]) {	
			// 立即函式(IIFE) Immediately Invoked Function Expression
			(function(index,dict_index){ 
				var img = './images/stop/bus_egg_'+index+'.png';//dict_info[all_query.Direction][dict_index].image;
				var icon = {
				url: img,
				scaledSize: new google.maps.Size(23, 23) 
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
						// alert(event.target.id)
						if(all_query.Direction == 0){
							var $objTr = $("#bus_list_1_"+dict_index); //找到要定位的地方  tr 
							// $objTr.css("background-color","lightgray"); //设置要定位地方的css 
							var objTr = $objTr[0]; //转化为dom对象 
							console.log(objTr)
							$("#Goto").animate({scrollTop:objTr.offsetTop},"slow"); //定位tr 
						}
						else if (all_query.Direction == 1){
							var $objTr = $("#bus_list_2_"+dict_index); //找到要定位的地方  tr 
							// $objTr.css("background-color","lightgray"); //设置要定位地方的css 
							var objTr = $objTr[0]; //转化为dom对象 
							console.log(objTr)
							$("#Goback").animate({scrollTop:objTr.offsetTop},"slow"); //定位tr 
						}
					},
					// animation: google.maps.Animation.DROP
				});
				realMarkers.push(marker);
			})(timeout,dict_index);
			timeout++;			
			// alert(all_query.Direction)
			if (dict_info[all_query.Direction][dict_index].BusPosition != undefined){
				if (carMarkers_pos.indexOf(dict_info[all_query.Direction][dict_index].BusPosition.PositionLat) == -1){
					// console.log(dict_info[all_query.Direction][dict_index].BusPosition.PositionLat)
					// console.log(dict_info[all_query.Direction][dict_index].BusPosition.PositionLon)
					carMarkers_pos.push(dict_info[all_query.Direction][dict_index].BusPosition.PositionLat)
					updateCar(dict_info[all_query.Direction][dict_index].BusPosition.PositionLat,dict_info[all_query.Direction][dict_index].BusPosition.PositionLon,dict_info[all_query.Direction][dict_index].PlateNumb,all_query.Direction,dict_index);
				}
			}
		}
	}
}

function GetBusInfo(all_query){
	// alert(all_query)
	// document.getElementsByClassName("time")[0].style.width=0+"%";
	// update_bar();
	return new Promise(function(resole,reject){
		$.ajax({
			type: 'GET',
			url: 'https://worldcrater.com/Ahfargo_bus_bot_api/bus?RouteName='+all_query.BusNum+'&City='+all_query.City+'&Direction='+'0',
			dataType: 'json',
			success:function(dict_info) {
				$('#tabcontent1').empty();
				$('#tabcontent2').empty();
				document.getElementById("tablink1").innerText = "往 "+dict_info[2][0].DestinationStopNameZh;
				document.getElementById("tablink2").innerText = "往 "+dict_info[2][0].DepartureStopNameZh;
				(function(dict_info){
					// console.log(dict_info)
					var count = 0;
					var table1 = document.getElementById("tabcontent1");
					var table2 = document.getElementById("tabcontent2");
					var create_list = function(dict_info,list_index,table){
						for (var i=dict_info[list_index].length-1; i>=0; i--){
							var row = table.insertRow(count);
							var cell1 = row.insertCell(0);
							var cell2 = row.insertCell(1);
							var cell3 = row.insertCell(2);
							if(list_index == 0){
								row.id = "bus_list_1_"+i
							}
							else if(list_index == 1){
								row.id = "bus_list_2_"+i
							}
							cell1.innerHTML = parseInt(dict_info[list_index][i].EstimateTime)/60 + '分';
							if (dict_info[list_index][i].EstimateTime == undefined){
								if (cell1.innerHTML = dict_info[list_index][i].NextBusTime == undefined){
									cell1.innerHTML = "離駛"
									cell1.className = 'bus_time bus_time_gray'
									cell3.innerHTML = "";
								}else{
									cell1.innerHTML = dict_info[list_index][i].NextBusTime.substr(11,5);
									cell1.className = 'bus_time bus_time_gray'
									cell3.innerHTML = "";
								}
							}else{
								if (0<=parseInt(dict_info[list_index][i].EstimateTime) && parseInt(dict_info[list_index][i].EstimateTime)<240){
									if (0<=parseInt(dict_info[list_index][i].EstimateTime) && parseInt(dict_info[list_index][i].EstimateTime)<120){
										cell1.innerHTML = "進站中";
										cell1.className = 'bus_time bus_time_red'
										if (dict_info[list_index][i-1].PlateNumb != dict_info[list_index][i].PlateNumb){
											cell3.innerHTML = dict_info[list_index][i].PlateNumb;
											cell3.className = 'bus_num'
											if (realMarkers != 0){
												carMarkers_pos = []
												for (var index in carMarkers) {
													// alert(index)
													carMarkers[index].setMap(null);
												}
												carMarkers = []
												for (var dict_index in dict_info[all_query.Direction]) {
													if (dict_info[all_query.Direction][dict_index].BusPosition != undefined){
														if (carMarkers_pos.indexOf(dict_info[all_query.Direction][dict_index].BusPosition.PositionLat) == -1){
															// console.log(dict_info[all_query.Direction][dict_index].BusPosition.PositionLat)
															// console.log(dict_info[all_query.Direction][dict_index].BusPosition.PositionLon)
															carMarkers_pos.push(dict_info[all_query.Direction][dict_index].BusPosition.PositionLat)
															updateCar(dict_info[all_query.Direction][dict_index].BusPosition.PositionLat,dict_info[all_query.Direction][dict_index].BusPosition.PositionLon,dict_info[all_query.Direction][dict_index].PlateNumb,all_query.Direction,dict_index);
														}
													}
												}
											}
										}
									}else{
										cell1.innerHTML = "即將進站";
										cell1.className = 'bus_time bus_time_red'
										if (dict_info[list_index][i-1].PlateNumb != dict_info[list_index][i].PlateNumb){
											cell3.innerHTML = dict_info[list_index][i].PlateNumb;
											cell3.className = 'bus_num'
											if (realMarkers != 0){
												carMarkers_pos = []
												for (var index in carMarkers) {
													// alert(index)
													carMarkers[index].setMap(null);
												}
												carMarkers = []
												for (var dict_index in dict_info[all_query.Direction]) {
													if (dict_info[all_query.Direction][dict_index].BusPosition != undefined){
														if (carMarkers_pos.indexOf(dict_info[all_query.Direction][dict_index].BusPosition.PositionLat) == -1){
															// console.log(dict_info[all_query.Direction][dict_index].BusPosition.PositionLat)
															// console.log(dict_info[all_query.Direction][dict_index].BusPosition.PositionLon)
															carMarkers_pos.push(dict_info[all_query.Direction][dict_index].BusPosition.PositionLat)
															updateCar(dict_info[all_query.Direction][dict_index].BusPosition.PositionLat,dict_info[all_query.Direction][dict_index].BusPosition.PositionLon,dict_info[all_query.Direction][dict_index].PlateNumb,all_query.Direction,dict_index);
														}
													}
												}
											}
										}
									}
								}
								else if(parseInt(dict_info[list_index][i].EstimateTime)<0){
									cell1.innerHTML = "離駛";
									cell1.className = 'bus_time bus_time_gray'
									cell3.innerHTML = "";
								}else{
									cell1.innerHTML = parseInt(dict_info[list_index][i].EstimateTime)/60 + '分';
									cell1.className = 'bus_time bus_time_green'
									cell3.innerHTML = "";
								}
							}
							cell2.innerHTML = dict_info[list_index][i].StopName.Zh_tw;
							cell2.className = 'bus_name'
						};
						//將table新增點擊功能
						if (list_index == 0){
							for (var i = 0; i < table1.rows.length; i++) {
								table1.rows[i].onclick = function () {
									for (var i = 0; i < table1.rows.length; i++) {
										realMarkers[i].infoWindow.close(realMarkers,realMarkers[i])
									}
									var marker_index = $(this).index();
									realMarkers[marker_index].infoWindow.open(realMarkers,realMarkers[marker_index])
								};
							}
						}
						else if (list_index == 1){
							for (var i = 0; i < table2.rows.length; i++) {
								table2.rows[i].onclick = function () {
									var table2 = document.getElementById("tabcontent2");
									for (var i = 0; i < table2.rows.length; i++) {
										realMarkers[i].infoWindow.close(realMarkers,realMarkers[i])
									}
									var marker_index = $(this).index();
									realMarkers[marker_index].infoWindow.open(realMarkers,realMarkers[marker_index])
								};
							}
						}
					}
					create_list(dict_info,0,table1);
					create_list(dict_info,1,table2);
				})(dict_info);
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
			url: 'https://worldcrater.com/Ahfargo_bus_bot_api/bus_path?bus_name='+all_query.BusNum,
			dataType: 'json',
			success: function(dict_path) {
				// console.log(dict_path)
				resole({all_query,dict_info,dict_path})
			},
			error: function(result) {
				dict_path = {Geometry0:[],Geometry1:[]}
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
	var loc1 = dict_info[all_query.Direction][dict_info[all_query.Direction].length-1].StopPosition
	var loc2 = dict_info[all_query.Direction][0].StopPosition
	var	camera = getLocationCenter(loc1,loc2)
	mapObj = new GMaps({
		zoom:12,
		disableDefaultUI: true,
		el: "#map",
		lat: camera.lat,
		lng: camera.lon
	});

	var timeout = 1;
	for (var dict_index in dict_info[all_query.Direction]) {	
		// 立即函式(IIFE) Immediately Invoked Function Expression
		(function(index,dict_index) { 
			var img = './images/stop/bus_egg_'+index+'.png';//dict_info[all_query.Direction][dict_index].image;
			var icon = {
			url: img,
			scaledSize: new google.maps.Size(23, 23) 
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
					// alert(event.target.id)
					if(all_query.Direction == 0){
						var $objTr = $("#bus_list_1_"+dict_index); //找到要定位的地方  tr 
						// $objTr.css("background-color","lightgray"); //设置要定位地方的css 
						var objTr = $objTr[0]; //转化为dom对象 
						console.log(objTr)
						$("#Goto").animate({scrollTop:objTr.offsetTop},"slow"); //定位tr 
					}
					else if (all_query.Direction == 1){
						var $objTr = $("#bus_list_2_"+dict_index); //找到要定位的地方  tr 
						// $objTr.css("background-color","lightgray"); //设置要定位地方的css 
						var objTr = $objTr[0]; //转化为dom对象 
						console.log(objTr)
						$("#Goback").animate({scrollTop:objTr.offsetTop},"slow"); //定位tr 
					}
				},
				// animation: google.maps.Animation.DROP
			});
			realMarkers.push(marker);
		})(timeout,dict_index);
		timeout++;
		if (dict_info[all_query.Direction][dict_index].BusPosition != undefined){
			if (carMarkers_pos.indexOf(dict_info[all_query.Direction][dict_index].BusPosition.PositionLat) == -1){
				// console.log(dict_info[all_query.Direction][dict_index].BusPosition.PositionLat)
				// console.log(dict_info[all_query.Direction][dict_index].BusPosition.PositionLon)
				carMarkers_pos.push(dict_info[all_query.Direction][dict_index].BusPosition.PositionLat)
				updateCar(dict_info[all_query.Direction][dict_index].BusPosition.PositionLat,dict_info[all_query.Direction][dict_index].BusPosition.PositionLon,dict_info[all_query.Direction][dict_index].PlateNumb,all_query.Direction,dict_index);
			}
		}
	}

	// //path
	var polyline = dict_path.Geometry0;
	mapObj.drawPolyline({
	path: polyline,
	strokeColor: '#0033cc',
	strokeOpacity: 0.5,
	strokeWeight: 5,
	});
	var change_action = Math.abs(dict_info[0].length - dict_info[1].length)
	document.getElementById("tablink1").addEventListener("click", function(i){
		all_query.Direction = 0;
		refleshMap(all_query,dict_info,dict_info[0].length,mapObj,change_action);
	});
	document.getElementById("tablink2").addEventListener("click", function(i){
		all_query.Direction = 1;
		refleshMap(all_query,dict_info,dict_info[1].length,mapObj,change_action);
	});
		
}

function updateCar(lat,lng,plate_numb,list_index,dict_index){
	var img = './images/duck_walk.gif';//dict_info[all_query.Direction][dict_index].image;
	var icon = {
	url: img,
	scaledSize: new google.maps.Size(50, 50) 
	};
	// Create marker
	var marker = mapObj.addMarker({
		lat: lat,
		lng: lng,
		title: 'car',
		icon:icon,
		infoWindow: {
			content: '公車:'+plate_numb
		},
		click: function(e) {
			if(list_index == 0){
				var $objTr = $("#bus_list_1_"+dict_index); //找到要定位的地方  tr 
				// $objTr.css("background-color","lightgray"); //设置要定位地方的css 
				var objTr = $objTr[0]; //转化为dom对象 
				console.log(objTr)
				$("#Goto").animate({scrollTop:objTr.offsetTop},"slow"); //定位tr 
			}
			else if (list_index == 1){
				var $objTr = $("#bus_list_2_"+dict_index); //找到要定位的地方  tr 
				// $objTr.css("background-color","lightgray"); //设置要定位地方的css 
				var objTr = $objTr[0]; //转化为dom对象 
				console.log(objTr)
				$("#Goback").animate({scrollTop:objTr.offsetTop},"slow"); //定位tr 
			}
		},
		// animation: google.maps.Animation.DROP
	});
	carMarkers.push(marker);
}