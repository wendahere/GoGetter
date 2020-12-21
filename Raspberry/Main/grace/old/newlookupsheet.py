PUT https://sheets.googleapis.com/v4/spreadsheets/1uqCwaVqo4EV3DC4Ue8bpi4BdwVLwzTG1w_xq6YTyxEU/values/LOOKUP_SHEET!A1?includeValuesInResponse=true&responseValueRenderOption=UNFORMATTED_VALUE&valueInputOption=USER_ENTERED&fields=updatedData

{
 "range": "LOOKUP_SHEET!A1",
 "values": [
  [
   "=MATCH("Search value", MySheet1!A:A, 0)"
  ]
 ]
}