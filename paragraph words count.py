str1=" An English paragraph is a group of sentences that develops a single topic, often beginning with a topic sentence that states the main idea. It should include supporting sentences that provide details, examples, or explanations related to the topic sentence, and it may end with a concluding sentence that summarizes the main points. Paragraphs are used to organize writing and help readers understand the structure and flow of ideas. "
str2= set(str1)

print (f"Total items are {len(str1)}")
print (f"Total items are {len(str2)}")
c=0
for item in str2:
	c+=1
	print(f"{item}",str1.count(item))
	
	
		
			
				
						#print (f"current loop {c} {item} count is {str1.count(item)}")