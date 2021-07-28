
""" HERE IS THE LAYOUT OF THE HOME PAGE FIRST DISPLAYED WHEN THE APP LAUNCHES """

import tkinter as tk
import layout.layout_irp as irp
import layout.layout_csm as csm

""" This class is responsible for the layout of the home page """
class Home_Page(tk.Frame):
    #region
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        master.title("Cybersecurity Assessment")

        irp_button = tk.Button(self, text="Inherent Risk Profile", command=lambda: master.switch_frame(irp.IRP_Page))
        csm_button = tk.Button(self, text="Cybersecurity Maturity", command=lambda: master.switch_frame(csm.CSM_Page))

        irp_button.pack(pady=50)
        csm_button.pack()
    #endregion