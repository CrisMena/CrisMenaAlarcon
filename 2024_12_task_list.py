tasks = ["pending", "completed", "pending", "pending"]
index = 0
while index < len(tasks):
  if tasks[index] == "completed":
    print(f"Skipping task {index + 1}")
    index += 1 
    continue
  print(f"Processing task {index + 1}")
  index += 1
