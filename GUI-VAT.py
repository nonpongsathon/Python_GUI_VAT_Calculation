from tkinter import *
from tkinter import ttk
GUI = Tk()
GUI.geometry('700x700')
GUI.title('โปรแกรมคำนณ VAT')

#FONT
FONT = ('Angsana New',20)

# ช่องชื่อสินค้า
L1 = ttk.Label(GUI, text = 'ชื่อสินค้า')
L1.pack(pady=10)
v_product = StringVar()
E1 =ttk.Entry(GUI,textvariable = v_product)
E1.pack()

#ราคาสินค้า
L2 = ttk.Label(GUI, text = 'ราคาสินค้า')
L2.pack(pady=10)
v_price = StringVar()
E2 = ttk.Entry(GUI,textvariable = v_price)
E2.pack()

#จำนวนสินค้า
L3 = ttk.Label(GUI, text = 'จำนวนสินค้า')
L3.pack(pady=10)
v_number = StringVar()
E3 = ttk.Entry(GUI,textvariable = v_number)
E3.pack()

# ปุ่มกดเพื่อคำนวณ
def CalC(event=None):
	totalprice =  int(v_price.get()) * int(v_number.get()) 
	VAT = totalprice * 7 / 107
	result = totalprice + VAT
	v_result.set('สินค้า: {} \nราคา {} บาท \nจำนวน {} ชิ้น \nเป็นจำนวนเงิน {} บาท \nVAT {:.2f} บาท ยอดรวม {:.2f} บาท'.format(v_product.get(),v_price.get(),v_number.get(),totalprice,VAT,result))
	

B1 = ttk.Button(GUI,text='Calculate',command = CalC)
B1.pack(pady=10)

E1.bind('<Return>',CalC)
E2.bind('<Return>',CalC)
E3.bind('<Return>',CalC)
#สรุปข้อมูลสินค้า
v_result = StringVar()

L4 = ttk.Label(GUI,textvariable = v_result,font=FONT)
L4.pack()

GUI.mainloop()