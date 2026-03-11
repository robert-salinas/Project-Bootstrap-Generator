$sLinkFile = "$env:USERPROFILE\Desktop\RS-Bootstrap.lnk"
$sTargetFile = "$PSScriptRoot\run_app.bat"
$sIconFile = "$PSScriptRoot\assets\icon.ico" 
$WshShell = New-Object -ComObject WScript.Shell
$Shortcut = $WshShell.CreateShortcut($sLinkFile)
$Shortcut.TargetPath = $sTargetFile
if (Test-Path $sIconFile) {
    $Shortcut.IconLocation = $sIconFile
}
$Shortcut.WorkingDirectory = $PSScriptRoot
$Shortcut.Save()
