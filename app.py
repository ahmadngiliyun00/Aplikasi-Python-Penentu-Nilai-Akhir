from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    final_grade = None
    status = None

    if request.method == 'POST':
        try:
            tugas = float(request.form['tugas'])
            uts = float(request.form['uts'])
            uas = float(request.form['uas'])

            # Perhitungan Nilai Akhir
            final_grade = (0.3 * tugas) + (0.3 * uts) + (0.4 * uas)

            # Menentukan Status Kelulusan
            if final_grade >= 60:
                status = "Lulus"
            else:
                status = "Tidak Lulus"
        except ValueError:
            final_grade = "Invalid input"
            status = "Error"

    return render_template('index.html', final_grade=final_grade, status=status)

if __name__ == '__main__':
    app.run(debug=True)
