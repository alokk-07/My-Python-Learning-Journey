# Write a program to fill in a letter template given below with name and date.

letter = '''Dear <|Name|>, 
            You are selected!
            <|Date|>'''

print(letter.replace("<|Name|>", "Alok").replace("<|Date|>", "2024-06-10"))  # Replace placeholders with actual values
