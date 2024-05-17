
try:
    import traceback
    import tkinter as tk
    from tkinter import filedialog
    import customtkinter as ctk
    from main import load_excel,query_excel

    # Initialize the main window
    root = tk.Tk()
    root.title("CVR COLLEGE OF ENGINEERING")
    root.iconbitmap('logo.ico')
    # icon_image = tk.PhotoImage(file="logo.ico")

    # Set the window icon
    # root.tk.call('wm', 'iconphoto', root._w, icon_image)
    # root.iconbitmap(False,root.iconify(file=r"C:\Users\SAAD\Desktop\file_reader\Cvrh_ibp.gif"))
    # root.icon = 'Cvrh_ibp.gif'
    root.geometry("500x600")

    def browse_file():
        filename = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx *.xls")])
        excel_entry.delete(0, tk.END)
        excel_entry.insert(0, filename)

    def process_inputs():
        excel_file = excel_entry.get()
        name = name_entry.get()
        day = day_entry.get()
        time = time_entry.get()

        df = load_excel(excel_file)
        result = query_excel(df,name.strip(),day.strip(),time.strip())
        
        # Simple processing: concatenating the inputs for demonstration

        # Displaying the result in the output text widget
        output_text.configure(state='normal')  # Enable editing
        output_text.delete(1.0, tk.END)  # Clear previous content
        output_text.insert(tk.END, result)  # Insert new content
        output_text.tag_add("output_font", "1.0", tk.END)  # Apply font tag to all text
        output_text.configure(state='disabled')  # Disable editing

    # Heading
    heading_label = ctk.CTkLabel(root, text="Tracking faculty location using timetables", font=("Helvetica", 20, "bold"))
    heading_label.pack(pady=8)

    # Create a frame for form elements
    form_frame = ctk.CTkFrame(root)
    form_frame.pack(pady=20)

    # Excel file input
    excel_label = ctk.CTkLabel(form_frame, text="Select Excel File:")
    excel_label.grid(row=0, column=0, pady=10, padx=10, sticky="e")

    excel_entry = ctk.CTkEntry(form_frame, width=200,placeholder_text='Select excel file')
    excel_entry.grid(row=0, column=1, pady=10, padx=10)

    browse_button = ctk.CTkButton(form_frame, text="Browse", command=browse_file)
    browse_button.grid(row=0, column=2, pady=10, padx=10)

    # Name input
    name_label = ctk.CTkLabel(form_frame, text="Faculty name:")
    name_label.grid(row=1, column=0, pady=10, padx=10, sticky="e")

    name_entry = ctk.CTkEntry(form_frame, width=200, placeholder_text='Enter faculty name')
    name_entry.grid(row=1, column=1, pady=10, padx=10)

    # Day input
    day_label = ctk.CTkLabel(form_frame, text="Day:")
    day_label.grid(row=2, column=0, pady=10, padx=10, sticky="e")

    day_entry = ctk.CTkEntry(form_frame, width=200, placeholder_text='Enter day')
    day_entry.grid(row=2, column=1, pady=10, padx=10)

    # Time input
    time_label = ctk.CTkLabel(form_frame, text="Time:")
    time_label.grid(row=3, column=0, pady=10, padx=10, sticky="e")

    time_entry = ctk.CTkEntry(form_frame, width=200, placeholder_text='Enter time')
    time_entry.grid(row=3, column=1, pady=10, padx=10)

    # Process button
    process_button = ctk.CTkButton(form_frame, text="Track", command=process_inputs)
    process_button.grid(row=4, column=1, padx=10, pady=10, sticky="w")

    output_label = ctk.CTkLabel(root, text="Status:")
    output_label.pack(pady=1)

    # Output text widget
    output_text = tk.Text(root, height=10, width=45, state='disabled', wrap='word')
    output_text.pack(pady=10, padx=10)

    # Configure the font for the output text
    output_text.tag_configure("output_font", font=("Helvetica", 12,'bold'))

    # Run the main loop
    root.mainloop()
except Exception as e:
    print(e)
    while True:
        pass
