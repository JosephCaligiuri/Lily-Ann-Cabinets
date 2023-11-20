import json

def create_json_file(questions_and_answers, output_file):
    data = []
    lines = questions_and_answers.split("? ")
    for line in lines:
        line = line.strip()
        if line:
            question, *answer_lines = line.split("\n")
            answer = " ".join(answer_lines)
            data.append({"question": question.strip(), "answer": answer.strip()})

    with open(output_file, 'w') as f:
        json.dump(data, f, indent=4)

# Example usage
input_text = """Which cabinets from Lily Ann are builder grade? Lily Ann Cabinets offers three builder grade cabinets: The Summit White Shaker, Madison Toffee, and Madison Chocolate. These Cabinets do not have the self-closing features like the premium cabinets do, which makes them less expensive. 
What is the most popular style of cabinet? The most popular style is the White Shaker!
What color paint goes best with grey cabinets? Grey cabinets often pair best with a white paint to keep the natural light feeling in your kitchen. 
What color hardware goes best with white cabinets? It depends on what style you are going for since white matches with just about everything! Black is a very popular color to do with white cabinetry. 
What is HDF? high-density fiberboard (HDF),[1] is a type of fiberboard, which is an engineered wood product.[2] It is used in furniture and in the construction industry.
Who is the owner of Lily Ann Cabinets? Bill Decker Jr. started Lily Ann Cabinets named after his youngest daughter in 2004 to enhance his building company. 
Why is the company named Lily Ann Cabinets? Lily Ann Cabinets is named after the founder's youngest daughter, Lily Ann! 
"""

output_filename = "questions.json"

create_json_file(input_text, output_filename)
print(f"JSON file '{output_filename}' created successfully!")
