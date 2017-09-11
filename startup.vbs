Set oShell = CreateObject ("Wscript.Shell")
Dim strArgs
strArgs = "python homeapi.py"
oShell.Run strArgs, 0, false