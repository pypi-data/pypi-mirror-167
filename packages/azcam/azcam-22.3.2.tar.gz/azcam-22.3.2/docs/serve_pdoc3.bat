@echo off

echo Doc web server will run while this window is open

pdoc --http localhost:8081 -c show_source_code=False -c show_type_annotations=True ..\..\mplesser.github.io\docs\azcam

pause
