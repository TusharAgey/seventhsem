'use strict';
var player = 1;
var lineColor = "#ddd";
var canvas = document.getElementById('tic-tac-toe-board'); //get the board properties
var context = canvas.getContext('2d');

var canvasSize = 500;
var sectionSize = canvasSize / 3;
canvas.width = canvasSize; 
canvas.height = canvasSize;
context.translate(0.5, 0.5);
var visited = [[0,0,0],[0,0,0],[0,0,0]]; //Master record of elements
function nextMove(){//The actual method that determines the next system move
	var myvisited = [0,0,0,0,0,0,0,0,0];
	var i = 0;
	for (var x = 0;x < 3;x++) {
  	  for (var y = 0;y < 3;y++) {
  	  	myvisited[i] = visited[x][y];
  	  	i++;
  	  }
  	}
  	//do all the AI processing
	//logic to choose next move
	//just find lok. and paint the box of x,y when i == lok
	i = 0;
outer:	for (x = 0; x < 3; x++) {
  	  for (y = 0; y < 3; y++) {
  	  	if(myvisited[i] == 0){
  	  		visited[x][y] = 'x';
  	  		break outer;
  	  	}
  	  	i++;
  	  }
  	}
	drawX(x * sectionSize, y * sectionSize,);
}
function addPlayingPiece (mouse) { //When user clicks an area, paint the area 
  var xCordinate;
  var yCordinate;

  for (var x = 0;x < 3;x++) {
    for (var y = 0;y < 3;y++) {
      xCordinate = x * sectionSize;
      yCordinate = y * sectionSize;

      if (
          mouse.x >= xCordinate && mouse.x <= xCordinate + sectionSize &&
          mouse.y >= yCordinate && mouse.y <= yCordinate + sectionSize &&
          !visited[x][y]
        ) {
        visited[x][y] = 'o';
        drawO(xCordinate, yCordinate);
        nextMove();
      }
    }
  }
}
function drawO (xCordinate, yCordinate) { //Draw O
  var halfSectionSize = (0.5 * sectionSize);
  var centerX = xCordinate + halfSectionSize;
  var centerY = yCordinate + halfSectionSize;
  var radius = (sectionSize - 100) / 2;
  var startAngle = 0 * Math.PI; 
  var endAngle = 2 * Math.PI;

  context.lineWidth = 10;
  context.strokeStyle = "#01bBC2";
  context.beginPath();
  context.arc(centerX, centerY, radius, startAngle, endAngle);
  context.stroke();
}

function drawX (xCordinate, yCordinate) { //Draw X
  context.strokeStyle = "#f1be32";

  context.beginPath();
  
  var offset = 50;
  context.moveTo(xCordinate + offset, yCordinate + offset);
  context.lineTo(xCordinate + sectionSize - offset, yCordinate + sectionSize - offset);

  context.moveTo(xCordinate + offset, yCordinate + sectionSize - offset);
  context.lineTo(xCordinate + sectionSize - offset, yCordinate + offset);

  context.stroke();
}

function drawLines (lineWidth, strokeStyle) {//Draw separating lines
  var lineStart = 4;
  var lineLenght = canvasSize - 5;
  context.lineWidth = lineWidth;
  context.lineCap = 'round';
  context.strokeStyle = strokeStyle;
  context.beginPath();

  /*
   * Horizontal lines 
   */
  for (var y = 1;y <= 2;y++) {  
    context.moveTo(lineStart, y * sectionSize);
    context.lineTo(lineLenght, y * sectionSize);
  }

  /*
   * Vertical lines 
   */
  for (var x = 1;x <= 2;x++) {
    context.moveTo(x * sectionSize, lineStart);
    context.lineTo(x * sectionSize, lineLenght);
  }

  context.stroke();
}

drawLines(10, lineColor);

function getCanvasMousePosition (event) { //get mouse position of where the click has occured
  var rect = canvas.getBoundingClientRect();
  return {
    x: event.clientX - rect.left,
    y: event.clientY - rect.top
  }
}

canvas.addEventListener('mouseup', function (event) { //handle the click event
  var canvasMousePosition = getCanvasMousePosition(event);
  addPlayingPiece(canvasMousePosition);
  drawLines(10, lineColor);
});