# Step 1 — Quick Revision (15–20 min)

# Without looking at notes, do these:

# Print all keys
# Print all values
# Calculate total marks
# Calculate average marks
# Find highest mark
# Find lowest mark

# If you get stuck, look at your previous code for only a minute, then continue.



dic={"name":"dipesh",
     "age":"21"}

     
print(dic)


marks={"Science":90,
       "maths":80,
       "english":40}

total=0   
average=0
hightest_marks=0 
lowest_marks=9999
lowest_marks_subect=""
hightest_marks_subject=""  
for totalmarks in marks:
    total=total+marks[totalmarks]
    average=total/len(marks)
    if marks[totalmarks] > hightest_marks:
        hightest_marks=marks[totalmarks]
        hightest_marks_subject=(totalmarks)
        
    if marks[totalmarks] < lowest_marks:
       lowest_marks=marks[totalmarks] 
       lowest_marks_subect=totalmarks
    
print(total)
print(average)

print(f"hightest marks is {hightest_marks_subject} : {hightest_marks}")
print(f"Lowest marks is {lowest_marks_subect} : {lowest_marks}")