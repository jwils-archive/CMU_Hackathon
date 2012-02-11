 <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN"
   "http://www.w3.org/TR/html4/strict.dtd">
<HTML>
  <HEAD>
 	<LINK href="static/css/bootstrap.min.css" rel="stylesheet" type="text/css">
	<LINK href="static/css/hacksy.css" rel="stylesheet" type="text/css">
 	</HEAD>
  <BODY>
   <div class="navbar navbar-fixed-top">
      <div class="navbar-inner">
        <div class="container">
          <a class="btn btn-navbar" data-toggle="collapse" data-target=".nav-collapse">
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </a>
          <a class="brand" href="#">Project name</a>
          <div class="nav-collapse">
            <ul class="nav">
              <li class="active"><a href="#">Home</a></li>
              <li><a href="#about">Team</a></li>
              <!-- <li><a href="#contact">Contact</a></li> -->
            </ul>
          </div><!--/.nav-collapse -->
        </div>
      </div>
    </div>

    <div class="container">

      <!-- Main hero unit for a primary marketing message or call to action -->
      <div class="hero-unit">
        <h1>App name</h1>
        <p>Do you like to keep your life in order? Are you the kind of person that puts everything on their calendar? Would you rather work on tasks in a couple smaller blocks of time instead of all at once (or do you at least wish you did)? Tell us what you need to get done, how long you think it'll take to finish, and when it needs to get done by, and we'll take care of the rest.</p>
        <!-- <p><a class="btn btn-primary btn-large">Learn more &raquo;</a></p> -->
      </div>

      <!-- Example row of columns -->
      <form method="post" action="/submit" enctype="multipart/form-data">
				<div id="todo" >
					<div class="row">
						<div class="span12"><h2>Select .ics file</h2></div>
					</div>
					<input id="hacksy_margin" type="file" name="cal_file"/>		
					<div class="row">
						<div class="span12"><h2>Todo List</h2></div>
					</div>
					<div class="row" id="item1">
						<div class="span3"> <label for="description1">Item description</label>
						<input type="text" name="description" id="description1"> </div>					
						<div class="span3"><label for="time1">Time estimate (hours)</label> 
						<input type="number" name="time" id="time1" step="0.5" min="0"/> </div>					
						<div class="span3"><label for="duedate1">Due date</label> 
						<input type="datetime-local" name="duedate" id="duedate1"></div>
						<div class="span3"><label>&nbsp;</label><button class="btn" type="button" onClick="del(1);">Delete Item</button></div>
					</div>
				</div>
				<div class="row">
					<div class="span12"><button class="btn" id="hacksy_margin" type="button" onClick="add();" >Add new item</button></div>
				</div>
				&nbsp;
				<div class="row">
					<div class="span12"><button class="btn btn-primary btn-large" type="submit" >Submit</button></div>
				</div>
      </form>
      
      <footer>
        <p>&copy; Company 2012</p>
      </footer>

    </div> <!-- /container -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.7.1/jquery.min.js"></script>
    <script type="text/JavaScript" src="static/js/bootstrap.min.js"></script>
    <script src="static/js/index.js"></script>
  </BODY>
</HTML>