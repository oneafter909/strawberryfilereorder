Imports System.IO
Public Class Form1
    Dim tD() As Decimal = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0} ' I SALVATAGGI AVVENGONO IN MB
    Public Sub reorder(ByRef e As String, ByRef fR As String, ByRef fN As String)
        Dim tF = 0
        Dim errorCounter = 0
        For Each item In Directory.GetFiles(fR)
            Dim est As String = Path.GetExtension(item)
            Try
                Dim p As String = Path.GetFileName(item)
                Dim informationFile As System.IO.FileInfo
                informationFile = My.Computer.FileSystem.GetFileInfo(item)
                Dim size As Decimal = informationFile.Length / 2 ^ 20
                Dim totalSize As Decimal = totalSize + size
                TextBox3.Text += "Size of transferred files: " + Math.Round(totalSize, 2).ToString + " MB" + vbCrLf
                TextBox4.Text += "Size of transferred files: " + Math.Round(totalSize, 2).ToString + " MB" + vbCrLf
                If est.ToLower() = e Then
                    File.Move(item, fN + "\" + Path.GetFileName(item))
                    tF += 1
                End If
            Catch Lol As IOException ' | duplicate |
                Try
                    duplicated += 1
                    File.Move(item, publicpath + Path.GetFileNameWithoutExtension(item) + Now.Year.ToString + Now.Month.ToString + Now.Day.ToString + Now.Hour.ToString + Now.Minute.ToString + Now.Second.ToString + "[dx]" + Path.GetExtension(item))
                    TextBox3.Text += $"The file {Path.GetFileName(item)} is a duplicated file. It will have the sign [dx] to be recognized easily." + vbCrLf
                    TextBox4.Text += $"The file {Path.GetFileName(item)} is a duplicated file. It will have the sign [dx] to be recognized easily." + vbCrLf
                    publicpath = ""
                    tF += 1
                Catch ex As Exception
                    errorCounter += 1
                    TextBox3.Text += "Error during the copy of the file" + item + vbCrLf + "RTERROR: " + ex.Message + vbCrLf
                    TextBox4.Text += "Error during the copy of the file" + item + vbCrLf + "RTERROR: " + ex.Message + vbCrLf
                End Try

            Catch ex As Exception
                errorCounter += 1
                TextBox3.Text += "Error during the copy of the file" + item + vbCrLf + "RTERROR: " + ex.Message + vbCrLf
                TextBox4.Text += "Error during the copy of the file" + item + vbCrLf + "RTERROR: " + ex.Message + vbCrLf
            End Try
        Next
        If tF = 0 And errorCounter = 0 Then
            TextBox3.Text += "Any file with recognized extension has been found." + vbCrLf
            TextBox4.Text += "Any file with recognized extension has been found." + vbCrLf
        Else
            TextBox3.Text += $"{tF} Success. {errorCounter} errors. {duplicated} duplicated." + vbCrLf
            TextBox4.Text += $"{tF} Success. {errorCounter} errors. {duplicated} duplicated." + vbCrLf
            MsgBox($"La cartella {ComboBox2.Text} è stata riordinata.", MsgBoxStyle.Information, "Cartella riordinata!")
        End If
        TextBox4.SelectionStart = TextBox4.TextLength
        TextBox4.ScrollToCaret()
        TextBox3.SelectionStart = TextBox3.TextLength
        TextBox3.ScrollToCaret()
    End Sub
    Dim publicpath As String
    Dim duplicated As Integer
    Private Sub finder(ByRef percorsDirectory As String)
        Dim tF = 0
        Dim errorCounter = 0

        For counter As Integer = 0 To tD.Length - 1
            tD(counter) = 0
        Next

        For Each item In Directory.GetFiles(percorsDirectory)
            Dim e As String = Path.GetExtension(item).ToLower()
            Try
                Dim p As String = Path.GetFileName(item)
                'FILE IMMAGINI
                If e = ".jfif" Or e = ".png" Or e = ".dng" Or e = ".cr2" Or e = ".jpg" Or e = ".jpeg" Or e = ".gif" Or e = ".bmp" Or e = ".webp" Or e = ".svg" Then
                    Dim newPath As String = percorsDirectory + "\Image files\"
                    publicpath = newPath
                    Dim informationFile As System.IO.FileInfo
                    informationFile = My.Computer.FileSystem.GetFileInfo(item)
                    Dim size As Decimal = informationFile.Length / 2 ^ 20
                    '| SALVATAGGIO INFORMAZIONI NELL'ARRAY |
                    tD(0) += size
                    TextBox3.Text += $"Transferring {Path.GetFileName(item)} size: " + Math.Round(size, 2).ToString + " MB" + vbCrLf
                    TextBox4.Text += $"Transferring {Path.GetFileName(item)} size: " + Math.Round(size, 2).ToString + " MB" + vbCrLf
                    If Directory.Exists(newPath) = False Then
                        Directory.CreateDirectory(newPath)
                        File.Move(item, newPath + Path.GetFileName(item))
                    Else
                        File.Move(item, newPath + Path.GetFileName(item))
                    End If
                    tF += 1
                End If

                'FILE photoshop
                If e = ".psd" Then
                    Dim newPath As String = percorsDirectory + "\Photoshop files\"
                    publicpath = newPath
                    Dim informationFile As System.IO.FileInfo
                    informationFile = My.Computer.FileSystem.GetFileInfo(item)
                    Dim size As Decimal = informationFile.Length / 2 ^ 20
                    '| SALVATAGGIO INFORMAZIONI NELL'ARRAY |
                    tD(1) += size
                    TextBox3.Text += $"Transferring {Path.GetFileName(item)} size: " + Math.Round(size, 2).ToString + " MB" + vbCrLf
                    TextBox4.Text += $"Transferring {Path.GetFileName(item)} size: " + Math.Round(size, 2).ToString + " MB" + vbCrLf
                    If Directory.Exists(newPath) = False Then
                        Directory.CreateDirectory(newPath)
                        File.Move(item, newPath + Path.GetFileName(item))
                    Else
                        File.Move(item, newPath + Path.GetFileName(item))
                    End If
                    tF += 1
                End If
                'FILE MUSICALI
                If e = ".mp3" Or e = ".wav" Or e = ".wma" Or e = ".ogg" Or e = ".flac" Or e = ".pcm" Or e = ".aiff" Or e = ".m4r" Or e = ".m4a" Then
                    Dim informationFile As System.IO.FileInfo
                    informationFile = My.Computer.FileSystem.GetFileInfo(item)
                    Dim size As Decimal = informationFile.Length / 2 ^ 20
                    '| SALVATAGGIO INFORMAZIONI NELL'ARRAY |
                    tD(2) += size
                    TextBox3.Text += $"Transferring {Path.GetFileName(item)} size: " + Math.Round(size, 2).ToString + " MB" + vbCrLf
                    TextBox4.Text += $"Transferring {Path.GetFileName(item)} size: " + Math.Round(size, 2).ToString + " MB" + vbCrLf
                    Dim newPath As String = percorsDirectory + "\Music files\"
                    publicpath = newPath
                    If Directory.Exists(newPath) = False Then
                        Directory.CreateDirectory(newPath)
                        File.Move(item, newPath + Path.GetFileName(item))
                    Else
                        File.Move(item, newPath + Path.GetFileName(item))
                    End If
                    tF += 1
                End If

                'FILE VIDEO
                If e = ".mp4" Or e = ".mov" Or e = ".avi" Or e = ".wmv" Or e = ".flav" Or e = ".flv" Or e = ".mpeg" Or e = ".rm" Or e = ".3gp" Then
                    Dim informationFile As System.IO.FileInfo
                    informationFile = My.Computer.FileSystem.GetFileInfo(item)
                    Dim size As Decimal = informationFile.Length / 2 ^ 20
                    '| SALVATAGGIO INFORMAZIONI NELL'ARRAY |
                    tD(3) += size
                    TextBox3.Text += $"Transferring {Path.GetFileName(item)} size: " + Math.Round(size, 2).ToString + " MB" + vbCrLf
                    TextBox4.Text += $"Transferring {Path.GetFileName(item)} size: " + Math.Round(size, 2).ToString + " MB" + vbCrLf
                    Dim newPath As String = percorsDirectory + "\Video files\"
                    publicpath = newPath
                    If Directory.Exists(newPath) = False Then
                        Directory.CreateDirectory(newPath)
                        File.Move(item, newPath + Path.GetFileName(item))
                    Else
                        File.Move(item, newPath + Path.GetFileName(item))
                    End If
                    tF += 1
                End If

                'FILE DOCUMENTI
                If e = ".accdb" Or e = ".pages" Or e = ".odb" Or e = ".dwg" Or e = ".txt" Or e = ".odt" Or e = ".ods" Or e = ".odp" Or e = ".xls" Or e = ".xlsx" Or e = ".pdf" Or e = ".doc" Or e = ".docx" Or e = ".ppt" Or e = ".pptx" Then
                    Dim informationFile As System.IO.FileInfo
                    informationFile = My.Computer.FileSystem.GetFileInfo(item)
                    Dim size As Decimal = informationFile.Length / 2 ^ 20
                    '| SALVATAGGIO INFORMAZIONI NELL'ARRAY |
                    tD(4) += size
                    TextBox3.Text += $"Transferring {Path.GetFileName(item)} size: " + Math.Round(size, 2).ToString + " MB" + vbCrLf
                    TextBox4.Text += $"Transferring {Path.GetFileName(item)} size: " + Math.Round(size, 2).ToString + " MB" + vbCrLf
                    Dim newPath As String = percorsDirectory + "\Document files\"
                    publicpath = newPath
                    If Directory.Exists(newPath) = False Then
                        Directory.CreateDirectory(newPath)
                        File.Move(item, newPath + Path.GetFileName(item))
                    Else
                        File.Move(item, newPath + Path.GetFileName(item))
                    End If
                    tF += 1
                End If
                'FILE EXE
                If e = ".bat" Or e = ".exe" Or e = ".msi" Then
                    Dim informationFile As System.IO.FileInfo
                    informationFile = My.Computer.FileSystem.GetFileInfo(item)
                    Dim size As Decimal = informationFile.Length / 2 ^ 20
                    '| SALVATAGGIO INFORMAZIONI NELL'ARRAY |
                    tD(5) += size
                    TextBox3.Text += $"Transferring {Path.GetFileName(item)} size: " + Math.Round(size, 2).ToString + " MB" + vbCrLf
                    TextBox4.Text += $"Transferring {Path.GetFileName(item)} size: " + Math.Round(size, 2).ToString + " MB" + vbCrLf
                    Dim newPath As String = percorsDirectory + "\Executable files\"
                    publicpath = newPath
                    If Directory.Exists(newPath) = False Then
                        Directory.CreateDirectory(newPath)
                        File.Move(item, newPath + Path.GetFileName(item))
                    Else
                        File.Move(item, newPath + Path.GetFileName(item))
                    End If
                    tF += 1
                End If
                'FILE FONT
                If e = ".ttf" Or e = ".otf" Or e = ".ttc" Then
                    Dim informationFile As System.IO.FileInfo
                    informationFile = My.Computer.FileSystem.GetFileInfo(item)
                    Dim size As Decimal = informationFile.Length / 2 ^ 20
                    '| SALVATAGGIO INFORMAZIONI NELL'ARRAY |
                    tD(6) += size
                    TextBox3.Text += $"Transferring {Path.GetFileName(item)} size: " + Math.Round(size, 2).ToString + " MB" + vbCrLf
                    TextBox4.Text += $"Transferring {Path.GetFileName(item)} size: " + Math.Round(size, 2).ToString + " MB" + vbCrLf
                    Dim newPath As String = percorsDirectory + "\Fonts\"
                    publicpath = newPath
                    If Directory.Exists(newPath) = False Then
                        Directory.CreateDirectory(newPath)
                        File.Move(item, newPath + Path.GetFileName(item))
                    Else
                        File.Move(item, newPath + Path.GetFileName(item))
                    End If
                    tF += 1
                End If
                'FILE ZIP
                If e = ".zip" Or e = ".rar" Or e = ".7z" Or e = ".tar" Or e = ".tar.gz" Or e = ".tar.xz" Or e = ".gz" Or e = ".xz" Then
                    Dim informationFile As System.IO.FileInfo
                    informationFile = My.Computer.FileSystem.GetFileInfo(item)
                    Dim size As Decimal = informationFile.Length / 2 ^ 20
                    '| SALVATAGGIO INFORMAZIONI NELL'ARRAY |
                    tD(7) += size
                    TextBox3.Text += $"Transferring {Path.GetFileName(item)} size: " + Math.Round(size, 2).ToString + " MB" + vbCrLf
                    TextBox4.Text += $"Transferring {Path.GetFileName(item)} size: " + Math.Round(size, 2).ToString + " MB" + vbCrLf
                    Dim newPath As String = percorsDirectory + "\Compressed files\"
                    publicpath = newPath
                    If Directory.Exists(newPath) = False Then
                        Directory.CreateDirectory(newPath)
                        File.Move(item, newPath + Path.GetFileName(item))
                    Else
                        File.Move(item, newPath + Path.GetFileName(item))
                    End If
                    tF += 1
                End If
                'FILE MIDI
                If e = ".mid" Or e = ".midi" Then
                    Dim informationFile As System.IO.FileInfo
                    informationFile = My.Computer.FileSystem.GetFileInfo(item)
                    Dim size As Decimal = informationFile.Length / 2 ^ 20
                    '| SALVATAGGIO INFORMAZIONI NELL'ARRAY |
                    tD(8) += size
                    TextBox3.Text += $"Transferring {Path.GetFileName(item)} size: " + Math.Round(size, 2).ToString + " MB" + vbCrLf
                    TextBox4.Text += $"Transferring {Path.GetFileName(item)} size: " + Math.Round(size, 2).ToString + " MB" + vbCrLf
                    Dim newPath As String = percorsDirectory + "\MIDI Files\"
                    publicpath = newPath
                    If Directory.Exists(newPath) = False Then
                        Directory.CreateDirectory(newPath)
                        File.Move(item, newPath + Path.GetFileName(item))
                    Else
                        File.Move(item, newPath + Path.GetFileName(item))
                    End If
                    tF += 1
                End If
                'FILE JAR
                If e = ".jar" Then
                    Dim informationFile As System.IO.FileInfo
                    informationFile = My.Computer.FileSystem.GetFileInfo(item)
                    Dim size As Decimal = informationFile.Length / 2 ^ 20
                    '| SALVATAGGIO INFORMAZIONI NELL'ARRAY |
                    tD(9) += size
                    TextBox3.Text += $"Transferring {Path.GetFileName(item)} size: " + Math.Round(size, 2).ToString + " MB" + vbCrLf
                    TextBox4.Text += $"Transferring {Path.GetFileName(item)} size: " + Math.Round(size, 2).ToString + " MB" + vbCrLf
                    Dim newPath As String = percorsDirectory + "\Java Files\"
                    publicpath = newPath
                    If Directory.Exists(newPath) = False Then
                        Directory.CreateDirectory(newPath)
                        File.Move(item, newPath + Path.GetFileName(item))
                    Else
                        File.Move(item, newPath + Path.GetFileName(item))
                    End If
                    tF += 1
                End If
                'FILE codice sorgente
                If e = ".meta" Or e = ".h" Or e = ".xml" Or e = ".sh" Or e = ".css" Or e = ".html" Or e = ".cpp" Or e = ".cs" Or e = ".php" Or e = ".c" Or e = ".py" Or e = ".vb" Then
                    Dim informationFile As System.IO.FileInfo
                    informationFile = My.Computer.FileSystem.GetFileInfo(item)
                    Dim size As Decimal = informationFile.Length / 2 ^ 20
                    '| SALVATAGGIO INFORMAZIONI NELL'ARRAY |
                    tD(10) += size
                    TextBox3.Text += $"Transferring {Path.GetFileName(item)} size: " + Math.Round(size, 2).ToString + " MB" + vbCrLf
                    TextBox4.Text += $"Transferring {Path.GetFileName(item)} size: " + Math.Round(size, 2).ToString + " MB" + vbCrLf
                    Dim newPath As String = percorsDirectory + "\Source code files\"
                    publicpath = newPath
                    If Directory.Exists(newPath) = False Then
                        Directory.CreateDirectory(newPath)
                        File.Move(item, newPath + Path.GetFileName(item))
                    Else
                        File.Move(item, newPath + Path.GetFileName(item))
                    End If
                    tF += 1
                End If
                'FILE Immagine
                If e = ".iso" Or e = ".img" Or e = ".bin" Or e = ".dmg" Or e = ".pdi" Then
                    Dim informationFile As System.IO.FileInfo
                    informationFile = My.Computer.FileSystem.GetFileInfo(item)
                    Dim size As Decimal = informationFile.Length / 2 ^ 20
                    '| SALVATAGGIO INFORMAZIONI NELL'ARRAY |
                    tD(11) += size
                    TextBox3.Text += $"Transferring {Path.GetFileName(item)} size: " + Math.Round(size, 2).ToString + " MB" + vbCrLf
                    TextBox4.Text += $"Transferring {Path.GetFileName(item)} size: " + Math.Round(size, 2).ToString + " MB" + vbCrLf
                    Dim newPath As String = percorsDirectory + "\Disk Image files\"
                    publicpath = newPath
                    If Directory.Exists(newPath) = False Then
                        Directory.CreateDirectory(newPath)
                        File.Move(item, newPath + Path.GetFileName(item))
                    Else
                        File.Move(item, newPath + Path.GetFileName(item))
                    End If
                    tF += 1
                End If
                'FILE configurazione
                If e = ".dll" Then
                    Dim informationFile As System.IO.FileInfo
                    informationFile = My.Computer.FileSystem.GetFileInfo(item)
                    Dim size As Decimal = informationFile.Length / 2 ^ 20
                    '| SALVATAGGIO INFORMAZIONI NELL'ARRAY |
                    tD(12) += size
                    TextBox3.Text += $"Transferring {Path.GetFileName(item)} size: " + Math.Round(size, 2).ToString + " MB" + vbCrLf
                    TextBox4.Text += $"Transferring {Path.GetFileName(item)} size: " + Math.Round(size, 2).ToString + " MB" + vbCrLf
                    Dim newPath As String = percorsDirectory + "\Configuration files\"
                    publicpath = newPath
                    If Directory.Exists(newPath) = False Then
                        Directory.CreateDirectory(newPath)
                        File.Move(item, newPath + Path.GetFileName(item))
                    Else
                        File.Move(item, newPath + Path.GetFileName(item))
                    End If
                    tF += 1
                End If
                'FILE collegamenti programmi
                If e = ".lnk" Or e = ".LNK" Then
                    Dim informationFile As System.IO.FileInfo
                    informationFile = My.Computer.FileSystem.GetFileInfo(item)
                    Dim size As Decimal = informationFile.Length / 2 ^ 20
                    '| SALVATAGGIO INFORMAZIONI NELL'ARRAY |
                    tD(13) += size
                    TextBox3.Text += $"Transferring {Path.GetFileName(item)} size: " + Math.Round(size, 2).ToString + " MB" + vbCrLf
                    TextBox4.Text += $"Transferring {Path.GetFileName(item)} size: " + Math.Round(size, 2).ToString + " MB" + vbCrLf
                    Dim newPath As String = percorsDirectory + "\Shortcuts\"
                    publicpath = newPath
                    If Directory.Exists(newPath) = False Then
                        Directory.CreateDirectory(newPath)
                        File.Move(item, newPath + Path.GetFileName(item))
                    Else
                        File.Move(item, newPath + Path.GetFileName(item))
                    End If
                    tF += 1
                End If
                'FILE collegamenti programmi 
                If e = ".pkg" Then
                    Dim informationFile As System.IO.FileInfo
                    informationFile = My.Computer.FileSystem.GetFileInfo(item)
                    Dim size As Decimal = informationFile.Length / 2 ^ 20
                    '| SALVATAGGIO INFORMAZIONI NELL'ARRAY |
                    tD(14) += size
                    TextBox3.Text += $"Transferring {Path.GetFileName(item)} size: " + Math.Round(size, 2).ToString + " MB" + vbCrLf
                    TextBox4.Text += $"Transferring {Path.GetFileName(item)} size: " + Math.Round(size, 2).ToString + " MB" + vbCrLf
                    Dim newPath As String = percorsDirectory + "\Apple packages\"
                    publicpath = newPath
                    If Directory.Exists(newPath) = False Then
                        Directory.CreateDirectory(newPath)
                        File.Move(item, newPath + Path.GetFileName(item))
                    Else
                        File.Move(item, newPath + Path.GetFileName(item))
                    End If
                    tF += 1
                End If

                'FILE database jonio
                If e = ".jdatabase" Then
                    Dim informationFile As System.IO.FileInfo
                    informationFile = My.Computer.FileSystem.GetFileInfo(item)
                    Dim size As Decimal = informationFile.Length / 2 ^ 20
                    '| SALVATAGGIO INFORMAZIONI NELL'ARRAY |
                    tD(15) += size
                    TextBox3.Text += $"Transferring {Path.GetFileName(item)} size: " + Math.Round(size, 2).ToString + " MB" + vbCrLf
                    TextBox4.Text += $"Transferring {Path.GetFileName(item)} size: " + Math.Round(size, 2).ToString + " MB" + vbCrLf
                    Dim newPath As String = percorsDirectory + "\Jonio Database files\"
                    publicpath = newPath
                    If Directory.Exists(newPath) = False Then
                        Directory.CreateDirectory(newPath)
                        File.Move(item, newPath + Path.GetFileName(item))
                    Else
                        File.Move(item, newPath + Path.GetFileName(item))
                    End If
                    tF += 1
                End If


                If e = ".ico" Then
                    Dim informationFile As System.IO.FileInfo
                    informationFile = My.Computer.FileSystem.GetFileInfo(item)
                    Dim size As Decimal = informationFile.Length / 2 ^ 20
                    '| SALVATAGGIO INFORMAZIONI NELL'ARRAY |
                    tD(16) += size
                    TextBox3.Text += $"Transferring {Path.GetFileName(item)} size: " + Math.Round(size, 2).ToString + " MB" + vbCrLf
                    TextBox4.Text += $"Transferring {Path.GetFileName(item)} size: " + Math.Round(size, 2).ToString + " MB" + vbCrLf
                    Dim newPath As String = percorsDirectory + "\Icon files\"
                    publicpath = newPath
                    If Directory.Exists(newPath) = False Then
                        Directory.CreateDirectory(newPath)
                        File.Move(item, newPath + Path.GetFileName(item))
                    Else
                        File.Move(item, newPath + Path.GetFileName(item))
                    End If
                    tF += 1
                End If
                If e = ".blend" Or e = ".c4d" Then
                    Dim informationFile As System.IO.FileInfo
                    informationFile = My.Computer.FileSystem.GetFileInfo(item)
                    Dim size As Decimal = informationFile.Length / 2 ^ 20
                    '| SALVATAGGIO INFORMAZIONI NELL'ARRAY |
                    tD(17) += size
                    TextBox3.Text += $"Transferring {Path.GetFileName(item)} size: " + Math.Round(size, 2).ToString + " MB" + vbCrLf
                    TextBox4.Text += $"Transferring {Path.GetFileName(item)} size: " + Math.Round(size, 2).ToString + " MB" + vbCrLf
                    Dim newPath As String = percorsDirectory + "\3D Model files\"
                    publicpath = newPath
                    If Directory.Exists(newPath) = False Then
                        Directory.CreateDirectory(newPath)
                        File.Move(item, newPath + Path.GetFileName(item))
                    Else
                        File.Move(item, newPath + Path.GetFileName(item))
                    End If
                    tF += 1
                End If

                If e = ".mjp" Then
                    Dim informationFile As System.IO.FileInfo
                    informationFile = My.Computer.FileSystem.GetFileInfo(item)
                    Dim size As Decimal = informationFile.Length / 2 ^ 20
                    '| SALVATAGGIO INFORMAZIONI NELL'ARRAY |
                    tD(18) += size
                    TextBox3.Text += $"Transferring {Path.GetFileName(item)} size: " + Math.Round(size, 2).ToString + " MB" + vbCrLf
                    TextBox4.Text += $"Transferring {Path.GetFileName(item)} size: " + Math.Round(size, 2).ToString + " MB" + vbCrLf
                    Dim newPath As String = percorsDirectory + "\Playlist\"
                    publicpath = newPath
                    If Directory.Exists(newPath) = False Then
                        Directory.CreateDirectory(newPath)
                        File.Move(item, newPath + Path.GetFileName(item))
                    Else
                        File.Move(item, newPath + Path.GetFileName(item))
                    End If
                    tF += 1
                End If

            Catch Lol As IOException ' | duplicate |

                Try
                    duplicated += 1
                    File.Move(item, publicpath + Path.GetFileNameWithoutExtension(item) + Now.Year.ToString + Now.Month.ToString + Now.Day.ToString + Now.Hour.ToString + Now.Minute.ToString + Now.Second.ToString + "[dx]" + Path.GetExtension(item))
                    TextBox3.Text += $"The file {Path.GetFileName(item)} is a duplicated file. It will have the sign [dx] to be recognized easily." + vbCrLf
                    TextBox4.Text += $"The file {Path.GetFileName(item)} is a duplicated file. It will have the sign [dx] to be recognized easily." + vbCrLf
                    publicpath = ""
                    tF += 1
                Catch ex As Exception
                    errorCounter += 1
                    TextBox3.Text += "Error during the copy of the file" + item + vbCrLf + "RTERROR: " + ex.Message + vbCrLf
                    TextBox4.Text += "Error during the copy of the file" + item + vbCrLf + "RTERROR: " + ex.Message + vbCrLf
                End Try

            Catch ex As Exception

                errorCounter += 1
                TextBox3.Text += "Error during the copy of the file" + item + vbCrLf + "RTERROR: " + ex.Message + vbCrLf
                TextBox4.Text += "Error during the copy of the file" + item + vbCrLf + "RTERROR: " + ex.Message + vbCrLf
            End Try
            TextBox4.SelectionStart = TextBox4.TextLength
            TextBox4.ScrollToCaret()
            TextBox3.SelectionStart = TextBox3.TextLength
            TextBox3.ScrollToCaret()
            'FILE EXE
        Next

        '| LET'S PRINT THE RESOCONTOOOSSSS |



        If tF = 0 And errorCounter = 0 Then
            TextBox3.Text += "Any file with recognized extension has been found." + vbCrLf
            TextBox4.Text += "Any file with recognized extension has been found." + vbCrLf
        Else


            If tD(0) <> 0 Then
                Dim dime As Decimal = tD(0)
                If dime >= 1024 Then
                    dime = dime / 1024
                    TextBox3.Text += $"Total transferred photos size: {Math.Round(dime, 2).ToString} GB" + vbCrLf
                    TextBox4.Text += $"Total transferred photos size: {Math.Round(dime, 2).ToString} GB" + vbCrLf
                ElseIf dime < 1 Then
                    dime = dime * 1024
                    TextBox3.Text += $"Total transferred photos size: {Math.Round(dime, 2).ToString} KB" + vbCrLf
                    TextBox4.Text += $"Total transferred photos size: {Math.Round(dime, 2).ToString} KB" + vbCrLf
                Else
                    TextBox3.Text += $"Total transferred photos size: {Math.Round(dime, 2).ToString} MB" + vbCrLf
                    TextBox4.Text += $"Total transferred photos size: {Math.Round(dime, 2).ToString} MB" + vbCrLf
                End If
            End If
            If tD(1) <> 0 Then
                Dim dime As Decimal = tD(1)
                If dime >= 1024 Then
                    dime = dime / 1024
                    TextBox3.Text += $"Total transferred Photoshop files size: {Math.Round(dime, 2).ToString} GB" + vbCrLf
                    TextBox4.Text += $"Total transferred Photoshop files size: {Math.Round(dime, 2).ToString} GB" + vbCrLf
                ElseIf dime < 1 Then
                    dime = dime * 1024
                    TextBox3.Text += $"Total transferred Photoshop files size: {Math.Round(dime, 2).ToString} KB" + vbCrLf
                    TextBox4.Text += $"Total transferred Photoshop files size: {Math.Round(dime, 2).ToString} KB" + vbCrLf
                Else
                    TextBox3.Text += $"Total transferred Photoshop files size: {Math.Round(dime, 2).ToString} MB" + vbCrLf
                    TextBox4.Text += $"Total transferred Photoshop files size: {Math.Round(dime, 2).ToString} MB" + vbCrLf
                End If
            End If
            If tD(2) <> 0 Then
                Dim dime As Decimal = tD(2)
                If dime >= 1024 Then
                    dime = dime / 1024
                    TextBox3.Text += $"Total transferred music files size: {Math.Round(dime, 2).ToString} GB" + vbCrLf
                    TextBox4.Text += $"Total transferred music files size: {Math.Round(dime, 2).ToString} GB" + vbCrLf
                ElseIf dime < 1 Then
                    dime = dime * 1024
                    TextBox3.Text += $"Total transferred music files size: {Math.Round(dime, 2).ToString} KB" + vbCrLf
                    TextBox4.Text += $"Total transferred music files size: {Math.Round(dime, 2).ToString} KB" + vbCrLf
                Else
                    TextBox3.Text += $"Total transferred music files size: {Math.Round(dime, 2).ToString} MB" + vbCrLf
                    TextBox4.Text += $"Total transferred music files size: {Math.Round(dime, 2).ToString} MB" + vbCrLf
                End If
            End If
            If tD(3) <> 0 Then
                Dim dime As Decimal = tD(3)
                If dime >= 1024 Then
                    dime = dime / 1024
                    TextBox3.Text += $"Total transferred video files size: {Math.Round(dime, 2).ToString} GB" + vbCrLf
                    TextBox4.Text += $"Total transferred video files size: {Math.Round(dime, 2).ToString} GB" + vbCrLf
                ElseIf dime < 1 Then
                    dime = dime * 1024
                    TextBox3.Text += $"Total transferred video files size: {Math.Round(dime, 2).ToString} KB" + vbCrLf
                    TextBox4.Text += $"Total transferred video files size: {Math.Round(dime, 2).ToString} KB" + vbCrLf
                Else
                    TextBox3.Text += $"Total transferred video files size: {Math.Round(dime, 2).ToString} MB" + vbCrLf
                    TextBox4.Text += $"Total transferred video files size: {Math.Round(dime, 2).ToString} MB" + vbCrLf
                End If
            End If
            If tD(4) <> 0 Then
                Dim dime As Decimal = tD(4)
                If dime >= 1024 Then
                    dime = dime / 1024
                    TextBox3.Text += $"Total transferred document files size: {Math.Round(dime, 2).ToString} GB" + vbCrLf
                    TextBox4.Text += $"Total transferred document files size: {Math.Round(dime, 2).ToString} GB" + vbCrLf
                ElseIf dime < 1 Then
                    dime = dime * 1024
                    TextBox3.Text += $"Total transferred document files size: {Math.Round(dime, 2).ToString} KB" + vbCrLf
                    TextBox4.Text += $"Total transferred document files size: {Math.Round(dime, 2).ToString} KB" + vbCrLf
                Else
                    TextBox3.Text += $"Total transferred document files size: {Math.Round(dime, 2).ToString} MB" + vbCrLf
                    TextBox4.Text += $"Total transferred document files size: {Math.Round(dime, 2).ToString} MB" + vbCrLf
                End If
            End If
            If tD(5) <> 0 Then
                Dim dime As Decimal = tD(5)
                If dime >= 1024 Then
                    dime = dime / 1024
                    TextBox3.Text += $"Total transferred executable files size:{Math.Round(dime, 2).ToString} GB" + vbCrLf
                    TextBox4.Text += $"Total transferred executable files size:{Math.Round(dime, 2).ToString} GB" + vbCrLf
                ElseIf dime < 1 Then
                    dime = dime * 1024
                    TextBox3.Text += $"Total transferred executable files size:{Math.Round(dime, 2).ToString} KB" + vbCrLf
                    TextBox4.Text += $"Total transferred executable files size:{Math.Round(dime, 2).ToString} KB" + vbCrLf
                Else
                    TextBox3.Text += $"Total transferred executable files size:{Math.Round(dime, 2).ToString} MB" + vbCrLf
                    TextBox4.Text += $"Total transferred executable files size:{Math.Round(dime, 2).ToString} MB" + vbCrLf
                End If
            End If
            If tD(6) <> 0 Then
                Dim dime As Decimal = tD(6)
                If dime >= 1024 Then
                    dime = dime / 1024
                    TextBox3.Text += $"Total transferred font files size: {Math.Round(dime, 2).ToString} GB" + vbCrLf
                    TextBox4.Text += $"Total transferred font files size: {Math.Round(dime, 2).ToString} GB" + vbCrLf
                ElseIf dime < 1 Then
                    dime = dime * 1024
                    TextBox3.Text += $"Total transferred font files size: {Math.Round(dime, 2).ToString} KB" + vbCrLf
                    TextBox4.Text += $"Total transferred font files size: {Math.Round(dime, 2).ToString} KB" + vbCrLf
                Else
                    TextBox3.Text += $"Total transferred font files size: {Math.Round(dime, 2).ToString} MB" + vbCrLf
                    TextBox4.Text += $"Total transferred font files size: {Math.Round(dime, 2).ToString} MB" + vbCrLf
                End If
            End If
            If tD(7) <> 0 Then
                Dim dime As Decimal = tD(7)
                If dime >= 1024 Then
                    dime = dime / 1024
                    TextBox3.Text += $"Total transferred compressed files size: {Math.Round(dime, 2).ToString} GB" + vbCrLf
                    TextBox4.Text += $"Total transferred compressed files size: {Math.Round(dime, 2).ToString} GB" + vbCrLf
                ElseIf dime < 1 Then
                    dime = dime * 1024
                    TextBox3.Text += $"Total transferred compressed files size: {Math.Round(dime, 2).ToString} KB" + vbCrLf
                    TextBox4.Text += $"Total transferred compressed files size: {Math.Round(dime, 2).ToString} KB" + vbCrLf
                Else
                    TextBox3.Text += $"Total transferred compressed files size: {Math.Round(dime, 2).ToString} MB" + vbCrLf
                    TextBox4.Text += $"Total transferred compressed files size: {Math.Round(dime, 2).ToString} MB" + vbCrLf
                End If
            End If
            If tD(8) <> 0 Then
                Dim dime As Decimal = tD(8)
                If dime >= 1024 Then
                    dime = dime / 1024
                    TextBox3.Text += $"Total transferred MIDI files size: {Math.Round(dime, 2).ToString} GB" + vbCrLf
                    TextBox4.Text += $"Total transferred MIDI files size: {Math.Round(dime, 2).ToString} GB" + vbCrLf
                ElseIf dime < 1 Then
                    dime = dime * 1024
                    TextBox3.Text += $"Total transferred MIDI files size: {Math.Round(dime, 2).ToString} KB" + vbCrLf
                    TextBox4.Text += $"Total transferred MIDI files size: {Math.Round(dime, 2).ToString} KB" + vbCrLf
                Else
                    TextBox3.Text += $"Total transferred MIDI files size: {Math.Round(dime, 2).ToString} MB" + vbCrLf
                    TextBox4.Text += $"Total transferred MIDI files size: {Math.Round(dime, 2).ToString} MB" + vbCrLf
                End If
            End If
            If tD(9) <> 0 Then
                Dim dime As Decimal = tD(9)
                If dime >= 1024 Then
                    dime = dime / 1024
                    TextBox3.Text += $"Total transferred Java files size: {Math.Round(dime, 2).ToString} GB" + vbCrLf
                    TextBox4.Text += $"Total transferred Java files size: {Math.Round(dime, 2).ToString} GB" + vbCrLf
                ElseIf dime < 1 Then
                    dime = dime * 1024
                    TextBox3.Text += $"Total transferred Java files size: {Math.Round(dime, 2).ToString} KB" + vbCrLf
                    TextBox4.Text += $"Total transferred Java files size: {Math.Round(dime, 2).ToString} KB" + vbCrLf
                Else
                    TextBox3.Text += $"Total transferred Java files size: {Math.Round(dime, 2).ToString} MB" + vbCrLf
                    TextBox4.Text += $"Total transferred Java files size: {Math.Round(dime, 2).ToString} MB" + vbCrLf
                End If
            End If
            If tD(10) <> 0 Then
                Dim dime As Decimal = tD(10)
                If dime >= 1024 Then
                    dime = dime / 1024
                    TextBox3.Text += $"Dimensioni File Codice Sorgente riordinati: {Math.Round(dime, 2).ToString} GB" + vbCrLf
                    TextBox4.Text += $"Dimensioni File Codice Sorgente riordinati: {Math.Round(dime, 2).ToString} GB" + vbCrLf
                ElseIf dime < 1 Then
                    dime = dime * 1024
                    TextBox3.Text += $"Dimensioni File Codice Sorgente riordinati: {Math.Round(dime, 2).ToString} KB" + vbCrLf
                    TextBox4.Text += $"Dimensioni File Codice Sorgente riordinati: {Math.Round(dime, 2).ToString} KB" + vbCrLf
                Else
                    TextBox3.Text += $"Dimensioni File Codice Sorgente riordinati: {Math.Round(dime, 2).ToString} MB" + vbCrLf
                    TextBox4.Text += $"Dimensioni File Codice Sorgente riordinati: {Math.Round(dime, 2).ToString} MB" + vbCrLf
                End If
            End If
            If tD(11) <> 0 Then
                Dim dime As Decimal = tD(11)
                If dime >= 1024 Then
                    dime = dime / 1024
                    TextBox3.Text += $"Total transferred disk image files size: {Math.Round(dime, 2).ToString} GB" + vbCrLf
                    TextBox4.Text += $"Total transferred disk image files size: {Math.Round(dime, 2).ToString} GB" + vbCrLf
                ElseIf dime < 1 Then
                    dime = dime * 1024
                    TextBox3.Text += $"Total transferred disk image files size: {Math.Round(dime, 2).ToString} KB" + vbCrLf
                    TextBox4.Text += $"Total transferred disk image files size: {Math.Round(dime, 2).ToString} KB" + vbCrLf
                Else
                    TextBox3.Text += $"Total transferred disk image files size: {Math.Round(dime, 2).ToString} MB" + vbCrLf
                    TextBox4.Text += $"Total transferred disk image files size: {Math.Round(dime, 2).ToString} MB" + vbCrLf
                End If
            End If
            If tD(12) <> 0 Then
                Dim dime As Decimal = tD(12)
                If dime >= 1024 Then
                    dime = dime / 1024
                    TextBox3.Text += $"Total transferred DLL files size: {Math.Round(dime, 2).ToString} GB" + vbCrLf
                    TextBox4.Text += $"Total transferred DLL files size: {Math.Round(dime, 2).ToString} GB" + vbCrLf
                ElseIf dime < 1 Then
                    dime = dime * 1024
                    TextBox3.Text += $"Total transferred DLL files size: {Math.Round(dime, 2).ToString} KB" + vbCrLf
                    TextBox4.Text += $"Total transferred DLL files size: {Math.Round(dime, 2).ToString} KB" + vbCrLf
                Else
                    TextBox3.Text += $"Total transferred DLL files size: {Math.Round(dime, 2).ToString} MB" + vbCrLf
                    TextBox4.Text += $"Total transferred DLL files size: {Math.Round(dime, 2).ToString} MB" + vbCrLf
                End If
            End If
            If tD(13) <> 0 Then
                Dim dime As Decimal = tD(13)
                If dime >= 1024 Then
                    dime = dime / 1024
                    TextBox3.Text += $"Total transferred shortcut files size: {Math.Round(dime, 2).ToString} GB" + vbCrLf
                    TextBox4.Text += $"Total transferred shortcut files size: {Math.Round(dime, 2).ToString} GB" + vbCrLf
                ElseIf dime < 1 Then
                    dime = dime * 1024
                    TextBox3.Text += $"Total transferred shortcut files size: {Math.Round(dime, 2).ToString} KB" + vbCrLf
                    TextBox4.Text += $"Total transferred shortcut files size: {Math.Round(dime, 2).ToString} KB" + vbCrLf
                Else
                    TextBox3.Text += $"Total transferred shortcut files size: {Math.Round(dime, 2).ToString} MB" + vbCrLf
                    TextBox4.Text += $"Total transferred shortcut files size: {Math.Round(dime, 2).ToString} MB" + vbCrLf
                End If
            End If
            If tD(14) <> 0 Then
                Dim dime As Decimal = tD(14)
                If dime >= 1024 Then
                    dime = dime / 1024
                    TextBox3.Text += $"Total transferred Apple packages size: {Math.Round(dime, 2).ToString} GB" + vbCrLf
                    TextBox4.Text += $"Total transferred Apple packages size: {Math.Round(dime, 2).ToString} GB" + vbCrLf
                ElseIf dime < 1 Then
                    dime = dime * 1024
                    TextBox3.Text += $"Total transferred Apple packages size: {Math.Round(dime, 2).ToString} KB" + vbCrLf
                    TextBox4.Text += $"Total transferred Apple packages size: {Math.Round(dime, 2).ToString} KB" + vbCrLf
                Else
                    TextBox3.Text += $"Total transferred Apple packages size: {Math.Round(dime, 2).ToString} MB" + vbCrLf
                    TextBox4.Text += $"Total transferred Apple packages size: {Math.Round(dime, 2).ToString} MB" + vbCrLf
                End If
            End If
            If tD(15) <> 0 Then
                Dim dime As Decimal = tD(6)
                If dime >= 1024 Then
                    dime = dime / 1024
                    TextBox3.Text += $"Total transferred Jonio Database files size: {Math.Round(dime, 2).ToString} GB" + vbCrLf
                    TextBox4.Text += $"Total transferred Jonio Database files size: {Math.Round(dime, 2).ToString} GB" + vbCrLf
                ElseIf dime < 1 Then
                    dime = dime * 1024
                    TextBox3.Text += $"Total transferred Jonio Database files size: {Math.Round(dime, 2).ToString} KB" + vbCrLf
                    TextBox4.Text += $"Total transferred Jonio Database files size: {Math.Round(dime, 2).ToString} KB" + vbCrLf
                Else
                    TextBox3.Text += $"Total transferred Jonio Database files size: {Math.Round(dime, 2).ToString} MB" + vbCrLf
                    TextBox4.Text += $"Total transferred Jonio Database files size: {Math.Round(dime, 2).ToString} MB" + vbCrLf
                End If
            End If
            If tD(16) <> 0 Then
                Dim dime As Decimal = tD(6)
                If dime >= 1024 Then
                    dime = dime / 1024
                    TextBox3.Text += $"Total transferred Icon files size: {Math.Round(dime, 2).ToString} GB" + vbCrLf
                    TextBox4.Text += $"Total transferred Icon files size: {Math.Round(dime, 2).ToString} GB" + vbCrLf
                ElseIf dime < 1 Then
                    dime = dime * 1024
                    TextBox3.Text += $"Total transferred Icon files size: {Math.Round(dime, 2).ToString} KB" + vbCrLf
                    TextBox4.Text += $"Total transferred Icon files size: {Math.Round(dime, 2).ToString} KB" + vbCrLf
                Else
                    TextBox3.Text += $"Total transferred Icon files size: {Math.Round(dime, 2).ToString} MB" + vbCrLf
                    TextBox4.Text += $"Total transferred Icon files size: {Math.Round(dime, 2).ToString} MB" + vbCrLf
                End If
            End If
            If tD(17) <> 0 Then
                Dim dime As Decimal = tD(17)
                If dime >= 1024 Then
                    dime = dime / 1024
                    TextBox3.Text += $"Total transferred 3D Model files size: {Math.Round(dime, 2).ToString} GB" + vbCrLf
                    TextBox4.Text += $"Total transferred 3D Model files size: {Math.Round(dime, 2).ToString} GB" + vbCrLf
                ElseIf dime < 1 Then
                    dime = dime * 1024
                    TextBox3.Text += $"Total transferred 3D Model files size: {Math.Round(dime, 2).ToString} KB" + vbCrLf
                    TextBox4.Text += $"Total transferred 3D Model files size: {Math.Round(dime, 2).ToString} KB" + vbCrLf
                Else
                    TextBox3.Text += $"Total transferred 3D Model files size: {Math.Round(dime, 2).ToString} MB" + vbCrLf
                    TextBox4.Text += $"Total transferred 3D Model files size: {Math.Round(dime, 2).ToString} MB" + vbCrLf
                End If
            End If
            If tD(18) <> 0 Then
                Dim dime As Decimal = tD(18)
                If dime >= 1024 Then
                    dime = dime / 1024
                    TextBox3.Text += $"Total transferred Jonio Player Playlist files size: {Math.Round(dime, 2).ToString} GB" + vbCrLf
                    TextBox4.Text += $"Total transferred Jonio Player Playlist files size: {Math.Round(dime, 2).ToString} GB" + vbCrLf
                ElseIf dime < 1 Then
                    dime = dime * 1024
                    TextBox3.Text += $"Total transferred Jonio Player Playlist files size: {Math.Round(dime, 2).ToString} KB" + vbCrLf
                    TextBox4.Text += $"Total transferred Jonio Player Playlist files size: {Math.Round(dime, 2).ToString} KB" + vbCrLf
                Else
                    TextBox3.Text += $"Total transferred Jonio Player Playlist files size: {Math.Round(dime, 2).ToString} MB" + vbCrLf
                    TextBox4.Text += $"Total transferred Jonio Player Playlist files size: {Math.Round(dime, 2).ToString} MB" + vbCrLf
                End If
            End If
        End If
        If tF = 0 And errorCounter = 0 Then

        Else
            TextBox3.Text += $"{tF} Success. {errorCounter} errors. {duplicated} duplicated." + vbCrLf
            TextBox4.Text += $"{tF} Success. {errorCounter} errors. {duplicated} duplicated." + vbCrLf
            MsgBox($"The folder {ComboBox2.Text} has been reordered.", MsgBoxStyle.Information, "Success!")
        End If
        tF = 0
        errorCounter = 0
        duplicated = 0
        TextBox4.SelectionStart = TextBox4.TextLength
        TextBox4.ScrollToCaret()
        TextBox3.SelectionStart = TextBox3.TextLength
        TextBox3.ScrollToCaret()
    End Sub
    Private Sub Button1_Click(sender As Object, e As EventArgs) Handles Button1.Click
        If TextBox1.Text = "C:\" Then
            MsgBox("Error, order the C: folder may damage the system!", MsgBoxStyle.Critical, "Error")
        Else
            TextBox3.Clear()
            TextBox4.Clear()
            Try
                finder(ComboBox1.Text)
            Catch ex As Exception
                MsgBox(ex.Message, MsgBoxStyle.Critical, "Error")
            End Try


        End If

    End Sub

    Private Sub Form1_Load(sender As Object, e As EventArgs) Handles MyBase.Load
        ComboBox1.Items.Add((Environment.GetFolderPath(Environment.SpecialFolder.Desktop)))
        ComboBox1.Items.Add((Environment.GetFolderPath(Environment.SpecialFolder.MyDocuments)))
        Dim pathDownload As String = ((Environment.GetFolderPath(Environment.SpecialFolder.MyVideos)))
        pathDownload = pathDownload.Replace("Videos", "Downloads")
        ComboBox1.Items.Add(pathDownload)
        ComboBox1.Items.Add((Environment.GetFolderPath(Environment.SpecialFolder.MyMusic)))
        ComboBox1.Items.Add((Environment.GetFolderPath(Environment.SpecialFolder.MyPictures)))
        ComboBox1.Items.Add((Environment.GetFolderPath(Environment.SpecialFolder.MyVideos)))

        ComboBox2.Items.Add((Environment.GetFolderPath(Environment.SpecialFolder.Desktop)))
        ComboBox2.Items.Add((Environment.GetFolderPath(Environment.SpecialFolder.MyDocuments)))
        pathDownload = pathDownload.Replace("Videos", "Downloads")
        ComboBox2.Items.Add(pathDownload)
        ComboBox2.Items.Add((Environment.GetFolderPath(Environment.SpecialFolder.MyMusic)))
        ComboBox2.Items.Add((Environment.GetFolderPath(Environment.SpecialFolder.MyPictures)))
        ComboBox2.Items.Add((Environment.GetFolderPath(Environment.SpecialFolder.MyVideos)))
        ComboBox2.SelectedItem = 0

        ComboBox3.Items.Add((Environment.GetFolderPath(Environment.SpecialFolder.Desktop)))
        ComboBox3.Items.Add((Environment.GetFolderPath(Environment.SpecialFolder.MyDocuments)))
        pathDownload = pathDownload.Replace("Videos", "Downloads")
        ComboBox3.Items.Add(pathDownload)
        ComboBox3.Items.Add((Environment.GetFolderPath(Environment.SpecialFolder.MyMusic)))
        ComboBox3.Items.Add((Environment.GetFolderPath(Environment.SpecialFolder.MyPictures)))
        ComboBox3.Items.Add((Environment.GetFolderPath(Environment.SpecialFolder.MyVideos)))

        ComboBox4.Items.Add((Environment.GetFolderPath(Environment.SpecialFolder.Desktop)))
        ComboBox4.Items.Add((Environment.GetFolderPath(Environment.SpecialFolder.MyDocuments)))
        pathDownload = pathDownload.Replace("Videos", "Downloads")
        ComboBox4.Items.Add(pathDownload)
        ComboBox4.Items.Add((Environment.GetFolderPath(Environment.SpecialFolder.MyMusic)))
        ComboBox4.Items.Add((Environment.GetFolderPath(Environment.SpecialFolder.MyPictures)))
        ComboBox4.Items.Add((Environment.GetFolderPath(Environment.SpecialFolder.MyVideos)))
    End Sub

    Private Sub Button2_Click(sender As Object, e As EventArgs) Handles Button2.Click

        Dim f As New FolderBrowserDialog
        If f.ShowDialog = DialogResult.OK Then
            ComboBox1.Text = f.SelectedPath
        End If


    End Sub

    Private Sub Button5_Click(sender As Object, e As EventArgs) Handles Button5.Click
        If TextBox1.Text <> Nothing And TextBox2.Text <> Nothing And ComboBox2.Text <> Nothing Then
            TextBox3.Clear()
            TextBox4.Clear()
            Try
                reorder(TextBox1.Text, ComboBox2.Text, TextBox2.Text)
            Catch ex As Exception
                TextBox3.Text += "E: " + ex.Message + vbCrLf
                TextBox4.Text += "E: " + ex.Message + vbCrLf
            End Try

        End If
    End Sub

    Private Sub Button7_Click(sender As Object, e As EventArgs) Handles Button7.Click
        Dim f As New FolderBrowserDialog
        If f.ShowDialog = DialogResult.OK Then
            TextBox2.Text = f.SelectedPath
        End If
    End Sub

    Private Sub Button6_Click(sender As Object, e As EventArgs) Handles Button6.Click
        Dim f As New FolderBrowserDialog
        If f.ShowDialog = DialogResult.OK Then
            ComboBox2.Text = f.SelectedPath
        End If
    End Sub

    Private Sub Button3_Click(sender As Object, e As EventArgs) Handles Button3.Click
        If Panel2.Visible = True Or Panel3.Visible = True Or Panel4.Visible = True Then
            Panel2.Hide()
            Panel1.Show()
            Panel3.Hide()
            Panel4.Hide()
        End If
    End Sub

    Private Sub Button4_Click(sender As Object, e As EventArgs) Handles Button4.Click
        If Panel1.Visible = True Or Panel3.Visible = True Or Panel4.Visible = True Then
            Panel1.Hide()
            Panel2.Show()
            Panel3.Hide()
            Panel4.Hide()
        End If
    End Sub
    Public Sub riordinaconChiave(ByRef p As String, ByRef key As String)
        TextBox5.Clear()
        Dim nuovoPercorso As String = p + "\" + key
        Dim totFile As Integer = 0
        Dim totDup As Integer = 0
        Dim errorCounter As Integer = 0
        Dim sizeB() As Double = {0}
        For Each item In Directory.GetFiles(p)
            If Path.GetFileName(item).Contains(key) Then
                Try
                    If Directory.Exists(nuovoPercorso) = False Then
                        Directory.CreateDirectory(nuovoPercorso)
                    End If
                    Dim informationFile As System.IO.FileInfo
                    informationFile = My.Computer.FileSystem.GetFileInfo(item)
                    Dim size As Decimal = informationFile.Length / 2 ^ 20
                    sizeB(0) += size
                    TextBox5.Text += $"Transferring {Path.GetFileName(item)} size: " + Math.Round(size, 2).ToString + $" MB" + vbCrLf
                    File.Move(item, nuovoPercorso + "\" + Path.GetFileName(item))
                    totFile += 1
                Catch lol As IOException
                    Try
                        If Directory.Exists(nuovoPercorso) = False Then
                            Directory.CreateDirectory(nuovoPercorso)
                        End If
                        Dim informationFile As System.IO.FileInfo
                        informationFile = My.Computer.FileSystem.GetFileInfo(item)
                        Dim size As Decimal = informationFile.Length / 2 ^ 20
                        sizeB(0) += size
                        TextBox5.Text += $"Transferring {Path.GetFileName(item)} size: " + Math.Round(size, 2).ToString + " MB. Questo è un file duplicato, avrà il sign [dx]" + vbCrLf
                        File.Move(item, nuovoPercorso + "\" + Path.GetFileNameWithoutExtension(item) + Now.Year.ToString + Now.Month.ToString + Now.Day.ToString + Now.Hour.ToString + Now.Minute.ToString + Now.Second.ToString + "[dx]" + Path.GetExtension(item))
                        totFile += 1
                        totDup += 1
                    Catch ex As Exception
                        TextBox5.Text += $"Error with the file  {Path.GetFileName(item)}" + vbCrLf + "E:" + ex.Message + vbCrLf
                        errorCounter += 1
                    End Try
                Catch ex As Exception
                    TextBox5.Text += $"Error with the file  {Path.GetFileName(item)}" + vbCrLf + "E:" + ex.Message + vbCrLf
                    errorCounter += 1
                End Try
            End If
        Next
        'Fine ciclo
        If sizeB(0) <> 0 Then
            Dim dime As Decimal = sizeB(0)
            If dime >= 1024 Then
                dime = dime / 1024
                TextBox5.Text += $"Size of the files with the keyword {key} transferred: {Math.Round(dime, 2).ToString} GB" + vbCrLf
            ElseIf dime < 1 Then
                dime = dime * 1024
                TextBox5.Text += $"Size of the files with the keyword {key} transferred: {Math.Round(dime, 2).ToString} KB" + vbCrLf
            Else
                TextBox5.Text += $"Size of the files with the keyword {key} transferred: {Math.Round(dime, 2).ToString} MB" + vbCrLf
            End If
        End If

        'RESOCONTO
        If totFile = 0 And errorCounter = 0 Then
            TextBox5.Text += $"Any file with the keyword <{key}> has been found." + vbCrLf
        Else
            TextBox5.Text += $"{totFile} files reodered. {errorCounter} errors. {totDup} duplicated." + vbCrLf
        End If

    End Sub
    Private Sub Button11_Click(sender As Object, e As EventArgs) Handles Button11.Click
        Try
            riordinaconChiave(ComboBox3.Text, TextBox6.Text)
        Catch ex As Exception
            TextBox5.Text += $"Si è verificato un errore" + vbCrLf + "E: " + ex.Message + vbCrLf
        End Try

    End Sub

    Private Sub Button8_Click(sender As Object, e As EventArgs) Handles Button8.Click
        If Panel1.Visible = True Or Panel2.Visible = True Or Panel4.Visible = True Then
            Panel1.Hide()
            Panel2.Hide()
            Panel3.Show()
            Panel4.Hide()
        End If
    End Sub
    Public Sub riordinaDate(ByRef p As String, ByRef dataIniziale As Date, ByRef dataFinale As Date)
        Dim finalpath As String
        Dim mese As String = ""
        Dim mesef As String = ""
        Dim totFile As Integer = 0
        Dim errorCounter As Integer = 0
        Dim totDup As Integer = 0
        Select Case (dataIniziale.Month)
            Case 1
                mese = "January"
            Case 2
                mese = "February"
            Case 3
                mese = "March"
            Case 4
                mese = "April"
            Case 5
                mese = "May"
            Case 6
                mese = "June"
            Case 7
                mese = "July"
            Case 8
                mese = "August"
            Case 9
                mese = "September"
            Case 10
                mese = "October"
            Case 11
                mese = "Novembrer"
            Case 12
                mese = "December"
        End Select

        Select Case (dataFinale.Month)
            Case 1
                mesef = "January"
            Case 2
                mesef = "February"
            Case 3
                mesef = "March"
            Case 4
                mesef = "April"
            Case 5
                mesef = "May"
            Case 6
                mesef = "June"
            Case 7
                mesef = "July"
            Case 8
                mesef = "August"
            Case 9
                mesef = "September"
            Case 10
                mesef = "October"
            Case 11
                mesef = "Novembrer"
            Case 12
                mesef = "December"
        End Select
        Dim dimensioni() As Long = {0}
        For Each item In Directory.GetFiles(p)
            If File.GetCreationTime(item) >= dataIniziale And File.GetCreationTime(item) <= dataFinale And Path.GetExtension(item) = ComboBox5.Text Then
                Dim foldername As String = ""
                If CheckBox1.Checked = True Then
                    foldername = $"Files from {dataIniziale.Day.ToString} {mese} {dataIniziale.Year.ToString} to {dataFinale.Day.ToString} {mesef} {dataFinale.Year.ToString} ({Path.GetExtension(item)})"
                Else
                    foldername = $"Files from  {mese} {dataIniziale.Year.ToString} to {mesef} {dataFinale.Year.ToString} ({Path.GetExtension(item)})"
                End If
                finalpath = $"{p}\{foldername}\"
                If Directory.Exists(finalpath) = False Then
                    Directory.CreateDirectory(finalpath)
                End If
                Try
                    Dim informationFile As System.IO.FileInfo
                    informationFile = My.Computer.FileSystem.GetFileInfo(item)
                    Dim size As Decimal = informationFile.Length / 2 ^ 20
                    dimensioni(0) += size
                    TextBox7.Text += $"Transferring {Path.GetFileName(item)} size: " + Math.Round(size, 2).ToString + " MB." + vbCrLf
                    totFile += 1
                    File.Move(item, finalpath + Path.GetFileName(item))
                Catch lol As IOException
                    Dim informationFile As System.IO.FileInfo
                    informationFile = My.Computer.FileSystem.GetFileInfo(item)
                    Dim size As Decimal = informationFile.Length / 2 ^ 20
                    dimensioni(0) += size
                    TextBox7.Text += $"Transferring {Path.GetFileName(item)} size: " + Math.Round(size, 2).ToString + " MB. This file is a duplicated. It will have the sign [dx]" + vbCrLf
                    totFile += 1
                    File.Move(item, finalpath + Path.GetFileName(item))
                Catch ex As Exception
                    errorCounter += 1
                    TextBox7.Text += $"Error with the file  {Path.GetFileName(item)}" + vbCrLf + "E:" + ex.Message + vbCrLf
                End Try
            End If
        Next
        If dimensioni(0) <> 0 Then
            Dim dime As Decimal = dimensioni(0)
            If dime >= 1024 Then
                dime = dime / 1024
                TextBox7.Text += $"Size of transferred files: {Math.Round(dime, 2).ToString} GB" + vbCrLf
            ElseIf dime < 1 Then
                dime = dime * 1024
                TextBox7.Text += $"Size of transferred files: {Math.Round(dime, 2).ToString} KB" + vbCrLf
            Else
                TextBox7.Text += $"Size of transferred files: {Math.Round(dime, 2).ToString} MB" + vbCrLf
            End If
        End If

        'RESOCONTO
        If totFile = 0 And errorCounter = 0 Then
            TextBox7.Text += $"No files to reorder between the two dates has been found.." + vbCrLf
        Else
            TextBox7.Text += $"{totFile} files reodered. {errorCounter} errors. {totDup} duplicated." + vbCrLf
        End If
    End Sub
    Private Sub Button13_Click(sender As Object, e As EventArgs) Handles Button13.Click
        If DateTimePicker1.Value > DateTimePicker2.Value Then
            MsgBox("E: The initial date can't be after the final date", MsgBoxStyle.Critical, "Error")
        Else
            Try
                riordinaDate(ComboBox4.Text, DateTimePicker1.Value, DateTimePicker2.Value)
            Catch ex As Exception
                MsgBox(ex.Message, MsgBoxStyle.Critical, "Error")
            End Try

        End If

    End Sub

    Private Sub Button9_Click(sender As Object, e As EventArgs) Handles Button9.Click
        If Panel1.Visible = True Or Panel2.Visible = True Or Panel3.Visible = True Then
            Panel1.Hide()
            Panel2.Hide()
            Panel3.Hide()
            Panel4.Show()
        End If
    End Sub

    Private Sub Button10_Click(sender As Object, e As EventArgs) Handles Button10.Click
        Dim f As New FolderBrowserDialog
        If f.ShowDialog = DialogResult.OK Then
            ComboBox3.Text = f.SelectedPath
        End If
    End Sub

    Private Sub Button12_Click(sender As Object, e As EventArgs) Handles Button12.Click
        Dim f As New FolderBrowserDialog
        If f.ShowDialog = DialogResult.OK Then
            ComboBox4.Text = f.SelectedPath
        End If
    End Sub

    Private Sub Button14_Click(sender As Object, e As EventArgs) Handles Button14.Click
        AboutBox.Show()
    End Sub
End Class
