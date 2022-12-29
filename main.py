from scripts import parser, graph, tuple_generator, backtracker

MAX_TRIES = 5

def main():	
	print("\n-------------------------------------------------------------------------------------------------\n")
	file_path = input("Please provide log file to parse (Default: ./data_files/logs.txt): ")
	graph_path = input("Please provide file to store graph (Default: ./data_files/output_raw.dot): ")
	
	print("\nParsing Log File\n")
	parsed_logs = parser.handle(file_path)
	
	print("Generating Tuples\n")
	events = tuple_generator.handle(parsed_logs)
	
	print_event = input("Do you want to print parsed events? (Yes/No): \n")
	if print_event and print_event.lower() in ['y', 'yes']:
		print(events)
	 
	do_backtrack = input("Do you have point of interest to backtrack and filter events? (Y/N) :")
	if do_backtrack.lower() in ['y','yes']:
		for _ in range(MAX_TRIES):
			try:
				print("\n1. Node")
				print("2. Edge")
				choice = int(input("Choose your required point of interest type: "))
				if choice == 1:
					node = input("\nPlease provide point of interest process : [Examples: (process_id), (process_name), (file_path)] \n") 
					events = backtracker.handle(events, node = node)
				elif choice == 2:
					subject = input("\nPlease provide point of interest process (Default: None) : [Examples: (process_id), (process_name), (file_path)] \n")
					operation = input("\nPlease provide point of interest operation (Default: None) : [Examples: read, write] \n")
					obj = input("\nPlease provide point of interest object (Default: None) : [Examples: (process_id), (process_name), (file_path)] \n")
					events = backtracker.handle(events, edge = [subject, operation, obj])
				else:
					raise Exception("Incorrect choice!")
				
				print("\nBacktracking Completed")
				break
			except Exception as e:
				print(f"Please try again!, error occured : {e}\n")
		
	print("\nGenerating Graph\n")
	graph.handle(events, graph_path)

	
	print("Process Complete")	
	print("\n-------------------------------------------------------------------------------------------------\n")

if __name__ == "__main__":
	main()