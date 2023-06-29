import tkinter

window = tkinter.Tk()
window.title("BMI Calculator")
window.config(pady= 50, padx=50)

def calculate_bmi():
    height = height_input.get()
    weight = weight_input.get()
    if weight=="" or height == "":
        result_label.config(text="Boy ve kilo giriniz!")
    else:
        try:
            bmi = float(weight) / (float(height) / 100) ** 2
            result_string = write_result(bmi)
            result_label.config(text=result_string)
        except:
            result_label.config(text="Bir numara giriniz!")


height_input_label = tkinter.Label(text="boyunuzu giriniz:",font=('Arial', 20,'normal'))
height_input_label.config(bg="black",fg="white")
height_input_label.pack()

calculate_button = tkinter.Button(text="sonuç", command= calculate_bmi)
calculate_button.pack()
calculate_button.update()
print(calculate_button.winfo_height())
print(calculate_button.winfo_width())


my_entry = tkinter.Entry(width=60)
my_entry.focus()
my_entry.pack()


weight_input_label = tkinter.Label(text="kilonuzu giriniz:",font=('Arial', 20,'normal'))
weight_input_label.config(bg="black",fg="white")
weight_input_label.pack()

my_entry = tkinter.Entry(width=60)
my_entry.pack()

result_label = tkinter.Label()
result_label.pack()

def write_result(bmi):
    result_string = "Senin BMI: {bmi}. Senin"
    if bmi <= 16:
        result_string += "zayıfsın!"
    elif bmi > 16 and bmi <=17:
        result_string += "orta zayıflıktasın!"
    elif bmi > 17 and bmi <= 25:
        result_string += "normal!"
    elif bmi > 25 and bmi <= 35:
        result_string += "obez"
    elif bmi > 35 and bmi <= 40:
        result_string += "obez 2"
    else:
        result_string += "obez 3"
    return result_string

window.mainloop()