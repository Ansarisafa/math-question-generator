# Math Assessment Generator

## 📝 Overview
A Python tool that automatically generates standardized math assessments with:
- Multiple-choice questions (MCQs)
- LaTeX-formatted equations
- Embedded diagrams
- Curriculum-aligned content

## ✨ Features
| Component          | Details |
|--------------------|---------|
| **Question Types** | • Uniform combinations<br>• Geometry (ball packing) |
| **Output Format**  | Microsoft Word (.docx) |
| **Math Notation**  | Proper LaTeX rendering (`\\(...\\)`) |
| **Visual Aids**    | Auto-generated diagrams |
| **Standards**      | Aligned with Quantitative Math curriculum |

## Example Output
# Question 1  
[Uniform combination problem with table]  

# Question 2  
[Geometry problem with embedded diagram]  

## 🛠️ Installation
```bash
# Clone repository
git clone https://github.com/Ansarisafa/math-question-generator.git
cd math-question-generator

# Install dependencies
pip install -r requirements.txt

## 🔧 Customization
"subject": "Quantitative Math",
"unit": "Problem Solving", 
"topic": "Data Analysis"  # or "Geometry"

Adjust diagram styles:
plt.savefig('diagram.png', dpi=120, bbox_inches='tight')
