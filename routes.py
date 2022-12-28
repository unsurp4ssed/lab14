from flask import render_template, request, redirect
from forms import AddForm
from table import  product, db, app


@app.route('/add/<int:id>/ed', methods=["GET", "POST"])
def edit(id):
    form = AddForm()
    if request.method == "POST":
        k = product.query.filter_by(id=id).first()
        mas_db = [k.type, k.name, k.description, k.brand, k.price, k.photo]
        print(k)
        print(mas_db)
        type = request.form['type']
        name = request.form['name']
        description = request.form['description']
        brand = request.form['brand']
        price = request.form['price']
        photo = request.files['photo']
        mass_db = [type, name, description, brand, price, photo.filename]
        if mass_db[5] == "":
            mass_db[5] = str('')
        for i in range(len(mass_db)):
            if mass_db[i] != "":
                mas_db[i] = mass_db[i]
            print(mas_db)
        k.type = str(mas_db[0])
        k.name = str(mas_db[1])
        k.description = str(mas_db[2])
        k.brand = str(mas_db[3])
        k.price = str(mas_db[4])
        k.photo = str(mas_db[5])

        db.session.commit()
        return redirect('/')
    return render_template('edit.html', form=form)