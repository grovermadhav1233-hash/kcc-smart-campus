from flask import Flask, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = "kcc-smart-campus-secret-key"

@app.route("/", methods=["GET", "POST"])
def home():

    answer = ""
    complaint_message = ""

    if request.method == "POST":

        question = request.form.get("question", "").lower()

        # Campus AIs
        if "question" in request.form:
            question = request.form["question"].lower()

        if "class" in question or "timing" in question:
            answer = "Class timing ke liye apne department ka timetable check karo."

        elif "maths" in question:
            answer = '📐 Engineering Maths available hai. <a href="/subject/maths">Open Maths</a>'

        elif "physics" in question:
            answer = '⚡ Engineering Physics available hai. <a href="/subject/physics">Open Physics</a>'

        elif "fme" in question or "mechanical" in question:
            answer = '🔧 FME available hai. <a href="/subject/fme">Open FME</a>'

        elif "programming" in question or "coding" in question:
            answer = '💻 Programming available hai. <a href="/subject/programming">Open Programming</a>'

        elif "electronics" in question:
            answer = '🔌 Electronics available hai. <a href="/subject/electronics">Open Electronics</a>'

        elif "syllabus" in question:
            answer = "BTech 1st semester me Maths, Physics, FME, Electronics aur Programming jaise subjects hain."

        elif "fee" in question:
            answer = "Fee information ke liye college administration/accounts department se contact karo."

        elif "exam" in question:
            answer = "Exam schedule ke liye college notice aur timetable check karo."

        elif "maths" in question:
             answer = "Engineering Maths ke notes aur syllabus Notes & Syllabus section me available hain."

        elif "physics" in question:
             answer = "Engineering Physics ke notes aur syllabus Notes & Syllabus section me available hain."

        elif "fme" in question:
             answer = "FME (Fundamentals of Mechanical Engineering) ke notes Notes & Syllabus section me available hain."

        elif "chemistry" in question or "applied chemistry" in question:
           answer = 'Applied Chemistry available hai. <a href="/subject/chemistry">Open Chemistry</a>'


        elif "programming" in question or "python" in question or "c" in question:
             answer = "Programming ke liye C, Python aur basic programming resources available hain."

        elif "college" in question:
            answer = "KCC Smart Campus aapko syllabus, notes, fee, exam aur campus information provide karta hai."

        else:
         if not question:
           answer = "Please enter a question first."
         else:
          answer = "Sorry, mujhe iska answer abhi nahi pata."
            
        # Report Issue
        if "complaint" in request.form:
            name = request.form["name"]
            complaint_message = f"Thank you {name}! Your issue has been submitted successfully. ✅"

    return f"""
    <html>

    <head>
        <title>KCC Smart Campus</title>

        <style>

            body {{
                margin: 0;
                font-family: Arial, sans-serif;
                background: linear-gradient(135deg, #071952, #088395);
                color: white;
            }}

            .container {{
                width: 85%;
                max-width: 1000px;
                margin: auto;
                padding: 40px 0;
            }}

            .header {{
                text-align: center;
                margin-bottom: 35px;
            }}

            .header h1 {{
                font-size: 42px;
                margin-bottom: 10px;
            }}

            .header p {{
                font-size: 18px;
            }}

            .card {{
                background: white;
                color: #222;
                border-radius: 18px;
                padding: 25px;
                margin-bottom: 25px;
                box-shadow: 0 10px 30px rgba(0,0,0,0.25);
            }}

            .card h2 {{
                color: #071952;
            }}

            input, textarea {{
                width: 90%;
                padding: 13px;
                margin: 8px 0;
                border: 1px solid #ccc;
                border-radius: 8px;
                font-size: 15px;
            }}

            button {{
                background: #071952;
                color: white;
                border: none;
                padding: 12px 22px;
                border-radius: 8px;
                cursor: pointer;
            }}

            button:hover {{
                background: #088395;
            }}

            .answer {{
                background: #e8f7ff;
                padding: 15px;
                border-radius: 10px;
                margin-top: 15px;
            }}

            .success {{
                background: #e8fff0;
                padding: 15px;
                border-radius: 10px;
                margin-top: 15px;
            }}

            .subjects {{
                display: flex;
                gap: 15px;
                flex-wrap: wrap;
            }}

            .subject {{
                background: #f1f5ff;
                color: #071952;
                padding: 18px;
                border-radius: 12px;
                width: 160px;
                text-align: center;
                font-weight: bold;
            }}

        </style>
    </head>

    <body>

        <div class="container">

            <div class="header">
                <h1>🏫 KCC Smart Campus</h1>
                <p>Your Digital Campus Assistant</p>
            </div>


            <!-- Campus AI -->

            <div class="card">

                <h2>🤖 Campus AI</h2>

                <form method="POST">

                    <input type="text"
                           name="question"
                           placeholder="Ask something about college..."
                           required>

                    <button type="submit">
                        Ask AI 🚀
                    </button>

                </form>

                {"<div class='answer'><b>AI:</b> " + answer + "</div>" if answer else ""}

            </div>


            <!-- Notes & Syllabus -->

            <div class="card">

                <h2>📚 Notes & Syllabus</h2>

                <p>Select your subject:</p>

                <div class="subjects">

    <a href="/subject/maths" class="subject">
        📐<br>
        Engineering Maths
    </a>

    <a href="/subject/physics" class="subject">
        ⚡<br>
        Engineering Physics
    </a>

    <a href="/subject/fme" class="subject">
        🔧<br>
        FME
    </a>

    <a href="/subject/programming" class="subject">
        💻<br>
        Programming
    </a>

    <a href="/subject/electronics" class="subject">
        🔌<br>
        Electronics
    </a>
    <a href="/subject/chemistry" class="subject">
    🧪<br>
    Applied Chemistry
</a>

</div>
            

            </div>
<br>

<div class="card">
    <h2>🎓 Student Login</h2>
    <p>Students can login to access their dashboard.</p>

    <a href="/student-login">
        <button style="padding:12px 25px; font-size:16px; cursor:pointer;">
            Student Login 🔐
        </button>
    </a>
</div>

            <!-- Report Issue -->

            <div class="card">

                <h2>🚨 Report an Issue</h2>

                <form method="POST">

                    <input type="hidden"
                           name="complaint"
                           value="yes">

                    <input type="text"
                           name="name"
                           placeholder="Enter your name"
                           required>

                    <textarea name="issue"
                              placeholder="Describe your issue..."
                              rows="5"
                              required></textarea>

                    <br>

                    <button type="submit">
                        Submit Issue 📩
                    </button>

                </form>

                {"<div class='success'>" + complaint_message + "</div>" if complaint_message else ""}

            </div>

        </div>

    </body>

    </html>
    """
@app.route("/subject/chemistry")
def chemistry():
    return """
    <html>
    <head>
        <title>Applied Chemistry for Smart Systems</title>
    </head>

    <body style="font-family: Arial; padding: 40px;">

        <h1>🧪 Applied Chemistry for Smart Systems</h1>
        <h2>📚 AKTU 2026-27 | AAS102D</h2>

        <h3>📘 Unit 1 – Chemistry of Hardware Materials</h3>
        <ul>
            <li>Materials used in computers and electronic devices</li>
            <li>Semiconductors and Conductors</li>
            <li>Silicon and its properties</li>
            <li>Basic concepts of doping</li>
            <li>PCB materials</li>
            <li>Soldering materials</li>
            <li>Insulating and dielectric materials</li>
            <li>Reliability and corrosion of electronic components</li>
        </ul>

        <h3>📘 Unit 2 – Energy Storage and Power Chemistry</h3>
        <ul>
            <li>Fundamentals of Electrochemistry</li>
            <li>Primary and Secondary Batteries</li>
            <li>Lithium-ion Batteries</li>
            <li>Applications in laptops, mobiles and EVs</li>
            <li>Battery Safety and Charging</li>
            <li>Supercapacitors</li>
            <li>Fuel Cells</li>
            <li>Energy Harvesting Materials</li>
            <li>Wireless Charging Technologies</li>
        </ul>

        <h3>📘 Unit 3 – Sensors and Chemical Detection</h3>
        <ul>
            <li>Chemical Sensing Principles</li>
            <li>Electrochemical Sensors</li>
            <li>Amperometric and Potentiometric Sensors</li>
            <li>Gas Sensors</li>
            <li>Metal Oxide, Optical and MEMS-based Sensors</li>
            <li>Biosensors</li>
            <li>Environmental Chemical Detection</li>
            <li>Electronic Nose (E-nose)</li>
        </ul>

        <h3>📘 Unit 4 – Nanomaterials and Functional Materials</h3>
        <ul>
            <li>Nanotechnology</li>
            <li>Carbon Nanotubes (CNTs)</li>
            <li>Graphene</li>
            <li>Quantum Dots</li>
            <li>Smart Coatings</li>
            <li>Self-cleaning and Hydrophobic Surfaces</li>
            <li>Photochromic and Thermochromic Materials</li>
            <li>Shape-memory Polymers</li>
            <li>Flexible Electronics and Smart Devices</li>
        </ul>

        <h3>📘 Unit 5 – Green Chemistry and E-waste Management</h3>
        <ul>
            <li>Principles of Green Chemistry</li>
            <li>Environmentally Friendly Electronic Materials</li>
            <li>Biodegradable Electronics</li>
            <li>E-waste Generation and Hazards</li>
            <li>E-waste Recycling</li>
            <li>Recovery of Valuable Metals</li>
            <li>RoHS and WEEE</li>
            <li>Sustainable Manufacturing</li>
            <li>Circular Economy in Electronics</li>
        </ul>

        <br>
        <a href="/">⬅ Back to Home</a>

    </body>
    </html>
    """
@app.route("/student-login", methods=["GET", "POST"])
def student_login():
    message = ""

    if request.method == "POST":
        student_id = request.form.get("student_id", "")
        password = request.form.get("password", "")

        if student_id == "KCC001" and password == "12345":
            session["student_id"] = student_id
            return redirect(url_for("student_dashboard"))
        else:
            message = "Invalid Student ID or Password."

    return f"""
    <html>
    <head>
        <title>Student Login</title>
    </head>

    <body style="font-family: Arial; padding: 40px;">

        <h1>🎓 KCC Smart Campus</h1>
        <h2>Student Login</h2>

        <form method="POST">

            <input type="text"
                   name="student_id"
                   placeholder="Student ID"
                   required
                   style="padding:12px; width:300px;">

            <br><br>

            <input type="password"
                   name="password"
                   placeholder="Password"
                   required
                   style="padding:12px; width:300px;">

            <br><br>

            <button type="submit" style="padding:12px 25px;">
                Login 🎓
            </button>

        </form>

        <p>{message}</p>

        <br>
        <a href="/">⬅ Back to Home</a>

    </body>
    </html>
    """


@app.route("/student-dashboard")
def student_dashboard():

    if "student_id" not in session:
        return redirect(url_for("student_login"))

    return f"""
    <html>
    <head>
        <title>Student Dashboard</title>
    </head>

    <body style="font-family: Arial; padding: 40px;">

        <h1>🎓 Student Dashboard</h1>
        <h2>Welcome, {session["student_id"]}!</h2>

        <hr>

        <h3>📚 Student Services</h3>

        <ul>
            <li><a href="/subject/maths">📚 Notes & Syllabus</a></li>
           <li><a href="/exam-info">📝 Exam Information</a></li>
            <li><a href="/fee-info">💰 Fee Information</a></li>
            <li><a href="/campus-ai">🤖 Campus AI</a></li>
           <li><a href="/report-issue">🚨 Report an Issue</a></li>
        </ul>

        <br>

        <a href="/">🏠 Home</a> |
        <a href="/student-logout">Logout</a>

    </body>
    </html>
    def student_dashboard():
    ...
    """
    
@app.route("/exam-info")
def exam_info():
    return """
<html>
<head>
    <title>Exam Information</title>
</head>

<body style="font-family: Arial; padding: 40px;">
    <h1>📄 Exam Information</h1>

    <h2>📅 Examination</h2>

    <ul>
        <li>Mid Semester Examination</li>
        <li>End Semester Examination</li>
        <li>Practical Examination</li>
        <li>End Semester Examination</li>
    </ul>

    <h2>📌 Important</h2>
    <p>Exam dates and timetable will be updated here.</p>

    <br>

    <a href="/student-dashboard">← Back to Student Dashboard</a>
</body>
</html>
"""
@app.route("/fee-info")
def fee_info():
    return """
    <html>
    <head>
        <title>Fee Information</title>
    </head>

    <body style="font-family: Arial; padding: 40px;">
        <h1>💰 Fee Information</h1>

        <h2>College Fees</h2>
        <ul>
            <li>Tuition Fee: ₹________</li>
            <li>Examination Fee: ₹________</li>
            <li>Hostel Fee: ₹________</li>
            <li>Other Charges: ₹________</li>
        </ul>

        <h2>📌 Important</h2>
        <p>Fee details and payment dates will be updated here.</p>

        <br>
        <a href="/student-dashboard">← Back to Student Dashboard</a>
    </body>
    </html>
    """
@app.route("/campus-ai")
def campus_ai():
    return """
    <html>
    <head>
        <title>Campus AI</title>
    </head>

    <body style="font-family: Arial; padding: 40px;">
        <h1>🤖 Campus AI</h1>

        <h2>How can I help you?</h2>

        <ul>
            <li>📚 Study & Notes Help</li>
            <li>📝 Exam Preparation</li>
            <li>🎓 College Information</li>
            <li>💻 Programming Help</li>
        </ul>

        <p>Campus AI will help students with their academic queries.</p>

        <br>
        <a href="/student-dashboard">← Back to Student Dashboard</a>
    </body>
    </html>
    """
@app.route("/report-issue")
def report_issue():
    return """
    <html>
    <head>
        <title>Report an Issue</title>
    </head>

    <body style="font-family: Arial; padding: 40px;">
        <h1>🚨 Report an Issue</h1>

        <form>
            <label>Issue:</label><br><br>
            <textarea rows="6" cols="50"
                placeholder="Describe your issue here..."></textarea>
            <br><br>
            <button type="submit">Submit Issue</button>
        </form>

        <br>
        <a href="/student-dashboard">← Back to Student Dashboard</a>
    </body>
    </html>
    """
@app.route("/student-logout")
def student_logout():
    session.pop("student_id", None)
    return redirect(url_for("student_login"))
@app.route("/subject/<subject>")
def subject(subject):

    subjects = {
        "maths": "Engineering Mathematics",
        "physics": "Engineering Physics",
        "fme": "Fundamentals of Mechanical Engineering",
        "programming": "Programming",
        "electronics": "Basic Electronics",
        "chemistry": "Applied Chemistry"
    }

    name = subjects.get(subject, "Subject")

    return f"""
    <html>
    <head>
        <title>{name}</title>
    </head>

    <body style="font-family: Arial; padding: 40px;">

        <h1>📚 {name}</h1>

        <h2>Notes & Syllabus</h2>

        <h3>
    <a href="/{subject}/unit1">
    🟦 Unit 1
</a>
</h3>
<ul>
    <li>Limits, Continuity & Differentiability</li>
    <li>Partial Derivatives</li>
    <li>Total Derivatives</li>
    <li>Euler's Theorem</li>
    <li>Jacobians</li>
    <li>Maxima & Minima</li>
    <li>Lagrange's Method of Multipliers</li>
</ul>

<h3>
    <a href="/maths/unit2">
        📘 Unit 2 – Multiple Integrals
    </a>
</h3>
<ul>
    <li>Double Integrals</li>
    <li>Triple Integrals</li>
    <li>Change of Order</li>
    <li>Change of Variables</li>
    <li>Beta & Gamma Functions</li>
    <li>Dirichlet's Integral</li>
</ul>

<h3>
    <a href="/maths/unit3">
        📘 Unit 3 – Vector Calculus
    </a>
</h3>
<ul>
    <li>Gradient</li>
    <li>Directional Derivatives</li>
    <li>Divergence</li>
    <li>Curl</li>
    <li>Solenoidal & Irrotational Vectors</li>
    <li>Stokes' Theorem</li>
    <li>Gauss Divergence Theorem</li>
</ul>

<h3>
    <a href="/maths/unit4">
        📘 Unit 4 – Matrices
    </a>
</h3>
<ul>
    <li>Elementary Transformations</li>
    <li>Rank of Matrix</li>
    <li>Gauss Elimination</li>
    <li>Gauss-Seidel Method</li>
    <li>Eigenvalues & Eigenvectors</li>
    <li>Diagonalization</li>
</ul>

<h3>
    <a href="/maths/unit5">
        📘 Unit 5 – Introduction to Vector Space
    </a>
</h3>
<ul>
    <li>Vector Spaces</li>
    <li>Subspaces</li>
    <li>Linear Dependence & Independence</li>
    <li>Basis</li>
    <li>Dimension</li>
</ul>

        <br>

        <a href="/">⬅ Back to KCC Smart Campus</a>

    </body>
    </html>
    """

@app.route("/maths/unit1")
def maths_unit1():

    return """
    <html>

    <head>
        <title>Maths Unit 1</title>
    </head>

    <body style="font-family: Arial; padding: 40px;">

        <h1>📘 Engineering Mathematics</h1>

        <h2>Unit 1 – Multivariable Calculus</h2>

        <h3>1. Partial Derivatives</h3>
        <p>
            Partial derivative kisi function ko ek variable ke respect
            me differentiate karna hota hai, jab baaki variables constant
            rakhe jaate hain.
        </p>

        <h3>2. Total Derivatives</h3>
        <p>
            Jab function multiple variables par depend karta hai,
            total derivative unke combined change ko represent karta hai.
        </p>

        <h3>3. Euler's Theorem</h3>
        <p>
            Homogeneous functions ke derivatives ke relation ko
            Euler's theorem describe karta hai.
        </p>

        <h3>4. Jacobian</h3>
        <p>
            Jacobian multiple variables ke transformation aur
            differentiation me use hota hai.
        </p>

        <h3>5. Maxima and Minima</h3>
        <p>
            Function ka maximum ya minimum value find karne ke
            liye critical points ka use kiya jaata hai.
        </p>

        <br>

        <a href="/subject/maths">
            ⬅ Back to Mathematics
        </a>

    </body>

    </html>
    """
@app.route("/maths/unit2")
def maths_unit2():

    return """
    <html>

    <head>
        <title>Maths Unit 2</title>
    </head>

    <body style="font-family: Arial; padding: 40px;">

        <h1>📘 Engineering Mathematics</h1>

        <h2>Unit 2 – Multiple Integrals</h2>

        <h3>1. Double Integrals</h3>
        <p>
            Double integration is used for integration with respect
            to two variables.
        </p>

        <h3>2. Triple Integrals</h3>
        <p>
            Triple integration involves integration with respect
            to three variables.
        </p>

        <h3>3. Change of Order</h3>
        <p>
            The order of integration can be changed to simplify
            the evaluation of multiple integrals.
        </p>

        <h3>4. Change of Variables</h3>
        <p>
            Change of variables is used to transform a difficult
            integral into a simpler form.
        </p>

        <h3>5. Beta and Gamma Functions</h3>
        <p>
            Beta and Gamma functions are important special functions
            used in mathematical analysis and integration.
        </p>

        <br>

        <a href="/subject/maths">
            ⬅ Back to Mathematics
        </a>

    </body>

    </html>
    """
@app.route("/maths/unit3")
def maths_unit3():

    return """
    <html>

    <head>
        <title>Maths Unit 3</title>
    </head>

    <body style="font-family: Arial; padding: 40px;">

        <h1>📘 Engineering Mathematics</h1>

        <h2>Unit 3 – Vector Calculus</h2>

        <h3>1. Gradient</h3>
        <p>
            Gradient kisi scalar function ke maximum rate of change
            aur uski direction ko represent karta hai.
        </p>

        <h3>2. Directional Derivative</h3>
        <p>
            Directional derivative kisi particular direction me
            function ke rate of change ko batata hai.
        </p>

        <h3>3. Divergence</h3>
        <p>
            Divergence vector field ke outward flow ko describe karta hai.
        </p>

        <h3>4. Curl</h3>
        <p>
            Curl vector field ke rotational nature ko represent karta hai.
        </p>

        <h3>5. Solenoidal and Irrotational Vectors</h3>
        <p>
            Solenoidal vector field me divergence zero hota hai,
            jabki irrotational vector field me curl zero hota hai.
        </p>

        <h3>6. Stokes' Theorem</h3>
        <p>
            Stokes' theorem surface integral aur line integral ke
            relationship ko establish karta hai.
        </p>

        <h3>7. Gauss Divergence Theorem</h3>
        <p>
            Gauss theorem closed surface ke flux ko volume ke
            divergence se relate karta hai.
        </p>

        <br>

        <a href="/subject/maths">
            ⬅ Back to Mathematics
        </a>

    </body>

    </html>
    """
@app.route("/maths/unit4")
def maths_unit4():

    return """
    <html>

    <head>
        <title>Maths Unit 4</title>
    </head>

    <body style="font-family: Arial; padding: 40px;">

        <h1>📘 Engineering Mathematics</h1>

        <h2>Unit 4 – Matrices</h2>

        <h3>1. Elementary Transformations</h3>
        <p>
            Row aur column transformations ka use matrices ko
            simplify karne ke liye kiya jata hai.
        </p>

        <h3>2. Rank of Matrix</h3>
        <p>
            Matrix ka rank uski maximum number of linearly independent
            rows ya columns ko represent karta hai.
        </p>

        <h3>3. Gauss Elimination Method</h3>
        <p>
            Linear equations ko solve karne ke liye matrix ko
            row operations ke through simplify kiya jata hai.
        </p>

        <h3>4. Gauss-Seidel Method</h3>
        <p>
            Gauss-Seidel ek iterative method hai jo simultaneous
            linear equations solve karne ke liye use hoti hai.
        </p>

        <h3>5. Eigenvalues and Eigenvectors</h3>
        <p>
            Eigenvalues aur eigenvectors matrix transformations
            aur linear algebra me important concepts hain.
        </p>

        <h3>6. Diagonalization</h3>
        <p>
            Matrix ko diagonal form me convert karne ki process
            ko diagonalization kehte hain.
        </p>

        <br>

        <a href="/subject/maths">
            ⬅ Back to Mathematics
        </a>

    </body>

    </html>
    """
@app.route("/maths/unit5")
def maths_unit5():

    return """
    <html>

    <head>
        <title>Maths Unit 5</title>
    </head>

    <body style="font-family: Arial; padding: 40px;">

        <h1>📘 Engineering Mathematics</h1>

        <h2>Unit 5 – Introduction to Vector Space</h2>

        <h3>1. Vector Spaces</h3>
        <p>
            Vector space ek mathematical structure hai jisme
            vectors ko addition aur scalar multiplication ke
            through operate kiya jata hai.
        </p>

        <h3>2. Subspaces</h3>
        <p>
            Subspace kisi vector space ka aisa subset hota hai
            jo khud bhi vector space ki properties satisfy karta hai.
        </p>

        <h3>3. Linear Dependence and Independence</h3>
        <p>
            Vectors ka set linearly dependent ya independent
            ho sakta hai depending on whether one vector can be
            represented using the others.
        </p>

        <h3>4. Basis</h3>
        <p>
            Basis vectors ka aisa set hai jo vector space ko
            span karta hai aur linearly independent hota hai.
        </p>

        <h3>5. Dimension</h3>
        <p>
            Vector space ki dimension uske basis me present
            vectors ki number hoti hai.
        </p>

        <br>

        <a href="/subject/maths">
            ⬅ Back to Mathematics
        </a>

    </body>

    </html>
    """
@app.route("/subject/fme")
def fme():

    return """
    <html>

    <head>
        <title>FME - KCC Smart Campus</title>
    </head>

    <body style="font-family: Arial; padding: 40px;">

        <h1>🔧 Fundamentals of Mechanical Engineering</h1>

        <h2>FME - Notes & Syllabus</h2>

        <h3>
    <a href="/fme/unit1">
        📘 Unit 1 – Introduction to Mechanical Engineering
    </a>
</h3>
        <ul>
            <li>Basic concepts of Mechanical Engineering</li>
            <li>Engineering materials</li>
            <li>Properties of materials</li>
        </ul>

        <h3>
    <a href="/fme/unit2">
        📘 Unit 2 – Thermodynamics
    </a>
</h3>
        <ul>
            <li>System and surroundings</li>
            <li>Types of thermodynamic systems</li>
            <li>First Law of Thermodynamics</li>
        </ul>

    <h3>
    <a href="/fme/unit3">
        📘 Unit 3 – IC Engines
    </a>
</h3>
        <ul>
            <li>Internal Combustion Engines</li>
            <li>SI and CI Engines</li>
            <li>Four Stroke and Two Stroke Engines</li>
        </ul>

        <h3>
    <a href="/fme/unit4">
        📘 Unit 4 – Manufacturing Processes
    </a>
</h3>
        <ul>
            <li>Casting</li>
            <li>Welding</li>
            <li>Machining</li>
            <li>Lathe Machine</li>
        </ul>

        <h3>
    <a href="/fme/unit5">
        📘 Unit 5 – Power and Energy
    </a>
</h3>
        <ul>
            <li>Renewable Energy</li>
            <li>Solar Energy</li>
            <li>Wind Energy</li>
            <li>Hydropower</li>
        </ul>

        <br>

        <a href="/">
            ⬅ Back to KCC Smart Campus
        </a>

    </body>

    </html>
    """
@app.route("/fme/unit1")
def fme_unit1():

    return """
    <html>

    <head>
        <title>FME Unit 1</title>
    </head>

    <body style="font-family: Arial; padding: 40px;">

        <h1>🔧 Fundamentals of Mechanical Engineering</h1>

        <h2>Unit 1 – Introduction to Mechanical Engineering</h2>

        <h3>1. Mechanical Engineering</h3>
        <p>
            Mechanical Engineering deals with the design,
            manufacturing and operation of machines and mechanical systems.
        </p>

        <h3>2. Engineering Materials</h3>
        <p>
            Engineering materials include metals, alloys, polymers,
            ceramics and composite materials.
        </p>

        <h3>3. Properties of Materials</h3>
        <p>
            Important properties include strength, hardness,
            toughness, ductility, brittleness and elasticity.
        </p>

        <h3>4. Types of Materials</h3>
        <ul>
            <li>Ferrous materials</li>
            <li>Non-ferrous materials</li>
            <li>Polymers</li>
            <li>Ceramics</li>
            <li>Composites</li>
        </ul>

        <br>

        <a href="/subject/fme">
            ⬅ Back to FME
        </a>

    </body>

    </html>
    """
@app.route("/fme/unit2")
def fme_unit2():

    return """
    <html>

    <head>
        <title>FME Unit 2</title>
    </head>

    <body style="font-family: Arial; padding: 40px;">

        <h1>🔧 Fundamentals of Mechanical Engineering</h1>

        <h2>Unit 2 – Thermodynamics</h2>

        <h3>1. Thermodynamic System</h3>
        <p>
            A thermodynamic system is a specified quantity of matter
            or a region in space selected for study.
        </p>

        <h3>2. Types of Systems</h3>
        <ul>
            <li>Open System</li>
            <li>Closed System</li>
            <li>Isolated System</li>
        </ul>

        <h3>3. Properties of a System</h3>
        <p>
            Important properties include pressure, temperature,
            volume and internal energy.
        </p>

        <h3>4. First Law of Thermodynamics</h3>
        <p>
            Energy can neither be created nor destroyed.
            It can only be converted from one form to another.
        </p>

        <h3>5. Applications</h3>
        <p>
            Thermodynamics is used in engines, refrigerators,
            air conditioners and power plants.
        </p>

        <br>

        <a href="/subject/fme">
            ⬅ Back to FME
        </a>

    </body>

    </html>
    """
@app.route("/fme/unit3")
def fme_unit3():

    return """
    <html>

    <head>
        <title>FME Unit 3</title>
    </head>

    <body style="font-family: Arial; padding: 40px;">

        <h1>🔧 Fundamentals of Mechanical Engineering</h1>

        <h2>Unit 3 – IC Engines</h2>

        <h3>1. Internal Combustion Engine</h3>
        <p>
            An IC engine is an engine in which fuel burns inside
            the engine cylinder to produce useful mechanical power.
        </p>

        <h3>2. SI Engine</h3>
        <p>
            In a Spark Ignition engine, the air-fuel mixture is
            ignited using a spark plug.
        </p>

        <h3>3. CI Engine</h3>
        <p>
            In a Compression Ignition engine, fuel ignites due to
            the high temperature produced by compression.
        </p>

        <h3>4. Four Stroke Engine</h3>
        <ul>
            <li>Suction</li>
            <li>Compression</li>
            <li>Power</li>
            <li>Exhaust</li>
        </ul>

        <h3>5. Two Stroke Engine</h3>
        <p>
            A two-stroke engine completes one operating cycle
            in two piston strokes.
        </p>

        <br>

        <a href="/subject/fme">
            ⬅ Back to FME
        </a>

    </body>

    </html>
    """
@app.route("/fme/unit4")
def fme_unit4():

    return """
    <html>

    <head>
        <title>FME Unit 4</title>
    </head>

    <body style="font-family: Arial; padding: 40px;">

        <h1>🔧 Fundamentals of Mechanical Engineering</h1>

        <h2>Unit 4 – Manufacturing Processes</h2>

        <h3>1. Casting</h3>
        <p>
            Casting is a manufacturing process in which molten metal
            is poured into a mould and allowed to solidify.
        </p>

        <h3>2. Welding</h3>
        <p>
            Welding is a joining process used to permanently join
            two or more pieces of material.
        </p>

        <h3>3. Machining</h3>
        <p>
            Machining removes unwanted material from a workpiece
            to obtain the required shape and size.
        </p>

        <h3>4. Lathe Machine</h3>
        <p>
            A lathe is a machine tool mainly used for turning,
            facing, drilling and other operations.
        </p>

        <h3>5. Important Manufacturing Processes</h3>
        <ul>
            <li>Casting</li>
            <li>Forging</li>
            <li>Welding</li>
            <li>Machining</li>
            <li>Sheet Metal Working</li>
        </ul>

        <br>

        <a href="/subject/fme">
            ⬅ Back to FME
        </a>

    </body>

    </html>
    """
@app.route("/fme/unit5")
def fme_unit5():

    return """
    <html>

    <head>
        <title>FME Unit 5</title>
    </head>

    <body style="font-family: Arial; padding: 40px;">

        <h1>🔧 Fundamentals of Mechanical Engineering</h1>

        <h2>Unit 5 – Power and Energy</h2>

        <h3>1. Renewable Energy</h3>
        <p>
            Renewable energy comes from naturally replenished
            sources such as sunlight, wind and flowing water.
        </p>

        <h3>2. Solar Energy</h3>
        <p>
            Solar energy is obtained from sunlight and can be
            converted into electrical or thermal energy.
        </p>

        <h3>3. Wind Energy</h3>
        <p>
            Wind turbines convert the kinetic energy of moving air
            into electrical energy.
        </p>

        <h3>4. Hydropower</h3>
        <p>
            Hydropower generates electricity using the energy
            of flowing or falling water.
        </p>

        <h3>5. Conventional Energy</h3>
        <ul>
            <li>Coal</li>
            <li>Petroleum</li>
            <li>Natural Gas</li>
        </ul>

        <br>

        <a href="/subject/fme">
            ⬅ Back to FME
        </a>

    </body>

    </html>
    """
@app.route("/subject/physics")
def physics():

    return """
    <html>

    <head>
        <title>Engineering Physics - KCC Smart Campus</title>
    </head>

    <body style="font-family: Arial; padding: 40px;">

        <h1>⚡ Engineering Physics</h1>

        <h2>Notes & Syllabus</h2>

        <h3>
    <a href="/physics/unit1">
        📘 Unit 1 – Quantum Mechanics
    </a>
</h3>
        <ul>
            <li>Wave-Particle Duality</li>
            <li>de Broglie Hypothesis</li>
            <li>Heisenberg Uncertainty Principle</li>
            <li>Schrodinger Wave Equation</li>
        </ul>

        <h3>
    <a href="/physics/unit2">
        📘 Unit 2 – Electromagnetic Theory
    </a>
</h3>
        <ul>
            <li>Electric Field</li>
            <li>Magnetic Field</li>
            <li>Maxwell's Equations</li>
            <li>Electromagnetic Waves</li>
        </ul>

        <h3>
    <a href="/physics/unit3">
        📘 Unit 3 – Laser and Optical Fiber
    </a>
</h3>
        <ul>
            <li>Laser Principle</li>
            <li>Types of Lasers</li>
            <li>Applications of Laser</li>
            <li>Optical Fiber</li>
        </ul>

        <h3>
    <a href="/physics/unit4">
        📘 Unit 4 – Semiconductor Physics
    </a>
</h3>
        <ul>
            <li>Intrinsic and Extrinsic Semiconductors</li>
            <li>PN Junction</li>
            <li>Diode</li>
            <li>Applications of Semiconductor</li>
        </ul>

        <h3>
    <a href="/physics/unit5">
        📘 Unit 5 – Nanotechnology
    </a>
</h3>
        <ul>
            <li>Nanomaterials</li>
            <li>Properties of Nanomaterials</li>
            <li>Applications of Nanotechnology</li>
        </ul>

        <br>

        <a href="/">
            ⬅ Back to KCC Smart Campus
        </a>

    </body>

    </html>
    """
@app.route("/physics/unit1")
def physics_unit1():

    return """
    <html>

    <head>
        <title>Physics Unit 1</title>
    </head>

    <body style="font-family: Arial; padding: 40px;">

        <h1>⚡ Engineering Physics</h1>

        <h2>Unit 1 – Quantum Mechanics</h2>

        <h3>1. Wave-Particle Duality</h3>
        <p>
            Matter and electromagnetic radiation can show both
            wave-like and particle-like properties.
        </p>

        <h3>2. de Broglie Hypothesis</h3>
        <p>
            According to de Broglie, a moving particle has an
            associated wavelength.
        </p>

        <h3>3. Heisenberg Uncertainty Principle</h3>
        <p>
            The position and momentum of a particle cannot both
            be known with unlimited precision at the same time.
        </p>

        <h3>4. Schrödinger Wave Equation</h3>
        <p>
            Schrödinger's equation is used to describe the quantum
            state and behaviour of microscopic particles.
        </p>

        <br>

        <a href="/subject/physics">
            ⬅ Back to Engineering Physics
        </a>

    </body>

    </html>
    """
@app.route("/physics/unit2")
def physics_unit2():

    return """
    <html>

    <head>
        <title>Physics Unit 2</title>
    </head>

    <body style="font-family: Arial; padding: 40px;">

        <h1>⚡ Engineering Physics</h1>

        <h2>Unit 2 – Electromagnetic Theory</h2>

        <h3>1. Electric Field</h3>
        <p>
            Electric field is the region around a charged particle
            where another charge experiences an electric force.
        </p>

        <h3>2. Magnetic Field</h3>
        <p>
            Magnetic field is the region around a magnet or
            current-carrying conductor where magnetic effects occur.
        </p>

        <h3>3. Maxwell's Equations</h3>
        <p>
            Maxwell's equations describe the fundamental relationship
            between electric fields, magnetic fields and charges.
        </p>

        <h3>4. Electromagnetic Waves</h3>
        <p>
            Electromagnetic waves consist of oscillating electric
            and magnetic fields and can travel through vacuum.
        </p>

        <br>

        <a href="/subject/physics">
            ⬅ Back to Engineering Physics
        </a>

    </body>

    </html>
    """
@app.route("/physics/unit3")
def physics_unit3():

    return """
    <html>

    <head>
        <title>Physics Unit 3</title>
    </head>

    <body style="font-family: Arial; padding: 40px;">

        <h1>⚡ Engineering Physics</h1>

        <h2>Unit 3 – Laser and Optical Fiber</h2>

        <h3>1. Laser</h3>
        <p>
            LASER stands for Light Amplification by Stimulated
            Emission of Radiation.
        </p>

        <h3>2. Principle of Laser</h3>
        <p>
            Laser works mainly on the principle of stimulated emission
            and requires population inversion.
        </p>

        <h3>3. Types of Lasers</h3>
        <ul>
            <li>Ruby Laser</li>
            <li>He-Ne Laser</li>
            <li>Semiconductor Laser</li>
        </ul>

        <h3>4. Applications of Laser</h3>
        <ul>
            <li>Medical applications</li>
            <li>Communication</li>
            <li>Industrial cutting and welding</li>
            <li>Barcode scanning</li>
        </ul>

        <h3>5. Optical Fiber</h3>
        <p>
            Optical fiber is a thin transparent fiber that transmits
            information using light through total internal reflection.
        </p>

        <br>

        <a href="/subject/physics">
            ⬅ Back to Engineering Physics
        </a>

    </body>

    </html>
    """
@app.route("/physics/unit4")
def physics_unit4():

    return """
    <html>

    <head>
        <title>Physics Unit 4</title>
    </head>

    <body style="font-family: Arial; padding: 40px;">

        <h1>⚡ Engineering Physics</h1>

        <h2>Unit 4 – Semiconductor Physics</h2>

        <h3>1. Semiconductor</h3>
        <p>
            Semiconductor materials have electrical conductivity
            between conductors and insulators.
        </p>

        <h3>2. Intrinsic and Extrinsic Semiconductors</h3>
        <p>
            Intrinsic semiconductors are pure materials, while
            extrinsic semiconductors are doped with impurities.
        </p>

        <h3>3. PN Junction</h3>
        <p>
            A PN junction is formed by joining P-type and N-type
            semiconductor materials.
        </p>

        <h3>4. Semiconductor Diode</h3>
        <p>
            A diode is a semiconductor device that mainly allows
            current to flow in one direction.
        </p>

        <h3>5. Applications</h3>
        <ul>
            <li>Rectifiers</li>
            <li>Switching circuits</li>
            <li>Signal processing</li>
            <li>Electronic devices</li>
        </ul>

        <br>

        <a href="/subject/physics">
            ⬅ Back to Engineering Physics
        </a>

    </body>

    </html>
    """
@app.route("/physics/unit5")
def physics_unit5():

    return """
    <html>

    <head>
        <title>Physics Unit 5</title>
    </head>

    <body style="font-family: Arial; padding: 40px;">

        <h1>⚡ Engineering Physics</h1>

        <h2>Unit 5 – Nanotechnology</h2>

        <h3>1. Nanomaterials</h3>
        <p>
            Nanomaterials are materials having structures or
            particles with dimensions in the nanometre range.
        </p>

        <h3>2. Properties of Nanomaterials</h3>
        <ul>
            <li>Large surface area</li>
            <li>Special optical properties</li>
            <li>Improved mechanical properties</li>
            <li>Unique electrical properties</li>
        </ul>

        <h3>3. Applications of Nanotechnology</h3>
        <ul>
            <li>Medicine</li>
            <li>Electronics</li>
            <li>Energy storage</li>
            <li>Environmental applications</li>
        </ul>

        <br>

        <a href="/subject/physics">
            ⬅ Back to Engineering Physics
        </a>

    </body>

    </html>
    """
@app.route("/subject/programming")
def programming():
    return """
    <html>
    <head>
        <title>Programming - KCC Smart Campus</title>
    </head>

    <body style="font-family: Arial; padding: 40px;">
        <h1>💻 Programming</h1>
        <h2>Notes & Syllabus</h2>

        <h3>
    <a href="/programming/unit1">
        📘 Unit 1 – Programming Basics
    </a>
</h3>
        <ul>
            <li>Introduction to Programming</li>
            <li>Algorithms and Flowcharts</li>
            <li>Variables and Data Types</li>
            <li>Operators</li>
        </ul>

        <h3>
    <a href="/programming/unit2">
        📘 Unit 2 – Control Statements
    </a>
</h3>
        <ul>
            <li>if-else</li>
            <li>for Loop</li>
            <li>while Loop</li>
            <li>do-while Loop</li>
        </ul>

        <h3>
    <a href="/programming/unit3">
        📘 Unit 3 – Functions
    </a>
</h3>
        <ul>
            <li>Functions</li>
            <li>Function Arguments</li>
            <li>Return Values</li>
            <li>Recursion</li>
        </ul>

        <h3>
    <a href="/programming/unit4">
        📘 Unit 4 – Arrays and Strings
    </a>
</h3>
        <ul>
            <li>One Dimensional Array</li>
            <li>Two Dimensional Array</li>
            <li>Strings</li>
        </ul>

        <h3>
    <a href="/programming/unit5">
        📘 Unit 5 – Pointers and Structures
    </a>
</h3>
        <ul>
            <li>Pointers</li>
            <li>Structures</li>
            <li>File Handling</li>
        </ul>

        <br>
        <a href="/">⬅ Back to KCC Smart Campus</a>
    </body>
    </html>
    """
@app.route("/programming/unit1")
def programming_unit1():
    return """
    <html>
    <head>
        <title>Programming Unit 1 - KCC Smart Campus</title>
    </head>

    <body style="font-family: Arial; padding: 40px;">
        <h1>💻 Programming – Unit 1</h1>
        <h2>📘 Programming Basics</h2>

        <h3>Topics</h3>
        <ul>
            <li>Introduction to Programming</li>
            <li>Algorithms</li>
            <li>Flowcharts</li>
            <li>Variables and Constants</li>
            <li>Data Types</li>
            <li>Operators</li>
            <li>Basic Input and Output</li>
        </ul>

        <h3>📝 Important Topics</h3>
        <ul>
            <li>Algorithm and its characteristics</li>
            <li>Flowchart symbols</li>
            <li>Types of data types</li>
            <li>Arithmetic and relational operators</li>
        </ul>

        <br>
        <a href="/subject/programming">⬅ Back to Programming</a>
    </body>
    </html>
    """
@app.route("/programming/unit2")
def programming_unit2():
    return """
    <html>
    <head>
        <title>Programming Unit 2 - KCC Smart Campus</title>
    </head>

    <body style="font-family: Arial; padding: 40px;">
        <h1>💻 Programming – Unit 2</h1>
        <h2>📘 Control Statements</h2>

        <h3>Topics</h3>
        <ul>
            <li>if Statement</li>
            <li>if-else Statement</li>
            <li>Nested if</li>
            <li>for Loop</li>
            <li>while Loop</li>
            <li>do-while Loop</li>
            <li>break and continue</li>
        </ul>

        <h3>📝 Important Programs</h3>
        <ul>
            <li>Check Even or Odd</li>
            <li>Check Leap Year</li>
            <li>Find Largest Number</li>
            <li>Print Multiplication Table</li>
            <li>Calculate Factorial</li>
        </ul>

        <br>
        <a href="/subject/programming">⬅ Back to Programming</a>
    </body>
    </html>
    """
@app.route("/programming/unit4")
def programming_unit4():
    return """
    <html>
    <head>
        <title>Programming Unit 4 - KCC Smart Campus</title>
    </head>

    <body style="font-family: Arial; padding: 40px;">
        <h1>💻 Programming – Unit 4</h1>
        <h2>📘 Arrays and Strings</h2>

        <h3>Topics</h3>
        <ul>
            <li>One Dimensional Array</li>
            <li>Two Dimensional Array</li>
            <li>Array Traversal</li>
            <li>Searching in Array</li>
            <li>Strings</li>
            <li>String Functions</li>
        </ul>

        <h3>📝 Important Programs</h3>
        <ul>
            <li>Find Largest Element in Array</li>
            <li>Find Smallest Element in Array</li>
            <li>Calculate Sum of Array Elements</li>
            <li>Reverse an Array</li>
            <li>Find Length of a String</li>
        </ul>

        <br>
        <a href="/subject/programming">⬅ Back to Programming</a>
    </body>
    </html>
    """
@app.route("/programming/unit5")
def programming_unit5():
    return """
    <html>
    <head>
        <title>Programming Unit 5 - KCC Smart Campus</title>
    </head>

    <body style="font-family: Arial; padding: 40px;">
        <h1>💻 Programming – Unit 5</h1>
        <h2>📘 Pointers and Structures</h2>

        <h3>Topics</h3>
        <ul>
            <li>Introduction to Pointers</li>
            <li>Pointer Variables</li>
            <li>Pointer Arithmetic</li>
            <li>Structures</li>
            <li>Structure Members</li>
            <li>Unions</li>
            <li>Basic File Handling</li>
        </ul>

        <h3>📝 Important Programs</h3>
        <ul>
            <li>Swap Two Numbers Using Pointers</li>
            <li>Access Array Using Pointers</li>
            <li>Student Record Using Structure</li>
            <li>Store and Read Data Using File Handling</li>
        </ul>

        <br>
        <a href="/subject/programming">⬅ Back to Programming</a>
    </body>
    </html>
    """
@app.route("/subject/electronics")
def electronics():
    return """
    <html>
    <head>
        <title>Electronics - KCC Smart Campus</title>
    </head>

    <body style="font-family: Arial; padding: 40px;">
        <h1>⚡ Basic Electronics</h1>
        <h2>Notes & Syllabus</h2>

        <h3>
    <a href="/electronics/unit1">
        📘 Unit 1 – Semiconductor Devices
    </a>
</h3>
        <ul>
            <li>Semiconductors</li>
            <li>PN Junction Diode</li>
            <li>Zener Diode</li>
            <li>Diode Applications</li>
        </ul>

        <h3>
    <a href="/electronics/unit2">
        📘 Unit 2 – Transistors
    </a>
</h3>
        <ul>
            <li>BJT</li>
            <li>Transistor Configurations</li>
            <li>Transistor Biasing</li>
            <li>Applications of Transistor</li>
        </ul>

        <h3>
    <a href="/electronics/unit3">
        📘 Unit 3 – Digital Electronics
    </a>
</h3>
        <ul>
            <li>Number Systems</li>
            <li>Logic Gates</li>
            <li>Boolean Algebra</li>
            <li>Truth Tables</li>
        </ul>

        <h3>
    <a href="/electronics/unit4">
        📘 Unit 4 – Operational Amplifier
    </a>
</h3>
        <ul>
            <li>Introduction to Op-Amp</li>
            <li>Ideal Op-Amp</li>
            <li>Inverting Amplifier</li>
            <li>Non-Inverting Amplifier</li>
        </ul>

        <h3>
    <a href="/electronics/unit5">
        📘 Unit 5 – Communication Systems
    </a>
</h3>
        <ul>
            <li>Basic Communication System</li>
            <li>Modulation</li>
            <li>AM and FM</li>
            <li>Applications of Communication</li>
        </ul>

        <br>
        <a href="/">⬅ Back to KCC Smart Campus</a>
    </body>
    </html>
    """
@app.route("/electronics/unit1")
def electronics_unit1():
    return """
    <html>
    <head>
        <title>Electronics Unit 1 - KCC Smart Campus</title>
    </head>

    <body style="font-family: Arial; padding: 40px;">
        <h1>⚡ Electronics – Unit 1</h1>
        <h2>📘 Semiconductor Devices</h2>

        <h3>Topics</h3>
        <ul>
            <li>Introduction to Semiconductors</li>
            <li>Intrinsic and Extrinsic Semiconductors</li>
            <li>PN Junction</li>
            <li>PN Junction Diode</li>
            <li>Zener Diode</li>
            <li>Diode Applications</li>
        </ul>

        <h3>📝 Important Topics</h3>
        <ul>
            <li>V-I Characteristics of PN Junction Diode</li>
            <li>Working of Zener Diode</li>
            <li>Half Wave Rectifier</li>
            <li>Full Wave Rectifier</li>
            <li>Bridge Rectifier</li>
        </ul>

        <br>
        <a href="/subject/electronics">⬅ Back to Electronics</a>
    </body>
    </html>
    """
@app.route("/electronics/unit2")
def electronics_unit2():
    return """
    <html>
    <head>
        <title>Electronics Unit 2 - KCC Smart Campus</title>
    </head>

    <body style="font-family: Arial; padding: 40px;">
        <h1>⚡ Electronics – Unit 2</h1>
        <h2>📘 Transistors</h2>

        <h3>Topics</h3>
        <ul>
            <li>Introduction to Transistors</li>
            <li>BJT – Bipolar Junction Transistor</li>
            <li>Transistor Configurations</li>
            <li>Common Emitter Configuration</li>
            <li>Common Base Configuration</li>
            <li>Common Collector Configuration</li>
            <li>Transistor Biasing</li>
        </ul>

        <h3>📝 Important Topics</h3>
        <ul>
            <li>Working of BJT</li>
            <li>Input and Output Characteristics</li>
            <li>Transistor as an Amplifier</li>
            <li>Transistor as a Switch</li>
        </ul>

        <br>
        <a href="/subject/electronics">⬅ Back to Electronics</a>
    </body>
    </html>
    """
@app.route("/electronics/unit3")
def electronics_unit3():
    return """
    <html>
    <head>
        <title>Electronics Unit 3 - KCC Smart Campus</title>
    </head>

    <body style="font-family: Arial; padding: 40px;">
        <h1>⚡ Electronics – Unit 3</h1>
        <h2>📘 Digital Electronics</h2>

        <h3>Topics</h3>
        <ul>
            <li>Number Systems</li>
            <li>Binary, Decimal, Octal and Hexadecimal</li>
            <li>Logic Gates</li>
            <li>AND, OR and NOT Gates</li>
            <li>NAND and NOR Gates</li>
            <li>Boolean Algebra</li>
            <li>Truth Tables</li>
        </ul>

        <h3>📝 Important Topics</h3>
        <ul>
            <li>Universal Logic Gates</li>
            <li>Boolean Algebra Laws</li>
            <li>Logic Gate Truth Tables</li>
            <li>Number System Conversions</li>
        </ul>

        <br>
        <a href="/subject/electronics">⬅ Back to Electronics</a>
    </body>
    </html>
    """
@app.route("/electronics/unit4")
def electronics_unit4():
    return """
    <html>
    <head>
        <title>Electronics Unit 4 - KCC Smart Campus</title>
    </head>

    <body style="font-family: Arial; padding: 40px;">
        <h1>⚡ Electronics – Unit 4</h1>
        <h2>📘 Operational Amplifier</h2>

        <h3>Topics</h3>
        <ul>
            <li>Introduction to Op-Amp</li>
            <li>Ideal Op-Amp</li>
            <li>Op-Amp Characteristics</li>
            <li>Inverting Amplifier</li>
            <li>Non-Inverting Amplifier</li>
            <li>Voltage Follower</li>
        </ul>

        <h3>📝 Important Topics</h3>
        <ul>
            <li>Ideal Op-Amp Characteristics</li>
            <li>Inverting Amplifier</li>
            <li>Non-Inverting Amplifier</li>
            <li>Applications of Op-Amp</li>
        </ul>

        <br>
        <a href="/subject/electronics">⬅ Back to Electronics</a>
    </body>
    </html>
    """
@app.route("/electronics/unit5")
def electronics_unit5():
    return """
    <html>
    <head>
        <title>Electronics Unit 5 - KCC Smart Campus</title>
    </head>

    <body style="font-family: Arial; padding: 40px;">
        <h1>⚡ Electronics – Unit 5</h1>
        <h2>📘 Communication Systems</h2>

        <h3>Topics</h3>
        <ul>
            <li>Basic Communication System</li>
            <li>Transmitter and Receiver</li>
            <li>Modulation</li>
            <li>Amplitude Modulation (AM)</li>
            <li>Frequency Modulation (FM)</li>
            <li>Applications of Communication</li>
        </ul>

        <h3>📝 Important Topics</h3>
        <ul>
            <li>Block Diagram of Communication System</li>
            <li>Amplitude Modulation</li>
            <li>Frequency Modulation</li>
            <li>Applications of Communication Systems</li>
        </ul>

        <br>
        <a href="/subject/electronics">⬅ Back to Electronics</a>
    </body>
    </html>
    """
if __name__ == "__main__":
    app.run(debug=True)