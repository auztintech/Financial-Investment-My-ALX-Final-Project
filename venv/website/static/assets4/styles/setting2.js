$(document).ready(function(){

	

	  //calculator1//
    
    
	

	function calc(){
	    var percent 	= [107];
		var minMoney 	= [50];
		var maxMoney	= [160000];

		if($("#amount").val().length == 0){
			$("#amount").val(minMoney[0]);
		}

		amount = parseFloat($("#amount").val());
		id = -1;
		var length = percent.length;
		var i = 0;
		do {
			if(minMoney[i] <= amount && amount <= maxMoney[i]){
				id = i;
				i = i + length;
			}
			i++
		}
		while(i < length)
		
		if(id != -1){
			profitDaily = amount / 100 * percent[id];
			profitDaily = profitDaily.toFixed(2);
			profitHourly = amount / 100 * percent[id];
			profitHourly = profitHourly.toFixed(2);
			profitTotal = profitDaily * 12;
			profitTotal = profitTotal.toFixed(2);
			profitMonthly = profitDaily * 30;
			profitMonthly = profitMonthly.toFixed(2);


			if(amount < minMoney[id] || isNaN(amount) == true){
				$("#profitHourly").text("Error!");
				$("#profitDaily").text("Error!");
				$("#profitTotal").text("Error!");
				$("#profitMonthly").text("Error!");
			} else {
				$("#profitHourly").text("USD " + profitHourly);
				$("#profitDaily").text("USD " + profitDaily);
				$("#profitTotal").text("USD " + profitTotal);
				$("#profitMonthly").text("USD" + profitMonthly);
			}
		} else {
			$("#profitHourly").text("Error!");
			$("#profitDaily").text("Error!");
			$("#profitTotal").text("Error!");
			$("#profitMonthly").text("Error!");
		}
	}

	calc();

	$("#amount").keyup(function(){
		calc();
	});

    
      //calculator2//
	
	//Calculator
	function calc1(){
		var percent 	= [152.5];
		var minMoney 	= [1000];
		var maxMoney	= [350000];
	
		if($("#amount1").val().length == 0){
			$("#amount1").val(minMoney[0]);
		}	
	
		amount = parseFloat($("#amount1").val());
		id = -1;
		var length = percent.length;
		var i = 0;
		do {
			if(minMoney[i] <= amount && amount <= maxMoney[i]){
				id = i;
				i = i + length;
			}
			i++
		}
		while(i < length)
		
		if(id != -1){
			profitDaily1 = amount / 100 * percent[id];
			profitDaily1 = profitDaily1.toFixed(2);
			profitHourly = amount / 100 * percent[id];
			profitHourly = profitHourly.toFixed(2);
			profitTotal1 = profitDaily1 * 13;
			profitTotal1 = profitTotal1.toFixed(2);
			profitMonthly1 = profitDaily1 * 30;
			profitMonthly1 = profitMonthly1.toFixed(2);


			if(amount < minMoney[id] || isNaN(amount) == true){
				$("#profitHourly").text("Error!");
				$("#profitDaily1").text("Error!");
				$("#profitTotal1").text("Error!");
				$("#profitMonthly1").text("Error!");
			} else {
				$("#profitHourly").text("USD " + profitHourly);
				$("#profitDaily1").text("USD " + profitDaily1);
				$("#profitTotal1").text("USD" + profitTotal1);
				$("#profitMonthly1").text("USD " + profitMonthly1);
			}
		} else {
			$("#profitHourly").text("Error!");
			$("#profitDaily1").text("Error!");
			$("#profitTotal1").text("Error!");
			$("#profitMonthly1").text("Error!");
		}
	}

	calc1();

	$("#amount1").keyup(function(){
		calc1();
	});
    
       //calculator3//
    
    

	//Calculator
	function calc2(){
		var percent 	= [190.2];
		var minMoney 	= [350];
		var maxMoney	= [650000];

		if($("#amount2").val().length == 0){
			$("#amount2").val(minMoney[0]);
		}
	
		amount = parseFloat($("#amount2").val());
		id = -1;
		var length = percent.length;
		var i = 0;
		do {
			if(minMoney[i] <= amount && amount <= maxMoney[i]){
				id = i;
				i = i + length;
			}
			i++
		}
		while(i < length)
		
		if(id != -1){
			profitDaily2 = amount / 100 * percent[id];
			profitDaily2 = profitDaily2.toFixed(2);
			profitHourly = amount / 100 * percent[id];
			profitHourly = profitHourly.toFixed(2);
			profitTotal2 = profitDaily2 * 13;
			profitTotal2 = profitTotal2.toFixed(2);
			profitMonthly2 = profitDaily2 * 30;
			profitMonthly2 = profitMonthly2.toFixed(2);


			if(amount < minMoney[id] || isNaN(amount) == true){
				$("#profitHourly").text("Error!");
				$("#profitDaily2").text("Error!");
				$("#profitTotal2").text("Error!");
				$("#profitMonthly2").text("Error!");
			} else {
				$("#profitHourly").text("USD " + profitHourly);
				$("#profitDaily2").text("USD " + profitDaily2);
				$("#profitTotal2").text("USD " + profitTotal2);
				$("#profitMonthly2").text("USD " + profitMonthly2);
			}
		} else {
			$("#profitHourly").text("Error!");
			$("#profitDaily2").text("Error!");
			$("#profitTotal2").text("Error!");
			$("#profitMonthly2").text("Error!");
		}
	}

	calc2();

	$("#amount2").keyup(function(){
		calc2();
	});


  //calculator4//
    
    

	//Calculator
	function calc3(){
		var percent 	= [110];
		var minMoney 	= [1000];
		var maxMoney	= [1600000];

		if($("#amount3").val().length == 0){
			$("#amount3").val(minMoney[0]);
		}
	
		amount = parseFloat($("#amount3").val());
		id = -1;
		var length = percent.length;
		var i = 0;
		do {
			if(minMoney[i] <= amount && amount <= maxMoney[i]){
				id = i;
				i = i + length;
			}
			i++
		}
		while(i < length)
		
		if(id != -1){
			profitDaily3 = amount / 100 * percent[id];
			profitDaily3 = profitDaily3.toFixed(2);
			profitHourly = amount / 100 * percent[id];
			profitHourly = profitHourly.toFixed(2);
			profitTotal3 = profitDaily3 * 13;
			profitTotal3 = profitTotal3.toFixed(2);
			profitMonthly3 = profitDaily3 * 30;
			profitMonthly3 = profitMonthly3.toFixed(2);


			if(amount < minMoney[id] || isNaN(amount) == true){
				$("#profitHourly").text("Error!");
				$("#profitDaily3").text("Error!");
				$("#profitTotal3").text("Error!");
				$("#profitMonthly3").text("Error!");
			} else {
				$("#profitHourly").text("USD " + profitHourly);
				$("#profitDaily3").text("USD " + profitDaily3);
				$("#profitTotal3").text("USD " + profitTotal3);
				$("#profitMonthly3").text("USD " + profitMonthly3);
			}
		} else {
			$("#profitHourly").text("Error!");
			$("#profitDaily3").text("Error!");
			$("#profitTotal3").text("Error!");
			$("#profitMonthly3").text("Error!");
		}
	}

	calc3();

	$("#amount3").keyup(function(){
		calc3();
	});



	//Animate scroll
	if($(".wow").length){
		new WOW().init();
	}
	//Parallax
	$("#scene").parallax({
		limitY: 0
	});
	$("#top").parallax();
});
