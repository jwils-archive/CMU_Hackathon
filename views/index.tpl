 <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN"
   "http://www.w3.org/TR/html4/strict.dtd">
<HTML>
  <HEAD>
 	<LINK href="static/css/bootstrap.min.css" rel="stylesheet" type="text/css">
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
              <li><a href="#about">About</a></li>
              <li><a href="#contact">Contact</a></li>
            </ul>
          </div><!--/.nav-collapse -->
        </div>
      </div>
    </div>

    <div class="container">

      <!-- Main hero unit for a primary marketing message or call to action -->
      <div class="hero-unit">
        <h1>Hello, world!</h1>
        <p>This is a template for a simple marketing or informational website. It includes a large callout called the hero unit and three supporting pieces of content. Use it as a starting point to create something more unique.</p>
        <p><a class="btn btn-primary btn-large">Learn more &raquo;</a></p>
      </div>

      <!-- Example row of columns -->
      <form  id="todo" method="post" action="/submit" enctype="multipart/form-data">
      <input type="file" name="cal_file"/>
       <h2>Todo List</h2>
       <div class="row" id="item1">
     <div class="span3"> <label for="description1">Item description</label>
      <input type="text" name="description" id="description1"> </div>
      <div class="span3"><label for="time1">Time estimate (hours)</label> 
      <input type="number" name="time" id="time1" step="0.5" min="0"/> </div>
      <div class="span3"><label for="duedate1">Due date</label> 
      <input type="datetime-local" name="duedate" id="duedate1"></div>
      <div class="span3"><label>&nbsp;</label><button class="btn" type="button" onClick="del(1);">Delete Item</button></div>
      </div>
      <button class="btn" type="submit" >submit</button> 
      </form>
      <div class="row">
      <button class="btn" type="button" onClick="add();" >Add new item</button> 
      
      </div>
      <footer>
        <p>&copy; Company 2012</p>
      </footer>

    </div> <!-- /container -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.7.1/jquery.min.js"></script>
    <script type="text/JavaScript" src="static/js/bootstrap.min.js"></script>
    <script src="static/js/index.js"></script>
  </BODY>
</HTML>