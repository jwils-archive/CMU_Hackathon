<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.7.1/jquery.min.js"></script>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
<title>tartanhacks-todo</title>
</head>

<body>
	<h3>Create items to be added to calendar</h3>
	<form id="todo">
		<div id="item1">
			<label for="description1">Item description</label>
			<input type="text" name="description" id="description1">
			<label for="time1">Time estimate (hours)</label>
			<input type="number" name="time" id="time1" step="0.5" min="0"/>
			<label for="duedate1">Due date<label>
			<input type="datetime-local" name="duedate" id="duedate1">	
			<button type="button" onClick="del(1);">Delete Item</button>
		</div>			
	</form>
	<button type="button" onClick="add();">Add new item</button>	
	<script src="static/todo.js"></script>
</body>

</html>