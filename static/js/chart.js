$(document).ready(function(){
	var createChart = function createChart(seriesOptions) {

		Highcharts.stockChart('chart-container', {
			rangeSelector: {
				selected: 4
			},

			yAxis: {
				labels: {
					formatter: function () {
						return (this.value > 0 ? ' + ' : '') + this.value + '%';
					}
				},
				plotLines: [{
					value: 0,
					width: 2,
					color: 'silver'
				}]
			},

			plotOptions: {
				series: {
					compare: 'percent',
					showInNavigator: true
				}
			},

			tooltip: {
				pointFormat: '<span style="color:{series.color}">{series.name}</span>: <b>{point.y}</b> ({point.change}%)<br/>',
				valueDecimals: 2,
				split: true
			},

			series: seriesOptions
		});
	}


	var chartAjax = function (pk) {
		var data = {
			startdate: $("#startdate").val(),
			enddate: $("#enddate").val()
			};
		console.log('startdate: ' + startdate)
		
		$.ajax({
			"url": "/tasks/" + pk,
			"method": "GET",
			"data": data, 
			"contentType": 'application/json',
			success: function(data) {
						console.log("Data = " + data);
						// timeout(data);
			}
		})
	}


	var timeout = function (pk) {
					setTimeout(function() {
						console.log("End Delay")
						var data = {
							'startdate': $("#startdate").val(),
							'enddate': $("#enddate").val()
							};
						console.log('startdate: ' + $("#startdate").val())
						
						$.ajax({
							"url": "/tasks/" + pk,
							"method": "GET",
							"data": data, 
							"contentType": 'application/json',
							success: function(data) {
								console.log("Data = " + data);
								// timeout(data);
								console.log("IF")
								if (data == 'Waiting') {
									timeout(pk);
								}
								else {
									result = JSON.parse(data)
									console.log("Final Result = " + result)
									datasetFunction(result)
								}

							}
						});
					}, 4000);
	}


	var initAjax = function (
		lp_low, lp_high, 
		pe_low, pe_high, 
		dy_low, dy_high, 
		rsi_buy, rsi_sell,
		startdate, enddate
		) {
		var formData = {
			'lp_low': lp_low,
			'lp_high': lp_high,
			'pe_low': pe_low,
			'pe_high': pe_high,
			'dy_low': dy_low,
			'dy_high': dy_high,
			'rsi_buy': rsi_buy,
			'rsi_sell': rsi_sell,
			'startdate': startdate,
			'enddate': enddate
		}

		$.ajax({
			url: "/filter",
			method: "POST",
			contentType: 'application/json',
			data: JSON.stringify(formData),
			success: function(data) {
						 console.log("Data = " + data);
						 console.log("Start Delay");
						 timeout(data);
			}
		})
	}




	var button = $("#run-backtest");
	console.log("Button = " + button)

	button.on('click', function(event){
		event.preventDefault();
		var lp_low = $("#inputLastPriceLow").val();
		var lp_high = $("#inputLastPriceHigh").val();
		var pe_low = $("#inputPeLow").val();
		var pe_high = $("#inputPeHigh").val();
		var dy_low = $("#inputDivYieldLow").val();
		var dy_high = $("#inputDivYieldHigh").val();
		var rsi_buy = $("#inputRsiBuy").val();
		var rsi_sell = $("#inputRsiSell").val();
		var startdate = $("#startdate").val();
		var enddate = $("#enddate").val();

		// console.log("enddate = " + enddate)

		pk = initAjax(lp_low, lp_high, pe_low, pe_high, 
			dy_low, dy_high, rsi_buy, rsi_sell, startdate, enddate)
	})

	var datasetFunction = function(ajaxData) {
		var realData = [ajaxData['ALGORITHM'], ajaxData['S&P_500']]
		console.log("AjaxData = " + ajaxData)
		var seriesOptions = [],
			realNames = ['ALGORITHM', 'S&P_500']
			seriesCounter = 0,
			names = ['MSFT', 'AAPL']; /* Change names to reflect S&P 500 and Algorithm
		/* Create the chart when all data is loaded @returns {undefined} */

		$.each(names, function (i, name) {

			$.getJSON('https://www.highcharts.com/samples/data/jsonp.php?filename=' + name.toLowerCase() + '-c.json&callback=?', function (data) {

				console.log("Data = ")
				console.log(data)
				seriesOptions[i] = {
					name: realNames[i],
					data: realData[i]
				};
				// As we're loading the data asynchronously, we don't know what order it will arrive. So we keep a counter and create the chart when all the data is loaded.
				seriesCounter += 1;
				console.log("series options = " + seriesOptions)
				if (seriesCounter === names.length) {
					createChart(seriesOptions);
				}
			});
		});
	}



});






