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
function hasFreeMoves(visited){
	for(var i = 0; i < 3; i++){
		for(var j = 0; j < 3; j++){
			if(visited[i][i] == 0)
				return true;
		}
	}
}

function minmax(vis, depth, isMax){
	if (hasFreeMoves(visited)==false)
		return 0;
	// If this maximizer's move
	var player;
	var best;
	if (isMax){
		player = 'o';
		best = -1000;
	}
	else{
		best = 1000
		player = 'x'
	}
	for (var i = 0; i<3; i++){
		for (var j = 0; j<3; j++){
 			if (vis[i][j]==0){
				vis[i][j] = player;
				//Now Call minimax recursively and choose the suitable value
				best = Math.max( best, minmax(vis, depth+1, !isMax) );
				// Undo the move
				vis[i][j] = 0;
			}
		}
	}
    return best;
}
function nextMove(){//The actual method that determines the next system move
	var myvisited = [[0,0,0],[0,0,0],[0,0,0]];
	var i = 0;
	for (var x = 0;x < 3;x++) {
  	  for (var y = 0;y < 3;y++) {
  	  	myvisited[x][y] = visited[x][y]; //creating a temporary copy of this array
  	  }
  	}
	for (var row = 0; row<3; row++){ //If next user's move is winning move
		if (myvisited[row][0]==myvisited[row][1] && myvisited[row][2] == 0){
			if(myvisited[row][0] == 'o'){
				visited[row][2] = 'x';
				drawX(row * sectionSize, 2 * sectionSize);
				return;
			}
  		}
  		else if (myvisited[0][row]==myvisited[1][row] && myvisited[2][row] == 0){
			if(myvisited[0][row] == 'o'){
				visited[2][row] = 'x';
				drawX(2 * sectionSize, row * sectionSize);
				return;
			}
  		}
  		else if (myvisited[row][1]==myvisited[row][2] && myvisited[row][0] == 0){
			if(myvisited[row][1] == 'o'){
				visited[row][0] = 'x';
				drawX(row * sectionSize, 0 * sectionSize);
				return;
			}
  		}
  		else if (myvisited[1][row]==myvisited[2][row] && myvisited[0][row] == 0){
			if(myvisited[1][row] == 'o'){
				visited[0][row] = 'x';
				drawX(0 * sectionSize, row * sectionSize);
				return;
			}
  		}
  		else if (myvisited[0][row]==myvisited[2][row] && myvisited[1][row] == 0){
			if(myvisited[0][row] == 'o'){
				visited[1][row] = 'x';
				drawX(1 * sectionSize, row * sectionSize);
				return;
			}
  		}

  		else if (myvisited[row][0]==myvisited[row][2] && myvisited[row][1] == 0){
			if(myvisited[row][0] == 'o'){
				visited[row][1] = 'x';
				drawX(row * sectionSize, 1 * sectionSize);
				return;
			}
  		}
  	}

	if(myvisited[0][0]=='o' && myvisited[1][1] == 'o' && myvisited[2][2] == 0){
		visited[2][2] = 'x';
		drawX(2 * sectionSize, 2 * sectionSize);
		return;
	}
	else if(myvisited[1][1]=='o' && myvisited[2][2] == 'o' && myvisited[0][0] == 0){
		visited[0][0] = 'x';
		drawX(0 * sectionSize, 0 * sectionSize);
		return;
	}
	else if(myvisited[2][0]=='o' && myvisited[1][1] == 'o' && myvisited[0][2] == 0){
		visited[0][2] = 'x';
		drawX(0 * sectionSize, 2 * sectionSize);
		return;
	}
	else if(myvisited[0][2]=='o' && myvisited[1][1] == 'o' && myvisited[2][0] == 0){
		visited[2][0] = 'x';
		drawX(2 * sectionSize, 0 * sectionSize);
		return;
	}
	else if(myvisited[0][0]=='o' && myvisited[2][2] == 'o' && myvisited[1][1] == 0){
		visited[1][1] = 'x';
		drawX(1 * sectionSize, 1 * sectionSize);
		return;
	}
	else if(myvisited[0][2]=='o' && myvisited[2][0] == 'o' && myvisited[1][1] == 0){
		visited[1][1] = 'x';
		drawX(1 * sectionSize, 1 * sectionSize);
		return;
	}
	else if(myvisited[0][1]=='o' && myvisited[2][1] == 'o' && myvisited[1][1] == 0){
		visited[1][1] = 'x';
		drawX(1 * sectionSize, 1 * sectionSize);
		return;
	}
	else if(myvisited[1][0]=='o' && myvisited[1][2] == 'o' && myvisited[1][1] == 0){
		visited[1][1] = 'x';
		drawX(1 * sectionSize, 1 * sectionSize);
		return;
	}
	var currBestVal = -9999, moveVal = 0;
	var bestMove = {
		"row" : -1,
		"col" : -1
 	};
    //This Traverses all the cells, evalutae minimax function for all empty cells. And return the cell with optimal value.
	for (var i = 0; i<3; i++){
		for(var j = 0; j<3; j++){
			if (myvisited[i][j]==0){ //If the cell is free
				// Make the move
				myvisited[i][j] = 'o';
				// compute evaluation function for this move.
				moveVal = minmax(myvisited, 0, false);
				// Undo the move
				myvisited[i][j] = 0;
				// If the value of the current move is more than the best value, then update best
				if(moveVal > currBestVal){
					bestMove.row = i;
					bestMove.col = j;
					currBestVal = moveVal;
                }
            }
        }
    }
  	visited[bestMove.row][bestMove.col] = 'x';
	drawX(bestMove.row * sectionSize, bestMove.col * sectionSize);
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
