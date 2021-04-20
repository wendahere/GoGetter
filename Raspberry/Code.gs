function doGet() {
  return HtmlService.createHtmlOutputFromFile('Index').setTitle('Index');
}

Array.prototype.contains = function(v) {
  for (var i = 0; i < this.length; i++) {
    if (this[i] === v) return true;
  }
  return false;
};

Array.prototype.unique = function() {
  var arr = [];
  for (var i = 0; i < this.length; i++) {
    if (!arr.contains(this[i])) {
      arr.push(this[i]);
    }
  }
  return arr;
}

function getCol(matrix, col){
  var column = [];
  for(var i=0; i<matrix.length; i++){
    column.push(matrix[i][col]);
  }
  return column;
}
  
function findGoogleSpreadsheetWithName(spreadSheetName){
//Finding the spreadsheet with a name
//And output the spreadsheet ID
  var files = DriveApp.searchFiles(
    'mimeType = "' + MimeType.GOOGLE_SHEETS + '"');
  
  while (files.hasNext()) {
    var spreadsheet = SpreadsheetApp.open(files.next());
    
    if (spreadSheetName == spreadsheet.getName()){
      var spreadSheetIO = spreadsheet.getId();
    }
  }  
  return spreadSheetIO;
}

function findGoogleSheetsInSpreadsheet(spreadSheet){
  var skip = "DO NOT DELETE";
  
  //Ignore "DO NOT DELETE"
  
  var sheetsNameArray = new Array();
  var allSheets = spreadSheet.getSheets();
  
  for (var i = 0; i < allSheets.length; i++){
    if (allSheets[i].getName() != skip)
       sheetsNameArray.push(allSheets[i].getName());
       }
  
  return sheetsNameArray;
}

function getOpenSpreadSheetFromName(spreadSheetName){
  return SpreadsheetApp.openById(findGoogleSpreadsheetWithName(spreadSheetName));
}

function getArrayofDataFromSpreadSheet(spreadSheetName, sheetName){ 
  return getArrayofDataFromSheet(getOpenSpreadSheetFromName(spreadSheetName), sheetName);
}

function getArrayofDataFromSheet(spreadSheet, sheetName){
  var sheet = spreadSheet.getSheetByName(sheetName);
  return sheet.getDataRange();
}

function countSheetRowNumber(spreadSheetName, sheetName, columnNumber){
  var dataArray = getArrayofDataFromSheet(getOpenSpreadSheetFromName(spreadSheetName),sheetName);
  
  for(var i = 1; i < dataArray.getNumRows(); i++) {
    if (dataArray.getCell(i, columnNumber).getValue() == ""){
      i--;
      break;
  }
    i++;
  }
  return i - 1;
  
  //var openSpreadSheet = getOpenSpreadSheetFromName(spreadSheetName);
  
  //var sheet = openSpreadSheet.getSheetByName(sheetName);
  
  //return sheet.getLastRow();
}

function countSheetColumnNumber(spreadSheetName, sheetName, rowNumber){
  var dataArray = getArrayofDataFromSheet(getOpenSpreadSheetFromName(spreadSheetName),sheetName);
 
  for(var i = 1; i < dataArray.getNumColumns(); i++) {
    if (dataArray.getCell(rowNumber,i).getValue() == ""){
      i--;
      break;
  }
    i++
  }
  return i - 1;
  
  //var openSpreadSheet = getOpenSpreadSheetFromName(spreadSheetName);
  
  //var sheet = openSpreadSheet.getSheetByName(sheetName);
  
  //return sheet.getLastColumn();
}

//function findArrayOfColumn(spreadSheetName, sheetName, columnNo){
//  var data = getArrayofDataFromSpreadSheet(spreadSheetName, sheetName);
  
 // var columnArray = new Array();
  
  //var i;
  
 // for (i = 1; i < countSheetRowNumber(spreadSheetName, sheetName, columnNo); i++){
   // columnArray.push(data.getCell(i + 1, columnNo).getValue());
  //}
  
  //return columnArray;
//}


function findArrayOfColumn(spreadSheetName, sheetName, columnNumber){
  var i;
  //var is_morethanpointRow;
  //var pointRow = 20; //Change this to estimated size of classes 
  var dataArray = getArrayofDataFromSheet(getOpenSpreadSheetFromName(spreadSheetName),sheetName);

  var columnRange;
  var columnArray = new Array();

  i = 0;
  is_morethanpointRow = false;

 

  for (i = 2; i < dataArray.getNumRows()+1; i++){
    columnArray.push(dataArray.getCell(i, columnNumber).getValue())
  }

  return columnArray;
}


 /*

  if(dataArray.getCell(pointRow, columnNumber).getValue() == ""){
  //If class is less than pointRow number

  do{
    i++;
  }while(dataArray.getCell(pointRow - i, columnNumber).getValue() == "");

  }else{
  //If class is more than pointRow number

  is_morethanpointRow = true;

  do{
    i++;
  }while(dataArray.getCell(pointRow + i, columnNumber).getValue() != "");
  }

  if (is_morethanpointRow){
    columnRange = dataArray.getRange(1, columnNumber, pointRow - i, columnNumber).getValues();
  }else{
    columnRange = dataArray.getRange(1, columnNumber, pointRow + i, columnNumber).getValues();
  }

  */

  //columnRange = dataArray.getCell(1, columnNumber).getDataRegion(SpreadsheetApp.Dimension.ROWS).getValues();
function findArrayOfRow(spreadSheetName, sheetName, rowNo){
  var data = getArrayofDataFromSpreadSheet(spreadSheetName, sheetName);
  
  var rowArray = new Array();
  
  var i;
  
  for (i = 1; i < countSheetColumnNumber(spreadSheetName, sheetName, rowNo); i++){
    rowArray.push(data.getCell(rowNo, i + 1).getValue());
  }
  
  return rowArray;
}



function getNames(sheetName, className){
  var nameClassArray = new Array();
  var nameColumns = findArrayOfColumn("database", sheetName, 2);
  var classColumns = findArrayOfColumn("database", sheetName, 3);
  
  
  for (var i = 0; i<nameColumns.length+1; i++){
    if (classColumns[i] == className){
      nameClassArray.push(nameColumns[i]);
    }
  }
  
  return nameClassArray;
}



function getClasses(spreadSheetName, sheetName){ //Search all unique classes and return an array of them
  var classColumnNumber = 3;
  
  var classColumns = findArrayOfColumn(spreadSheetName, sheetName, classColumnNumber);
  
  return classColumns.unique(); 
}

function getClasses_1(spreadSheetName, year){ //Search all unique classes and return an array of them
  var classRowNumber = 1;
  var functionalProgramSheet = "DO NOT DELETE";
  
  var yearArray = findArrayOfRow(spreadSheetName, functionalProgramSheet, classRowNumber); 

  for (var i = 0; i < yearArray.length; i++) {   
      if (yearArray[i] == year) {
        break;
      }
    }
  var classArray = findArrayOfColumn(spreadSheetName, functionalProgramSheet, i + 2)
  
  return classArray;
}

function getYearsForHTML(){
  return findGoogleSheetsInSpreadsheet(getOpenSpreadSheetFromName("database"));
}

function getPoints(sheetName, className, studentName){
  var namesArray = getNames(sheetName, className);
  
    for (var i = 0; i < namesArray.length; i++){
    if (namesArray[i] == studentName){
      break;
    }
  }
  
  var points = findArrayOfColumn("database", sheetName, 4);

  return points[i];
}

function editPoints(spreadSheetName, sheetName, className, studentName, newPoints){

var sheetData = getArrayofDataFromSpreadSheet(spreadSheetName, sheetName);

var checkSuccessMatch = false;

//Find data
for (var i = 1; i < sheetData.getNumRows(); i++){

  //Logger.log(sheetData.getCell(i,2).getValue());
  if (sheetData.getCell(i,2).getValue() == studentName && sheetData.getCell(i,3).getValue() == className){
    checkSuccessMatch = true;
    break;
  }
}

if (checkSuccessMatch){
  var spreadSheet = getOpenSpreadSheetFromName(spreadSheetName);
  var sheet = spreadSheet.getSheetByName(sheetName);

  //SpreadsheetApp.setActiveSheet(spreadSheet.getSheetByName(sheetName));
  //SpreadsheetApp.getActiveSheet().getRange("E9").setValue('Hello');
  var cell = "D"+i;
  var dateCell = "E"+i;

  var pointsDifference = newPoints - getPoints(sheetName, className, studentName);

  sheet.getRange(cell).setValue(newPoints);

  var dateUpdated = Utilities.formatDate(new Date(), "GMT+8", "dd/MM/yyyy HH:mm:ss");

  sheet.getRange(dateCell).setValue(dateUpdated);

  UIDCellDatabase = sheetData.getCell(i,1).getValue();

  // Log points in Log
  var logMonthYear = Utilities.formatDate(new Date(), "GMT+8", "MM/yyyy");
  var logSheetName = "Logs "+ logMonthYear;
  var logSheet = getOpenSpreadSheetFromName("Logs").getSheetByName(logSheetName);

  if (!logSheet){
    logSheet = getOpenSpreadSheetFromName("Logs").insertSheet();
    logSheet.setName(logSheetName);

    logSheet.getRange("A1").setValue("Date Updated");
    logSheet.getRange("B1").setValue("UID");
    logSheet.getRange("C1").setValue("Name");
    logSheet.getRange("D1").setValue("Class");
    logSheet.getRange("E1").setValue("Year");
    logSheet.getRange("F1").setValue("Points (+/-)");
    logSheet.getRange("G1").setValue("Remaining Points");

    var j = logSheet.getLastRow() + 1;

    var logsDateCell = "A"+j;
    var UIDCell = "B"+j;
    var nameCell = "C"+j;
    var classCell = "D"+j;
    var yearCell = "E"+j;
    var pointsCell = "F"+j;
    var remainingCell = "g"+j;

    logSheet.getRange(logsDateCell).setValue(dateUpdated);
    logSheet.getRange(UIDCell).setValue(UIDCellDatabase);
    logSheet.getRange(nameCell).setValue(studentName);
    logSheet.getRange(classCell).setValue(className);
    logSheet.getRange(yearCell).setValue(sheetName);
    logSheet.getRange(pointsCell).setValue(pointsDifference);
    logSheet.getRange(remainingCell).setValue(newPoints);
  }
  else{


  var j = logSheet.getLastRow() + 1;

  var logsDateCell = "A"+j;
  var UIDCell = "B"+j;
  var nameCell = "C"+j;
  var classCell = "D"+j;
  var yearCell = "E"+j;
  var pointsCell = "F"+j;
  var remainingCell = "g"+j;

  logSheet.getRange(logsDateCell).setValue(dateUpdated);
  logSheet.getRange(UIDCell).setValue(UIDCellDatabase);
  logSheet.getRange(nameCell).setValue(studentName);
  logSheet.getRange(classCell).setValue(className);
  logSheet.getRange(yearCell).setValue(sheetName);
  logSheet.getRange(pointsCell).setValue(pointsDifference);
  logSheet.getRange(remainingCell).setValue(newPoints);
  }
}

return newPoints;

//If can get data, continue
  //Write data
//Cannot get data
 //SpreadsheetApp.getActiveSheet().getRange(2,3).setValue('Hello'); 
}

function Function(value){
    var logMonthYear = Utilities.formatDate(new Date(), "GMT+8", "MM");
    var logSheetName = "Logs "+ logMonthYear;
    var logSheet = getOpenSpreadSheetFromName("Logs").getSheetByName(logSheetName);
    Logger.log(logSheet)
    
    
}










