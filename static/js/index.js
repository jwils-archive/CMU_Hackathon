var counter = 2;



function del(number){		
		$("#item" + number).remove();			
}

function add(){
	$("#todo").append('<div class="row" id="item' + counter + '">\
	<div class="span3"><label for="description' + counter + '">Item description</label>\
	<input type="text" id="description" name="description' + counter + '"/></div>\
	<div class="span3"><label for="time' + counter + '">Time estimate (hours)</label>\
	<input type="number" id="time" name="time' + counter + '" step="0.5" min="0"/></div>\
	<div class="span3"><label for="duedate' + counter + '">Due date</label>\
	<input type="datetime-local" id="duedate" name="duedate' + counter + '"/></div>\
	<div class="span3"><label>&nbsp;</label><button class="btn" onClick="del(' + counter + ');">Delete Item</button></div></div>');		
	counter++;
}
			
