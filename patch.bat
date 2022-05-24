<# : patch.bat
:: launches a File... Open sort of file chooser and outputs choice(s) to the console
:: https://stackoverflow.com/a/15885133/1683264

@echo off
setlocal

echo Metroid Prime Practice World Patcher

echo.
echo Jumping once with Space Jump puts you higher into the air than without Space Jump.
echo Do you understand? (y/n)
SET /P AREYOUSURE=:
IF /I "%AREYOUSURE%" NEQ "y" goto :EOF

echo.
echo Bomb Jumping with Space Jump puts you higher into the air than without Space Jump.
echo Do you understand? (y/n)
SET /P AREYOUSURE=:
IF /I "%AREYOUSURE%" NEQ "y" goto :EOF

echo.
echo Please select your input ISO...

for /f "delims=" %%I in ('powershell -noprofile "iex (${%~f0} | out-string)"') do (
    randomprime_patcher.exe --profile prime-practice-world.json --quickplay --input-iso "%%~I" --output-iso prime-practice-world.iso
)

pause

goto :EOF

: end Batch portion / begin PowerShell hybrid chimera #>

Add-Type -AssemblyName System.Windows.Forms
$f = new-object Windows.Forms.OpenFileDialog
$f.InitialDirectory = pwd
$f.Filter = "Gamecube ROM (*.iso)|*.iso|All Files (*.*)|*.*"
$f.ShowHelp = $true
$f.Multiselect = $true
[void]$f.ShowDialog()
if ($f.Multiselect) { $f.FileNames } else { $f.FileName }
