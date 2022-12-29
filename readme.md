Main processes occured during the log monitoring
1. Download bash script from github (wget https://raw.githubusercontent.com/tejasrpatil812/SystemLogParser/main/shell_script.sh)
2. Renamed the downloaded script (mv ./shell_script.sh ./temp)
3. Ran the updated script (bash temp)
4. Renamed the file created through the script (mv ./script ./dummy)

File Structure
* data_files/logs.txt contains logs captured through sysdig (Format in query.sh).
* data_files/output_raw.dot contains graph data in dot language.
* output_full.svg contains whole graph without any filters.
* output_filtered.svg contains graph backtracked through "dummy" file created at the end of the above processes.
* main.py is the entry point and scripts/* contains all helper scripts for each step.
