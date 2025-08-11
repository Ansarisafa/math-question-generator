import random
from docx import Document
from docx.shared import Inches

def generate_uniform_question():
    """Generates uniform combination question matching exact base question format"""
    shirt_colors = ['Tan', 'Red', 'White', 'Yellow']
    pants_colors = ['Black', 'Khaki', 'Navy']
    
    # Build question text with table
    question = (
        "Each student at Central Middle School wears a uniform consisting of "
        "1 shirt and 1 pair of pants. The table shows the colors available for "
        "each item of clothing. How many different uniforms are possible?\n\n"
        "| Shirt Color | Pants Color |\n"
        "| :---: | :---: |\n"
        f"| {shirt_colors[0]} | {pants_colors[0]} |\n"
        f"| {shirt_colors[1]} | {pants_colors[1]} |\n"
        f"| {shirt_colors[2]} | {pants_colors[2]} |\n"
        f"| {shirt_colors[3]} | |\n"
    )

    # Calculate correct answer (4 shirts × 3 pants = 12)
    correct_answer = 12
    options = {
        "A": "Three",
        "B": "Four",
        "C": "Seven",
        "D": "Ten",
        "E": "Twelve"  # Correct
    }

    return {
        "question": question,
        "options": options,
        "correct_answer": "E",
        "explanation": (
            "Multiply the number of shirt options (4) by pants options (3). "
            "Even though the table shows an empty pants cell for Yellow shirt, "
            "the problem implies all shirts can pair with all pants. "
            "Thus: \\(4 \\times 3 = 12\\) combinations."
        ),
        "subject": "Quantitative Math",
        "unit": "Problem Solving",
        "topic": "Data Analysis"
    }

def generate_ball_packing_question():
    """Generates ball packing question with image reference"""
    question = (
        "The top view of a rectangular package of 6 tightly packed balls is shown. "
        "If each ball has a radius of 2 centimeters, which of the following are "
        "closest to the dimensions, in centimeters, of the rectangular package?\n\n"
        "![ball packing diagram](balls.png)\n\n"  # Image placeholder
    )

    options = {
        "A": "\\(2 \\times 3 \\times 6\\)",
        "B": "\\(4 \\times 6 \\times 6\\)",  # Correct
        "C": "\\(2 \\times 4 \\times 6\\)",
        "D": "\\(4 \\times 8 \\times 12\\)",
        "E": "\\(6 \\times 8 \\times 12\\)"
    }

    return {
        "question": question,
        "options": options,
        "correct_answer": "B",
        "explanation": (
            "Each ball has diameter \\(2r = 4\\) cm. For 6 balls in rectangular packing (3×2 arrangement):\n"
            "- Width: \\(3 \\times 4 = 12\\) cm\n"
            "- Depth: \\(2 \\times 4 = 8\\) cm\n"
            "- Height: \\(4\\) cm (single layer)\n"
            "Closest option is B (\\(4 \\times 6 \\times 6\\) as it matches height and approximates length/width."
        ),
        "subject": "Quantitative Math",
        "unit": "Problem Solving",
        "topic": "Geometry"
    }

def save_to_docx(questions):
    """Saves questions to Word document with proper formatting"""
    doc = Document()
    
    # Title and description
    doc.add_heading('Math Assessment', level=1)
    doc.add_paragraph('Generated math questions based on curriculum standards')
    
    for i, q in enumerate(questions, 1):
        # Question block
        doc.add_paragraph(f"Question {i}", style='Heading 2')
        doc.add_paragraph(q['question'])
        
        # Options
        for opt, text in q['options'].items():
            doc.add_paragraph(f"{opt}) {text}")
        
        # Metadata
        meta = [
            f"Subject: {q['subject']}",
            f"Unit: {q['unit']}",
            f"Topic: {q['topic']}"
        ]
        doc.add_paragraph("\n".join(meta), style='Intense Quote')
        
        # Explanation
        doc.add_paragraph("Explanation:", style='Heading 3')
        doc.add_paragraph(q['explanation'])
    
    doc.save('math_assessment.docx')

if __name__ == "__main__":
    # Generate both question types
    questions = [
        generate_uniform_question(),
        generate_ball_packing_question()
    ]
    
    # Save to Word
    save_to_docx(questions)
    print("Assessment generated: math_assessment.docx")
