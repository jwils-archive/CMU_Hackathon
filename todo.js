var counter = 2;
		
function del(number){		
		$("#item" + number).remove();			
}

function add(){
	$("#todo").append('<div id="item' + counter + '">\
	<label for="description' + counter + '">Item description</label>\
	<input type="text" name="description" id="description' + counter + '">\
	<label for="time' + counter + '">Time estimate (hours)</label>\
	<input type="number" name="time" id="time' + counter + '" step="0.5" min="0"/>\
	<label for="duedate' + counter + '">Due date<label>\
	<input type="datetime-local" name="duedate" id="duedate' + counter + '">\
	<button onClick="del(' + counter + ');">Delete Item</button></div>');		
	counter++;
}
		
/*function add(){
	$("#todo").append('<div id="item' + counter + '">\
	<label for="description' + counter + '">Item description</label>\
	<input type="text" name="description" id="description' + counter + '">\
	<label for="time' + counter + '">Time estimate (hours)</label>\
	<input type="number" name="time" id="time' + counter + '" step="0.5" min="0"/>\
	<label for="duedate' + counter + '">Due date<label>\
	<input type="datetime-local" name="duedate" id="duedate' + counter + '">\
	<label for="maxperday' + counter + '">Max time per day (hours)</label>\
	<input type="number" name="maxdaytime" id="maxdaytime' + counter + '" step="0.5"\ min="0" max="24"/>\
	<button onClick="del(' + counter + ');">Delete Item</button></div>');		
	counter++;
}*/
			