Attribute VB_Name = "Module1"
Sub StockVBA():
    Dim ws As Worksheet
    Dim starting_ws As Worksheet
    Set starting_ws = ActiveSheet
    For Each ws In ThisWorkbook.Worksheets
        ws.Activate
    'was looking for how to loop through the worksheets in a workbook in excel and this was the function given
        
        'difine variable used
        
        Dim Ticker As String
        Dim year_open As Double
            year_open = Cells(2, 3).Value
        Dim year_close As Double
            year_close = Cells(2, 6).Value
        Dim year_change As Double
            year_change = 0
        Dim Percentage_change As Double
            Percentage_change = 0
        Dim Volume As Double
            Volume = 0
        Dim Place As Long
            Place = 2
        Dim LastRow As Long
            LastRow = Cells(Rows.Count, 1).End(xlUp).Row
            
        'looked up a function to grab the last row in this worksheet
    
    'header
        Cells(1, 9).Value = "Ticker"
        Cells(1, 10).Value = "Yearly Change"
        Cells(1, 11).Value = "Percent Change"
        Cells(1, 12).Value = "Total Stock Volume"
        
    'loop
        For i = 2 To LastRow
            If Cells(i + 1, 1).Value <> Cells(i, 1).Value Then
            'checking ticker againest the one above so the code will go throght the list
                Ticker = Cells(i, 1).Value
                'year_open = Cells(i, 3).Value
                'year_close = Cells(i, 6).Value
                'year_change = year_close - year_open
                'percentage_change = Year_change / Year_close
                
                year_change = Cells(i, 6).Value - year_open
            
                'formula for calculating the percent change, since dividing by 0 will cause problems, i set it = 0 if it starts at 0
                If year_open = 0 Then
                    Percentage_change = 0
                Else
                    Percentage_change = year_change / year_open
                End If
                'code for grabing the volume and adding it from the preset value of 0 from above
                Volume = Volume + Cells(i, 7).Value
                Range("i" & Place).Value = Ticker
                Range("j" & Place).Value = year_change
                
                'code for color coding and green for above 0 and red for below 0
                If Range("j" & Place).Value > 0 Then
                    Range("j" & Place).Interior.Color = vbGreen
                ElseIf Range("j" & Place).Value < 0 Then
                    Range("j" & Place).Interior.Color = vbRed
                End If
                
                'code for putting all the data gathered into cells
                Range("k" & Place).Value = Percentage_change
                Range("k" & Place).NumberFormat = "0%"
                Range("l" & Place).Value = Volume
                Place = Place + 1
                year_open = Cells(i + 1, 3).Value
                Percentage_change = 0
                Volume = 0
            Else
                Volume = Volume + Cells(i, 7).Value
            End If
        Next i
    starting_ws.Activate
    Next ws
End Sub



